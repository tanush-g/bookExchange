#!/usr/bin/env python3
"""
Test script to verify MySQL connection and database setup
"""
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    # Get configuration from environment variables
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'bookexchange')
    
    print("✅ Environment variables loaded successfully")
    print(f"   Host: {MYSQL_HOST}")
    print(f"   User: {MYSQL_USER}")
    print(f"   Database: {MYSQL_DB}")
    print(f"   Password set: {'Yes' if MYSQL_PASSWORD else 'No - PLEASE SET YOUR MYSQL PASSWORD'}")
except Exception as e:
    print(f"❌ Error loading environment variables: {e}")
    sys.exit(1)

if not MYSQL_PASSWORD:
    print("\n🚨 IMPORTANT: Please set your MySQL password in the .env file before running the app!")
    print("   Update the MYSQL_PASSWORD variable in the .env file with your MySQL root password.")
    sys.exit(1)

try:
    from flask import Flask
    from flask_mysqldb import MySQL
    
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = MYSQL_HOST
    app.config['MYSQL_USER'] = MYSQL_USER
    app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
    app.config['MYSQL_DB'] = MYSQL_DB
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    
    mysql = MySQL(app)
    
    with app.app_context():
        cur = mysql.connection.cursor()
        
        # Test user table
        cur.execute("SELECT COUNT(*) as count FROM user")
        user_count = cur.fetchone()['count']
        print(f"✅ Found {user_count} users in database")
        
        # Test unique_books table
        cur.execute("SELECT name, author FROM unique_books LIMIT 3")
        books = cur.fetchall()
        print("✅ Sample books:")
        for book in books:
            print(f" - {book['name']} by {book['author']}")
        
        # Test genres
        cur.execute("SELECT COUNT(*) as count FROM genre")
        genre_count = cur.fetchone()['count']
        print(f"✅ Found {genre_count} genres in database")
        
        cur.close()
        print("\n🎉 All systems ready! Your Flask app should work perfectly.")

except Exception as e:
    print(f"❌ Database connection failed: {e}")
    print("\nPlease check:")
    print("1. MySQL is running")
    print("2. Your password is correct in the .env file")
    print("3. The 'bookexchange' database exists")
    sys.exit(1)
