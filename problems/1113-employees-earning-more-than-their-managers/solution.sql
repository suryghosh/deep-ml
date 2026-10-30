-- your query
SELECT e.name
from employees as e
where salary >(select salary
                from employees e1
                where e.manager_id = e1.id);
