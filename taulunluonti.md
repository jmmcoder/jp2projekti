# Liiketunnistinta varten tehty MySQL-taulukko, johon tallennetaan Raspberry Pi:ltä tulut sensoridata

	mysql> CREATE TABLE motionData (
		id		AUTO_INCREMENT PRIMARY KEY,
		liike		varchar(20),
		paivays			TIMESTAMP
		);
