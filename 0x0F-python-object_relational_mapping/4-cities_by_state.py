#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
 Results must be sorted in ascending order by cities.id
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    # cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    quarry_exe = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id;"
    cursor.execute(quarry_exe)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
