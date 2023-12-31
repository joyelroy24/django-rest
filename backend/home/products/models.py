from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

    def __str__(self) -> str:
        return self.title
    
    @property
    def sale_price(self):
        # print(self.price)
        return "%.2f"%(float(self.price)*0.10)
    
    def get_discount(self):
        return 5.7
