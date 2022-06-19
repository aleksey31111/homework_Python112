from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.database_homework_45 import Base


class Customer(Base):
    __tablename__ = 'customer'

    ID_product = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    Col = Column(Integer)
    Product = Column(String(250), nullable=False)

    def __init__(self, Cust_people, Col, Product):
        self.surname = Cust_people[0]
        self.name = Cust_people[1]
        self.patronymic = Cust_people[2]
        self.Col = Col
        self.Product = Product

    def __repr__(self):
        return f"Покупатель: (ФИО: {self.surname} {self.name} {self.patronymic})" \
               f"В количестве {self.Col}шт Покупает товар: {self.Product}"
