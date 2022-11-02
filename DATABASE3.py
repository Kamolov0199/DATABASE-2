import sqlite3 as sql

boglanish = sql.connect("Kalonkalar.db")

Calonca = boglanish.cursor()

Calonca.execute("""
CREATE TABLE IF NOT EXISTS Bass(
    Narxi INTEGER,
    Rangi TEXT,
    BassKuchi INTEGER
)                                          
""")

Calonca.execute("""
CREATE TABLE IF NOT EXISTS Sambuffer(
    Dizayn TEXT,
    Rangi TEXT,
    Garantiya INTEGER
)                                          
""")

Calonca.execute("""
CREATE TABLE IF NOT EXISTS Oddiy(
    Rangi TEXT,
    Qulayliklari TEXT,
    Narx INTEGER
)                                          
""")