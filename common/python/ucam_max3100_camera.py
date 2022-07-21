
from ucam import uCAM_III_MAX3100

def setup_camera():
    return uCAM_III_MAX3100(spiDevice=(0,0), 
                            resetPin=23,
                            responseDelay=0,
                            syncResponseDelay=0.01)
