-------------------------------------------------------------------------------------------------------------------------------------------------------
Hardware Components: A local server (Or personal computer) with 8GB RAM, 512GB SSD storage, Intel Core i3 Processor.
-------------------------------------------------------------------------------------------------------------------------------------------------------
Software Modules/Frameworks Used:Python microweb framework Flask, CSS framework Bootstrap, JS Library JQuery, Magic Zoom Plus, SQLite Database engine.
--------------------------------------------------------------------------------------------------------------------------------------------------------




STEP-BY-STEP INSTRUCTIONS TO RE-CREATE THE PROTOTYPE:

--------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Project Directory Set-Up
---------------------------------------------------------------------------------------------------------------------------------------------------------------
*Choose a multi-programming-language supoorted source code editor (VS Code recommended).

*Define a folder (In our case market) to store the codebase for the wesbite.

*Define two subfolders static and templates within the market folder.

*Define an __init__.py file within the market folder to change its form to a Python package.

*Define Python files forms.py (for authentication), models.py (to store database models), routes (to store the main views or URL endpoints of the front-end)

*Exit the market folder and define an app.py Python file within the root project folder to intiate the website on the local server.

![Image](https://user-images.githubusercontent.com/102164507/177009387-c1d5757a-294d-4071-9894-083909e886fc.PNG)


---------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Package Installation
---------------------------------------------------------------------------------------------------------------------------------------------------------------
*Ensure that you have a working python interpretor installed on your local server. If not vist https://www.python.org/downloads/ and select the desired version

*Use the following command either on your local terminal or the one provided with VS Code to install Flask,
>pip install flask

*Use the following command to install Flask for authentication,
>pip install flask-login

*Use the follwoing command to install SQLite for Flask,
>pip install flask-sqlalchemy

---------------------------------------------------------------------------------------------------------------------------------------------------------------
3. Intializing the Flask Application
---------------------------------------------------------------------------------------------------------------------------------------------------------------
*Open the __init__.py file and import flask,
>from flask import Flask

*Intialize the application,
>app = Flask(__name__)

*Set-up a config variable to encrypt cookies and session data related to the application
>app.config['SECRET_KEY'] = 'c4bf4de01682284bd683366b' 

(!IMPORTANT: DO NOT DISCLOSE THE SECRET KEY IN A PRODUCATION SETTING AND USE ANOTHER KEY AS THE ONE MENTIONED ABOVE)

*Open the app.py file and import the app,
>from market import app

*Add the follwing code to kick start the local web server,

>if __name__ == "__main__":
>    app.run(debug=True, threaded=True)

*Click on the link to get a preview of the application,

![Image](https://user-images.githubusercontent.com/102164507/177009301-22d02cf2-1792-4f59-b695-7f13ae83e5ff.PNG)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

4. Adding Static And Template Files

--------------------------------------------------------------------------------------------------------------------------------------------------------------

*Use the Static folder for all CSS, JavaScript and image files

*Use the template folder for all the HTML files

*Add the code base for all HTML templates. 

*Create two seperate CSS files, one for styling (styles.css) and for Bootstrap (bootstrap.css)

*Link the style and Bootstrap files with the HTML by using the <link/> tag in the <head> section

*Add links to the JavaScript files on the bootom of each HTML file using the <script> tag

![Image](https://user-images.githubusercontent.com/102164507/177031227-6e8879de-90a9-4064-bd39-ff2abd5cef4d.PNG)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

5. Route Definition

--------------------------------------------------------------------------------------------------------------------------------------------------------------

*Routes include all the various pages that a user potentially visit

*Go to the routes.py file

*Use the annotaion @app.route('/[URL OF ENDPOINT]') and define a function under the annotation. Pass the render_tempate function to read html files.

>@@app.route('/[URL OF ENDPOINT]') 
>def NAME_OF_THE_FUNCTION():
>    return render_tempate('[HTML FILE NAME]')  

![Image](https://user-images.githubusercontent.com/102164507/177010920-ee8d0857-c605-4076-ba1e-6e497a73eaf1.PNG
)

*Move back to the __init__.py file and import the defined routes

>from market import routes

--------------------------------------------------------------------------------------------------------------------------------------------------------------

6. Database Set-Up

--------------------------------------------------------------------------------------------------------------------------------------------------------------

*Move to the __init__.py and import sqlalchemy from Flask

>from flask_sqlalchemy import SQLAlchemy 

*Now move back to the models.py file and import the database object from the market file

>from market import db

*Now import the custom UserMixin class with the properties for user login

>from flask_login import UserMixin

*Create a class that inherits both the database object and usermixin for different object (This is for the users)

>class Users(db.Model,UserMixin):
>   User_id = db.Column(db.Integer, primary_key=True)
>   User_name = db.Column(db.String(30), unique=True, nullable=False)
>   User_Email = db.Column(db.String(40), nullable=False)
>   User_pass = db.Column(db.String(40), nullable=False)
>   User_cart = db.relationship('Cart', backref='users', lazy = True)
>   User_Orders = db.relationship('Orders', backref='users',lazy = True)

*Now do the same for products, carts, cart items, orders, order details and payment

!IMPOTRANT: THE USERMIXIN INHERITENCE IS ONLY FOR THE USER OBJECT

