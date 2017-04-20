from django.db import models

# Create your models here.    

class Page(models.Model):
    name = models.CharField(max_length=32, db_index=True, unique=True)
    url = models.CharField(max_length=128, db_index=True, unique=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    keywords = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)      
    
    def __unicode__(self):
        return str(self.name)
    
    
class PageContent(models.Model):
    page = models.ForeignKey(Page, related_name="page_name")
    container = models.CharField(max_length=32)
    content = models.TextField()
    
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  
    
    def __unicode__(self):
        return self.page.name    