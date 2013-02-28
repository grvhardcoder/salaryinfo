from django.db import models
from django.contrib.auth.models import User
 
class UserProfile(models.Model):
    username = models.OneToOneField(User)
    email    = models.EmailField(max_length=20)
    password1 = models.TextField(max_length=20)   
    password2 = models.TextField(max_length=20)
    
    def __unicode__(self):
        return u'%s %s' % (self.username, self.email) 
    
    class Admin:
        pass
