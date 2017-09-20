from PyQt4 import QtGui, QtCore

class TTRI_Ui(QtGui.QWidget):

    def __init__(self, argv):
        self._app = QtGui.QApplication(argv)
        super(TTRI_Ui, self).__init__()
        self.init_ui()
        self.center_ui()

    def init_ui(self):
        
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('TomTom Runner Importer')

        self._playlist_title_edit = QtGui.QLineEdit()
        self._playlist_title_label = QtGui.QLabel("Playlist title")
        self._playlist_upload = QtGui.QPushButton("Upload")
        self._playlist_list_edit = QtGui.QTextEdit()
        self._playlist_list_label = QtGui.QLabel("Playlists loaded on device")
        self._playlist_tracks_label = QtGui.QLabel("Tracks");
        self._playlist_tracks_list = QtGui.QTextEdit()
        self._status = QtGui.QPushButton("Status");
        
        self._grid = QtGui.QGridLayout()
        self._grid.addWidget(self._playlist_title_label, 0, 0)
        self._grid.addWidget(self._playlist_title_edit, 1, 0)
        self._grid.addWidget(self._playlist_upload, 3, 0)
        self._grid.addWidget(self._playlist_list_label, 4, 0)
        self._grid.addWidget(self._playlist_list_edit, 5, 0, 5, 1)
        self._grid.addWidget(self._playlist_tracks_label, 0, 1)
        self._grid.addWidget(self._playlist_tracks_list, 1, 1, 6, 1)
        self._grid.addWidget(self._status, 7, 1)
        self.setLayout(self._grid)

        self.show()

    def center_ui(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_main_app(self):
        return self._app
