from django.db import models

# Create your models here.
from django.db import models

from datetime import date


class Task(models.Model):
    "Stores a Task"

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)

    created_on = models.DateField(default=date.today)


    # Due date.
    due_date = models.DateField(default=date.today)

    # Meta data about the database table.
    class Meta:
        # Set the table name.
        db_table = 'task'

        # Set default ordering
        ordering = ['id']

    # Define what to output when the model is printed as a string.
    def __str__(self):
        return self.title



