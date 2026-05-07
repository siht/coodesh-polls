from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)


class Choice(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    text = models.CharField(max_length=256, blank=False, null=False)


class Vote(models.Model):
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
