import usb.core
import usb.util
from threading import Timer

class TTRI_Usb():
    def __init__(self, id_vendor, id_product, polling_interval=1, usb_status_cb=None):
        self._polling_interval = polling_interval
        self._usb_status_cb = usb_status_cb
        self._id_vendor = id_vendor
        self._id_product = id_product
        self._current_status = None
        self._current_status = self.search_ttr_device()

    def start(self):
        self._poll_timer = Timer(self._polling_interval, self.poll)
        self._poll_timer.start()

    def search_ttr_device(self):
        status_changed = False
        dev = usb.core.find(idVendor=self._id_vendor, idProduct=self._id_product)
        if ((dev is None and self._current_status == True) or
                (dev is not None and self._current_status == False)):
            status_changed = True
        self._current_status = (dev != None)
        if(status_changed):
            self._usb_status_cb(self._current_status)

        return (dev != None)


    def poll(self):
        self.search_ttr_device()
        self._poll_timer = Timer(self._polling_interval, self.poll)
        self._poll_timer.start()

if __name__ == "__main__":
    print "Starting USB test"
    app = TTRI_Usb()
    app.start()

