#!/bin/env python3
import sys, os.path, shutil, glob

scriptdir = os.path.split(sys.argv[0])[0]

step = sys.argv[1]
hostname = sys.argv[2]
password = sys.argv[3]

if hostname.startswith('satellite'):
    config = 'payload-board'
elif hostname.startswith('ground'):
    config = 'ground-station'
else:
    raise ValueError("Unexpected hostname: "+hostname)

shutil.copyfile(os.path.join(scriptdir,'../setup.sh'),
                os.path.join(scriptdir,'step1','setup.sh'))

allfiles = [ os.path.split(f)[1] for f in glob.glob(step+"/*") ]

for file in allfiles:
    print("Copying",file)
    local = os.path.join(scriptdir,step,file)
    shutil.copyfile(local,"boot/"+file)

def fixlines(filename, **kwargs):
    data = open(filename).read()
    wh = open(filename, "wt", newline="\n")
    for k,v in kwargs.items():
        data = data.replace(k,v)
    wh.write(data)
    wh.close()

details = dict(XXXXHOSTNAMEXXXX=hostname,
               XXXXCONFIGXXXX=config,
               XXXXPASSWORDXXXX=password)
for file in allfiles:
    fixlines("boot/"+file,**details)

