# **Projekto Tikslas**
Nuskreipinti duomenis iš Lietuviškų darbo skelbimų portalų duomenis ir juos išsaugoti sukurtoje duomenų bazėje. 

# Duomenu susrinkimas 
Duomenis imame iš puslapio `CVBANKAS`.\
Pirmu žingsniu randame maksimalų puslapių skaičių ir url kuris keliauja per puslaius. 

## **Maksimalus Puslaių Skaičius**
```
response.css('ul.pages_ul_inner a::text').getall()[-1]
```
Šiame puslapyje yra rodomi visi puslapiai nuo pirmo ir pačioje pabaigoje paskutinis puslapis. Taip mes pasiimame paskutinį puslapį ir galime iteruoti per visus.\
Taip pat randame pagrindinį url, prie kurio pridėjus puslapio numerį galime eiti per puslapius. 
```
response.css('ul.pages_ul_inner a')[-1].attrib['href']
```
gražinama reikšmė yra `https://www.cvbankas.lt/?page=103`. Paskaičiuojame kiek simbolių yra paskutiniame puslapyje ir kiek sumažiname tekstą. \
Įterpiame f string, kad galėtume iteruoti per puslapius. 

## **Surenakme Kiekvino puslapio url i sarasa"


# **Duomenis kuriuos noriu pasiimti** 
1. Darbo pasvadinimas
2. Atlyginimas: atkreipti demesi, kad kartais nebuna nurodytas, arba gali buti valandinis 
3. atlyginimas: menesinis, valandinis 
4. atskaicius/ neatskaicius mokesciu 
5. Darbo laikas: visa darbo diena, terminuota ir pan 
6. Miestas
7. Darbdavio pavadinimas 
8. Kiek laiko liko iki skelbimo pabaigos 
9. Kiek perziurejo 
10. 

# **Darbo Eiga**
0. Kai baigsiu projektą, aprašyti, kaip sukurti naują projektą.
1. Susirašome į `items.py` laukų pavadinimus kuriuos pasiimsiu iš svetainės.
2. Importuojame `items.py` sukurta class į spider failą. 
3. `spider` faile kuri surenka visas nuorodas esančias tame puslapyje 
4. `spider` faile randame vietą, kur pereiti į naują puslapį, mintis yra, kad praėjus visus puslapius mes spaudžiame ant naujo puslapio ir vėl surenkame visas nuorodas. taip darome, kol pereiname per visus puslapius. 

settings.py faile pakoreguojame `CONCURRENT_REQUESTS` į 5, kad neapkarauti sveytainės serverio. Šis nustatymas parodo kiek užklausu vienu metu gali išsiųsti.\
settings.py faile pakoreguojame `DOWNLOAD_DELAY` į 2, taip pat, kad smarkiai neapkrauti serverio. Šis nustatymas pasako kokiu intervalu siusti užklausas. 2 kas dvi sekundes. 

