-- your query
with distinct_values as(
    select id,num,lag(num,1) over(order by id) as prev1,lag(num,2) over(order by id) as prev2 
from logs
)

select distinct(num)
from distinct_values
where num = prev1 and num = prev2
order by id ASC
