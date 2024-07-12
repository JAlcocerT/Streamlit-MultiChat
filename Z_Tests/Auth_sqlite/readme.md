

* https://blog.jcharistech.com/2020/05/30/how-to-add-a-login-section-to-streamlit-blog-app/
* https://www.youtube.com/watch?v=HU_kd-1uIkQ

The data is stored in a file named 'data.db', and it is using SQLite as the database management system.

In the code, the line `conn = sqlite3.connect('data.db')` establishes a connection to an SQLite database file named 'data.db'. If the file doesn't exist, it will be created automatically.

SQLite is a lightweight, file-based relational database management system. It is widely used for local data storage in applications, especially in scenarios where a full-fledged database server is not required. SQLite databases are self-contained, meaning the entire database is stored in a single file on the filesystem.