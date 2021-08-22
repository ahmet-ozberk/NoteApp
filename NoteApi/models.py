from django.db import models

# Create your models here.
class NoteModel(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(null=False,max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now=True)

    def __str___(self):
        return self.title
