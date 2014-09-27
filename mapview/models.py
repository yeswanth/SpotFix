from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_by = models.ForeignKey(User,verbose_name='user',editable=False,related_name='%(app_label)s_%(class)s_created_set')
    last_edited_by = models.ForeignKey(User,editable=False,related_name='%(app_label)s_%(class)s_edited_set')
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class Tag(BaseModel):
    tag = models.CharField(max_length=20)

class Issue(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    #photo = models.FileField()
    tags = models.ForeignKey(Tag,null=True,blank=True)

    
    
    

