#Cargar los elementos necesarios para utilzar los modelos de django
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memexpress.settings')
import django
# Import settings
django.setup()

#Script para poblar la tabla Product
from faker import Faker
import random
from shopapp.models import Contacts

fake_generator = Faker()

def populate_contacts(n_products=5):
    for i in range(n_products):
        #creamos un valor falso
        fake_name = fake_generator.name()
        fake_address = fake_generator.address()
        fake_phone = fake_generator.phone_number()
        fake_email = fake_generator.email()
        fake_active = random.random() > 0.5

    contact = Contacts.objects.get_or_create(
    contact_name = fake_name,
    contact_address = fake_address,
    contact_phone = fake_phone,
    contact_email = fake_email,
    contact_active = fake_active
    )
#
if __name__ == '__main__':
    print("Empezar a poblar la tabla de datos. ")
    populate_contacts(30)
    print('Finalizando.')