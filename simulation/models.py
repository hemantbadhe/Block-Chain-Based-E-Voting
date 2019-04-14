import datetime, uuid, random

from django.contrib.auth.models import AbstractUser, User
from django.db import models


def get_vote():
    return random.randint(1, 3)


def get_timestamp():
    return datetime.datetime.now().timestamp()


class UserDetail(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # gender = models.CharField(choices=GENDER_CHOICES, max_length=112, blank=True, null=True)
    # contact_no = models.CharField(max_length=15, blank=True, null=True)
    # address = models.CharField(max_length=512, blank=True, null=True)
    public_key = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        ordering = ['-created_at', ]
        pass


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vote = models.IntegerField(default=get_vote)
    timestamp = models.FloatField(default=get_timestamp)
    # Not ForeignKey! See transactions() in simulation.views for implications
    block_id = models.IntegerField(null=True)

    def __str__(self):
        return "{}|{}|{}".format(self.id, self.vote, self.timestamp)


class Block(models.Model):
    prev_h = models.CharField(max_length=64, blank=True)
    merkle_h = models.CharField(max_length=64, blank=True)
    h = models.CharField(max_length=64, blank=True)
    nonce = models.IntegerField(null=True)
    timestamp = models.FloatField(default=get_timestamp)

    def __str__(self):
        return str(self.id)


class VoteBackup(models.Model):
    """This model acts as backup; its objects shall never be tampered."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vote = models.IntegerField(default=get_vote)
    timestamp = models.FloatField(default=get_timestamp)
    block_id = models.IntegerField(null=True)

    def __str__(self):
        return "{}|{}|{}".format(self.id, self.vote, self.timestamp)
