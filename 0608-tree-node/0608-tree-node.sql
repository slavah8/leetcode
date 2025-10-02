# Write your MySQL query statement below

#CASE 
#    WHEN p_id = 'null' THEN 'Root'
#    WHEN p_id = 

SELECT DISTINCT t1.id AS id, 
CASE
    WHEN t1.p_id IS NULL THEN 'Root'
    WHEN COUNT(t2.id) = 0 THEN 'Leaf'
    ELSE 'Inner'
    END AS type
FROM Tree t1
LEFT JOIN Tree t2
  ON t1.id = t2.p_id
GROUP BY t1.id, t1.p_id

