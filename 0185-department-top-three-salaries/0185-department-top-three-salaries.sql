/* Write your T-SQL query statement below */

SELECT d.name as Department, e.name as Employee, e.salary as Salary 
FROM Employee e JOIN Department d 
ON e.departmentId = d.id 
WHERE (SELECT COUNT(DISTINCT em.salary) FROM Employee em WHERE em.salary > e.salary AND 
      em.departmentId = e.departmentId) < 3 ORDER BY e.salary DESC