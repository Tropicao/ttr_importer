import sys
from ttri_ui import TTRI_Ui

class TTRI_App():

    def __init__(self, argv):
        self._ui = TTRI_Ui(sys.argv)
        self._app = self._ui.get_main_app()
        if self._app is None:
            print "Error retrieving Qt main app"
            exit(1)

    def start(self):
        sys.exit(self._app.exec_())

if __name__ == "__main__":
    print "Initializing app"
    app = TTRI_App(sys.argv)
    print "Starting app"
    app.start()
    print "Exiting app"
