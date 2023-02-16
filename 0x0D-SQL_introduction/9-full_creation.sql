-- Creates a table in current database in mysql server
-- insert data into newly created table

CREATE table IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT `second_table` (id, name, score) VALUES(1, 'John', 10);
INSERT `second_table` (id, name, score) VALUES(2, 'Alex' 3);
INSERT `second_table` (id, name, score) VALUES(3, 'Bob' 14);
INSERT `second_table` (id, name, score) VALUES(4, 'George', 8);
