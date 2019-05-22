from django.db import models
from django.utils.text import slugify

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    department_id = models.IntegerField()
    allocated_time= models.IntegerField()
    doctor_id = models.IntegerField()
    reg_num = models.IntegerField()
    image = models.ImageField(upload_to='doctors/')
    slug = models.SlugField(blank=True, null= True)




    def save(self , *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Doctors , self).save(*args , **kwargs)


    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'


    
    def __str__(self):
        return self.name