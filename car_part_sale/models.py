from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "categories"
    
    

class Part(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    model = models.CharField(max_length=255)
    description = models.TextField(blank=True)
   # condition = models.BooleanField()
    price = models.DecimalField(decimal_places=2,max_digits=16)
    stock = models.IntegerField(default=0)
    creted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    part_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
            nam = self.user.username +"_"+self.part.name 
            return nam 


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=False)
    email = models.EmailField(null=False)
    address = models.TextField(null=False)
    total_price = models.FloatField(max_length=150, null=False)
    payment_mode = models.CharField(max_length=150,null=True)
    orderstatuses = (
        ('Pending','Pending'),
        ('Out for Shipping', 'Out for Shipping'),
        ('Completed', 'Completed'),
    )
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=150, choices=orderstatuses,default='Pending')
    tracking_no = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)


    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)
    