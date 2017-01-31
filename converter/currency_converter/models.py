from django.db import models

# Create your models here.

class history(models.Model):

      Date = models.DateField()
      From = models.CharField(max_length=10)
      To = models.CharField(max_length=10)
      From_value = models.DecimalField(max_digits=10, decimal_places=2)
      To_value = models.DecimalField(max_digits=10, decimal_places=2)

      def __unicode__(self):
      	return self.Date



