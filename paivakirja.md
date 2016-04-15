##	Järjestelmäprojekti 2 -kurssi
####	Projektityö

13.4.2016

Asensimme Raspbian Jessie -jakelun 8 GB:n microSD-muistikortille. Tämä tapahtui lataamalla levykuva Linux-pohjaiselle työasemalle. Työasemana toimi koulun laboratorioluokan 5005 työasema, jossa on muistikortinlukija. Ensiksi putsataan microSD-kortti GParted-ohjelmalla. Tämän jälkeen kirjoitetaan Rasbian-levykuva kortille.

	$ sudo -i		# tarvitsemme pääkäyttäjän oikeudet
	$ fdisk -l	# tunnistetaan muistikorttimme tunniste, tapauksessamme "/dev/sdf"
	$ dd bs=1M if=[<TIEDOSTOPOLKU>/<LEVYKUVAN NIMI>] of=/dev/sdf

Kirjoitus onnistui ja voimme tarkastella muistikortin tietoja. Muokataan /boot/config.txt -tiedostoa käyttämään HDMI-liitäntää.

	$ nano /boot/config.txt
	# Etsitään tiedostosta kohta "hdmi:force_hotplug=1" ja poistetaan kommentointi

Kytketään Raspberry Pi:hin virtapiuha, HDMI-kaapeli, näppäimistö ja hiiri. Saamme kuvan näkyviin, joten Raspberry Pi toimii ja boottaa Raspbian-levykuvan onnistuneesti muistikortilta.


15.4.2016

Konfiguroidaan Raspberry Pi käyttämään staattisia ip-asetuksia, jotta koneen ip-osoite pysyy muuttumattomana.

	$ sudoedit /etc/network/interfaces

Muutetaan "iface eth0 inet manual" -riviä seuraavanlaiseksi.

	iface eth0 inet static
		address		172.28.175.21
		netmask		255.255.0.0
		network		172.28.0.0
		broadcast	172.28.255.255
		gateway		172.28.1.254

Käynnistetään verkkoliitäntä "eth0" uudelleen.

	$ sudo ifdown eth0 && sudo ifup eth0

Tämän jälkeen kokeillaan ottaa SSH-yhteys Raspberry Pi:hin. Tämä toimenpide onnistuu.
