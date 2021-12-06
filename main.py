import sqlite3
from data_collection.collector import Collector

def main():
    con = sqlite3.connect('acnh')
    coll = Collector(con)
    
    # populate DB with fish and bug data
    coll.collect_fish()
    coll.collect_bugs()

    con.close()

if __name__ == '__main__':
    main()
