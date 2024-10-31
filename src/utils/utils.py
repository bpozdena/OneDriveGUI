import os


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
