import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_1.settings')

import django
django.setup()

#Configuraciones generales
from test_app.models import uwu
from faker import Faker

faker_generator = Faker()

def populate(N=5):
    for entry in range(N):
        #Crear datos falsos
        fake_first_name = faker_generator.first_name()
        fake_last_name = faker_generator.last_name()
        fake_email = faker_generator.email()
        fake_phone_number = faker_generator.phone_number()

        #Crear registro falso
        uwu_t = uwu.objects.get_or_create(f_name=fake_first_name, l_name=fake_last_name, mail=fake_email, tel=fake_phone_number)[0]

if __name__ == '__main__':
    print("Comienza la poblacion 😎")
    populate(30)
    print("Exceso de Coito y Copulacion")