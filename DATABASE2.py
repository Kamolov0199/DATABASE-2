import sqlite3 as sql

boglanish = sql.connect("Kitoblar.db")

Books = boglanish.cursor()

Books.execute("""
CREATE TABLE IF NOT EXISTS Badiiy(
    Mazmuni TEXT,
    Necha qatorligi INTEGER,
    Necha BET INTEGER
)                                          
""")

Books.execute("""
CREATE TABLE IF NOT EXISTS Detiktiv(
    QurolYarog TEXT,
    Detektivlar TEXT,
    Vorlar INTEGER
)                                          
""")

Books.execute("""
CREATE TABLE IF NOT EXISTS Romantik(
    Sevishganlar TEXT,
    Romantilar TEXT,
    Janjallar INTEGER
)                                          
""")