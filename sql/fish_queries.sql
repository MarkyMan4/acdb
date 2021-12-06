-- show ultra rare fish
select * from fish where rarity = 'Ultra-rare';

-- fish with a specific location
select * from fish where location = 'Sea (when raining or snowing)';

-- fish available in month of December
select *
from fish
where id in (
    select fish_id
    from fish_month_availability
    where month = 12
)
and is_all_year = false
order by price desc;

-- show all months coelacanths are available
select 
    group_concat(month) 
from fish_month_availability 
where 
    fish_id = (select id from fish where name = 'coelacanth') 
group by fish_id;