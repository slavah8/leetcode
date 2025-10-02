# Write your MySQL query statement below

SELECT *
FROM Patients
WHERE REGEXP_LIKE(conditions, 
                  '(^|[[:space:]])DIAB1[0-9]*([[:space:]]|$)'
)