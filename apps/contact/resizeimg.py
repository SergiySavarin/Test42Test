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
        if original.size[0] > 200 or original.size[1] > 200:
            # calculate ratio
            ratio = min(200.0 / original.size[0], 200.0 / original.size[1])
            # colculate new size
            size = (original.size[0] * ratio,  original.size[1] * ratio)
            original.thumbnail(size, Image.ANTIALIAS)
            if testpath:
                original.save(testpath)
            else:
                original.save(path)
        return True
    except:
        return False
