-- this is comment 
SELECT score FROM second_table WHERE score = (SELECT count(score) as number FROM second_table) ORDER BY score DESC;