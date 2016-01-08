from PIL import Image


def resize(path, testpath=None):
    """ Funtoin for resizing photo
        if it size more than 200x200px.
        args:
            path: path to photo.
            testpath: path for test this method work or not
        returns:
            True: if photo resized and saved successfuly.
            False: if something going wrong.
    """
    try:
        original = Image.open(path)
        width = original.size[0]
        heigth = original.size[1]
        if width > 200 or heigth > 200:
            # calculate ratio
            ratio = min(200.0 / width, 200.0 / heigth)
            # colculate new size
            size = (width * ratio, heigth * ratio)
            # scale image
            original.thumbnail(size, Image.ANTIALIAS)
            if testpath:
                original.save(testpath)
            else:
                original.save(path)
        return True
    except:
        return False
