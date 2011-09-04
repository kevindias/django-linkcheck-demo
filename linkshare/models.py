from django.db import models


class Post(models.Model):
    """Lets users share a url with a title and comment."""
    id = models.AutoField(primary_key=True, db_column='post_id')
    title = models.CharField(max_length=255)
    link = models.URLField(verify_exists=False)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/post/%s/' % self.id
