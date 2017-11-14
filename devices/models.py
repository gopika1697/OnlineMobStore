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
class Cart(models.Model):
    user_name=models.CharField(max_length=50,unique=True)
    item1=models.CharField(max_length=50,null=True)
    qt1=models.IntegerField(default=1)
    price1=models.BigIntegerField(default=0)
    status1=models.CharField(max_length=20,default="not bought")
    item2=models.CharField(max_length=50,null=True)
    qt2=models.IntegerField(default=1)
    price2=models.BigIntegerField(default=0)
    status2=models.CharField(max_length=20,default="not bought")
    item3=models.CharField(max_length=50,null=True)
    qt3=models.IntegerField(default=1)
    price3=models.BigIntegerField(default=0)
    status3=models.CharField(max_length=20,default="not bought")
    total=models.BigIntegerField(default=0)
    def __str__(self):
        return self.user_name+' cart '
    def save(self,*args,**kwargs):
        self.total=(self.qt1*self.price1)+(self.qt2*self.price2)+(self.qt3*self.price3)
        super(Cart,self).save(*args, **kwargs)


class Address(models.Model):
    user_name=models.CharField(max_length=50,unique=True)
    doorno=models.CharField(max_length=20)
    streetname=models.CharField(max_length=100)
    locality=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=10)
    contact=models.CharField(max_length=20)
    def __str__(self):
        return self.user_name+' addr'
class Lenovo(models.Model):
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
    camera_primary=models.CharField(max_length=30,default="16MP, f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.model_name
class Motorola(models.Model):
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
    camera_primary=models.CharField(max_length=30,default="16MP, f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.model_name
class Asus(models.Model):
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
    camera_primary=models.CharField(max_length=30,default="16MP, f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.model_name
class Sony(models.Model):
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
    camera_primary=models.CharField(max_length=30,default="16MP, f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.model_name
class Google(models.Model):
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
    camera_primary=models.CharField(max_length=30,default="16MP, f/2.0")
    album_logo=models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.model_name

class LG(models.Model):
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
