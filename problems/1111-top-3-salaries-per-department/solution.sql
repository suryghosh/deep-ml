-- your query
with rank_employee as(
    select department, salary,name,
    DENSE_RANK() over(
        partition by department
        order by salary desc
    ) as rnk
    from employees
)

select department,name,salary,rnk
from rank_employee
where rnk<=3
order by department asc,salary desc,name asc;

