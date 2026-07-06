 
# Nädal 4: SQL agregatsioonid – UrbanStyle kliendi- ja müügiandmete koondanalüüs

## Eesmärk

Selle nädala eesmärk oli kasutada SQL agregatsioonifunktsioone UrbanStyle'i müügi- ja kliendiandmete analüüsimiseks. Fookus oli klientide segmenteerimisel, koondstatistika koostamisel ja äriliselt oluliste mustrite leidmisel.

## Tegevused

- Uurisin `sales` ja `products` tabelite andmeid SQL-päringute abil.
- Kasutasin `GROUP BY`, `HAVING` ja CTE-päringuid andmete koondamiseks.
- Analüüsisin klientide ostukäitumist ja müügimustreid.
- Leidsin kliendisegmentide arvu ja jaotuse.
- Analüüsisin klientide paiknemist linnade lõikes.
- Arvutasin segmentide osakaalusid ja protsente.
- Leidsin TOP kliendid müügimahu põhjal.
- Osalesin meeskonna ühise andmemaastiku täiendamisel.

## Kasutatud SQL-võtted

- `GROUP BY` – andmete grupeerimiseks klientide, linnade ja segmentide lõikes.
- `HAVING` – agregeeritud tulemuste filtreerimiseks.
- `COUNT` – kirjete ja klientide arvu leidmiseks.
- `SUM` – müügitulu arvutamiseks.
- `AVG` – keskmiste väärtuste leidmiseks.
- CTE ehk `WITH` – keerukamate päringute loetavamaks muutmiseks.
- `ROUND` – protsentide ja koondnäitajate vormindamiseks.

Näide kasutatud SQL-loogikast:

```sql
WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(total_price) AS total_revenue,
        COUNT(sale_id) AS order_count
    FROM sales
    GROUP BY customer_id
)

SELECT
    customer_id,
    total_revenue,
    order_count
FROM customer_sales
ORDER BY total_revenue DESC;
```

```sql
SELECT
    city,
    COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;
```

## Peamised õppetunnid

- Õppisin kasutama SQL agregatsioonifunktsioone äriliste küsimuste lahendamiseks.
- Sain praktilise kogemuse kliendigruppide ja segmentide analüüsimisel.
- Harjutasin TOP klientide leidmist müügitulu põhjal.
- Mõistsin, kuidas CTE-d aitavad keerukamaid päringuid paremini struktureerida.
- Sain aru, kuidas protsente ja osakaalusid kasutada segmentide võrdlemisel.
- Nägin, kuidas koondstatistika aitab muuta toorandmed otsustamiseks sobivaks infoks.

## Andmeanalüüsi tähelepanekud

Agregatsioonide abil oli võimalik paremini mõista:

- millised kliendid toovad kõige rohkem müügitulu;
- kuidas kliendid jagunevad segmentidesse;
- millistes linnades on rohkem kliente;
- milline on segmentide osakaal kogu kliendibaasis;
- kuidas koondnäitajad aitavad tuvastada äriliselt olulisemaid kliendigruppe.

Need tulemused on kasulikud turunduse, kliendisuhete ja müügistrateegia planeerimisel.

## Failid

- [Screenshot agregatsioonide analüüsist](./individual/Screenshot%202026-06-29%20113217.png)
- [Screenshot meeskonnatööst](./team/Screenshot%202026-05-28%142511.png)

## Meeskonnatöö

Osalesin meeskonna ühises töös, kus koondasime SQL agregatsioonide abil saadud analüüsitulemused ja täiendasime UrbanStyle'i andmemaastikku.

- [Nädal 4 meeskonnatöö](https://docs.google.com/presentation/d/1tbIiPYJxc-yxuHtq9sLmANHu4wQizf4JiTInjs3-Zw8/edit?usp=sharing)
- [Nädal 4 esitlus](https://docs.google.com/presentation/d/13s3JPCfBR9_IiEsRQUb8sc7okAs09u4Pq71ZO_vHQQA/edit?usp=sharing)

## Tulemus

Nädala lõpuks oskasin kasutada SQL agregatsioone kliendi- ja müügiandmete koondamiseks. Analüüsi tulemusena sain parema ülevaate kliendisegmentidest, TOP klientidest ja linnade lõikes jaotuvatest müügiandmetest. Need oskused on olulised andmeanalüütiku töös, sest aitavad muuta detailsed andmed juhtimisotsuseid toetavaks kokkuvõtteks.
 
