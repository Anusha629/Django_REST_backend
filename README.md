# API Documentation using Django_REST Framework

FRAMEWORK CHOICE
     
Chosen the Django REST framework as the foundation for API project.
Django REST framework is a powerful toolkit for building Web APIs based on the Django framework. 
It provides a flexible, customizable, and efficient way to create APIs, making development faster and more manageable.

DATABASE SCHEME
The schema includes the following fields:

Username: The unique identifier for a user.
Email: The email address associated with the user.
Password: The user's password.
Age: The age of the user.
Gender: The gender of the user.

INSTRUCTIONS TO SETUP & RUN THE CODE

Follow these steps to run  Django REST API project on your local machine
              
Getting Started
1. Create Virtual Environment
      python -m venv myvenv
2. Activate Virtual Environment
      myvenv\Scripts\activate
3. Install Dependencies
      pip install django djangorestframework
4. Create a Requirements File
      pip freeze > requirements.txt
5. Project and App Setup
      django-admin startproject myproject
      cd myproject
      python manage.py startapp myapp
7. Configuration and Settings
   Add the following to myproject/settings.py:
      INSTALLED_APPS = [
    
    'myapp',
    'rest_framework',
    'rest_framework.authtoken',
   ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [ 'rest_framework.authentication.TokenAuthentication',],
    }
7. Create Model
   Define your custom model in myapp/models.py.
       python manage.py makemigrations
       python manage.py migrate
9. Serializers and Views
   Create serializers and views for your API endpoints in myapp/serializers.py and myapp/views.py.
10. URL Routing
  Connect your app's URLs by adding to myproject/urls.py:
       urlpatterns = [path('', include('myapp.urls')),]

  connect api endpoints to myapp/urls.py

11. Run the Development Server
       python manage.py runserver


     API Endpoints
User Registration: POST /api/register/
Generate Token: POST /api/token/
Store Data: POST /api/data/
Retrieve Data: GET /retrieve-data/<int:id>/
Update Data: PUT /update-data/<int:id>/
Delete Data: DELETE /delete-data/<int:id>/


     




    
