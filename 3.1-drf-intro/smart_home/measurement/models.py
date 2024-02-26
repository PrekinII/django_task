from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True, verbose_name='image')
