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
        self._playlist_list_edit = QtGui.QListWidget()
        self._playlist_list_label = QtGui.QLabel("Playlists loaded on device")
        self._playlist_tracks_label = QtGui.QLabel("Tracks");
        self._playlist_tracks_list = QtGui.QListWidget()
        self._select_track = QtGui.QPushButton("Add track...");
        self._status = QtGui.QPushButton("Status");
        self._frame_top_left = QtGui.QFrame(self)
        self._frame_top_right = QtGui.QFrame(self)
        self._frame_down_left = QtGui.QFrame(self)
        self._frame_down_right = QtGui.QFrame(self)
        self._frame_top_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self._frame_top_right.setFrameShape(QtGui.QFrame.StyledPanel) 
        self._frame_down_left.setFrameShape(QtGui.QFrame.StyledPanel) 
        self._frame_down_right.setFrameShape(QtGui.QFrame.StyledPanel)
        self._layout_top_left = QtGui.QVBoxLayout()
        self._layout_down_left = QtGui.QVBoxLayout()
        self._layout_top_right = QtGui.QVBoxLayout()
        self._layout_down_right = QtGui.QVBoxLayout()
        self._splitter1 = QtGui.QSplitter(QtCore.Qt.Vertical)
        self._splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        self._splitter3 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self._main_layout = QtGui.QHBoxLayout(self)


        self._layout_top_left.addWidget(self._playlist_title_label)
        self._layout_top_left.addWidget(self._playlist_title_edit)
        self._layout_top_left.addWidget(self._playlist_upload)
        self._layout_down_left.addWidget(self._playlist_list_label)
        self._layout_down_left.addWidget(self._playlist_list_edit)
        self._layout_top_right.addWidget(self._playlist_tracks_label)
        self._layout_top_right.addWidget(self._playlist_tracks_list)
        self._layout_top_right.addWidget(self._select_track)
        self._layout_down_right.addWidget(self._status)

        self._frame_top_left.setLayout(self._layout_top_left)
        self._frame_down_left.setLayout(self._layout_down_left)
        self._frame_top_right.setLayout(self._layout_top_right)
        self._frame_down_right.setLayout(self._layout_down_right)
        self._splitter1.addWidget(self._frame_top_left)
        self._splitter1.addWidget(self._frame_down_left)
        self._splitter2.addWidget(self._frame_top_right)
        self._splitter2.addWidget(self._frame_down_right)
        self._splitter3.addWidget(self._splitter1)
        self._splitter3.addWidget(self._splitter2)
        self._main_layout.addWidget(self._splitter3)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

        self.show()

    def center_ui(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_main_app(self):
        return self._app
