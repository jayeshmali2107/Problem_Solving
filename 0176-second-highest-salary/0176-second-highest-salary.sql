# Write your MySQL query statement below
Select(
    select distinct salary
    from Employee
    order by salary DESC
    limit 1 offset 1
) AS SecondHighestSalary ;