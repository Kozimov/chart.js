from django.db import models

# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    nomi = models.CharField(max_length=50)
    daromadi = models.IntegerField()

    def __str__(self):
        return self.nomi


class Country(models.Model):
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Davlatlar"

    nomi = models.CharField(max_length=50)
    daromadi = models.IntegerField()

    def __str__(self):
        return self.nomi


class BoxChart(models.Model):
    class Meta:
        verbose_name = "BoxChart"
        verbose_name_plural = "Box Chartlar"

    date = models.CharField(max_length=50)
    opens = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    close = models.IntegerField()

    def __str__(self):
        return self.date