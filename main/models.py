from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=50)
    rate = models.PositiveIntegerField(default=0, max_length=10, verbose_name="Рейтинг")
    duration = models.DurationField(verbose_name="Продолжительность")
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=500)
    # director = models.ForeignKey('')

    def __str__(self):
        return self.name