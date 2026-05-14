supabase snippets download 262feae3-fe9f-4955-bae3-e6bf2ce41373 > \
  week_2_sales_cleaning.sql
portfolio/week-2/individual/week2_cleaning.sql

-- Müügiandmete puhastamine roll A 
--Loo tabel sales test koopia
CREATE TABLE sales_test AS SELECT * FROM sales;

-- Kontrolli ridade arvu
SELECT COUNT(*) AS ridade_arv FROM sales_test;
--ridade arv 15234

--Korduvate tellimuste duplikaatide leidmine
SELECT sale_id, 
  COUNT(*) AS koopiate_arv
FROM sales_test
GROUP BY sale_id
HAVING COUNT(*) > 1
ORDER BY koopiate_arv DESC;
--Suurim korduvate tellimuste id number on 6


--Mitu rida on duplikaatseid sale_id-sid
SELECT COUNT(*) AS duplikaat_read
FROM sales_test
WHERE id NOT IN (
    SELECT MIN(id)    --iga id veeru kohta kõige väiksema
    FROM sales_test
    GROUP BY invoice_id
);
--duplikaatsid sale_id sid on kokku 5116 rida

SELECT COUNT(*) AS duplikaat_read
FROM (
    SELECT invoice_id
    FROM sales_test
    GROUP BY invoice_id
    HAVING COUNT(*) > 1
) t;
--Duplikaate müügiarvetes 4013

--NULL väärtuste leidmine kriitilistes väljades
SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS null_customer_id,
    COUNT(*) FILTER (WHERE sale_date IS NULL) AS null_sale_date,
    COUNT(*) FILTER (WHERE total_price IS NULL) AS null_total_price
FROM sales_test;
--Customer_id-s 1487 NULL väärtust
--Sales_dates ei ole NULL väärtuseid
--Total_prises ei ole NULL väärtust

--Tuleviku kuupäevade kontrollimine
SELECT COUNT(*) AS tuleviku_kuupaevad
FROM sales_test
WHERE sale_date > CURRENT_DATE;
--Kokku 8 rida tulevikukuupäevi


--Duplikaatide leidmine mitme veeru järgi
SELECT customer_id, invoice_id, COUNT(*) AS duplikaate
FROM sales_test
GROUP BY customer_id, invoice_id
HAVING COUNT(*) > 1;

SELECT * FROM sales_test

-- Kustuta duplikaadid (jäta alles ainult esimene rida iga sale_id kohta)
DELETE FROM sales_test
WHERE id NOT IN (
    SELECT MIN(id)
    FROM sales_test
    GROUP BY sale_id
);
--Enne ridu kokku 15234
-- Pärast ridu kokku 10118

SELECT COUNT(*) AS ridade_arv FROM sales_test;

--Külalisostude leidmine
SELECT COUNT(*) AS külalisostud FROM sales_test WHERE customer_id IS NULL;
--Tundmatuid kliente kokku 988

--Ajutise sildi andmine tundmatutele klientidele
SELECT COALESCE(customer_id, -1) AS customer_id_puhas FROM sales_test;

-- Paranda tuleviku kuupäevad
UPDATE sales_test
SET sale_date = CURRENT_DATE
WHERE sale_date > CURRENT_DATE;


-- Kontrolli tulemust
SELECT COUNT(*) AS ridu_parast FROM sales_test;

