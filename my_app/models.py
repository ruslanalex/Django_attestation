from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    reg_date = models.DateField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    image = models.ImageField(null=True)
    added_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    @property  # данный декоратор говорит что данный метод, воспринимается именно как метод, а не свойство
    def total_quantity(self):
        return sum(product.amount for product in Product.objects.all()) # перебераю каждый продкт, обращаюсь к его свойству amount и суммурую его

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    common_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
