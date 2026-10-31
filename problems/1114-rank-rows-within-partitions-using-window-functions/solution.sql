-- your query--
with rank_employee as(
    select department,employee,score,Row_Number() over (
        partition by department
        order by score desc, employee asc
    ) as rn, Rank() over(
        partition by department
        order by score desc
    )as rnk, Dense_Rank() over(
        partition by department
        order by score desc 
    )as dense_Rnk
 from scores)

 select department,employee,score,rn,rnk,dense_Rnk
 from rank_employee
 order by department asc,score desc,employee asc;
