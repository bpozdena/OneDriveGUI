import sys
from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import *


class LayerObject(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.enabled = kwargs.get('enabled', False)


class LayerManager(QtGui.QWidget):
    def __init__(self):
        super(LayerManager, self).__init__()
        self.resize(400, 300)
        self.list_widget = QtGui.QListWidget()
        main_layout = QtGui.QHBoxLayout(self)
        main_layout.addWidget(self.list_widget)
        self.add_layers()

    def add_layers(self):
        layers = [
            LayerObject(name='Layer001', enabled=False),
            LayerObject(name='Layer002', enabled=False),
            LayerObject(name='Layer003', enabled=True),
            LayerObject(name='Layer004', enabled=False),
            LayerObject(name='Layer005', enabled=True),
            LayerObject(name='Layer006', enabled=False),
            LayerObject(name='Layer007', enabled=False),
            LayerObject(name='Layer008', enabled=True),
            LayerObject(name='Layer009', enabled=False),
            LayerObject(name='Layer010', enabled=True)
        ]

        for x in layers:
            widget = LayerWidget(layer=x)
            item =  QtGui.QListWidgetItem()
            self.list_widget.insertItem(self.list_widget.count(), item)
            self.list_widget.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())


    # properties
    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, value):
        self._layer== value
        self.ui_layername.setText(value.name)
        self.ui_enabled.setChecked(value.enabled)


class LayerManager(QWidget):
    def __init__(self):
        super(LayerManager, self).__init__()
        self.resize(400, 300)

        # controls
        self.ui_scroll = QWidget()
        self.ui_scroll_layout = QtGui.QVBoxLayout()
        self.ui_scroll.setLayout(self.ui_scroll_layout)

        self.ui_scroll_area = QtGui.QScrollArea()
        self.ui_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ui_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui_scroll_area.setWidgetResizable(True)
        self.ui_scroll_area.setWidget(self.ui_scroll)

        main_layout = QtGui.QHBoxLayout()
        main_layout.addWidget(self.ui_scroll_area)
        self.setLayout(main_layout)


        self.add_layers()

    def add_layers(self):
        layers = [
            LayerObject(name='Layer001', enabled=False),
            LayerObject(name='Layer002', enabled=False),
            LayerObject(name='Layer003', enabled=True),
            LayerObject(name='Layer004', enabled=False),
            LayerObject(name='Layer005', enabled=True),
            LayerObject(name='Layer006', enabled=False),
            LayerObject(name='Layer007', enabled=False),
            LayerObject(name='Layer008', enabled=True),
            LayerObject(name='Layer009', enabled=False),
            LayerObject(name='Layer010', enabled=True)
        ]

        for x in layers:
            widget = LayerWidget(layer=x)
            self.ui_scroll_layout.addWidget(widget)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = LayerManager()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()