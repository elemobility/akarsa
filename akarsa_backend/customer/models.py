
from django.db import models
from seller import models as seller_model
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,BaseUserManager

from django.db.models import IntegerField

# Create your models here.
class CustomerManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone_number, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone_number:
            raise ValueError('The given phone must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)

class Customer(AbstractUser):
    username=None
    email=models.EmailField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    phone_number=IntegerField( unique=True, verbose_name='Phone Number', blank=False, help_text='Enter 10 digits phone number')
    is_verified=models.BooleanField(default=False)
    last_login=models.DateTimeField(null=True, blank=True)
    last_logout=models.DateTimeField(null=True, blank=True)
    country_code=models.IntegerField(default=91)
    gender=models.CharField(max_length=15,choices=(("Male","Male"),("Female","Female"),("Others","Others")))
    address_line_1=models.CharField(max_length=200)
    address_line_2=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='customer/profile_image')
    otp=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    is_user_blocked=models.BooleanField(default=False)
    date_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS=[]

    objects=CustomerManager()
    def __str__(self):
        return str(self.id)

class Brand(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
     return self.name
class Subbrand(models.Model):
    name=models.CharField(max_length=100)
    brand_id=models.ForeignKey(Brand,on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)



class Category(models.Model):
    name=models.CharField(max_length=200)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
        return self.name

class Sub_category(models.Model):
    name=models.CharField(max_length=200)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
        return self.name

class Concern(models.Model):
    name=models.CharField(max_length=200)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True, editable = False)
    def __str__(self):
      return self.name

class Sub_concern(models.Model):
    name=models.CharField(max_length=200)
    concern_id=models.ForeignKey(Concern,on_delete=models.CASCADE)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
       return self.name

class Ingrediant(models.Model):
    name=models.CharField(max_length=200)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
       return self.name

class Sub_ingrediant(models.Model):
    name=models.CharField(max_length=200)
    ingrediant_id=models.ForeignKey(Ingrediant,on_delete=models.CASCADE)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
       return self.name

#type will be body and hair
1
class Type(models.Model):
    name=models.CharField(max_length=200)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
       return self.name

class Sub_type(models.Model):
    name=models.CharField(max_length=200)
    type_id=models.ForeignKey(Type,on_delete=models.CASCADE)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
       return self.name




 
 

    







slab_list=(
    ("5%","5%"),
    ("12%","12%"),
    ("18%","18%"),
    ("28%","28%")
)
currency=(
    ("$","$"),
    ("Rs","Rs"),

)


class Product_colors(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Product_type(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

gst_type=(

    ("CGST/SGST","CGST/SCGST"),
    ("IGST","IGST")
)







class Product(models.Model):
    name=models.CharField(max_length=100)
    product_type=models.ForeignKey(Product_type,on_delete=models.DO_NOTHING,null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    sub_brand=models.ForeignKey(Subbrand,on_delete=models.DO_NOTHING,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    subcategory=models.ForeignKey(Sub_category,on_delete=models.DO_NOTHING)
    concern=models.ForeignKey(Concern,on_delete=models.DO_NOTHING)
    subconcern=models.ForeignKey(Sub_concern,on_delete=models.DO_NOTHING)
    type=models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    subtype_id=models.ForeignKey(Sub_type,on_delete=models.DO_NOTHING)
    ingrediant=models.ForeignKey(Ingrediant,on_delete=models.DO_NOTHING)
    subingrediant=models.ForeignKey(Sub_ingrediant,on_delete=models.DO_NOTHING)
    weight=models.CharField(max_length=200)
    sku=models.CharField(max_length=100)
    #param_link=models.CharField(max_length=400,null=True,blank=True)
    barcode=models.CharField(max_length=200)
    hsn=models.CharField(max_length=200)
    
    color_id=models.ManyToManyField(Product_colors)
    description=models.CharField(max_length=400)
    image1=models.ImageField(upload_to="product/image")
    image2=models.ImageField(upload_to="product/image",default="product.jpg")
    image3=models.ImageField(upload_to="product/image",default="product.jpg")
    image4=models.ImageField(upload_to="product/image",default="product.jpg")
    image5=models.ImageField(upload_to="product/image",default="product.jpg")
    image6=models.ImageField(upload_to="product/image",default="product.jpg")
    
    currency=models.CharField(max_length=100,choices=currency,null=True,blank=True)
    quantity=models.IntegerField()
    gst_slab=models.CharField(max_length=200,choices=slab_list) 
   
    seller_id=models.ForeignKey(seller_model.Seller,on_delete=models.CASCADE)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
       return (self.name)
    

class Shopping_order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    product_id=models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,related_name="order")
    status=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
       return str(self.id)

class Gift(models.Model):
    product=models.ManyToManyField(Product,null=True,blank=True)
    type=models.CharField(max_length=100,choices=(("Custom","Custom"),("Standard","Standard")))
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    size=models.CharField(max_length=200)
    color=models.ManyToManyField(Product_colors,related_name="gift_color",null=True,blank=True)
    price=models.IntegerField(null=True, blank=True)
   
    no_of_items=models.IntegerField()
    date_created=models.DateTimeField( auto_now_add=True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
       return self.name 



class Combo_product(models.Model):
    name=models.CharField(max_length=100)
    pruduct=models.ManyToManyField(Product,null=True,blank=True,related_name="product")
    upcell_product=models.ManyToManyField(Product,null=True,blank=True,related_name="upcell")
    crosssell_product=models.ManyToManyField(Product,null=True,blank=True,related_name="crosssell")
    def __str__(self):
        return self.name

class Offer(models.Model):
    product_id=models.OneToOneField(Product,on_delete=models.CASCADE, null=True,blank=True)
    combo_id=models.OneToOneField(Combo_product,on_delete=models.CASCADE, null=True,blank=True)
    gift_id=models.OneToOneField(Gift,on_delete=models.CASCADE, null=True,blank=True)
    name=models.CharField(max_length=200)
    discount_in_percent=models.CharField(max_length=200)
    discount_in_value=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    start_date=models.DateTimeField(null=True, blank=True)
    end_date=models.DateTimeField(null=True, blank=True)
    active=models.BooleanField(default=False)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
       return str(self.id) 
  

   





 

class Payment(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    order=models.OneToOneField(Shopping_order, on_delete=models.CASCADE,null=True, blank=True)
    total_amount=models.IntegerField(null=True, blank=True)
    currency=models.CharField(max_length=100,null=True, blank=True,choices=currency)
    status=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return str(self.id)
shipping_type=(
     ("a","same day delivery"),
     ("b","two day delivery"),
     ("c","overnight shipping")

 )

class Shipping(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    order_id=models.OneToOneField(Shopping_order, on_delete=models.CASCADE,null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    weight=models.CharField(max_length=100,null=True, blank=True)
    shipping_type=models.CharField(max_length=100,null=True, blank=True,choices=shipping_type)
    shipping_charge=models.IntegerField(default=0)
    currency=models.CharField(max_length=100,choices=currency,default="Rs")
    gst_slab=models.CharField(max_length=100,choices=slab_list,default="5%")
    free_shipping=models.BooleanField(default=False)
    from_date=models.DateTimeField(null=True,blank=True)
    to_date=models.DateTimeField(null=True,blank=True)
    def __str__(self):
       return str(self.id)


class Transaction_report(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, blank=True)
    payment_id=models.OneToOneField(Payment, on_delete=models.CASCADE,null=True, blank=True)
    shipping_id=models.OneToOneField(Shipping, on_delete=models.CASCADE,null=True, blank=True)
    shopping_order=models.OneToOneField(Shopping_order, on_delete=models.CASCADE,null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return str(self.id)





class Feedback(models.Model):
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
   
    feedback=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return str(self.id)



class Cart(models.Model):
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    gift_id=models.ForeignKey(Gift, on_delete=models.DO_NOTHING,null=True, blank=True)
    combo_id=models.ForeignKey(Combo_product, on_delete=models.CASCADE, null=True, blank=True)
    offer_id=models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    description=models.CharField(max_length=200)
    date_created=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    def __str__(self):
       return str(self.id)







    


    







