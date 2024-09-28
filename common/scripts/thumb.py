#!/usr/bin/env python3

import sys
from PIL import Image

imgfn = sys.argv[1]
assert(imgfn.endswith('.jpg'))
basefn = imgfn.rsplit('.',1)[0]

if len(sys.argv) > 2:
    outfn = sys.argv[2]
else:
    outfn = basefn + ".thumb.jpg"

image = Image.open(imgfn)
# print(image.info)

THUMB_SIZE=(128,96)
image.thumbnail(THUMB_SIZE)

image.save(outfn)
