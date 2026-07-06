# Nädal 6: UrbanStyle Power BI Dashboard

## Eesmärk

Selle nädala eesmärk oli täiendada UrbanStyle'i Power BI dashboardi ning kujundada andmete põhjal selge juhtimisvaade, mis aitab esile tuua ettevõtte müügitulemused, kasvutrendid ja võimalikud riskikohad.

## Minu roll: C

Minu roll oli keskenduda dashboardi analüütilisele loole ja peamiste äriliste leidude esiletoomisele. Fookuses olid müügitulu, aastane kasv, enim panustavad tootekategooriad ja kaupluste tulemuslikkus.

## Peamised leiud

- **Kogu müügitulu:** 2,79 miljonit eurot.
- **Aastane kasv:** +119,6% YoY.
- **Hero product:** Denim Jacket, mis moodustas 28% kogukäibest.
- **Peamine risk:** Tartu kaupluse müügitulemuse langus −5%.
- **Äriline võimalus:** Denim tooteliini tugev tulemus viitab võimalusele investeerida rohkem selle kategooria sortimenti ja turundusse.

## Kasutatud tehnoloogiad

| Tööriist / tehnoloogia | Kasutus |
|---|---|
| Power BI Desktop | Dashboardi loomine ja andmete visualiseerimine |
| Power BI Service | Dashboardi avaldamine ja jagamine |
| Supabase | PostgreSQL andmebaasi haldamine |
| PostgreSQL | Andmete pärimine ja ettevalmistamine |
| DAX | Mõõdikute loomine, sh YoY Growth ja Revenue Category |

## Kasutatud mõõdikud

Dashboardis kasutati äriliste järelduste tegemiseks järgmisi mõõdikuid:

- kogumüügitulu;
- müügitulu muutus ajas;
- YoY kasv;
- müügitulu tootekategooriate lõikes;
- müügitulu kaupluste lõikes;
- kõige suurema mõjuga tooted ja kategooriad.

## Dashboardi lugu

### Setup

UrbanStyle on kasvav moebränd, mille müük toimub kolme kaupluse kaudu. Juhtkonna jaoks on oluline mõista, millised tooted, kategooriad ja kauplused veavad ettevõtte kasvu ning kus võivad tekkida ärilised riskid.

### Data

Kolme aasta müügiandmed näitasid tugevat kasvu. Suurima panuse andis Denim tooteseeria, eriti Denim Jacket, mis moodustas märkimisväärse osa kogukäibest.

### Insight

Analüüs näitas, et Denim tooteliin on ettevõtte üks olulisemaid kasvumootoreid. Samal ajal vajab tähelepanu Tartu kauplus, kus müügitulemus oli languses.

### Action

Soovitusena tuleks:

- suurendada investeeringuid Denim tooteliini;
- analüüsida Tartu kaupluse languse põhjuseid;
- võrrelda Tartu kaupluse tulemust teiste kauplustega;
- hinnata, kas probleem on seotud sortimendi, kliendivoo, kampaaniate või piirkondliku nõudlusega.

## Peamised õppetunnid

- Õppisin looma dashboardi, mis ei näita ainult graafikuid, vaid räägib ärilise loo.
- Sain praktilise kogemuse DAX-mõõdikute kasutamisel.
- Harjutasin YoY kasvu ja kategooriapõhise müügitulu analüüsimist.
- Mõistsin, kui oluline on dashboardi puhul siduda andmed konkreetsete juhtimisotsustega.
- Sain paremini aru, kuidas esile tuua nii kasvuvõimalusi kui ka äririske.

## Failid

- [dashboard_iseseisevtöö](./individual/Screenshot%202026-06-09%20123154.png)

## Meeskonnatöö

Osalesin meeskonna ühises töös, kus koondasime UrbanStyle'i müügiandmete analüüsi ja dashboardi tulemused juhtimisvaateks.

- [Nädal 6 esitlus](https://docs.google.com/presentation/d/18FoIuTprMaYyE0hOBaxyL5kXHzFRYriQQ8YB4auNi1M/edit?usp=sharing)

## Failid ja materjalid

Kui dashboardi pilt asub samas kaustas kui README, kasuta:

```markdown
![UrbanStyle Dashboard](./dashboard_screenshot.png)
```

Kui pilt asub näiteks `team` kaustas, kasuta:

```markdown
![UrbanStyle Dashboard](./team/dashboard_screenshot.png)
```

## Tulemus

Nädala lõpuks valmis UrbanStyle'i Power BI dashboard, mis tõi esile ettevõtte müügitulemused, YoY kasvu, tugevaima tootekategooria ja Tartu kauplusega seotud riski. Dashboardi põhjal sai teha selgeid ärilisi soovitusi edasiseks tegevuseks.
