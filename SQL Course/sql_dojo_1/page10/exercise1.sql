-- dapatkan data total penjualan untuk gender pria, wanita, dan netral
SELECT items.gender, SUM(price) AS "total penjualan"
FROM sales_records
JOIN items
ON sales_records.item_id = items.id
GROUP BY items.gender