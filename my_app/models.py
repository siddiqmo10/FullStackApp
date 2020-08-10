from django.db import models


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateField(auto_now=True)
    # whenever you make changes migrate so python can acces it

    # don't like it says search objects when accessing the searched items
    # so we do this to name it with what we searched
    def __str__(self):
        return '{}'.format(self.search)

    # need to remove s error from searchs in the site
    class Meta:
        verbose_name_plural = 'Searches'
