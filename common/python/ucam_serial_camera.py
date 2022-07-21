
from ucam import uCAM_III_Serial

def setup_camera():
    return uCAM_III_Serial(serialDevice="/dev/serial0", 
                           resetPin=23,
                           responseDelay=0.2,
                           syncResponseDelay=0.05)
