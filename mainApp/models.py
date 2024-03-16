from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
class contact_Us(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return str(self.name)+" "+str(self.phone)

class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500,default='')
    image=models.ImageField(upload_to="uploads",default='')
    content=HTMLField(default='')
    def __str__(self):
      return self.title


class City(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='')
    slug=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to="uploads",default='')
    def __str__(self):
        return self.slug


class Package(models.Model):
    id=models.AutoField(primary_key=True)
    city= models.ForeignKey(City,on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=150,default='')
    price=models.CharField(max_length=10,default='')
    description=models.TextField(default='')
    total_day=models.CharField(max_length=50,default='')
    start_from=models.CharField(max_length=100,default='')
    end_to=models.CharField(max_length=100,default='')
    pic1 = models.ImageField(upload_to="uploads",default='')
    pic2 = models.ImageField(upload_to="uploads",default='')
    pic3 = models.ImageField(upload_to="uploads",default='')
    pic4 = models.ImageField(upload_to="uploads",default='')
    pic5 = models.ImageField(upload_to="uploads",default='')
    attraction=HTMLField(default='')
    location_image = models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    package_pdf=models.FileField(default='',null=True,blank=True)
    highlight=HTMLField(default='')
    day1_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day1_description=models.TextField(default='',null=True,blank=True)
    day2_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day2_description=models.TextField(default='',null=True,blank=True)
    day3_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day3_description=models.TextField(default='',null=True,blank=True)
    day4_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day4_description=models.TextField(default='',null=True,blank=True)
    day5_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day5_description=models.TextField(default='',null=True,blank=True)
    day6_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day6_description=models.TextField(default='',null=True,blank=True)
    day7_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day7_description=models.TextField(default='',null=True,blank=True)
    day8_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day8_description=models.TextField(default='',null=True,blank=True)

    day9_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day9_description=models.TextField(default='',null=True,blank=True)
    day10_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day10_description=models.TextField(default='',null=True,blank=True)
    day11_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day11_description=models.TextField(default='',null=True,blank=True)
    day12_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day12_description=models.TextField(default='',null=True,blank=True)
    day13_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day13_description=models.TextField(default='',null=True,blank=True)
    day14_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day14_description=models.TextField(default='',null=True,blank=True)
    day15_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day15_description=models.TextField(default='',null=True,blank=True)
    day16_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day16_description=models.TextField(default='',null=True,blank=True)
    day17_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day17_description=models.TextField(default='',null=True,blank=True)
    day18_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day18_description=models.TextField(default='',null=True,blank=True)
    day19_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day19_description=models.TextField(default='',null=True,blank=True)
    day20_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day20_description=models.TextField(default='',null=True,blank=True)
    day21_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day21_description=models.TextField(default='',null=True,blank=True)
    day22_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day22_description=models.TextField(default='',null=True,blank=True)
    day23_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day23_description=models.TextField(default='',null=True,blank=True)
    day24_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day24_description=models.TextField(default='',null=True,blank=True)
    day25_title=models.CharField(max_length=200,default='',null=True,blank=True)
    day25_description=models.TextField(default='',null=True,blank=True)


    seo_title=models.CharField(max_length=300,default="",null=True,blank=True)
    seo_description=models.TextField(default="",null=True,blank=True)
    seo_keyword=models.TextField(default="",null=True,blank=True)
    def __str__(self):
        return self.name

class Package_Enquiry(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    message=models.TextField()

    package_name=models.CharField(max_length=100,default='')
    package_price=models.CharField(max_length=10,default='')
    package_description=models.TextField(default='')
    package_total_day=models.CharField(max_length=50,default='')
    start_from=models.CharField(max_length=100,default='')
    end_to=models.CharField(max_length=100,default='')
    location_image = models.ImageField(upload_to="uploads",default='')
    summery_pdf=models.FileField(upload_to="uploads",default='')


    def __str__(self):
        return self.name+" "+self.phone


class home_banner1(models.Model):
    id=models.AutoField(primary_key=True)
    image1=models.ImageField(upload_to="uploads")
    image2=models.ImageField(upload_to="uploads")
    image3=models.ImageField(upload_to="uploads")
    image4=models.ImageField(upload_to="uploads")
    image5=models.ImageField(upload_to="uploads")


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    address = models.TextField()
    otp = models.IntegerField(default=-115151)

    def __str__(self):
        return str(self.id)+" "+self.name
    


class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    package = models.ForeignKey(Package,on_delete=models.CASCADE,default='')
    qty = models.IntegerField(default=1)
    total = models.IntegerField()
    gst=models.IntegerField(default=0)
    final = models.IntegerField()
    rppid = models.CharField(max_length=30,default="",null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    payment = models.CharField(max_length=100,default='',null=True,blank=True)
  
   
    #Billing Address
    billing_Name=models.CharField(max_length=100,default='',null=True,blank=True)
    billing_Phone=models.CharField(max_length=100,default='',null=True,blank=True)
    billing_Address=models.TextField(default='',null=True,blank=True)
    billing_PIN=models.CharField(max_length=100,default='',null=True,blank=True)
    billing_City=models.CharField(max_length=100,default='',null=True,blank=True)
    billing_State=models.CharField(max_length=100,default='',null=True,blank=True)

    #Shipping Address
    shipping_Name=models.CharField(max_length=100,default='',null=True,blank=True)
    shipping_Phone=models.CharField(max_length=100,default='',null=True,blank=True)
    shipping_Address=models.TextField(default='',null=True,blank=True)
    shipping_PIN=models.CharField(max_length=100,default='',null=True,blank=True)
    shipping_City=models.CharField(max_length=100,default='',null=True,blank=True)
    shipping_State=models.CharField(max_length=100,default='',null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.user.name