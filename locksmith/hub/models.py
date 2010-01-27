import datetime
from django.db import models
from locksmith.common import KEY_STATUSES

class Api(models.Model):
    name = models.CharField(max_length=30)
    signing_key = models.CharField(max_length=32)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'locksmith_hub_api'

class Key(models.Model):
    key = models.CharField(max_length=32)
    email = models.EmailField()
    issued_by = models.ForeignKey(Api, related_name='keys')
    issued_on = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=1, choices=KEY_STATUSES, default='U')

    def __unicode__(self):
        return self.key

    class Meta:
        db_table = 'locksmith_hub_key'

class Report(models.Model):
    date = models.DateField()
    api = models.ForeignKey(Api, related_name='reports')
    key = models.ForeignKey(Key, related_name='reports')
    endpoint = models.CharField(max_length=100)
    calls = models.IntegerField()
    reported_time = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'locksmith_hub_report'
