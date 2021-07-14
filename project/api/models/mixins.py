import os
import requests

from django.conf import settings


class ImageFromUrlMixin:
    def load_image(self, *, image_url, save=False):
        if self.__class__.objects.exists():
            new_id = self.__class__.objects.latest('id').id + 1
        else:
            new_id = 1
        directory = self.__class__.image.field.upload_to
        try:
            response = requests.get(image_url)
            if not os.path.isdir(settings.MEDIA_ROOT / f'{directory}'):
                os.mkdir(settings.MEDIA_ROOT / f'{directory}')
            with open(
                settings.MEDIA_ROOT / f'{directory}/{new_id}_pic.jpg',
                'wb'
            ) as image:
                image.write(response.content)
                self.image = f'{directory}/{new_id}_pic.jpg'
            if save:
                self.save()
        except requests.exceptions.ConnectionError:
            pass
