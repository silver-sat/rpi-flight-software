# See: https://forums.raspberrypi.com/viewtopic.php?t=255770#p1560095

import RPi.GPIO as GPIO

def test_jumper(pins):

    # Assumes two general GPIO pins...
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # floating
    GPIO.setup(pins[0], GPIO.IN)

    GPIO.setup(pins[1], GPIO.IN, GPIO.PUD_UP)
    v1 = GPIO.input(pins[0])

    GPIO.setup(pins[1], GPIO.IN, GPIO.PUD_DOWN)
    v2 = GPIO.input(pins[0])

    return (v1 == 1) and (v2 == 0)

def test_jumpers(pins):

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # floating pins 1,2,3
    for p in pins[1:]:
        GPIO.setup(p, GPIO.IN)
        
    GPIO.setup(pins[0], GPIO.IN, GPIO.PUD_UP)
    v1 = [ GPIO.input(p) for p in pins[1:] ]
    
    GPIO.setup(pins[0], GPIO.IN, GPIO.PUD_DOWN)
    v2 = [ GPIO.input(p) for p in pins[1:] ]

    values = [ ((v1i == 1) and (v2i == 0)) for v1i,v2i in zip(v1,v2) ]
    if True in values:
        return (values.index(True) + 1)
    return 0        

if __name__ == "__main__":

    import pins

    print(test_jumpers(pins.JUMPERS))
