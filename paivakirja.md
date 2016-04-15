##	Järjestelmäprojekti 2 -kurssi
####	Projektityö

13.4.2016

Asensimme Raspbian Jessie -jakelun 8 GB:n microSD-muistikortille. Tämä tapahtui lataamalla levykuva Linux-pohjaiselle työasemalle. Työasemana toimi koulun laboratorioluokan 5005 työasema, jossa on muistikortinlukija. Ensiksi putsataan microSD-kortti GParted-ohjelmalla. Tämän jälkeen kirjoitetaan Rasbian-levykuva kortille.

	sudo -i		# tarvitsemme pääkäyttäjä
	fdisk -l	# tunnistetaan muistikorttimme tunniste, tapauksessamme "/dev/sdf"
	dd bs=1M if=[<TIEDOSTOPOLKU>/<LEVYKUVAN NIMI>] of=/dev/sdf


