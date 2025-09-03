# Write your MySQL query statement below
select firstName,lastName,city,state from Person left join Address ON Person.personId = Address.personId


-- SELECT column_name(s)
-- FROM table1
-- FULL OUTER JOIN table2
-- ON table1.column_name = table2.column_name
-- WHERE condition;