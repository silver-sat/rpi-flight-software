
import os, os.path

def make_ssdv(imgfn,ssdvfn):
    os.system("sh /home/pi/.ssdv.sh %s %s"%(imgfn,ssdvfn))
    if os.path.exists(ssdvfn):
        print("SSDV packets placed in filename:",ssdvfn,file=sys.stderr)