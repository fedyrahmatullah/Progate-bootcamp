/*
dapatkan id dan jumlah penjualan per unitnya dari 5 barang paling populer.
Susun hasilnya secara menurun
*/
SELECT item_id, COUNT(*)
FROM sales_records
GROUP BY item_id
ORDER BY COUNT(item_id) DESC
LIMIT 5;