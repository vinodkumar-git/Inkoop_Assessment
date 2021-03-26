from django.db import models
from PIL import Image

# Create your models here.
class Document(models.Model):
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=100)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', default='abc')
    final_docfile = models.FileField(upload_to='documents/%Y/%m/%d', default='abc')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.docfile.path)
        h = int(self.height)
        w = int(self.width)
        output_size = (h,w)
        img.thumbnail(output_size)
        img.save(self.final_docfile.path)

