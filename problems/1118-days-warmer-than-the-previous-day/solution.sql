-- your query
with required_dates as(
    select recorded_on,temperature, lag(temperature,1) over(order by recorded_on) as prev1
    from weather
)

select recorded_on
from required_dates
where temperature > prev1
order by recorded_on asc
