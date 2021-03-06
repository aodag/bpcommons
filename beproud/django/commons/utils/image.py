# vim:fileencoding=utf-8
import os
import re
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from PIL import Image

def valid_image(image):
    try:
        Image.open(image)
    except IOError:
        return False
    image.seek(0)
    return True

def optimize_resize(image,size):
    frm = image.format
    w, h = image.size
    box = () 
    if w < h :
        s = (h - w) / 2
        box = (0, s, w, s + w)
    else :
        s = (w-h) / 2
        box = (s, 0, s + h, h)
    image = image.crop(box)
    image = image.resize(size, Image.ANTIALIAS)
    return image

def make_content_image_file(image, size=None):
    """ """
    from django.core.files.base import ContentFile
    format = image.format
    if size:
        image = image.resize(size, Image.ANTIALIAS);
    sio = StringIO()
    image.save(sio, format)
    return ContentFile(sio.getvalue());

def get_image_size(fileobj, limit=None):
    image = Image.open(fileobj)
    w, h = image.size
    if limit:
        if max(w, h) > limit:
            if w > h:
                h = h * limit / w
                w = limit
            else:
                w = w * limit / h
                h = limit
    return w, h
