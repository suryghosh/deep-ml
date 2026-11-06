-- your query

with company_total as(
    select company,sum(profit) as total_profit
    from sales
    group by company
),

company_rank as(
    select company,total_profit, dense_rank() over(order by total_profit desc) as rn
    from company_total
)

select company, total_profit
from company_rank
where rn<=3
order by total_profit desc,company asc