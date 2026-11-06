-- your query--
with cheapest_per_customer as(
    select *,row_number() over(
        partition by customer_id
        order by amount asc,order_id asc
    )as rn
    from orders
    
)

select order_id,customer_id,amount
from cheapest_per_customer
where rn=1
order by customer_id asc