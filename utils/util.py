import random
import string


def email(self):
    return f"{self.name_ds.random_choice()}.{self.surname_ds.random_choice()}.{random.randint(100, 10000)}@gmail.com"


def phone(self):
    return f"+380{random.randint(6, 10)}{random.randint(2, 8)}{''.join(random.choices(string.digits, k=7))}"


def name(self):
    return f"{self.name_ds.random_choice()} {self.surname_ds.random_choice()}"


def zip_code():
    return ''.join(random.choices(string.digits, k=5))


def bool_rand():
    return bool(random.randint(0, 1))


def rand_img(self):
    return f"/var/tmp/{name(self)}.jpg"
