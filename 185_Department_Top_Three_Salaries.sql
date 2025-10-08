# Write your MySQL query statement below
with new as(
select d.name as Department, e.name as Employee, e.salary as Salary,
dense_rank() over(partition by e.departmentId order by e.salary desc) as ranker
from Employee e, Department d 
where  e.departmentId = d.id
)

select Department, Employee, Salary
from new
where ranker <4 
