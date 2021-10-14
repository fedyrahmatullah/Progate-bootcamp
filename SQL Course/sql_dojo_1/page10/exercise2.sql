-- dapatkan data untuk 5 produk dengan penjualan tertinggi 
SELECT items.id, items.name, items.price * COUNT(*) AS "total penjualan"
FROM sales_records
JOIN items
ON sales_records.item_id = items.id
GROUP BY items.id, items.name, items.price
ORDER BY items.price * COUNT(*) DESC
LIMIT 5;