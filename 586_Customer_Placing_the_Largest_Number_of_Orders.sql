with cte as(
    select *, count(customer_number) as count_track 
    from Orders
    group by customer_number
    order by count_track desc

)

select customer_number 
from cte
limit 1
