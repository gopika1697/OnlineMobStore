from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    price_range=models.CharField(max_length=50)
    genre=models.CharField(max_length=10)
    comp_logo=models.CharField(max_length=1000)

    def __str__(self):
        return self.name+' - '+self.price_range

class Oneplus(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    model_no = models.CharField(max_length=30)
    price=models.IntegerField(default=15000)
    ram=models.CharField(max_length=10)
    battery=models.CharField(max_length=10,default='3000 mAh')
    display_size=models.FloatField(default=5.0)
    display_type=models.CharField(max_length=100,default="AMOLED")
    processor=models.CharField(max_length=200,default='Snapdragon')
    gpu=models.CharField(max_length=40,default='Adreno')
    stockrom=models.CharField(max_length=40,default='Android')
    internal_mem=models.CharField(max_length=50,default="64GB")
    camera_primary=models.CharField(max_length=30,default="16MP,f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.model_name+' - '+self.model_no


class Xiaomi(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    price=models.IntegerField(default=15000)
    ram=models.CharField(max_length=10)
    battery=models.CharField(max_length=10,default='3000 mAh')
    display_size=models.FloatField(default=5.0)
    display_type=models.CharField(max_length=100,default="AMOLED")
    processor=models.CharField(max_length=200,default='Snapdragon')
    gpu=models.CharField(max_length=40,default='Adreno')
    stockrom=models.CharField(max_length=40,default='Android')
    internal_mem=models.CharField(max_length=50,default="64GB")
    camera_primary=models.CharField(max_length=30,default="16MP,f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.model_name


class Samsung(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    price=models.IntegerField(default=15000)
    ram=models.CharField(max_length=10)
    battery=models.CharField(max_length=10,default='3000 mAh')
    display_size=models.FloatField(default=5.0)
    display_type=models.CharField(max_length=100,default="AMOLED")
    processor=models.CharField(max_length=200,default='Snapdragon')
    gpu=models.CharField(max_length=40,default='Adreno')
    stockrom=models.CharField(max_length=40,default='Android')
    internal_mem=models.CharField(max_length=50,default="64GB")
    camera_primary=models.CharField(max_length=30,default="16MP,f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.model_name

class Apple(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    price=models.IntegerField(default=15000)
    ram=models.CharField(max_length=10)
    battery=models.CharField(max_length=10,default='3000 mAh')
    display_size=models.FloatField(default=5.0)
    display_type=models.CharField(max_length=100,default="AMOLED")
    processor=models.CharField(max_length=200,default='Snapdragon')
    gpu=models.CharField(max_length=40,default='Adreno')
    stockrom=models.CharField(max_length=40,default='Android')
    internal_mem=models.CharField(max_length=50,default="64GB")
    camera_primary=models.CharField(max_length=30,default="16MP,f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.model_name
