# Write your MySQL query statement below

with new as(
    select score, dense_rank() over(order by score desc) as another
    from Scores
)

select score , another as 'rank'
from new
