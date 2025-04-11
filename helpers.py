import random

#генерация уникального емейла
def generation_email():

    random_number = random.randint(100, 999)
    email = f'kuvykina_20_{random_number}@gmail.com'

    return email
