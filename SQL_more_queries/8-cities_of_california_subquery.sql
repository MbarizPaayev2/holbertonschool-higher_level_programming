-- THIS IS CODE 
SELECT id, name 
FROM cities 
WHERE state.id IN( 
SELECT id 
FROM states 
WHERE name = 'California'
)
ORDER BY id ASC;