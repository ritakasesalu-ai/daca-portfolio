# UrbanStyle andmeanalüüsi projekt

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white)
![Power BI](https://img.shields.io/badge/-Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![VS Code](https://img.shields.io/badge/-VS%20Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white)

## Projekti ülevaade

UrbanStyle projekt oli praktiline andmeanalüüsi õppeprojekt, mille eesmärk oli töötada läbi andmeanalüütiku töövoog alates andmete mõistmisest ja puhastamisest kuni visualiseerimise, automatiseeritud andmepipeline'i ja karjääriks valmistumiseni.

Projektis kasutati UrbanStyle'i näidisettevõtte andmeid, mis hõlmasid kliendiandmeid, müügiandmeid, tooteandmeid, inventuuri ja turundusega seotud infot. Töö käigus analüüsisin andmekvaliteeti, koostasin SQL-päringuid, lõin Power BI dashboarde, tegin Pythonis RFM kliendisegmenteerimise ning töötasin välja automatiseeritud andmepipeline.

Projekt toimus meeskonnatööna, kuid igal nädalal oli ka individuaalne roll ja vastutusala.

### Projekti kestvus

27.04-10.07.2026

---

## Projekti eesmärk

Projekti eesmärk oli arendada praktilisi andmeanalüütiku oskusi järgmistes valdkondades:

- andmebaaside ja tabelite uurimine;
- SQL-päringute kirjutamine;
- andmete puhastamine ja valideerimine;
- tabelite ühendamine JOIN-ide abil;
- agregatsioonide ja koondstatistika koostamine;
- Power BI dashboardide loomine;
- Python Pandase kasutamine andmeanalüüsis;
- RFM kliendisegmenteerimine;
- API-põhise andmepipeline'i loomine;
- portfoolio, CV ja LinkedIn profiili korrastamine.

---

## Kasutatud tööriistad ja tehnoloogiad

| Tööriist / tehnoloogia | Kasutus projektis |
|---|---|
| **SQL** | Andmete uurimine, puhastamine, JOIN-id ja agregatsioonid |
| **PostgreSQL** | Andmebaasipäringud ja andmete analüüs |
| **Supabase** | Pilvepõhine andmebaas ja andmete haldamine |
| **Power BI Desktop** | Dashboardide loomine ja andmete visualiseerimine |
| **Power BI Service** | Dashboardide avaldamine ja jagamine |
| **DAX** | Mõõdikute loomine Power BI-s |
| **Python** | Andmetöötlus, pipeline ja analüüs |
| **Pandas** | Andmete puhastamine, grupeerimine ja RFM analüüs |
| **Plotly** | Interaktiivsete graafikute loomine |
| **GitHub** | Projekti dokumentatsioon ja portfoolio haldamine |
| **Markdown** | README failide koostamine |
| **NotebookLM** | Õppematerjalide struktureerimine ja kokkuvõtete tegemine |
| **Google Slides** | Meeskonnatöö tulemuste esitlemine |
| **AI tööriistad** | Koodi selgitamine, vigade parandamine, sõnastuse parendamine ja analüüsi struktureerimine |

---

## Projekti struktuur

```text
urbanstyle-portfolio/
├── README.md
├── .gitignore
├── week-0/
├── week-1/
├── week-2/
├── week-3/
├── week-4/
├── week-5/
├── week-6/
├── week-7/
├── week-8/
├── week-9/
└── week-10/
```

| Nädal        | Teema                                     | Peamine fookus                                                          | Kasutatud tööriistad                      |
| ------------ | ----------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------- |
| **Nädal 0**  | Onboarding ja töökeskkondade seadistamine | Projekti töövahendite seadistamine ja UrbanStyle andmestikuga tutvumine | GitHub, Supabase, NotebookLM              |
| **Nädal 1**  | SQL Basics – andmete esmane uurimine      | `customers` tabeli analüüs, puuduvad väärtused ja duplikaadid           | SQL, Supabase, PostgreSQL                 |
| **Nädal 2**  | SQL Basics – müügiandmete puhastamine     | `sales` tabeli puhastamine, duplikaadid ja vigased kuupäevad            | SQL, PostgreSQL                           |
| **Nädal 3**  | SQL JOIN-id                               | Tabelite ühendamine, müügita toodete ja enim müüdud toodete leidmine    | SQL JOIN-id                               |
| **Nädal 4**  | SQL agregatsioonid                        | Kliendisegmentide, TOP klientide ja koondstatistika koostamine          | SQL, CTE, GROUP BY, HAVING                |
| **Nädal 5**  | Visualiseerimise disain                   | CEO dashboardi planeerimine ja esmane Power BI visualiseerimine         | Power BI                                  |
| **Nädal 6**  | UrbanStyle Dashboard                      | Power BI juhtimisvaate loomine ja äriliste leidude esitlemine           | Power BI, DAX, Supabase                   |
| **Nädal 7**  | Python Pandas – RFM analüüs               | Kliendisegmenteerimine Recency, Frequency ja Monetary näitajate põhjal  | Python, Pandas, Plotly                    |
| **Nädal 8**  | Python APIs – pipeline                    | Supabase andmete pärimine ja automatiseeritud andmepipeline             | Python, Supabase API, Pandas, logging     |
| **Nädal 9**  | Karjääri ettevalmistus                    | Portfolio, CV, LinkedIn ja CV screening juhend                          | GitHub, LinkedIn, CV, AI                  |
| **Nädal 10** | Projekti kokkuvõte / lõppesitlus          | Projekti tulemuste koondamine ja portfoolio viimistlemine               | GitHub, Markdown, Power BI, Google Slides |

## Peamised tööetapid
### 1. Andmete mõistmine ja töövahendite seadistamine

Projekti alguses seadistati töövahendid ning tutvuti UrbanStyle'i andmestiku ja äriprobleemiga. Kasutusele võeti GitHub dokumentatsiooni jaoks, Supabase andmebaasi haldamiseks ning NotebookLM õppematerjalide struktureerimiseks.

### 2. Andmete uurimine SQL-iga

Esimestel nädalatel keskendus töö SQL-i põhioskustele. Uuriti kliendi- ja müügiandmeid, kontrolliti tabelite struktuuri, otsiti puudulikke väärtuseid, duplikaate ja andmekvaliteedi probleeme.

Olulisemad SQL-võtted:

SELECT
FROM
WHERE
ORDER BY
GROUP BY
HAVING
COUNT
SUM
AVG
COALESCE
TRIM

### 3. Andmete puhastamine

Müügiandmete puhastamisel tuvastati olulisi andmekvaliteedi probleeme, sh duplikaate, puuduvaid customer_id väärtuseid ja ebaloogilisi kuupäevi. Andmeid puhastati testtabelis, et säilitada algandmete terviklikkus.

Näited tuvastatud probleemidest:

duplikaadid müügiandmetes;
puuduvad kliendi ID-d;
tulevikku suunatud kuupäevad;
ebaühtlane kirjapilt tekstiväljades.

### 4. Tabelite ühendamine JOIN-ide abil

JOIN-ide abil ühendati toote-, müügi- ja inventuuriandmeid. Selle tulemusena oli võimalik leida müügita tooteid, enim müüdud tooteid ja enim müüdud kategooriaid.

Kasutatud SQL JOIN-id:

INNER JOIN
LEFT JOIN
RIGHT JOIN
LEFT JOIN ... WHERE ... IS NULL

### 5. Agregatsioonid ja kliendianalüüs

Agregatsioonide abil koostati kliendi- ja müügiandmete koondanalüüs. Töö käigus leiti TOP kliendid, kliendisegmentide arvud, linnade jaotused ning protsendid.

Kasutatud võtted:

GROUP BY
HAVING
CTE ehk WITH
ROUND
koondstatistika ja osakaalude arvutamine.

### 6. Power BI dashboardid

Power BI abil loodi juhtimisvaated, mis tõid esile ettevõtte peamised ärinäitajad. Dashboardide eesmärk oli anda kiire ülevaade müügitulust, kasvust, tootekategooriatest ja kaupluste tulemuslikkusest.

Dashboardides kasutati:

KPI kaarte;
joondiagramme;
tulpdiagramme;
kategooriapõhiseid vaateid;
filtreid;
DAX mõõdikuid.

### 7. RFM kliendisegmenteerimine Pythonis

Pythonis ja Pandases koostati RFM analüüs, mille abil jaotati kliendid segmentidesse ostude hiljutisuse, sageduse ja rahalise väärtuse põhjal.

RFM mõõdikud:

Recency – mitu päeva on möödunud kliendi viimasest ostust;
Frequency – kui sageli klient ostab;
Monetary – kui suur on kliendi kogukulu.

Analüüsi põhjal tuvastati näiteks Loyal, Regular, At Risk ja Lost kliendisegmendid.

### 8. Automatiseeritud andmepipeline

Pythoniga loodi andmepipeline, mis võimaldas andmeid Supabase'ist pärida, töödelda, valideerida ja logida.

Pipeline sisaldas järgmisi samme:

ühendus Supabase andmebaasiga;
andmete pärimine API kaudu;
pagination suuremate andmemahtude jaoks;
retry-loogika ebaõnnestunud päringute korral;
andmetüüpide valideerimine;
transformatsioonid;
logimine;
tulemuste eksport.

### 9. Karjääri ettevalmistus

Projekti lõpuosas keskenduti portfoolio, CV ja LinkedIn profiili korrastamisele. Lisaks koostati CV screening juhend, mis aitab hinnata andmeanalüütiku kandidaadi tugevusi ja riske.

## Fookuses olid:

portfolio struktuur;
GitHub README failid;
CV punased ja rohelised lipud;
LinkedIn profiili professionaalsus;
praktiliste projektide esitlemine.
Peamised tulemused

## Projekti lõpuks valmisid:

struktureeritud GitHub portfoolio;
nädalapõhised README failid;
SQL analüüsid;
andmekvaliteedi kontrollid;
Power BI dashboardid;
RFM kliendisegmenteerimise analüüs;
automatiseeritud Python pipeline;
CV screening juhend;
karjääriks sobiv andmeanalüütiku portfoolio alus.
Peamised õppetunnid

## Projekti jooksul arendasin oskusi järgmistes valdkondades:

SQL-päringute kirjutamine ja vigade parandamine;
andmete puhastamine ja kvaliteedikontroll;
andmebaasi tabelite ühendamine;
koondstatistika koostamine;
Power BI dashboardide loomine;
DAX mõõdikute kasutamine;
Python Pandase kasutamine andmeanalüüsis;
andmepipeline'i ülesehitus;
andmeanalüüsi tulemuste äriline tõlgendamine;
tehnilise töö dokumenteerimine GitHubis.
AI kasutamine projektis

## AI-d kasutati projekti jooksul abivahendina, mitte lõpptulemuse automaatse asendajana. AI toetas:

SQL-veateadete mõistmist;
Python koodi parandamist;
Pandase ja Plotly koodi koostamist;
RFM analüüsi loogika selgitamist;
Power BI mõõdikute sõnastamist;
README failide korrastamist;
CV ja portfolio sõnastuse parandamist.

Kõik tulemused kontrolliti ja kohandati vastavalt projekti sisule.

## Projekti äriline väärtus

UrbanStyle projekt näitas, kuidas andmeanalüüsi abil saab toetada ärilisi otsuseid. Analüüside abil oli võimalik:

tuvastada andmekvaliteedi probleeme;
leida väärtuslikumaid kliendisegmente;
hinnata toodete ja kategooriate tulemuslikkust;
jälgida müügitulu ja kasvutrende;
tuvastada riskikohti kaupluste lõikes;
teha soovitusi turunduse ja kliendihoidmise parandamiseks.

## Kokkuvõte

UrbanStyle projekt andis praktilise kogemuse kogu andmeanalüüsi töövoost: andmete kogumisest ja puhastamisest kuni visualiseerimise, automatiseerimise ja äriliste järeldusteni. Projekt aitas kinnistada SQL-i, Power BI, Pythoni ja GitHubi kasutamist ning lõi tugeva aluse andmeanalüütiku portfoolio edasiarendamiseks.







