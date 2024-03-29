
import traceback
import sys
import time

def take_photo(camera, filename, max_attempts=20):
    attempt = 0
    while True:
    
        if attempt >= max_attempts:
            print("Connect w/ camera failed after",attempt,"attempts.",file=sys.stderr)
            return False
            
        print("Connect w/ camera, attempt",attempt+1,file=sys.stderr)
        attempt += 1
        camera.reset()
        try:
            camera.sync()
        except:
            time.sleep(1)
            continue
        try:
            camera.set_baud(camera.baudRate)
        except:
            time.sleep(1)
            continue
        break
        
    time.sleep(2)
    
    camera.takephoto()

    time.sleep(2)

    print("Save photo",file=sys.stderr)
    
    try:
        camera.savePicture(filename)
        print("Photo placed in filename:",filename,file=sys.stderr)
        return True
    except:
        traceback.print_exc()
    return False

