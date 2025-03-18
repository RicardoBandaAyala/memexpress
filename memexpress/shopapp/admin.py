from django.contrib import admin
from shopapp.models import Product, HistoricalCost, Contacts

#Registrar los modelos que queremos se muestren
admin.site.register(Product)
admin.site.register(HistoricalCost)
admin.site.register(Contacts)
