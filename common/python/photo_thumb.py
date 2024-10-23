
from PIL import Image

def make_thumb(scale,imgfn,thumbfn):
    image = Image.open(imgfn)
    w,h = image.size
    w = w//scale
    h = h//scale
    THUMB_SIZE=(w,h)
    image.thumbnail(THUMB_SIZE)
    image.save(thumbfn)
    print("Thumbnail placed in filename:",thumbfn,file=sys.stderr)