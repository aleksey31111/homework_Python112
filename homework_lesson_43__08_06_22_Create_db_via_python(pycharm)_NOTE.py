import sqlite3 as sq

print("Задание: Програмно создать БД, таблицу наполнить данными с помощью методов модуля sqlite3")

bicycles = [
    ("Велосипед Горный RUSH HOUR RX 905, 29, 2022", "RUSH HOUR", 17, 120),
    ("Велосипед горный MILANO M500", "MILANO M500 26", 16.5, 120),
    ("Велосипед горный NEXTbike OBSIDIAN 26", "NEXTbike", 17.2, 120),
    ("Городской Велосипед DeWolf Asphalt 20 W, 28, 2022", "DeWolf", 16, 60),
    ("Городской Велосипед STELS Navigator-300 Lady 28 20 \
    Красный Городской Горный Двухколёсный Колесо 28 \
    Мужской Женский С Багажником С Корзинкой Спорт Отдых, \
    28, 2021", "STELS", 17.43, 100),
    ("Складной Велосипед Stark , 29, 2021", "Start", 20,110)
]
# def read_picture(n):
#     try:
#         with open(f"avatars_bicycles/{n}.jpg", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
# def write_picture


# con = None
with sq.connect('bicycles.db') as con:
    # con = sq.connect('bicycles.db')
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bicycles(
    bike_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    brand TEXT,
    weight INTEGER,
    load_mass INTEGER
    )
    """)

    # BEGIN;
    # INSERT
    # INTO
    # bicycles
    # VALUES("Велосипед Горный RUSH HOUR RX 905, 29, 2022", "RUSH HOUR", 17, 120);
    # INSERT
    # INTO
    # bicycles
    # VALUES("Велосипед горный MILANO M500 26", "MILANO", 16, 120);
    # INSERT
    # INTO
    # bicycles
    # VALUES("Велосипед горный NEXTbike OBSIDIAN 26", "NEXTbike", 17, 120);
    # INSERT
    # INTO
    # bicycles
    # VALUES("Городской Велосипед DeWolf Asphalt 20 W, 28, 2022", "DeWolf", 16, 60);
    # INSERT
    # INTO
    # bicycles
    # VALUES("Городской Велосипед STELS Navigator-300 Lady 28 20 \
    #  Красный Городской Горный Двухколёсный Колесо 28 \
    #  Мужской Женский С Багажником С Корзинкой Спорт Отдых, \
    #  28, 2021", "STELS", 17, 100);
    # INSERT
    # INTO
    # bicycles
    # VALUES("Складной Велосипед Stark , 29, 2021", "Start", 20, 110);

    for bike in bicycles:
        cur.execute("INSERT INTO bicycles VALUES(NULL, ?, ?, ?, ?)", bike)

    con.commit()

    # imgs = ["avatars_bicycles/Велосипед_горный_MILANO_M500.jpg",
    #         "avatars_bicycles/Велосипед_горный_NEXTbike_OBSIDIAN.jpg",
    # "avatars_bicycles/Горный_Велосипед_RUSH_HOUR_RX.jpg",
    #         "avatars_bicycles/Городской_Велосипед_DeWolf_Asphalt.jpg",
    # "avatars_bicycles/Городской_Велосипед_STELS_Navigator_300_Lady.jpg",
    #         "avatars_bicycles/Складной_Велосипед_Stark.jpg"]
    # # for img in imgs:
    # img = read_picture([i for i in imgs])
    # if img:

# except sq.Error:
#     if con:
#         con.rollback()
#     print("Ощибка выполнения запроса")
# finally:
#     if con:
#         con.close()
#
