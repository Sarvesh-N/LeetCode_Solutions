with cte as(
    select *, row_number() over(partition by email order by id) as cnt
    from Person 
)

delete from Person
where id in(
    select id from cte where cnt > 1
)
