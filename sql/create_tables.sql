-- create tables for fish and bugs
-- this includes the month and hour availability tables

create table fish (
    id int,
    name varchar,
    month_northern varchar,
    month_southern varchar,
    time varchar,
    is_all_day boolean,
    is_all_year boolean,
    location varchar,
    rarity varchar,
    shadow varchar,
    price int,
    price_cj int,
    catch_phrase varchar,
    museum_phrase varchar,
    image_uri varchar,
    icon_uri varchar    
);

create table fish_month_availability (
    fish_id int,
    month int
);

create table fish_hour_availability (
    fish_id int,
    hour int
);

create table bug (
    id int,
    name varchar,
    month_northern varchar,
    month_southern varchar,
    time varchar,
    is_all_day boolean,
    is_all_year boolean,
    location varchar,
    rarity varchar,
    price int,
    price_flick int,
    catch_phrase varchar,
    museum_phrase varchar,
    image_uri varchar,
    icon_uri varchar    
);

create table bug_month_availability (
    bug_id int,
    month int
);

create table bug_hour_availability (
    bug_id int,
    hour int
);

create table sea_creature (
    id int,
    name varchar,
    month_northern varchar,
    month_southern varchar,
    time varchar,
    is_all_day boolean,
    is_all_year boolean,
    speed varchar,
    shadow varchar,
    price int,
    catch_phrase varchar,
    museum_phrase varchar,
    image_uri varchar,
    icon_uri varchar    
);

create table sea_creature_month_availability (
    sea_creature_id int,
    month int
);

create table sea_creature_hour_availability (
    sea_creature_id int,
    hour int
);
