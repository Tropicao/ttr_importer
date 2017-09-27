import sys
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

    def stop(self):
        self._poll_timer.cancel()

    def search_ttr_device(self):
        status_changed = False
        dev = usb.core.find(idVendor=self._id_vendor, idProduct=self._id_product)
        if ((dev is None and self._current_status == True) or
                (dev is not None and self._current_status == False)):
            status_changed = True
        self._current_status = (dev != None)
        if(status_changed):
            if(self._usb_status_cb != None):
                self._usb_status_cb(self._current_status)
            else:
                print "New device connection status : ", self._current_status

        return (dev != None)


    def poll(self):
        self.search_ttr_device()
        self._poll_timer = Timer(self._polling_interval, self.poll)
        self._poll_timer.start()

    def get_current_status(self):
        return self._current_status

def help():
    print "Python class used to detect a specific USB device connection/disconnection"
    print "Usage : python ttri_usb.py 0x<id_vendor> 0x<id_product> [polling_interval_s]"

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        help()
        exit(1)
    id_vendor = int(sys.argv[1], 16)
    id_product = int(sys.argv[2], 16)
    if (len(sys.argv) > 3):
        interval = int(sys.argv[3])
    else:
        interval = 1
    print "Starting USB detector on device ", hex(id_vendor),":",hex(id_product), ", polling at ", interval, "s."
    app = TTRI_Usb(id_vendor, id_product, interval)
    app.start()

