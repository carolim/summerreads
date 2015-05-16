from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import AnonymousRatingField

class Book(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    CURRENT = 'CUR'
    FINISHED = 'FIN'
    WANT_TO_READ = 'WNT'
    READING_STATUS_CHOICES = (
    	(CURRENT, 'Currently Reading'),
    	(FINISHED, 'Finished Reading'),
    	(WANT_TO_READ, 'Want to Read'),
    	)
    reading_status = models.CharField(max_length=3,
    									choices=READING_STATUS_CHOICES,
    									default=WANT_TO_READ)
    # rating = AnonymousRatingField(range=5, can_change_vote=True)
    quotes = models.ManyToManyField('Quote', blank=True, null=True)


class Quote(models.Model):
    page_number = models.CharField(max_length=10, blank=True, null=True)
    text = models.TextField()