# Sensoridatan esittäminen

Sensoridata palvelimen puolella esitetään verkkosivuilla, jotka ovat luotu projektia varten. Palvelimelle siirretty sensoridata on tallennettuna MySQL-tietokantaan. Frontend-puoli on toteutettu PHP:lla, eli tietokantadata haetaan verkkosivuille PHP:skripteillä. Verkkosivuilla näkyy viesti kun liikettä on tunnistettu ja kellonaika, milloin liike tunnistettiin. Sivuilla esitettävä data päivittyy aina minuutin välein.

Verkkosivulle lisätään PHP-skriptit, joilla muodostetaan tietokantayhteys. Tämän jälkeen määritellään tietokanta ja taulukko, josta data luetaan.
	
	# Tietokantayhteyden muodostaminen toimii tällä tavalla
	<?php
		$dbhost = 'localhost:3306';
		$dbuser = '["käyttäjä"]';
		$dbpass = '["salasana"]';
   
		$conn = mysql_connect($dbhost, $dbuser, $dbpass);
   
		if(! $conn ) {
			die('Yhteyden muodostaminen epäonnistui: ' . mysql_error());
	}

