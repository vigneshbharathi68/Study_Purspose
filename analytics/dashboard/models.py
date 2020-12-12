from django.db import models

# Create your models here


class StateWiseTesting(models.Model):
    date = models.DateField()
    state = models.CharField(max_length=100)
    total_samples = models.IntegerField()
    negative = models.IntegerField()
    positive = models.IntegerField()

    def __str__(self):
        return '{} \t {} \t {}'.format(
            self.date,
            self.state,
            self.positive)
