from django.db import models
from django.core.urlresolvers import reverse

class Thread(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('thread_detail', args=[self.pk])

class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    author = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s: %s...' % (self.author, self.content[:10])