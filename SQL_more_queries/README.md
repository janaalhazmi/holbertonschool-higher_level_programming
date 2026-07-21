# SQL - More Queries

This project is part of the Holberton School Higher Level Programming curriculum.

## Description

This project focuses on advanced MySQL queries and database management. It covers user management, privileges, table constraints, relationships between tables, and querying data using different types of JOIN operations.

## Learning Objectives

At the end of this project, I am able to explain:

- How to create and manage MySQL users.
- How to grant and revoke privileges.
- How to use table constraints.
- The purpose of PRIMARY KEY and FOREIGN KEY.
- The difference between UNIQUE and NOT NULL constraints.
- How to create tables with relationships.
- How to retrieve data using INNER JOIN and LEFT JOIN.
- How to filter and sort query results.
- How to aggregate data using COUNT and GROUP BY.

## Requirements

- Ubuntu 24.04 LTS
- MySQL 8.0
- SQL scripts executable on MySQL server
- All SQL keywords written in uppercase
- Each file starts with a comment describing its purpose

## Files

| File | Description |
|------|-------------|
| 0-privileges.sql | Lists the privileges of MySQL users. |
| 1-create_user.sql | Creates the user `user_0d_1`. |
| 2-create_read_user.sql | Creates a read-only user with SELECT privileges. |
| 3-force_name.sql | Creates a table where the name column cannot be NULL. |
| 4-never_empty.sql | Creates a table with an ID column that cannot be NULL. |
| 5-unique_id.sql | Creates a table with a unique ID column. |
| 6-states.sql | Creates the `states` table. |
| 7-cities.sql | Creates the `cities` table with a foreign key. |
| 8-cities_of_california_subquery.sql | Lists all cities in California. |
| 9-cities_by_state_join.sql | Lists cities with their states using JOIN. |
| 10-genre_id_by_show.sql | Lists all shows with their genre IDs. |
| 11-genre_id_all_shows.sql | Lists all shows and their genre IDs. |
| 12-no_genre.sql | Lists shows without a genre. |
| 13-count_shows_by_genre.sql | Counts the number of shows for each genre. |
| 14-my_genres.sql | Lists all genres of the show Dexter. |
| 15-comedy_only.sql | Lists only comedy shows. |
| 16-shows_by_genre.sql | Lists all shows with their genres. |

## Concepts

- MySQL
- Users
- Privileges
- Constraints
- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- INNER JOIN
- LEFT JOIN
- Subqueries
- GROUP BY
- ORDER BY
- Aggregate Functions

## Author

**Jana Alhazmi**
