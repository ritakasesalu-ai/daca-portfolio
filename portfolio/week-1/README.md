# Nädal 1: SQL Basics – UrbanStyle andmete esmane uurimine

## Eesmärk

Selle nädala eesmärk oli tutvuda UrbanStyle'i andmebaasi struktuuriga ning teha esmane andmete uurimine SQL-päringute abil. Minu fookuses oli `customers` tabel ehk kliendiandmete kvaliteedi ja sisu analüüs.

## Minu roll: B

Minu vastutusala oli **customers tabeli** uurimine. Keskendusin kliendiandmete struktuurile, puuduvatele väärtustele, duplikaatidele ja andmekvaliteedi probleemidele.

## Tegevused

- Uurisin `customers` tabelit SQL-päringutega.
- Kasutasin peamisi SQL-käske:
  - `SELECT`
  - `FROM`
  - `WHERE`
  - `ORDER BY`
- Kontrollisin, millised veerud ja väärtused tabelis olemas on.
- Tuvastasin linnade kirjapildi erinevusi ja võimalikke duplikaate.
- Otsisin puudulikke andmeid ja `NULL` väärtuseid.
- Harjutasin ridade nummerdamist ja duplikaatide leidmist.
- Osalesin meeskonna andmemaastiku koostamisel.

## Kasutatud SQL-võtted

```sql
SELECT *
FROM customers;

SELECT city, COUNT(*) AS klientide_arv
FROM customers
GROUP BY city
ORDER BY klientide_arv DESC;

SELECT *
FROM customers
WHERE city IS NULL;
```

## Peamised õppetunnid

- Õppisin kirjutama lihtsamaid SQL-päringuid andmete uurimiseks.
- Sain paremini aru, kuidas kasutada `SELECT`, `WHERE` ja `ORDER BY` käske.
- Harjutasin SQL-veateadete lugemist ja parandamist.
- Sain praktilise kogemuse andmekvaliteedi probleemide leidmisel.
- Mõistsin, miks on oluline kontrollida puudulikke väärtuseid, duplikaate ja ebaühtlast kirjapilti enne analüüsi tegemist.

## Andmekvaliteedi tähelepanekud

**`customers` tabeli uurimisel ilmnes, et kliendiandmetes võib esineda:**

- puudulikke väärtuseid;
- linnade erinevaid kirjapilte;
- võimalikke duplikaate;
- andmeid, mis vajavad enne edasist analüüsi puhastamist.

Need tähelepanekud olid olulised, sest kliendiandmete kvaliteet mõjutab otseselt hilisemat segmenteerimist, müügi analüüsi ja turunduskanalite hindamist.

## Failid ja lingid

Osalesin meeskonna andmemaastiku koostamisel, kus kaardistasime UrbanStyle'i andmestikud, tabelid ja võimalikud andmekvaliteedi probleemid.

- [Meeskonna töö esitlus](https://docs.google.com/presentation/d/1aXzLf3nE0F-znkdW4CAMFus0Ee_wwbt3CyUBsSquF4Q/edit?usp=sharing)
- [Ühisväljund](https://docs.google.com/presentation/d/1aXzLf3nE0F-znkdW4CAMFus0Ee_wwbt3CyUBsSquF4Q/edit?usp=sharing)

## Tulemus

Nädala lõpuks oli mul parem ülevaade UrbanStyle'i kliendiandmetest ja SQL-i kasutamisest andmete esmaseks uurimiseks. Tuvastatud andmekvaliteedi probleemid andsid sisendi järgmisteks etappideks, kus keskendutakse andmete puhastamisele ja põhjalikumale analüüsile.

