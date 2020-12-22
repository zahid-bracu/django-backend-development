from django.db import models

# Create your models here.
# class person(models.Model):
#     id=models.AutoField(primary_key=True)
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=30)


class Musician(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,blank=False)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=100)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    
    rating=(
        (1,'worst'),
        (2,'Bad'),
        (3,'Not Bad'),
        (4,'Good'),
        (5,'Excellent')
    )
    
    num_stars=models.IntegerField(choices=rating)
    def __str__(self):
        return self.name




