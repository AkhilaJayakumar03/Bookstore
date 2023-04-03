from django.db import models

# Create your models here.


class bookupmodel(models.Model):
    bookname=models.CharField(max_length=40)
    author=models.CharField(max_length=40)
    bookimage=models.FileField(upload_to='bookapp/static')
    date = models.DateTimeField(auto_now_add=True)
    bookpdf=models.FileField(upload_to='bookapp/static')
    def __str__(self):
        return self.bookname
