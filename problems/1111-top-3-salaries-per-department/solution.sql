-- your query
with rank_per_dept as(
    select department,name,salary, dense_rank() over(
        partition by department
        order by salary desc) as rnk
        from employees
)

select *
from rank_per_dept
where rnk<=3
order by department asc,salary desc,name asc
