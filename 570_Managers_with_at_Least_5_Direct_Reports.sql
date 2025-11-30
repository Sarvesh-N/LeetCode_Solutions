-- # Write your MySQL query statement below
-- with cte as (
--     select *, rank() over(partition by managerId) as rank_v from Employee
-- )

-- select name from cte 
-- where managerId is null

select name 
from Employee
where id in (
    select managerId from Employee 
    group by managerId
    having count(managerId) >= 5
)
