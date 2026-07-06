# Nädal 3: SQL JOIN-id – UrbanStyle tabelite ühendamine

## Eesmärk

Selle nädala eesmärk oli õppida kasutama SQL JOIN-e ning ühendada UrbanStyle'i erinevaid tabeleid, et saada terviklikum ülevaade toodetest, müügist ja inventuurist.

## Tegevused

- Analüüsisin UrbanStyle'i toodete, müügi ja inventuuri andmeid SQL JOIN-ide abil.
- Kasutasin `LEFT JOIN` päringuid, et leida seoseid toodete ja müügiandmete vahel.
- Tuvastasin tooted, mida ei ole kunagi müüdud.
- Analüüsisin enim müüdud tooteid ja tootekategooriaid.
- Harjutasin tabelite ühendamist erinevate võtmeväljade kaudu.
- Osalesin meeskonna ühise andmemaastiku täiendamisel ja tulemuste koondamisel.

## Kasutatud SQL-võtted

- `INNER JOIN` – ainult kattuvate kirjete ühendamiseks.
- `LEFT JOIN` – vasakpoolses tabelis olevate kirjete säilitamiseks ka siis, kui seotud tabelis vastet ei ole.
- `RIGHT JOIN` – parempoolses tabelis olevate kirjete säilitamiseks.
- `LEFT JOIN ... WHERE ... IS NULL` – selliste kirjete leidmiseks, millel seotud tabelis vastet ei ole.
- `GROUP BY` – müügitulemuste koondamiseks toodete või kategooriate lõikes.
- `ORDER BY` – tulemuste sorteerimiseks.

Näide kasutatud SQL-loogikast:

```sql
SELECT 
    p.product_id,
    p.product_name,
    s.sale_id
FROM products p
LEFT JOIN sales s
    ON p.product_id = s.product_id
WHERE s.sale_id IS NULL;
```

```sql
SELECT 
    p.category,
    COUNT(s.sale_id) AS muukide_arv
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY p.category
ORDER BY muukide_arv DESC;
```

## Peamised õppetunnid

- Sain aru, kuidas SQL JOIN-id aitavad ühendada erinevates tabelites asuvaid andmeid.
- Õppisin eristama `INNER JOIN`, `LEFT JOIN` ja `RIGHT JOIN` kasutusjuhtumeid.
- Harjutasin `LEFT JOIN ... WHERE ... IS NULL` loogikat, et leida müügita tooteid.
- Mõistsin, miks on tabelite vahelised võtmeväljad olulised usaldusväärse analüüsi tegemisel.
- Sain praktilise kogemuse toodete ja müügiandmete ühendamisel äriliste küsimuste lahendamiseks.

## Andmeanalüüsi tähelepanekud

JOIN-päringute abil oli võimalik tuvastada:

- tooted, mida ei ole müügiandmetes esinenud;
- enim müüdud tooted;
- enim müüdud tootekategooriad;
- võimalikud seosed toodete, müügi ja inventuuri vahel.

Need tulemused aitavad paremini mõista sortimendi toimivust ja toetavad otsuseid, milliseid tooteid hoida, täiendada või turunduses esile tõsta.

## Failid

- [Toodete_inventuur](./individual/week3_roll_c_tooted_inventuur.sql.pdf)
- [Tooted_mida_pole_müüdud](./team/Screenshot 2026-06-29 110641.png)

## Meeskonnatöö

Osalesin meeskonna ühises töös, kus koondasime JOIN-ide abil saadud analüüsitulemused ja täiendasime UrbanStyle'i andmemaastikku.

- [Meeskonna ühine väljund](https://docs.google.com/presentation/d/1stgOnJj5M1Ad-faRhcyw6zJNZPI51Py9pXDsiZ-9yJU/edit?usp=sharing)
- [Nädal 3 esitlus](https://docs.google.com/presentation/d/1W0El676wx7z0IxYhrn1IA5g9TkEOSEp8q1nX2Pd82Ao/edit?usp=sharing)

## Tulemus

Nädala lõpuks oskasin kasutada SQL JOIN-e mitme tabeli ühendamiseks ning sain aru, kuidas tabelitevaheliste seoste abil vastata sisulistele äriküsimustele. Analüüsi tulemusena oli võimalik leida müügita tooteid, hinnata enim müüdud tooteid ja toetada andmepõhisemat sortimendi analüüsi.


