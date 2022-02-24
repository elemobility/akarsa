from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Admin(models.Model):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    phone_number=models.IntegerField()
    gender=models.CharField(max_length=15,choices=(("Male","Male"),("Female","Female"),("Others","Others")))
    country_code=models.IntegerField()
    address_line_1=models.CharField(max_length=200)
    address_line_2=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='customer/profile_image')
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    otp=models.CharField(max_length=200)
    is_user_blocked=models.BooleanField(default=False)
    date_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
        return str(self.id)


class Cms(models.Model):
    name=models.CharField(max_length=200,unique=True)
    content = models.TextField()
    def __str__(self):
        return self.name

class Faq_category(models.Model):
    category_name=models.TextField()
    def __str__(self):
        return self.category_name


class Faq(models.Model):
    category=models.ForeignKey(Faq_category,on_delete=models.CASCADE,related_name='faqs')
    question=models.CharField(max_length=200)
    answer=models.TextField()
    def __str__(self):
        return str(self.id)

class Social_media_settings(models.Model):
    appstore_link=models.CharField(max_length=2000)
    playstore_link=models.CharField(max_length=2000)
    company_url=models.CharField(max_length=2000)
    facebook_url=models.CharField(max_length=2000)
    twitter_url=models.CharField(max_length=2000)
    instagram_url=models.CharField(max_length=2000)
    linkedin_url=models.CharField(max_length=2000)
    youtube_url=models.CharField(max_length=2000)
    def __str__(self):
        return str(self.id)


   
class General_settings(models.Model):
    company_name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=30)
    website_url = models.CharField(max_length=3, null=True, blank=True)
    company_email = models.EmailField(verbose_name="email", max_length=60)
    company_country_code = models.CharField(max_length=10)
    company_phone_no = models.CharField(max_length=20)
    company_address_line_1=models.CharField(max_length=200)
    company_address_line_2=models.CharField(max_length=200)
    company_country=models.CharField(max_length=100)
    company_city=models.CharField(max_length=100)
    company_state=models.CharField(max_length=100,)
    company_zip_code=models.CharField(max_length=100) 
    company_country=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to="akarsa")
    cin_no=models.CharField(max_length=200,null=True,blank=True)
    gstin_no=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.id)


class Notification_admin(models.Model):
    notification_type=models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

