-- your query
with max_salary_dept as (select p.name as worker_name,p.salary as max_salary,titles.title as final_title
from workers as p
inner join titles on p.title_id = titles.title_id
where p.salary = (select max(salary)
                from workers as p1
                where p.title_id = p1.title_id)
)

select worker_name,max_salary,final_title
from max_salary_dept
where max_salary = (select max(max_salary) from max_salary_dept)
order by worker_name asc

