# Python script to extract data and send it to Node.js

import sqlite3
import requests
import json

# Extract data from SQLite3
# Assume 'accounts', 'followers', and 'posts' are tables in the SQLite database

# Example SQLite3 connection
conn = sqlite3.connect('your_sqlite_database.db')
cursor = conn.cursor()

# Extract accounts
cursor.execute('SELECT * FROM accounts')
accounts_data = cursor.fetchall()

# Extract followers
cursor.execute('SELECT * FROM followers')
followers_data = cursor.fetchall()

# Extract posts
cursor.execute('SELECT * FROM posts')
posts_data = cursor.fetchall()

# Close SQLite connection
conn.close()

# Prepare data for migration
migration_data = {
    'accounts': accounts_data,
    'followers': followers_data,
    'posts': posts_data
}

# Send data to Node.js server
nodejs_url = 'http://your-nodejs-server:port/migrate'
response = requests.post(nodejs_url, json=migration_data)

print(response.text)  # Print the response from Node.js server
