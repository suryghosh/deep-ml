-- your query
with arranged_table as(
    select customer_id,order_date,sum(amount) as total
    from orders
    group by customer_id,order_date
    having order_date >='2024-01-01' and order_date<='2024-01-31'
    
)

select total
from arranged_table
order by total desc
limit 1

