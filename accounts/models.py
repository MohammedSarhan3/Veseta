from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الإسم :"), max_length=80)
    who_i=models.TextField(_("نبذة عنك:  "),max_length=500)
    price=models.IntegerField(_("السعر: "),null=True,blank=True)
    image=models.ImageField(_(" صورة لك:  "),upload_to='profile',null=True,blank=True)
    slug=models.SlugField(_("slug"),null=True,blank=True)
    facebook=models.CharField(_("facebook"), max_length=50,null=True,blank=True)
    twiter=models.CharField(_("facebook"), max_length=50,null=True,blank=True)
    google=models.CharField(_("facebook"), max_length=50,null=True,blank=True)



    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return str(self.user.username) 

def creat_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
      
post_save.connect(creat_profile,sender=User)