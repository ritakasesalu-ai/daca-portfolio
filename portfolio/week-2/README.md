# Nädal 2: SQL Basics – UrbanStyle müügiandmete puhastamine

## Eesmärk

Selle nädala eesmärk oli jätkata UrbanStyle'i andmete uurimist ja keskenduda müügiandmete kvaliteedi parandamisele. Minu fookuses oli `sales` tabeli kontrollimine, probleemsete kirjete tuvastamine ja andmete puhastamine SQL-päringute abil.

## Minu roll: A

Minu vastutusala oli **müügiandmete** analüüs ja puhastamine. Töötasin `sales` tabeliga ning lõin puhastamise ja testimise jaoks eraldi töökoopia `sales_test`.

## Tegevused

- Lõin `sales` tabelist koopia nimega `sales_test`, et teha andmete kontroll ja puhastamine turvaliselt ilma algandmeid muutmata.
- Tuvastasin müügiandmetes duplikaate.
- Kontrollisin puudulikke väärtuseid, sh puuduvaid `customer_id` väärtuseid.
- Otsisin ebaloogilisi kuupäevi, sh tulevikku suunatud müügikuupäevi.
- Kasutasin andmete puhastamiseks ja kontrollimiseks SQL-päringuid.
- Osalesin meeskonna andmemaastiku koostamisel ja tulemuste koondamisel.

## Kasutatud SQL-võtted

- `HAVING COUNT` – duplikaatide ja korduvate kirjete leidmiseks.
- `COALESCE` – puuduvate väärtuste käsitlemiseks.
- `TRIM` – tekstiväljade puhastamiseks üleliigsetest tühikutest.
- `GROUP BY` – andmete grupeerimiseks.
- `COUNT` – kirjete arvu kontrollimiseks.
- `WHERE` – probleemsete ridade filtreerimiseks.

Näide kasutatud SQL-loogikast:

```sql
SELECT 
    sale_id,
    COUNT(*) AS korduste_arv
FROM sales_test
GROUP BY sale_id
HAVING COUNT(*) > 1;
```

```sql
SELECT *
FROM sales_test
WHERE customer_id IS NULL;
```

```sql
SELECT *
FROM sales_test
WHERE sale_date > CURRENT_DATE;
```

## Tuvastatud andmekvaliteedi probleemid

Müügiandmete kontrollimisel ilmnesid järgmised probleemid:

| Probleem | Tuvastatud kirjete arv |
|---|---:|
| Duplikaadid | 5116 |
| Puuduvad `customer_id` väärtused | 1487 |
| Tulevikku suunatud kuupäevad | 8 |

Need probleemid olid olulised, sest müügiandmete kvaliteet mõjutab otseselt hilisemat müügianalüüsi, kliendikäitumise hindamist ja aruannete usaldusväärsust.

## Peamised õppetunnid

- Õppisin, miks on andmete puhastamisel oluline töötada esmalt tabeli koopiaga, mitte algandmetega.
- Harjutasin duplikaatide leidmist SQL-i abil.
- Sain praktilise kogemuse puuduvate väärtuste ja ebaloogiliste kuupäevade tuvastamisel.
- Mõistsin, et enne analüüsi tegemist tuleb andmekvaliteedi probleemid süsteemselt kaardistada.
- Sain paremini aru, kuidas SQL-päringuid kasutada andmete valideerimiseks ja puhastamiseks.

## Failid ja materjalid

- [sales_raport.md](./individual/sales_raport.md)
- [Screenshot andmekvaliteedi kontrollist](./Screenshot%202026-06-29%20104913.png)

> Märkus: lokaalse arvuti failiteed nagu `C:\Users\kasutaja\Downloads\...` ei tööta GitHubis teiste kasutajate jaoks. Failid tuleks lisada GitHubi repositooriumisse ja linkida sealt.

## Meeskonnatöö

Osalesin meeskonna ühises andmemaastiku koostamises ja tulemuste esitlemises.

- [Nädal 2 esitlus](https://docs.google.com/presentation/d/1BcnNsggshzlO7VPdt3HL2pVNQ6fUf51dU6TCUTvWZsI/edit?usp=sharing)
- [Meeskonna ühine väljund](https://docs.google.com/presentation/d/1SgkHDv14phoKXOC8JEAE0xnzBpogqmn39e7obn6Km-I/edit?usp=sharing)

## Tulemus

Nädala lõpuks oli `sales` tabeli andmekvaliteedist parem ülevaade. Tuvastasin olulised probleemkohad, sh duplikaadid, puuduvad kliendi ID-d ja ebaloogilised kuupäevad. Need tulemused andsid aluse edasiseks andmete puhastamiseks ja usaldusväärsema analüüsi koostamiseks.

