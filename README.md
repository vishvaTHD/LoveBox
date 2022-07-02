-------------------------------------------------------------------------------------------------------------------------------------------------------
Hardware Components: A local server (Or personal computer) with 8GB RAM, 512GB SSD storage, Intel Core i3 Processor.
-------------------------------------------------------------------------------------------------------------------------------------------------------
Software Modules/Frameworks Used:Python microweb framework Flask, CSS framework Bootstrap, JS Library JQuery, Magic Zoom Plus, SQLite Database engine.
--------------------------------------------------------------------------------------------------------------------------------------------------------

Step-by-Step Instructions to Re-Create The Prototype:

---------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Project Directory Set-Up
---------------------------------------------------------------------------------------------------------------------------------------------------------------
*Choose a multi-programming-language supoorted source code editor (VS Code recommended).

*Define a folder (In our case market) to store the codebase for the wesbite.

*Define two subfolders static and templates within the market folder.

*Define an __init__.py file within the market folder to change its form to a Python package.

*Define Python files forms.py (for authentication), models.py (to store database models), routes (to store the main views or URL endpoints of the front-end)

*Exit the market folder and define an app.py Python file within the root project folder to intiate the website on the local server.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Package Installation

*Ensure that you have a working python interpretor installed on your local server. If not vist https://www.python.org/downloads/ and select the desired version

*Use the following command either on your local terminal or the one provided with VS Code to install Flask,
>pip install flask

*Use the following command to install Flask for authentication,
>pip install flask-login

*Use the follwoing command to install SQLite for Flask,
>pip install flask-sqlalchemy

---------------------------------------------------------------------------------------------------------------------------------------------------------------

3. Intializing the Flask Application

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

*Click on the link to get a preview of the application

![initializing the application](LoveBox\Code\market\static\images\instructions\1- Intializing Local Server.png)
