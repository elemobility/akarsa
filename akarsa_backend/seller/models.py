from django.db import models

# Create your models here.
class Seller(models.Model):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=15,choices=(("Male","Male"),("Female","Female"),("Others","Others")))
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    phone_number=models.IntegerField(unique=True)
    country_code=models.IntegerField()
    address_line_1=models.CharField(max_length=200)
    address_line_2=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='customer/profile')
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    is_user_blocked=models.BooleanField(default=False)
    otp=models.CharField(max_length=200)
    date_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    aadhar_no=models.CharField(max_length=100,null=True,blank=True)
    pan_no=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.id)

country=(
    ("India","India"),
    ("India","US"),
    ("India","Auatralia"),
    ("India","Singapure"),
)
class Seller_company_info(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(null=True,blank=True)
    address_line_1=models.CharField(max_length=200,null=True,blank=True)
    address_line_2=models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    zip_code=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,choices=country,null=True,blank=True)
    logo=models.ImageField(upload_to='company/logo',null=True,blank=True)
    gstin_no=models.CharField(max_length=200,null=True,blank=True)
    website=models.CharField(max_length=100,null=True,blank=True)



