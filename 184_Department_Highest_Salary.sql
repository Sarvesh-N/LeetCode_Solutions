# Write your MySQL query statement below
with another as(
select *,
dense_rank() over(partition by departmentId order by salary desc) as for_salary
from Employee
)

select d.name as Department, e.name as Employee, e.salary as Salary
from another e 
inner join Department d on e.departmentId = d.id
where e.for_salary = 1


