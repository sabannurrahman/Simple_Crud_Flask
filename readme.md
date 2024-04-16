# Simple Inventory CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) inventory application developed using Flask, Selenium 4.19, and BeautifulSoup 4.

## Introduction

The Simple Inventory CRUD Application is a web-based system designed to manage inventory items. It allows users to perform CRUD operations on items, register new users, perform multi-user login, view a dashboard, and read and delete user accounts.

## Technologies Used

- Flask
- Selenium 4.19
- BeautifulSoup 4
- mysql

## Features

1. **Multi-User Login**

   - Users can register and login with unique credentials.
   - Authentication system ensures secure access to the application.

2. **CRUD Item**

   - Users can perform CRUD operations (Create, Read, Update, Delete) on inventory items.
   - Create: Users can add new items to the inventory.
   - Read: Users can view details of existing items.
   - Update: Users can edit details of existing items.
   - Delete: Users can remove items from the inventory.

3. **User Registration**

   - New users can register for an account by providing required information.
   - Registration process ensures unique usernames and secure passwords.

4. **Read and Delete User**

   - Admin or privileged users can view and delete user accounts.
   - Deleting a user account removes access to the application for that user.

5. **Dashboard**
   - Count total data user and item

## Installation

To run the Simple Inventory CRUD Application, follow these steps:

1. Clone the repository from GitHub.
2. Install Python and required dependencies (`Flask`, `Selenium`, `BeautifulSoup`).
3. Set up the database according to the application's database configuration.
4. Run the Flask application using `python app.py`.
5. Access the application through the provided URL.

## Usage

1. Navigate to the registration page to create a new user account.
2. Log in using your credentials.
3. Access the dashboard to view inventory statistics.
4. Perform CRUD operations on inventory items as needed.
5. Administrators can manage user accounts, including reading and deleting users.

## Contributors

- [Saban Nurrahman] - Web Developer

## Acknowledgements

- Mention any resources, libraries, or tutorials used as inspiration or reference.
