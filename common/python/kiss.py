
__all__ = [ "kiss_encode", "kiss_decode" ]

FEND=b'\xc0' # Frame End
FESC=b'\xdb' # Frame Escape
TFEND=b'\xdc' # Transposed Frame End
TFESC=b'\xdd' # Transposed Frame Escape 
REPFEND=FESC+TFEND
REPFESC=FESC+TFESC
HEADER=FEND+b'\x00'

def kiss_encode(buffer):
    buffer = buffer.replace(FESC,REPFESC)
    buffer = buffer.replace(FEND,REPFEND)
    return HEADER + buffer + FEND

def kiss_decode(buffer):
    assert buffer[:1] == FEND
    assert buffer[-1:] == FEND
    buffer = buffer.strip(FEND)[1:]
    buffer = buffer.replace(REPFEND,FEND)
    buffer = buffer.replace(REPFESC,FESC)
    return buffer
    
if __name__ == "__main__":

   import random

   buffer = bytes([ random.randint(0,255) for i in range(0,10240000) ])
   buffer1 = kiss_encode(buffer)
   buffer2 = kiss_decode(buffer1)
   assert buffer == buffer2
