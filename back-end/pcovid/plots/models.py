from django.db import models


class DataObject(models.Model):
    metric_name = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=30)
    data = models.TextField()

    def __str__(self):
        return self.metric_name
