from django.db import models

# Create your models here.

class regestration(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Number=models.CharField(max_length=12)
    File=models.FileField(upload_to="static")
    Image=models.ImageField(upload_to="Image")
    Password=models.CharField(max_length=10)
    Repassword=models.CharField(max_length=10)

    class Meta:
        db_table="regestration"
