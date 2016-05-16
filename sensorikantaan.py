#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Python-ohjelma, joka lisää dataa MySQL-tietokantaan
# Lisättävä tieto haetaan sensoriohjelmalta 

# Tarvittavat kirjastot ja tiedostot
import MySQLdb
import sensori.py

# Avataan tietokantayhteys
db	= [TIETOKANNAN OSOITE, KÄYTTÄJÄ JA SALASANA]

# Cursor-olio, joka vaaditaan tietokantaohjelmoinnissa
cursor = db.cursor()

# Valmistellaan SQL-lauseke
# Haetaan sensoridata sensoriohjelmalta
sql	= """[INSERT LAUSEKE TÄHÄN]"""

try:
	# Suoritetaan SQL-lauseke
	cursor.execute(sql)
	# Lisätään data kantaan
	db.commit()
except:
	# Rollback, mikäli ilmenee virhe
	db.rollback()

# Suljetaan lopuksi tietokantayhetys
db.close()
