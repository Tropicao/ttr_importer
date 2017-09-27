import sys
from ttri_ui import TTRI_Ui
from ttri_usb import TTRI_Usb

class TTRI_App():

    def __init__(self, argv):
        self._ui = TTRI_Ui(sys.argv)
        self._usb = TTRI_Usb(0x1390, 0x7475, 1, self.usb_status_cb)
        self._app = self._ui.get_main_app()
        self.set_device_status(self._usb.get_current_status())
        if self._app is None:
            print "Error retrieving Qt main app"
            exit(1)

    def start(self):
        self._usb.start()
        sys.exit(self._app.exec_())

    def stop(self):
        self._ui.stop()
        self._usb.stop()
        self._app.exec_()

    def set_device_status(self, value):
        if value == True:
            self._ui.set_status("Device connected")
        else:
            self._ui.set_status("Device disconnected")

    def usb_status_cb(self, status):
        self.set_device_status(status)

if __name__ == "__main__":
    print "Initializing app"
    app = TTRI_App(sys.argv)
    print "Starting app"
    app.start()
    print "Exiting app"
