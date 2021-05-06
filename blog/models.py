"""
mysite URL Configuration


importing requirements


class Post(models.Model): – this line defines our model (it is an object).


author(ForeignKey): the user
title(CharField): title of blog
text(TextField): place to ente content of blog
created_date(DateTimeField): time of creation
published_date(DateTimeField): time of publishing


ForeignKey – this is a link to another model.
CharField – this is how you define text with a limited number of characters.
TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
DateTimeField – this is a date and time.

"""



from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #publish function

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #fuction to nicely printable string representation of an object

    def __str__(self):
        return self.title
