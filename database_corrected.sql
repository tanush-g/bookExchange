-- Corrected Database Schema for Book Exchange Application
-- Drop existing database and recreate
DROP DATABASE IF EXISTS bookexchange;
CREATE DATABASE bookexchange;
USE bookexchange;
-- Create user table first (referenced by others)
CREATE TABLE `user` (
    `user_id` INT NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `user_type` INT NOT NULL,
    `email_id` varchar(255) NOT NULL UNIQUE,
    `contact_num` varchar(20) NOT NULL,
    `location` varchar(100) NOT NULL,
    `password` varchar(255) NOT NULL,
    `coins` INT NOT NULL DEFAULT 0,
    PRIMARY KEY (`user_id`)
);
-- Create genre table (referenced by others)
CREATE TABLE `genre` (
    `genre_name` varchar(30) NOT NULL,
    `book_count` INT NOT NULL DEFAULT 0,
    PRIMARY KEY (`genre_name`)
);
-- Create unique_books table (referenced by others)
CREATE TABLE `unique_books` (
    `unique_id` INT NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `author` varchar(255) NOT NULL,
    `rating` FLOAT NOT NULL DEFAULT 0,
    `review_count` INT NOT NULL DEFAULT 0,
    `recommendation_count` INT NOT NULL DEFAULT 0,
    `book_count` INT NOT NULL DEFAULT 0,
    PRIMARY KEY (`unique_id`),
    CONSTRAINT CHK_RATING CHECK (
        rating >= 0
        AND rating <= 10
    )
);
-- Create all_books table
CREATE TABLE `all_books` (
    `book_id` INT NOT NULL AUTO_INCREMENT,
    `description` varchar(1024) NOT NULL,
    `page_count` INT NOT NULL,
    `transaction_type` INT NOT NULL,
    `unique_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    PRIMARY KEY (`book_id`),
    FOREIGN KEY (`unique_id`) REFERENCES `unique_books`(`unique_id`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
    CONSTRAINT CHK_TRANSACTION_TYPE CHECK (
        transaction_type >= 1
        AND transaction_type <= 3
    )
);
-- Create transaction type specific tables
CREATE TABLE `available_for_borrowing` (
    `book_id` INT NOT NULL,
    `price` INT NOT NULL,
    `num_of_days` INT NOT NULL,
    PRIMARY KEY (`book_id`),
    FOREIGN KEY (`book_id`) REFERENCES `all_books`(`book_id`) ON DELETE CASCADE,
    CONSTRAINT CHK_BORROW_PRICE CHECK (price >= 0)
);
CREATE TABLE `available_for_buying` (
    `book_id` INT NOT NULL,
    `price` INT NOT NULL,
    PRIMARY KEY (`book_id`),
    FOREIGN KEY (`book_id`) REFERENCES `all_books`(`book_id`) ON DELETE CASCADE,
    CONSTRAINT CHK_BUY_PRICE CHECK (price >= 0)
);
CREATE TABLE `available_for_exchange` (
    `book_id` INT NOT NULL,
    `exchange_with` varchar(255) NOT NULL,
    PRIMARY KEY (`book_id`),
    FOREIGN KEY (`book_id`) REFERENCES `all_books`(`book_id`) ON DELETE CASCADE
);
-- Create review table
CREATE TABLE `review` (
    `title` varchar(255) NOT NULL,
    `user_id` INT NOT NULL,
    `body` varchar(1024) NOT NULL,
    `unique_id` INT NOT NULL,
    PRIMARY KEY (`user_id`, `unique_id`),
    FOREIGN KEY (`unique_id`) REFERENCES `unique_books`(`unique_id`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`)
);
-- Create book_genre_relation table
CREATE TABLE `book_genre_relation` (
    `unique_id` INT NOT NULL,
    `genre_name` varchar(30) NOT NULL,
    PRIMARY KEY (`unique_id`, `genre_name`),
    FOREIGN KEY (`unique_id`) REFERENCES `unique_books`(`unique_id`),
    FOREIGN KEY (`genre_name`) REFERENCES `genre`(`genre_name`)
);
-- Create preferences table
CREATE TABLE `preferences` (
    `user_id` INT NOT NULL,
    `genre_name` varchar(30) NOT NULL,
    `user_type` INT NOT NULL,
    PRIMARY KEY (`user_id`, `genre_name`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
    FOREIGN KEY (`genre_name`) REFERENCES `genre`(`genre_name`)
);
-- Create recommendations table
CREATE TABLE `recommendations` (
    `user_id` INT NOT NULL,
    `unique_id` INT NOT NULL,
    PRIMARY KEY (`unique_id`, `user_id`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
    FOREIGN KEY (`unique_id`) REFERENCES `unique_books`(`unique_id`)
);
-- Create archive table
CREATE TABLE `archive` (
    `archive_id` INT NOT NULL AUTO_INCREMENT,
    `unique_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    `transaction_type` INT NOT NULL,
    PRIMARY KEY (`archive_id`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
    FOREIGN KEY (`unique_id`) REFERENCES `unique_books`(`unique_id`)
);

-- Insert some sample data for testing
INSERT INTO `genre` (`genre_name`, `book_count`)
VALUES ('fiction', 0),
    ('non-fiction', 0),
    ('science', 0),
    ('technology', 0),
    ('biography', 0),
    ('mystery', 0),
    ('romance', 0),
    ('thriller', 0),
    ('fantasy', 0),
    ('history', 0),
    ('horror', 0),
    ('action', 0),
    ('physics', 0),
    ('comic', 0);
-- Insert sample users
INSERT INTO `user` (
        `name`,
        `user_type`,
        `email_id`,
        `contact_num`,
        `location`,
        `password`,
        `coins`
    )
VALUES (
        'John Doe',
        1,
        'john@example.com',
        '1234567890',
        'New York',
        'password123',
        100
    ),
    (
        'Jane Smith',
        2,
        'jane@example.com',
        '0987654321',
        'California',
        'password456',
        150
    ),
    (
        'Dr. Brown',
        3,
        'brown@university.edu',
        '5555555555',
        'Boston',
        'professor123',
        200
    );
-- Insert sample books
INSERT INTO `unique_books` (
        `name`,
        `author`,
        `rating`,
        `review_count`,
        `recommendation_count`,
        `book_count`
    )
VALUES (
        'The Great Gatsby',
        'F. Scott Fitzgerald',
        4.5,
        3,
        1,
        2
    ),
    (
        'To Kill a Mockingbird',
        'Harper Lee',
        4.8,
        5,
        2,
        1
    ),
    (
        '1984',
        'George Orwell',
        4.6,
        4,
        1,
        3
    );

-- Insert sample book instances
INSERT INTO `all_books` (
        `description`,
        `page_count`,
        `transaction_type`,
        `unique_id`,
        `user_id`
    )
VALUES (
        'Classic American literature in good condition',
        180,
        1,
        1,
        1
    ),
    (
        'Well-preserved copy of this timeless novel',
        376,
        2,
        2,
        2
    ),
    (
        'Dystopian masterpiece, slight wear on cover',
        328,
        3,
        3,
        3
    );
-- Insert corresponding transaction type records
INSERT INTO `available_for_borrowing` (`book_id`, `price`, `num_of_days`)
VALUES (1, 5, 14);
INSERT INTO `available_for_buying` (`book_id`, `price`)
VALUES (2, 15);
INSERT INTO `available_for_exchange` (`book_id`, `exchange_with`)
VALUES (
        3,
        'Looking for another classic novel or sci-fi book'
    );
-- Insert book-genre relations
INSERT INTO `book_genre_relation` (`unique_id`, `genre_name`)
VALUES (1, 'fiction'),
    (2, 'fiction'),
    (3, 'fiction'),
    (3, 'science');
-- Insert sample reviews (note: field order is title, user_id, body, unique_id as expected by app)
INSERT INTO `review` (`title`, `user_id`, `body`, `unique_id`)
VALUES (
        'Amazing Classic',
        2,
        'This book is a true masterpiece of American literature. Highly recommended!',
        1
    ),
    (
        'Thought Provoking',
        3,
        'A powerful story that stays with you long after reading. Essential reading.',
        2
    ),
    (
        'Dystopian Warning',
        1,
        'Orwells vision feels more relevant than ever. A must-read for everyone.',
        3
    );
-- Insert sample preferences
INSERT INTO `preferences` (`user_id`, `genre_name`, `user_type`)
VALUES (1, 'fiction', 1),
    (1, 'science', 1),
    (2, 'fiction', 2),
    (2, 'history', 2),
    (3, 'non-fiction', 3),
    (3, 'science', 3);
-- Insert sample recommendations  
INSERT INTO `recommendations` (`user_id`, `unique_id`)
VALUES (1, 2),
    (2, 1),
    (3, 3);
-- Create useful indexes for better performance
CREATE INDEX idx_all_books_unique ON all_books(unique_id);
CREATE INDEX idx_all_books_user ON all_books(user_id);
CREATE INDEX idx_all_books_transaction ON all_books(transaction_type);
CREATE INDEX idx_unique_books_name ON unique_books(name);
CREATE INDEX idx_unique_books_author ON unique_books(author);
CREATE INDEX idx_unique_books_rating ON unique_books(rating);
CREATE INDEX idx_user_email ON user(email_id);
CREATE INDEX idx_user_location ON user(location);
CREATE INDEX idx_book_genre_genre ON book_genre_relation(genre_name);
CREATE INDEX idx_review_unique ON review(unique_id);
CREATE INDEX idx_available_borrow_price ON available_for_borrowing(price);
CREATE INDEX idx_available_buy_price ON available_for_buying(price);