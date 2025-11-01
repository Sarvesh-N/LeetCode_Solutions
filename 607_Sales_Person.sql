# Write your MySQL query statement below
with cte as(
    select o.sales_id from Orders o 
    left join  Company c on o.com_id = c.com_id
    where c.name = 'RED'
)
select sp.name from SalesPerson sp
where sp.sales_id not in (select * from cte)
