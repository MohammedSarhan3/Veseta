from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
TYPE_OF_PESRON=(
    ('Male',"Male"),
    ('Femal',"Femal")

)
DOCTORS_IN=(
    ('عظام',"عظام"),
    ('جلديه',"جلديه"),
    ('أسنان',"أسنان")

)
class Profile(models.Model):
    user=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الإسم :"), max_length=80)
    subtitle=models.CharField(_("نبذة عنك :"), max_length=50,null=True,blank=True)
    adress=models.CharField(_("المحافظة:"), max_length=50,null=True,blank=True)
    adress_detail=models.CharField(_("العنوان بالتفصيل:"), max_length=50,null=True,blank=True)
    number_phone=models.IntegerField(_("رقم الهاتف :"),null=True,blank=True)
    working_hours=models.IntegerField(_(" ساعات العمل :"),null=True,blank=True)
    wating_time=models.IntegerField(_(" مدة الإنتظار :"),null=True,blank=True)
    spcalist_doctor=models.CharField(_("متخصص في ؟ :"), max_length=500,null=True,blank=True)
   
    join_new=models.DateField( auto_now_add=True,null=True,blank=True)
    type=models.CharField(_("النوع: "),choices=TYPE_OF_PESRON, max_length=50,null=True,blank=True)
    
    
    who_i=models.TextField(_(" من أنا : "),max_length=500,null=True,blank=True)
    doctor=models.CharField(_(" دكتور؟:"), choices=DOCTORS_IN,max_length=50,null=True,blank=True)
   
    price=models.IntegerField(_("السعر: "),null=True,blank=True)
    image=models.ImageField(_(" صورة لك:  "),upload_to='profile',null=True,blank=True)
    slug=models.SlugField(_("slug"),null=True,blank=True)
    facebook=models.CharField(_("facebook"), max_length=50,null=True,blank=True)
    twiter=models.CharField(_("twiter"), max_length=50,null=True,blank=True)
    google=models.CharField(_("google"), max_length=50,null=True,blank=True)



    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return self.user.username 

def creat_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
      
post_save.connect(creat_profile,sender=User)





from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
TYPE_OF_PESRON=(
    ('Male',"Male"),
    ('Femal',"Femal")

)
class Profile(models.Model):
    user=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الإسم :"), max_length=80)
    subtitle=models.CharField(_("نبذة عنك :"), max_length=50)
    adress=models.CharField(_("المحافظة:"), max_length=50)
    adress_detail=models.CharField(_("العنوان بالتفصيل:"), max_length=50)
    number_phone=models.IntegerField(_("رقم الهاتف :"))
    working_hours=models.IntegerField(_(" ساعات العمل :"),null=True,blank=True)
    wating_time=models.IntegerField(_(" مدة الإنتظار :"),null=True,blank=True)
    doctor=models.CharField(_(" دكتور؟:"), max_length=50,null=True,blank=True)
    spcalist_doctor=models.CharField(_("متخصص في ؟ :"), max_length=500,null=True,blank=True)
   
    join_new=models.DateField( auto_now_add=True,null=True,blank=True)
    type=models.CharField(_("النوع: "),choices=TYPE_OF_PESRON, max_length=50)
    
    
    who_i=models.TextField(_(" من أنا : "),max_length=500)
   
    price=models.IntegerField(_("السعر: "),null=True,blank=True)
    image=models.ImageField(_(" صورة لك:  "),upload_to='profile',null=True,blank=True)
    slug=models.SlugField(_("slug"),null=True,blank=True)
    facebook=models.CharField(_("facebook"), max_length=50,null=True,blank=True)
    twiter=models.CharField(_("twiter"), max_length=50,null=True,blank=True)
    google=models.CharField(_("google"), max_length=50,null=True,blank=True)



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
