# MySQL-tunnelin luonti

MySQL tunnelia varten meidän täytyy sallia yhteydet MySQL-palvelimelle ulkoisista verkko-osoitteista.

	$ cd /etc/mysql

	# Otetaan kopio MySQL:n asetustiedostosta
	$ sudo cp my.conf my.conf.back

	$ sudoedit my.conf

	# Etsitään rivi "bind-address	= 127.0.0.1"
	# Kommentoidaan rivi ulos ja laitetaan osoitteeksi 0.0.0.0

	# Käynnistetään MySQL uudelleen
	$ sudo service mysql restart

Otamme yhteyttä palvelimelle Haaga-Helian verkosta ja ulospäin näkyvä verkko-osoite on 193.166.11.250. Sallitaan MySQL-etäyhteydet ainoastaan tästä ooitteesta, joten lisätään palomuuriin uusi sääntö.

	$ sudo ufw allow from 193.166.11.250 to any port 3306

Kirjaudutaan virtuaalipalvelimella MySQL:ään.

	$ mysql -u [käyttäjä] -p
	
	# Luodaan testitietokanta ja -taulukko
	mysql> create database sensor;
	mysql> use sensor
	mysql> CREATE TABLE testData (
		id		INT(2)		AUTO_INCREMENT PRIMARY KEY,
		name		VARCHAR(20)	NOT NULL,
		reg_dat		TIMESTAMP
		);

	# Annetaan etäoikeudet mysql-käyttäjällemme kyseiseen "sensor"-kantaan.
	mysql> GRANT ALL on sensor.* to '[käyttäjä]'@'193.166.11.250' identified by '[salasana]';

Tämän jälkeen kokeillaan Raspberry Pi:llä kirjautua MySQL:ään etänä Haaga-Helian verkosta.

	$ mysql -h [palvelimen ip-osoite] -u [käyttäjä] -p

Annettuamme salasanan olemme onnistuneesti kirjautuneet palvelimelle. Kun tarkastelemme tietokantoja, niin meille näkyy tuo "sensor"-tietokanta.

	mysql> show databases;
