from django.db import models

# Create your models here.

#creamos una clase llamada Product donde definimos los campos de la tabla
class Product(models.Model):
    #creamos un atributo llamado name
    product_name = models.CharField(max_length=100, unique=True)
    #creamos un atributo llamado full_cost
    product_full_cost = models.DecimalField(max_digits=10, decimal_places=2)
    #creamos un atributo llamado description
    product_description = models.CharField(max_length=255)
    #creamos un atributo llamado product_is_offer para saber si el producto esta en oferta
    product_is_offer = models.BooleanField()
    #creamos un atributo llamado offer_cost
    product_offer_cost = models.DecimalField(max_digits=10, decimal_places=2)

    #funcion para definir como se ve cada producto
    def __str__(self):
        return self.product_name

#clase para el historial de costos
class HistoricalCost(models.Model):
    #creamos un atributo llamado product que se relaciona con la clase Product
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #on_delete=models.CASCADE es para que si se borra un producto se borren todos los historiales de costo
    #creamos un atributo llamado cost que es un decimal
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    #creamos un atributo llamado date que es una fecha
    change_date = models.DateTimeField()
    #creamos un atributo llamado product_is_offer
    product_is_offer = models.BooleanField()
    
    #funcion para definir como se ve cada salida del historial de costo
    def __str__(self):
        #funcion para definir como se ve cada historial de costo
        return self.product.product_name + " " + self.change_date.strftime("%Y-%m-%d %H:%M:")
        #return f"{self.product} - {self.cost} - {self.date}"

#clase para los contactos
class Contacts(models.Model):
    full_name = models.CharField(max_length=100, unique="True")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    active = models.BooleanField()

    def __str__(self):
        return self.full_name

#Cuando se crean modelos, hay que migrar para que se apliquen los cambios (y eso implica el migrate y makemigrations).
#Revisar que se muestren los cambios/datos usando el shell
#Usar  href="{% url 'nombre' %}" para hacer referencia a otras rutas