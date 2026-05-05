--kui palju on unikaalseid kliente
SELECT
    COUNT(*) AS ridade_arv,
    COUNT(customer_id) AS klientidega,
    COUNT(*) - COUNT(customer_id) AS puudub_klient,
    COUNT(DISTINCT customer_id) AS unikaalseid_kliente
FROM sales;

--Unikaalsed kliendid
SELECT DISTINCT channel
FROM sales
ORDER BY channel;

--Harjutus 3B Leia kõigi ridade arv
SELECT COUNT(*) AS kokku FROM sales;

--Leia unikaalsete ridade arv 
SELECT COUNT (DISTINCT sale_id) AS unikaalseid FROM sales;

--duplikaatide arvu leidmine
SELECT
  COUNT(*) AS kokku,
  COUNT (DISTINCT sale_id) AS unikaalseid,
  COUNT(*) - COUNT (DISTINCT sale_id) AS duplikaadid
  FROM sales;


  --puuduvate hindade leidmine
select
  COUNT (*) AS koguarv,
  COUNT (DISTINCT category) AS kategooriad,
  COUNT(*) - COUNT (DISTINCT cost_price) AS puuduvad_hinnad
  FROM products;


-- Küsimus: mitu duplikaati on?
SELECT
    COUNT(*) AS ridu_kokku,
    COUNT(DISTINCT sale_id) AS unikaalseid,
    COUNT(*) - COUNT(DISTINCT sale_id) AS duplikaate
FROM sales;


--Mitmel real puudub customer_id
SELECT COUNT (*) customer_id
FROM sales
WHERE customer_id IS NULL;


--kümme suurimat tellimust
SELECT sale_id, customer_id, total_price
FROM sales
ORDER BY total_price desc
LIMIT 10;
