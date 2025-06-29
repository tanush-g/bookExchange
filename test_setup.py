#!/usr/bin/env python3
"""
Test script to verify the Flask application setup
"""
import sys
import os

# Add current directory to path to import config
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import config
    print("✅ Config imported successfully")
    print(f"   Database: {config.MYSQL_DB}")
    print(f"   Host: {config.MYSQL_HOST}")
    print(f"   User: {config.MYSQL_USER}")
    
    # Test database connection
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
        print(f"✅ Sample books:")
        for book in books:
            print(f"   - {book['name']} by {book['author']}")
        
        # Test genres
        cur.execute("SELECT COUNT(*) as count FROM genre")
        genre_count = cur.fetchone()['count']
        print(f"✅ Found {genre_count} genres in database")
        
        cur.close()
        print("\n🎉 All systems ready! Your Flask app should work perfectly.")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nPlease check:")
    print("1. MySQL is running")
    print("2. Database 'bookexchange' exists")
    print("3. Your MySQL password is correct in config.py")
    sys.exit(1)
