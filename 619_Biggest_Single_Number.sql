with cte as (
select *,count(*) as cnt from 
MyNumbers
group by num
)

select max(num) as num from cte
where cnt = 1
