# Write your MySQL query statement below
-- select player_id, min(event_date) as first_login
-- from Activity 
-- group by player_id 

with cte as (
    select *, dense_rank() over(partition by player_id order by event_date) as rnk
    from Activity
    
)

select player_id, event_date as first_login from cte 
where rnk = 1
