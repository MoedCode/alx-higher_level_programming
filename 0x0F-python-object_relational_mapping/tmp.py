+--------+
| name |
+--------+
| Dallas |
| Houston|
| Austin |
+--------+
+----+-----------+
| id | name |
+----+-----------+
| 1 | California |
| 2 | Arizona |
| 3 | Texas |
+----+-----------+
+----+-----------+----------+
| id | state_id | name |
+----+-----------+----------+
| 1 | 1 | San Francisco |
| 2 | 1 | San Jose |
| 3 | 2 | Page |
| 4 | 3 | Dallas |
| 5 | 3 | Houston |
+----+-----------+----------+
# Assuming the State table has the following data:
# | id | name         |
# |----|--------------|
# | 1  | Alabama      |
# | 2  | Alaska       |
# | 3  | Arizona      |
# | 4  | Arkansas     |

# The query statement:
state_list = session.query(State).filter(
    State.name.like('%a%')).order_by(State.id).all()

# 1. session.query(State): Initiates a query for all columns in the State table.
# Output (query object): SELECT * FROM State;

# 2. .filter(State.name.like('%a%')): Adds a filter to include only rows where the 'name' column contains the letter 'a'.
# Output (query object): SELECT * FROM State WHERE State.name LIKE '%a%';

# 3. .order_by(State.id): Orders the results based on the 'id' column in ascending order.
# Output (query object): SELECT * FROM State WHERE State.name LIKE '%a%' ORDER BY State.id;

# 4. .all(): Executes the query and retrieves all rows as a list.
# Output (list of State objects): [{'id': 1, 'name': 'Alabama'}, {'id': 2, 'name': 'Alaska'}, {'id': 3, 'name': 'Arizona'}]

# The final state_list variable contains the list of State objects meeting the specified conditions.
