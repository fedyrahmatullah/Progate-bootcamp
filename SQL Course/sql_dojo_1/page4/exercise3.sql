-- dapatkan nama dan laba dari 5 barang dengan laba tertinggi
SELECT name, price - cost
FROM items
ORDER BY AVG(price - cost) DESC
LIMIT  5;