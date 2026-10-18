import os
import subprocess
import re
from datetime import datetime

import logging
# from logger import logger

from ..settings.gui_settings import gui_settings


def humanize_file_size(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


# Shorten a folder path to a given length by removing the middle of the path
def shorten_path(path, limit):
    # Split the path into individual segments
    segments = path.split(os.path.sep)
    num_segments = len(segments)

    # If the path is already shorter than the limit, return it as is
    if len(path) <= limit:
        return path

    # If there's only one segment, return it as is
    if num_segments == 1:
        return path

    # Keep track of the left and right halves of the path
    left = segments[:-1]
    right = [segments[-1]]

    # Join the left and right halves back together with "..." in the middle
    def join(left, right):
        # # If the right half is empty, return the left half plus "..."
        if len(right) == 0:
            return os.path.join(*left) + os.path.sep + "..."

        # If the left half is empty, return "..." plus the right half
        if len(left) == 0:
            return "..." + os.path.sep + os.path.join(*right)

        # Join the left and right halves back together with "..." in the middle
        return os.path.join(*left) + os.path.sep + "..." + os.path.sep + os.path.join(*right)

    # Loop until we reach the limit or can no longer split the path
    while len(path) > limit and len(segments) > 1:
        # Find the middle of the path segments list
        middle = num_segments // 2

        # Drop the path segment closest to the middle
        if num_segments % 2 == 0:
            # If there is only 1 element in each half, drop from the left half and exit the loop
            if len(right) == 1 and len(left) == 1:
                left.pop(middle - 1)
                path = join(left, right)
                break
            else:
                # If the list has an even number of segments, choose the longer one
                if len(left[middle - 1]) >= len(right[0]):
                    left.pop(middle - 1)
                else:
                    right.pop(0)
        else:
            # If the list has an odd number of segments, just drop the middle one
            left.pop(middle)

        # Update the segments, left, and right lists
        segments = left + right
        num_segments = len(segments)

        left = segments[:middle]
        right = segments[middle:]

        # Update the total length of the path
        path = join(left, right)

    return path


# Minimum supported OneDrive client version, required for the in-browser login
# flow (client v2.5.11+). See version_number() for the encoding.
MIN_CLIENT_VERSION = 20511


def version_number(version: str) -> int:
    """
    Comparable number for a client version string such as 'v2.5.12' or
    'onedrive v2.5.12-master-2bf2f9f': each component is zero-padded to two
    digits (2.5.12 -> 20512), so 2.5.9 < 2.5.11 < 2.6.0. Returns 0 when no
    version can be found.
    """
    match = re.search(r"v?(\d+)\.(\d+)(?:\.(\d+))?", version or "")
    if not match:
        return 0
    return int("".join((part or "0").zfill(2) for part in match.groups()))


def get_installed_client_version(client_bin_path: str) -> int:
    """Installed client version as a version_number(), or 0 if the client is not found."""
    try:
        client_version_check = subprocess.check_output([client_bin_path, "--version"], stderr=subprocess.STDOUT)
        installed_client_version_num = version_number(client_version_check.decode(errors="replace"))
    except Exception:
        logging.error(f"[GUI] Onedrive client not found!")
        installed_client_version_num = 0

    logging.debug(f"[GUI] Installed client version is {installed_client_version_num}")
    return installed_client_version_num


def config_client_bin_path() -> str:
    client_bin_path = gui_settings.get("client_bin_path")
    logging.info(f"Onedrive client location: '{client_bin_path}'")

    if client_bin_path == "":
        return "onedrive"
    else:
        return gui_settings.get("client_bin_path")


def format_relative_time(timestamp):
    """
    Format a datetime timestamp into compact relative time string.
    Examples: "now", "2m ago", "3h ago", "2d ago"
    """
    if timestamp is None:
        return ""

    now = datetime.now()
    delta = now - timestamp
    total_seconds = int(delta.total_seconds())

    if total_seconds < 60:
        return "now"
    elif total_seconds < 3600:  # Less than 1 hour
        minutes = total_seconds // 60
        return f"{minutes}m ago"
    elif total_seconds < 86400:  # Less than 1 day
        hours = total_seconds // 3600
        return f"{hours}h ago"
    else:  # 1 day or more
        days = total_seconds // 86400
        return f"{days}d ago"
