from sqlalchemy import Column, ForeignKey, Integer, String

from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.database_homework_45 import Base


class Seller(Base):
    __tablename__ = 'seller'

    ID_product = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    Place = Column(String(250), nullable=False)
    Product = Column(String(250), nullable=False)
    Col = Column(Integer)
    Price = Column(Integer, nullable=False)

    def __init__(self, Seller_people, Place, Product, Col, Price):
        self.surname = Seller_people[0]
        self.name = Seller_people[1]
        self.patronymic = Seller_people[2]
        self.Place = Place
        self.Product = Product
        self.Col = Col
        self.Price = Price

    def __repr__(self):
        return f"Продавец (ФИО: {self.surname} {self.name} {self.patronymic})" \
               f"По адресу: {self.Place}, Продает: {self.Product}, в количестве: {self.Col}, По цене: {self.Price}"
