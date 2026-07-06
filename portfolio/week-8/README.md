# Nädal 8: Python APIs – automatiseeritud andmepipeline

## Eesmärk

Selle nädala eesmärk oli ühendada Python Supabase andmebaasiga ning luua automatiseeritud andmepipeline, mis võimaldab andmeid pärida, töödelda, valideerida ja edasiseks analüüsiks ette valmistada.

## Minu roll: A + D

Minu vastutusala oli **Pythoni ühendamine Supabase andmebaasiga** ning andmete toomine Supabase'ist. Lisaks osalesin automatiseeritud script-pipeline'i kokkupanemisel, et muuta iganädalane andmete töötlemine korduvkasutatavaks ja süsteemseks.

## Tegevused

- Ühendasin Pythoni Supabase andmebaasiga.
- Tõin andmed Supabase tabelitest Pythonisse.
- Osalesin automatiseeritud andmepipeline'i koostamisel.
- Aitasin struktureerida pipeline'i etappe:
  - andmete pärimine;
  - andmete puhastamine;
  - andmete valideerimine;
  - transformatsioonid;
  - logimine;
  - tulemuste eksport.
- Arvestasin suuremate andmemahtude puhul pagination-loogikaga.
- Harjutasin API-päringute vigade käsitlemist ja töökindluse parandamist.

## Kasutatud tööriistad ja tehnoloogiad

| Tööriist / tehnoloogia | Kasutus |
|---|---|
| Python | Pipeline'i loomine ja automatiseerimine |
| Supabase | Andmebaas ja andmeallikas |
| API päringud | Andmete toomine Supabase'ist |
| Pandas | Andmete töötlemine ja valideerimine |
| Logging | Pipeline'i töö jälgimine ja vigade leidmine |
| Retry logic | Ebaõnnestunud päringute uuesti proovimine |
| Exponential backoff | API-päringute töökindlam käsitlemine |
| AI | Koodi struktureerimise, pagination'i ja valideerimisloogika tugi |

## Pipeline'i üldine loogika

Automatiseeritud pipeline koosnes järgmistest sammudest:

```text
1. Ühendus Supabase andmebaasiga
2. Andmete pärimine tabelitest
3. Pagination suuremate andmemahtude jaoks
4. Andmete puhastamine
5. Andmetüüpide ja väärtusvahemike valideerimine
6. Transformatsioonid ja arvutused
7. Logimine igas olulisemas etapis
8. Tulemuste eksport või edastamine järgmisse analüüsietappi
```

## Peamised leiud

- Kui pipeline on korrektselt üles ehitatud, saab iganädalast andmete uuendamist ja kuvamist oluliselt lihtsustada.
- Kuupäeva määramine ja ajaperioodi kontroll on pipeline'is väga oluline, sest see mõjutab, millised andmed analüüsi kaasatakse.
- API-põhises andmetöötluses tuleb arvestada päringupiirangute, katkestuste ja võimalike andmemahu piirangutega.
- Logimine aitab kiiresti aru saada, millises etapis pipeline töötab või ebaõnnestub.
- Andmete valideerimine vähendab riski, et analüüsi jõuavad vigased või ootamatul kujul andmed.

## AI kasutamine

Kasutasin AI abi pipeline'i töökindlamaks muutmisel. AI aitas:

- lisada pagination-loogika suuremate andmemahtude pärimiseks;
- koostada retry-loogika ebaõnnestunud API-päringute jaoks;
- kasutada exponential backoff lähenemist;
- lisada andmevalideerimise samme;
- kontrollida, kas veerutüübid vastavad ootustele;
- hinnata, kas väärtusvahemikud on mõistlikud;
- lisada logimisteateid iga olulisema transformatsiooni kohta;
- muuta koodi paremini loetavaks ja hooldatavaks.

## Peamised õppetunnid

- Õppisin, kuidas Pythoniga andmebaasist andmeid pärida.
- Sain paremini aru, kuidas API-põhine andmetöötlus erineb käsitsi CSV-failidega töötamisest.
- Mõistsin, miks on pipeline'is oluline veakäsitlus, logimine ja andmete valideerimine.
- Harjutasin suuremate andmemahtude käsitlemist pagination'i abil.
- Sain praktilise kogemuse automatiseeritud andmevoo ülesehitamisel.
- Mõistsin, et hea pipeline peab olema korduvkasutatav, kontrollitav ja vajadusel laiendatav.

## Meeskonnatöö

Osalesin meeskonna ühises töös automatiseeritud andmepipeline'i loomisel ja testimisel.

> Märkus: lokaalne failitee `C:\Users\kasutaja\Documents\DACA-Python\Python_pipeline.py` ei tööta GitHubis teiste kasutajate jaoks. Kui soovid sellele failile README-s viidata, tuleks fail lisada GitHubi repositooriumisse ja linkida suhtelise lingiga.

Näiteks kui fail asub samas kaustas kui README:

```markdown
[Python pipeline script](./Python_pipeline.py)
```

Kui fail asub `individual` kaustas:

```markdown
[Python pipeline script](./individual/Python_pipeline.py)
```

## Failid ja materjalid

- [Python pipeline script](./Python_pipeline.py)

## Tulemus

Nädala lõpuks valmis automatiseeritud Python pipeline'i lahendus, mis võimaldab Supabase andmebaasist andmeid pärida, neid töödelda, valideerida ja edasiseks analüüsiks ette valmistada. Töö tulemusena tekkis parem arusaam sellest, kuidas andmeanalüütiku töös automatiseerida korduvaid andmetöötluse samme.

