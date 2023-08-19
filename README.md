# Grocery Management System
The Grocery Management System is a comprehensive solution for efficiently managing and organizing a grocery store's operations. It provides an integrated platform that combines both frontend and backend technologies to streamline various processes related to inventory management, customer interactions, and order tracking. This README file provides an overview of the project, its features, and how to set it up for local development.

# Features
- User-Friendly Interface: The frontend of the system is built using HTML, CSS, JavaScript, and Bootstrap, ensuring an intuitive and responsive user interface for both customers and store administrators.

- Database Integration: The system employs MySQL as the database management system to store and manage crucial data related to products, customers,order tracking and total sales.

- Python Backend: The backend of the system is developed using Python, leveraging the Flask web framework to manage business logic.

- Individual Project: The project was developed by an individual and followed a structured development approach.

# Database Setup
To set up the database for the Grocery Management System, follow these steps:

- Install MySQL:
Make sure you have MySQL installed on your machine. If not, you can download and install it from the official MySQL website: https://dev.mysql.com/downloads/

- Create a Database:
Open your MySQL command line interface or a MySQL client of your choice. Create a new database named grocery_store (or any name you prefer):

  CREATE DATABASE grocery_store;
  
- Create Tables:
The system utilizes four tables: products, uom, orders, and order_details. Here's how you can create these tables:
We can use the MySql UI.
![table01](https://github.com/CharudattaGhute/Grocery-Management-System/assets/122104600/17ac9ff8-9d8b-4779-ad27-f4cb00fdde43)

  Similarly we can create other tables such as uom,oders and order_details which includes column name,Datatype,etc.

# Update Database Configuration:

Open the server.py file in your project and update the database connection configuration. You'll need to provide the host, username, password, and database name that you've set up.

DATABASE_CONFIG = {
    'host': '127.0.0.1',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'grocery_store'
}

# Access the Application:
Open a web browser and navigate to http://localhost:5000 to access the Grocery Management System.

# Contributing

Contributions to the Grocery Management System are welcome! If you find any issues or would like to enhance the system with new features, feel free to fork the repository, make your changes, and submit a pull request.

Please ensure to follow coding standards, write clear commit messages, and provide appropriate documentation for your contributions.

# Project Demo Video
Check out our project demo video to get a visual walkthrough of the Grocery Management System in action. This video provides an overview of the system's features, functionality, and how it can help streamline your grocery store operations.


https://github.com/CharudattaGhute/Grocery-Management-System/assets/122104600/1a549cd9-11f9-4295-9ed2-7e6a784141d2



We hope you find the video informative and insightful. If you have any questions or would like to explore specific aspects of the system further, please don't hesitate to reach out to us.

# Contact

If you have any questions or need assistance, feel free to reach out me at ghutecharudatta@gmail.com. Your feedback and inquiries are highly valued as we strive to enhance the Grocery Management System for a better experience.


