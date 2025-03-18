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
from shopapp.models import Product

fake_generator = Faker()

def populate_products(n_products=5):
    for i in range(n_products):
        #creamos un valor falso
        fake_name = fake_generator.sentences(nb_words=6, variable_nb_words=True)
        fake_description = fake_generator.paragraph(nb_sentences=3, variable_nb_sentences=True)
        fake_full_cost = random.uniform(1, 14000)
        fake_is_offer = random.random() > 0.5
        fake_offer_cost = random.uniform(5, fake_full_cost) if fake_is_offer else fake_full_cost

    product = Product.objects.get_or_create(
    product_name = fake_name,
    product_description = fake_description,
    product_full_cost = fake_full_cost,
    product_is_offer = fake_is_offer,
    product_offer_cost = fake_offer_cost
    )
#
if __name__ == '__main__':
    print("Empezar a poblar la tabla de datos. ")
    populate_products(20)
    print('Finalizando.')