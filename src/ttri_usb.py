import usb.core
import usb.util
from threading import Timer

class TTRI_Usb():
    def __init__(self, polling_interval=1):
        self._polling_interval = polling_interval
        self._poll_timer = Timer(self._polling_interval, self.poll)
        self._poll_timer.start()

    def search_ttr_device(self):
        dev = usb.core.find(idVendor=0x1390, idProduct=0x7475)
        if dev is None:
            print "Device not connected ..."
            return False
        print "Device connected !"
        return True

    def poll(self):
        self.search_ttr_device()
        self._poll_timer = Timer(self._polling_interval, self.poll)
        self._poll_timer.start()

if __name__ == "__main__":
    print "Starting USB test"
    app = TTRI_Usb()

