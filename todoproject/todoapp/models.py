from django.db import models


# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField()
    options = models.TextField()
    createdDate = models.DateField(auto_now=True)
     