import sqlite3 as sql

boglanish = sql.connect("Ichimliklar.db")

Suvlar = boglanish.cursor()

Suvlar.execute("""
CREATE TABLE IF NOT EXISTS Oddiysuv(
    ismi TEXT,
    rangi TEXT,
    srok INTEGER
)                                          
""")

Suvlar.execute("""
CREATE TABLE IF NOT EXISTS Gazlangansuv(
    Gaz Tarkibi TEXT,
    Rangi TEXT,
    Gaz Miqdori INTEGER
)                                          
""")

Suvlar.execute("""
CREATE TABLE IF NOT EXISTS ranglisuv(
    Rangi TEXT,
    Gazli TEXT,
    Bezgaz INTEGER
)                                          
""")