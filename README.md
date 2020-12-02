# CRM-Website 
CRM website built with django <br>
Project for the Django Crash Course taught by Dennis Ivy. <br>
(https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)

# Tech & Tools:
1. Backend: Django 3.1.3
2. Frontend: Bootstrap 4.3.1 
3. Database: SQLite

# To use:
1. git clone this repository to your computer
2. `python3 -m venv venv`
3. `. venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. run http://localhost:8000/

# Functions:
- Login:
  - Redirect to login page if you're not logged in
  - Signup link and password reset link 
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/login.png)
- Sign up:
  - Use `python manage.py createsuperuser` to create superuser/admin user
  - Create customer user with the website
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/signup.png)
- Customer User:
  - You can see all your orders (product, note, date and status) after logging in
  - Logout your account from the top right 
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/customer1.png)
  - Settings to change your personal information (Name, Phone, Email and Photo)
  - With default image
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/customer2.png)
- Admin User (Superuser)
  - Access to a dashboard after loggin in
  - Show orders statistics, customers and the last 5 orders
  - (todo) Create Customer 
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/admin_dashboard.png)
  - View a certain customer
  - Update Customer (todo), Place Orders, Search, Update and Delete orders
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/admin_view_customer.png)
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/admin_order_related.png)
  - Access to all the products 
  ![image](https://github.com/dlin99/CRM-Website/blob/main/demo/admin_products.png)


