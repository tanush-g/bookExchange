#!/usr/bin/env python3
"""
Test script to verify MySQL connection and database setup
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import config
    print("✅ Config module imported successfully")
    print(f"   Host: {config.MYSQL_HOST}")
    print(f"   User: {config.MYSQL_USER}")
    print(f"   Database: {config.MYSQL_DB}")
    print(f"   Password set: {'Yes' if config.MYSQL_PASSWORD else 'No - PLEASE SET YOUR MYSQL PASSWORD'}")
except Exception as e:
    print(f"❌ Error importing config: {e}")
    sys.exit(1)

if not config.MYSQL_PASSWORD:
    print("\n🚨 IMPORTANT: Please set your MySQL password in config.py before running the app!")
    print("   Update the MYSQL_PASSWORD variable with your MySQL root password.")
    sys.exit(1)

try:
    from flask import Flask
    from flask_mysqldb import MySQL
    
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = config.MYSQL_HOST
    app.config['MYSQL_USER'] = config.MYSQL_USER
    app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
    app.config['MYSQL_DB'] = config.MYSQL_DB
    app.config['MYSQL_CURSORCLASS'] = config.MYSQL_CURSORCLASS
    
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
    print("2. Your password is correct in config.py")
    print("3. The 'bookexchange' database exists")
    sys.exit(1)
