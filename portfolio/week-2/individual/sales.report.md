
--Enne puhastamist
-- Kontrolli ridade arvu
SELECT COUNT(*) AS ridade_arv FROM sales_test;
--ridade arv 15234


--Peale puhastamist
-- Kustuta duplikaadid (jäta alles ainult esimene rida iga sale_id kohta)
DELETE FROM sales_test
WHERE id NOT IN (
    SELECT MIN(id)
    FROM sales_test
    GROUP BY sale_id
);
--Enne ridu kokku 15234
-- Pärast ridu kokku 10118
