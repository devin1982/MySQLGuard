from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)

class Pstat(models.Model):
    trx_id = models.CharField(max_length=200,null=True)
    trx_mysql_thread_id = models.CharField(max_length=200,null=True)
    user = models.CharField(max_length=200,null=True)
    host = models.CharField(max_length=200,null=True)
    dhost = models.CharField(max_length=200,null=True)
    db = models.CharField(max_length=200,null=True)
    command = models.CharField(max_length=200,null=True)
    time = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    

    info = models.TextField()
    trx_stat = models.CharField(max_length=200,null=True)
    trx_wait_started = models.CharField(max_length=200,null=True)
    trx_query = models.TextField()
    blocking_trx_id = models.CharField(max_length=200,null=True)
    is_blocker = models.CharField(max_length=200,null=True)
    create_time = models.DateTimeField()

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username    
