from django.db import models

class Lessons(models.Model):
    title = models.CharField(max_length=128,unique=True)
    description = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.title

class Documents(models.Model):
    title = models.CharField(max_length=128,unique=True)
    description = models.TextField(null=False, blank=False)
    document = models.FileField(null=False, blank=False, upload_to='documents/')
    def __str__(self):
        return self.title

class Letters(models.Model):
    title = models.CharField(max_length=4,unique=True)
    image = models.ImageField(null=False, blank=False, upload_to='images/letters/',default='images/letters/default.jpg',)
    audio = models.FileField(null=False, blank=False, upload_to='audio/letters/')
    def __str__(self):
        return self.title

class Numbers(models.Model):
    title = models.CharField(max_length=12,unique=True)
    description = models.TextField(null=False, blank=False)
    audio = models.FileField(null=False, blank=False, upload_to='audio/numbers/')
    def __str__(self):
        return self.title


