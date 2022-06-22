import os
from sqlalchemy import and_, or_, not_, desc, func, distinct, text
from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.database_homework_45 import DATABASE_NAME, Session

from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy import create_database_45 as db_creator

from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.customer import Customer
from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.seller import Seller

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
    #1
    session = Session()
    print(session.query(Customer).all())
    print("=" * 77)

    #2
    for sel in session.query(Seller):
        print(sel)
    print("=" * 77)

    #3
    print(session.query(Customer).count())
    print("=" * 77)

    #4
    print(session.query(Seller).first())
    print("=" * 77)

    #5
    print(session.query(Customer).get(13))
    print("=" * 77)

    #6
    for sel in session.query(Seller).filter(and_(Seller.Col > 55, Seller.name.like("%a%"))):
        print(sel)
    print("=" * 77)

    #7
    for custsel in session.query(Customer.name, Seller.name, Seller.Place).filter(
            and_(Customer.ID_product == Seller.ID_product, Seller.Product == "Смартфон Apple iPhone 11 64GB Purple (MHDF3RU/A) ")):
        print(custsel)
    print("=" * 77)

    #8
    for custsel in session.query(Customer.name, Seller.name, Seller.Place).filter(
            or_(Customer.ID_product == Seller.ID_product, Seller.Product == "Смартфон Apple iPhone 11 64GB Purple (MHDF3RU/A) ")):
        print(custsel)
    print("=" * 77)

    #9
    for custsel in session.query(Customer.name, Seller.name, Seller.Place).filter(
            Customer.ID_product == Seller.ID_product, not_(Seller.Product == "Смартфон Apple iPhone 11 64GB Purple (MHDF3RU/A) ")):
        print(custsel)
    print("=" * 77)

    #10
    for cust in session.query(Customer).filter(Customer.ID_product is not None).all():
        print(cust)
    print("=" * 77)

    #11
    print(session.query(Seller).filter(not_(Seller.Col.between(10,70))).all())



