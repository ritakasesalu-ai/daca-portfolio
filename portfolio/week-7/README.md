# Nädal 7: Python Pandas — RFM kliendisegmenteerimine

## Eesmärk

Selle nädala eesmärk oli kasutada Pythonit ja Pandase teeki kliendiandmete analüüsimiseks ning RFM-meetodi abil kliendisegmentide loomiseks. Fookus oli klientide ostukäitumise hindamisel ja äriliselt oluliste segmentide tuvastamisel.

## Minu roll: C

Minu vastutusala oli **RFM kliendisegmentide analüüs**. Keskendusin klientide jaotamisele segmentidesse ostude hiljutisuse, sageduse ja rahalise väärtuse põhjal.

## Tegevused

- Kasutasin Pythonit ja Pandast kliendi- ja müügiandmete töötlemiseks.
- Arvutasin RFM-näitajad:
  - **Recency** – mitu päeva on möödunud kliendi viimasest ostust;
  - **Frequency** – kui sageli klient on ostnud;
  - **Monetary** – kui suur on kliendi kogukulu.
- Lõin RFM skoorid ja kliendisegmendid.
- Analüüsisin segmentide suurust ja ärilist tähendust.
- Visualiseerisin tulemusi Plotly graafikutega.
- Kasutasin AI abi RFM-loogika struktureerimisel ja visualiseeringute koostamisel.

## Kasutatud tööriistad ja tehnoloogiad

| Tööriist / teek | Kasutus |
|---|---|
| Python | Andmetöötlus ja analüüs |
| Pandas | Andmete puhastamine, grupeerimine ja RFM arvutused |
| Plotly | Interaktiivsete visualiseeringute loomine |
| Jupyter Notebook / VS Code | Analüüsi läbiviimine |
| AI | Koodi selgitamine, RFM-loogika täpsustamine ja graafikute koostamise tugi |

## Peamised leiud

- Kõige suuremad kliendigrupid olid **Loyal Customers** ja **Regular Customers**.
- **Lost** segmendis oli 426 klienti.
- **At Risk** segmendis oli 339 klienti.
- Lost ja At Risk kliendid vajavad eraldi tähelepanu, sest nende varasem ostukäitumine viitab väärtusele, kuid nad ei ole viimasel ajal aktiivsed olnud.
- Segmentide põhjal saab koostada täpsemaid turundus- ja kliendihoidmise tegevusi.

## Analüüsi äriline tõlgendus

RFM analüüs aitab paremini mõista, millised kliendid on ettevõttele kõige väärtuslikumad ja millised kliendid vajavad taasaktiveerimist. Loyal ja Regular kliendid moodustavad tugeva kliendibaasi, kuid Lost ja At Risk segmentide suurus viitab sellele, et ettevõttel on oluline võimalus parandada kliendihoidmist.

## Soovitused

- Luua **win-back kampaania** Lost ja At Risk klientidele.
- Pakkuda Loyal klientidele personaalset lojaalsusprogrammi või varajast ligipääsu kampaaniatele.
- Analüüsida, millised tooted või kategooriad on seotud klientide lahkumisega.
- Jälgida RFM segmente ajas, et hinnata turundustegevuste mõju.

## AI kasutamine

Kasutasin AI abi RFM segmentide loomise loogika täpsustamisel ja Plotly graafikute koostamisel. AI aitas selgitada koodivigu, struktureerida analüüsi ning muuta visualiseeringud arusaadavamaks.

## Peamised õppetunnid

- Õppisin kasutama Pandast kliendiandmete segmenteerimiseks.
- Sain aru, kuidas RFM-mudel aitab klientide väärtust hinnata.
- Harjutasin andmete grupeerimist, skoorimist ja segmentide loomist.
- Sain praktilise kogemuse Plotly abil visuaalse analüüsi koostamisel.
- Mõistsin, kuidas tehniline analüüs siduda äriliste soovitustega.

## Failid

- [Kliendisegmendid_plotly](./individual/Plotly%202026-06-16%20134012.png)
- ![Grupitöö Plotly joonis](./team/Week-7%20grupitöö%20joonis.png)


## Meeskonnatöö

Osalesin meeskonna ühises töös, kus koondasime RFM analüüsi tulemused ja koostasime järeldused kliendisegmentide kohta.

- [Nädal 7 meeskonnatöö esitlus](https://docs.google.com/presentation/d/1CZDkJQtLjBZfta96Us-zmRCxgM44lmzfpXJE0tmJcXA/edit?usp=sharing)

## Tulemus

Nädala lõpuks valmis RFM kliendisegmenteerimise analüüs, mis aitas tuvastada väärtuslikumad kliendigrupid ning kliendid, kelle puhul on suurim taasaktiveerimise potentsiaal. Analüüs andis praktilise sisendi kliendihoidmise ja turundustegevuste planeerimiseks.
