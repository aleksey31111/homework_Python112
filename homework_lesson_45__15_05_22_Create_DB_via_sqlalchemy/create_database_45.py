from faker import Faker

from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.database_homework_45 import create_db, Session
from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.seller import Seller
from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.customer import Customer


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    place_names = ['г.Нижнекмск "Центральный рынок"', 'г.Нихнекамск "Бызовский рынок"', 'г.Нижнекамск ТЦ"Рамус"',
                   'г.Нижнекамск ТЦ"Олимп"', 'г.Нижнекамск ТЦ"Радуга"', 'г.Нижнекамск ТЦ"Планета"',
                   'г.Набережные челны ТЦ"Торговый квартал"', 'т.Набережные челны ТЦ"Омега"',
                   'г.Набережные челны ТЦ"SUNPRISE CITY"', 'г.Москва "ЦУМ"']
    product_names = ['Телевизор Haier 43 Smart TV MX ', 'Телевизор Toshiba 32V35KE', 'Телевизор Philips 55PUS7406/60',
                     'Ноутбук Acer Acer A715-42G-R3FW NH.QDLER.003', 'Ноутбук HP 17-cp0126ur 5D666EA',
                     'Ноутбук Honor MagicBook X 15 i5/8/512 Gray (BBR-WAH9)', 'Ноутбук ASUS Vivobook R565JA-BQ2497W',
                     'Смартфон Apple iPhone 11 64GB Purple (MHDF3RU/A) ', 'Смартфон Xiaomi Redmi Note 10S 6+64GB Gray ']

    #                ]
    #
    # for key1, pl in enumerate(place_names):
    #     place = Seller(seller_title=pl)
    #
    # for key2, pr in enumerate(product_names):
    #     products = Seller.Product(product_title=pr)
    #     productc = Customer.Product(product_title=pr)


    faker = Faker('ru-Ru')
    session.commit()

    for _ in range(60):
        full_name_s = faker.name().split()
        place = faker.random.choice(place_names)
        product = faker.random.choice(product_names)
        col = faker.random.randint(1, 50)
        price = faker.random.randint(20000, 100000)
        seller = Seller(full_name_s, place, product, col, price)
        session.add(seller)
        session.commit()

        full_name_c = faker.name().split()
        Col = faker.random.randint(1, 100)
        Product = faker.random.choice(product_names)
        customer = Customer(full_name_c, Col, Product)
        session.add(customer)
        session.commit()
        session.close()
