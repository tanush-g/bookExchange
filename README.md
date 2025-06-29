# BookExchange - Secure Book Exchange Platform

A Flask-based web application for exchanging, lending, and selling books between users. This application has been thoroughly secured with industry-standard security practices.

## 🔒 Security Features

- **Password Hashing**: Secure password storage with salt-based hashing
- **SQL Injection Protection**: All queries use parameterized statements
- **Input Validation**: Comprehensive validation and sanitization
- **Session Security**: Secure session configuration with timeouts
- **Security Headers**: Complete security header implementation
- **HTTPS Ready**: Production-ready with SSL/TLS support

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- MySQL 5.7+
- pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd bookExchange
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment**:

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Configure database**:

   ```bash
   mysql -u root -p < database_corrected.sql
   ```

5. **Run the application**:

   ```bash
   python app.py
   ```

## 📋 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
FLASK_ENV=development
SECRET_KEY=your-super-secret-key-here
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your-mysql-password
MYSQL_DB=bookexchange
```

### Database Configuration

Update your `.env` file with your MySQL settings:

```python
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your-password'
MYSQL_DB = 'bookexchange'
MYSQL_CURSORCLASS = 'DictCursor'
```

## 📁 Project Structure

```text
bookExchange/
├── app.py                 # Main Flask application
├── .env                   # Environment configuration
├── requirements.txt       # Python dependencies
├── requirements.txt       # Python dependencies
├── migrate_passwords.py   # Password migration script
├── database_corrected.sql # Database schema
├── SECURITY_REVIEW.md     # Security documentation
├── static/                # CSS, JS, images
│   ├── css/
│   ├── add-book.js
│   └── ...
├── templates/             # HTML templates
│   ├── login.html
│   ├── create_account.html
│   └── ...
└── figure.py             # Analytics visualization
```

## 🎯 Features

### User Management

- Secure user registration with password validation
- Encrypted password storage
- Session management with timeouts
- User type classification (student, professor, etc.)

### Book Management

- Add books with detailed information
- Search books by name, author, genre
- Categorize by transaction type (lend, sell, exchange)
- Book recommendations and reviews

### Analytics

- Book distribution visualization
- Genre preference analytics
- Transaction type statistics

### Security Features

- SQL injection prevention
- XSS protection
- CSRF protection
- Secure headers
- Input sanitization

## 🔧 Development

### Running in Development Mode

```bash
FLASK_ENV=development python app.py
```

### Running Tests

```bash
python test_setup.py
```

## 🚀 Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment Setup

1. Set `FLASK_ENV=production`
2. Use a secure `SECRET_KEY`
3. Configure HTTPS with reverse proxy (nginx)
4. Set up SSL certificates
5. Configure firewall rules

### Nginx Configuration Example

```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 📊 Database Schema

The application uses the following main tables:

- `user` - User accounts and profiles
- `unique_books` - Book catalog
- `all_books` - Individual book instances
- `review` - Book reviews and ratings
- `preferences` - User genre preferences
- `archive` - Transaction history

## 🔍 API Endpoints

### Authentication

- `GET /login` - Login page
- `POST /checkuser` - Login processing
- `GET /createaccount` - Registration page
- `POST /signup` - Registration processing

### Books

- `GET /search` - Book search
- `GET /book/<id>` - Book details
- `POST /addbook` - Add new book
- `GET /mybooks` - User's books

### Analytics

- `GET /analytics` - Analytics dashboard
- `GET /plot.png` - Chart generation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:

1. Check the `SECURITY_REVIEW.md` for security-related issues
2. Review the database schema in `database_corrected.sql`
3. Run `python test_setup.py` to verify .env configuration

## 🔄 Changelog

### v2.0.0 - Security Update

- ✅ Implemented password hashing
- ✅ Fixed SQL injection vulnerabilities
- ✅ Added input validation and sanitization
- ✅ Enhanced session security
- ✅ Added security headers
- ✅ Production-ready configuration

### v1.0.0 - Initial Release

- Basic book exchange functionality
- User management
- Search and analytics features
