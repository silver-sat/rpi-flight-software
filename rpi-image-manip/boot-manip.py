#!/bin/env python3
import sys, os.path, shutil, glob

scriptdir = os.path.split(sys.argv[0])[0]

boot = sys.argv[1]
step = sys.argv[2]
hostname = sys.argv[3]
password = sys.argv[4]
release = sys.argv[5]

if hostname.startswith('satellite'):
    config = 'payload-board'
    hostbase = 'satellite'
elif hostname.startswith('ground'):
    config = 'ground-station'
    hostbase = 'ground'
else:
    raise ValueError("Unexpected hostname: "+hostname)

if step == "step1":
    for fn in ("setup.sh", "VERSION"):
        shutil.copyfile(os.path.join(scriptdir,'../'+fn),
                        os.path.join(scriptdir,'step1',fn))

allfiles = list(glob.glob(step+"/*")) + list(glob.glob(step+"-"+hostbase+"/*"))

for file in allfiles:
    local = os.path.join(scriptdir,file)
    bootfile = os.path.split(file)[1]
    print("Copying",file,"to",boot+"/"+bootfile)
    shutil.copyfile(local,boot+"/"+bootfile)

def fixlines(filename, **kwargs):
    data = open(filename).read()
    wh = open(filename, "wt", newline="\n")
    for k,v in kwargs.items():
        data = data.replace(k,v)
    wh.write(data)
    wh.close()

details = dict(XXXXHOSTNAMEXXXX=hostname,
               XXXXCONFIGXXXX=config,
               XXXXPASSWORDXXXX=password,
               XXXXRELEASEXXXX=release)
for file in allfiles:
    bootfile = os.path.split(file)[1]
    fixlines(boot+"/"+bootfile,**details)

