from django.test import TestCase
from PIL import Image

from fortytwo_test_task.settings import BASE_DIR
from apps.contact.resizeimg import resize, size


class OwnerPhotoResize(TestCase):
    """Test for owner photo resizing."""
    def test_resizing_owner_photo_and_save_instaed_original_photo(self):
        """ Test resizing and saving photo instaed original
            photo with same name and ration, max size 200x200px.
        """
        path = '%s/%s' % (
            BASE_DIR, 'apps/contact/tests/data/test_img.jpg'
        )
        testpath = '%s/%s' % (
            BASE_DIR, 'apps/contact/tests/data/test_img_200x200.jpg'
        )
        original = Image.open(path)
        # calculate ratio
        ratio = min(200.0 / original.size[0], 200.0 / original.size[1])
        # calculate new image size
        new_size = (original.size[0] * ratio,  original.size[1] * ratio)
        # resize image and save with testpath
        if not size(path):
            resize(path, testpath)
            test_img = Image.open(testpath)
            # compare test image size with our new_size
            self.assertEqual(new_size[0], test_img.size[0])
            self.assertEqual(new_size[1], test_img.size[1])
