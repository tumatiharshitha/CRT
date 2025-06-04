CREATE TABLE sales (
  sno INT,
  product_name VARCHAR(100),
  quantity INT,
  category VARCHAR(300)
);

INSERT INTO sales (sno, product_name, quantity, category)
VALUES
  (1, 'charger', 10, 'electronics'),
  (2, 'keypad', 20, 'home'),
  (3, 'mouse', 25, 'home'),
  (4, 'wire', 30, 'electronics'),
  (5, 'cpu', 40, 'clothes'),
  (6, 'display', 60, 'home'),
  (8, 'chair', 70, 'electronics'),
  (9, 'remote', 80, 'electronics'),
  (10, 'fan', 90, 'home');

UPDATE sales
SET quantity = 20
WHERE category = 'electronics';

SELECT *
FROM sales;