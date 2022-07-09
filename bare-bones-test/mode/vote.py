
# Adapted from code written by Jalin
# https://github.com/silver-sat/payload2/blob/main/vote.py

def voting(PINS):
    count = 0
    for pin in PINS:
        if pin:
            count += 1
    if count >= 2:
        return True
    return False