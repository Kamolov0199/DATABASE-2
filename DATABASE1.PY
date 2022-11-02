import sqlite3 as sql

boglanish = sql.connect("Mashinalar.db")

Cars = boglanish.cursor()

Cars.execute("""
CREATE TABLE IF NOT EXISTS SpartivniMoshin(
    Narxi TEXT,
    Rangi TEXT,
    Tezligi INTEGER
)                                          
""")

Cars.execute("""
CREATE TABLE IF NOT EXISTS DizaynliMoshin(
    Dizayn TEXT,
    Rangi TEXT,
    Garantiya INTEGER
)                                          
""")

Cars.execute("""
CREATE TABLE IF NOT EXISTS ComfortMoshin(
    Rangi TEXT,
    Qulayliklari TEXT,
    BalonRazmeri INTEGER
)                                          
""")