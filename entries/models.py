from django.db import models
from django.utils import timezone
# Create your models here.
class Entry(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
#Dunder Methods---> the method that start with a double under score(__)
#anther name for this function is "magic methods"
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Entries"


    



# Django tip:
# Django automatically creates a plural verbose name from your object by adding and "s" to the end.
# child -> childs
# To change the plural verbose name, you can define the verbose_name_plural property of the Meta class like so:
