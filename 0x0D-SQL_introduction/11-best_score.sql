-- list all records from top top to bottom based on score

SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10  ORDER BY `score` DESC;
