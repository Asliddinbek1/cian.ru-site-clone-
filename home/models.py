from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name



class Cities(models.Model):
    name = models.CharField(max_length=35)
    
    def __str__(self) -> str:
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateField()
    publisher = models.CharField(max_length=20)
    city = models.ForeignKey(Cities,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',default=True)
    image = models.ImageField(upload_to='images',default=True)
    def __str__(self) -> str:
        return  f'{self.name} {self.price}'

    
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=40) 
    phone = models.IntegerField()

    def __str__(self) -> str:
        return self.name





