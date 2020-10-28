from django.db import models
from django.utils.timezone import now
from django.db.models import Q
from functools import reduce
from .constants import file_path


def files_directory_path(instance, filename):
    """pet images directory"""
    return '{}'.format(filename) + "t_C" + str(now())


class Uploads_MANAGER(models.Manager):
    def create_new_file(self, file):
        return self.create(file=file,created_at=now())

    def get_files(self, keywords=None):
        if keywords:
            keywords = keywords.split(',')
            files = super(Uploads_MANAGER, self).get_queryset().filter(reduce(lambda x, y: x | y, [Q(file__icontains=keyword) for keyword in keywords]))

        else:
            files = super(Uploads_MANAGER, self).get_queryset().all()
        return files

class Uploads(models.Model):
  file = models.FileField(upload_to=files_directory_path, blank=True, null=True)
  created_at = models.DateField(auto_now_add=True)
  objects = Uploads_MANAGER()