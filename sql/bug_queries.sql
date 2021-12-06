select * from bug;

-- show all possible bug locations
select distinct location from bug;

-- show all stump bugs, their price and months/hours available
select 
    b.id,
    b.name,
    b.price,
    months_avail.months,
    hours_avail.hours
from 
    bug b
    inner join (select bug_id, group_concat(month) as months from bug_month_availability group by bug_id) months_avail
        on b.id = months_avail.bug_id
    inner join (select bug_id, group_concat(hour) as hours from bug_hour_availability group by bug_id) hours_avail
        on b.id = hours_avail.bug_id
where location = 'On tree stumps';

select * from bug_month_availability where bug_id = 45;
