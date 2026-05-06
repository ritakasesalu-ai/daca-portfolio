--Mitmel real puudub customer_id
SELECT COUNT (*) customer_id
FROM sales
WHERE customer_id IS NULL;


--kümme suurimat tellimust
SELECT sale_id, customer_id, total_price
FROM sales
ORDER BY total_price desc
LIMIT 10;


--10 väiksemat tellimust ja read, kus summa on 0 või väiksem
SELECT total_price, sale_id
FROM sales
WHERE total_price <= 0
ORDER BY total_price asc
LIMIT 10;
