
import sys, os.path, shutil

scriptdir = os.path.split(sys.argv[0])[0]

hostname = sys.argv[1]
password = sys.argv[2]

if hostname.startswith('satellite'):
    config = 'payload-board'
elif hostname.startswith('ground'):
    config = 'ground-station'
else:
    raise ValueError("Unexpected hostname: "+hostname)

allfiles = [ "config.txt", "cmdline.txt", "setup.sh", "params.sh", 
             "firstrun.sh", "runsetup.service", "runsetup.sh" ]

shutil.copyfile(os.path.join(scriptdir,'../setup.sh'),
                os.path.join(scriptdir,'setup.sh'))

for file in allfiles:
    print("Copying",file)
    local = os.path.join(scriptdir,file)
    shutil.copyfile(local,"d:\\"+file)

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
    fixlines("d:\\"+file,**details)

