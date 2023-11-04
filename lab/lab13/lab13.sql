.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students as a, students as b
  WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time
  ;


CREATE TABLE sevens AS
  SELECT s.seven
  FROM students AS s, numbers as n
  WHERE s.time = n.time AND n."7" = "True" AND s.number = 7
  ;


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price
  FROM products
  GROUP BY category;



CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price)
  FROM inventory
  GROUP BY item 
  ;

CREATE TABLE shopping_list AS
SELECT
  p.name AS product_name,
  lp.store AS store_name
FROM products p
JOIN (
  SELECT item, store
  FROM lowest_prices
) lp ON p.name = lp.item
WHERE (p.category, p.MSRP / p.rating) IN (
  SELECT category, MIN(MSRP / rating)
  FROM products
  GROUP BY category
);


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs)
  FROM stores, shopping_list AS s
  WHERE s.store_name = store
  ;

