import requests
import json
import sqlite3

class Collector:
    # con: sqlite connection object
    def __init__(self, con):
        self.con = con
        self.base_url = 'http://acnhapi.com/v1/'

    def truncate_tables(self, cur, table_list):
        # truncate tables in the list provided
        for t in table_list:
            try:
                cur.execute(f'delete from {t}')
            except:
                print(f'table {t} does not exist')

    def collect_fish(self):
        url = self.base_url + 'fish'
        cur = self.con.cursor()

        self.truncate_tables(cur, ['fish', 'fish_month_availability', 'fish_hour_availability'])

        r = requests.get(url)
        data = json.loads(r.text)

        # each key in the JSON is the fish name, pull the fields out of the JSON and insert records into tables
        for key in data.keys():
            fish_id = data[key]['id']
            name = data[key]['name']['name-USen'].replace("'", "''")
            month_northern = data[key]['availability']['month-northern'].replace("'", "''")
            month_southern = data[key]['availability']['month-southern'].replace("'", "''")
            time = data[key]['availability']['time'].replace("'", "''")
            is_all_day = data[key]['availability']['isAllDay']
            is_all_year = data[key]['availability']['isAllYear']
            location = data[key]['availability']['location'].replace("'", "''")
            rarity = data[key]['availability']['rarity'].replace("'", "''")
            shadow = data[key]['shadow'].replace("'", "''")
            price = data[key]['price']
            price_cj = data[key]['price-cj']
            catch_phrase = data[key]['catch-phrase'].replace("'", "''")
            museum_phrase = data[key]['museum-phrase'].replace("'", "''")
            image_uri = data[key]['image_uri']
            icon_uri = data[key]['icon_uri']

            month_availability_list = data[key]['availability']['month-array-northern']
            hour_availability_list = data[key]['availability']['time-array']

            # insert record into fish table
            cur.execute(f"""
                insert into fish values (
                    {fish_id}, 
                    '{name}', 
                    '{month_northern}', 
                    '{month_southern}', 
                    '{time}', 
                    {is_all_day}, 
                    {is_all_year}, 
                    '{location}', 
                    '{rarity}', 
                    '{shadow}', 
                    {price},
                    {price_cj},
                    '{catch_phrase}',
                    '{museum_phrase}',
                    '{image_uri}',
                    '{icon_uri}'
                )
            """)

            # insert records into month availability table
            for month in month_availability_list:
                cur.execute(f"""
                    insert into fish_month_availability values (
                        {fish_id},
                        {month}
                    )
                """)

            # insert records into hour availability table
            for hour in hour_availability_list:
                cur.execute(f"""
                    insert into fish_hour_availability values (
                        {fish_id},
                        {hour}
                    )
                """)

        self.con.commit()

    def collect_bugs(self):
        url = self.base_url + 'bugs'
        cur = self.con.cursor()

        self.truncate_tables(cur, ['bug', 'bug_month_availability', 'bug_hour_availability'])

        r = requests.get(url)
        data = json.loads(r.text)

        # each key in the JSON is the bug name, pull the fields out of the JSON and insert records into tables
        for key in data.keys():
            bug_id = data[key]['id']
            name = data[key]['name']['name-USen'].replace("'", "''")
            month_northern = data[key]['availability']['month-northern'].replace("'", "''")
            month_southern = data[key]['availability']['month-southern'].replace("'", "''")
            time = data[key]['availability']['time'].replace("'", "''")
            is_all_day = data[key]['availability']['isAllDay']
            is_all_year = data[key]['availability']['isAllYear']
            location = data[key]['availability']['location'].replace("'", "''")
            rarity = data[key]['availability']['rarity'].replace("'", "''")
            price = data[key]['price']
            price_flick = data[key]['price-flick']
            catch_phrase = data[key]['catch-phrase'].replace("'", "''")
            museum_phrase = data[key]['museum-phrase'].replace("'", "''")
            image_uri = data[key]['image_uri']
            icon_uri = data[key]['icon_uri']

            month_availability_list = data[key]['availability']['month-array-northern']
            hour_availability_list = data[key]['availability']['time-array']

            # insert record into fish table
            cur.execute(f"""
                insert into bug values (
                    {bug_id}, 
                    '{name}', 
                    '{month_northern}', 
                    '{month_southern}', 
                    '{time}', 
                    {is_all_day}, 
                    {is_all_year}, 
                    '{location}', 
                    '{rarity}', 
                    {price},
                    {price_flick},
                    '{catch_phrase}',
                    '{museum_phrase}',
                    '{image_uri}',
                    '{icon_uri}'
                )
            """)

            # insert records into month availability table
            for month in month_availability_list:
                cur.execute(f"""
                    insert into bug_month_availability values (
                        {bug_id},
                        {month}
                    )
                """)

            # insert records into hour availability table
            for hour in hour_availability_list:
                cur.execute(f"""
                    insert into bug_hour_availability values (
                        {bug_id},
                        {hour}
                    )
                """)

        self.con.commit()

    def collect_sea_creatures(self):
        url = self.base_url + 'sea'
        cur = self.con.cursor()

        self.truncate_tables(cur, ['sea_creature', 'sea_creature_month_availability', 'sea_creature_hour_availability'])

        r = requests.get(url)
        data = json.loads(r.text)

        # each key in the JSON is the sea_creature name, pull the fields out of the JSON and insert records into tables
        for key in data.keys():
            sea_creature_id = data[key]['id']
            name = data[key]['name']['name-USen'].replace("'", "''")
            month_northern = data[key]['availability']['month-northern'].replace("'", "''")
            month_southern = data[key]['availability']['month-southern'].replace("'", "''")
            time = data[key]['availability']['time'].replace("'", "''")
            is_all_day = data[key]['availability']['isAllDay']
            is_all_year = data[key]['availability']['isAllYear']
            price = data[key]['price']
            catch_phrase = data[key]['catch-phrase'].replace("'", "''")
            museum_phrase = data[key]['museum-phrase'].replace("'", "''")
            image_uri = data[key]['image_uri']
            icon_uri = data[key]['icon_uri']

            month_availability_list = data[key]['availability']['month-array-northern']
            hour_availability_list = data[key]['availability']['time-array']

            # insert record into fish table
            cur.execute(f"""
                insert into sea_creature values (
                    {sea_creature_id}, 
                    '{name}', 
                    '{month_northern}', 
                    '{month_southern}', 
                    '{time}', 
                    {is_all_day}, 
                    {is_all_year}, 
                    {price},
                    '{catch_phrase}',
                    '{museum_phrase}',
                    '{image_uri}',
                    '{icon_uri}'
                )
            """)

            # insert records into month availability table
            for month in month_availability_list:
                cur.execute(f"""
                    insert into sea_creature_month_availability values (
                        {sea_creature_id},
                        {month}
                    )
                """)

            # insert records into hour availability table
            for hour in hour_availability_list:
                cur.execute(f"""
                    insert into sea_creature_hour_availability values (
                        {sea_creature_id},
                        {hour}
                    )
                """)

        self.con.commit()
