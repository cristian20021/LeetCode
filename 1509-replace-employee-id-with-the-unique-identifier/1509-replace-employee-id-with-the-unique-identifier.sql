# Write your MySQL query statement below
select unique_id, name from Employees as e left JOIN EmployeeUNI as uni on e.id = uni.id