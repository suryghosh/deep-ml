-- your query
select p.id,p.email from person p
where not exists(
    select 1
    from person p2
    where p2.email = p.email
    and p2.id<p.id
)
order by p.id asc;
