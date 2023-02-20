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

if __name__ == "__main__":

    import pins

    if test_jumper(pins.JUMPER):
		    print "TRUE"
    else:
		    print "FALSE"
