from django.db import models
from django.core.validators import FileExtensionValidator


class PDFFile(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Файл',
                            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return self.file.file.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Photo(models.Model):
    # photo = models.ImageField(verbose_name='Фото', upload_to='images/')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотки'


class PhotoItem(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

