-- your query
with group_month as(
    select DATE_TRUNC('month',sale_date) as months,sum(amount) as total
    From sales
    group by DATE_TRUNC('month',sale_date)

),

previous_sale as(
    select months, total,
    lag(total) over (order by months) as previous_total
    from group_month
)

select months,total, ROUND(100*(total-previous_total)/NULLIF(previous_total,0),2) as pct_change
from previous_sale
order by months asc
