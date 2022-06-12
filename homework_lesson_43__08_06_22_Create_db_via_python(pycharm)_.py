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
with sq.connect('bicycles.db') as con:
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

    for bike in bicycles:
        cur.execute("INSERT INTO bicycles VALUES(NULL, ?, ?, ?, ?)", bike)

    con.commit()
