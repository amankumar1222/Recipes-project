# Recipe Project - Full Stack Web Application

Welcome to the Recipe Project! This is a full stack web application built using Python Django, Bootstrap, and CSS. The project allows users to add and search for their favorite recipes. It also provides user authentication features like login, logout, and signup to ensure a personalized experience.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to provide a platform for users to store and share their recipes in a convenient manner. Users can easily add their recipes to the system and search for recipes based on various criteria. The application ensures user privacy and security through the login and logout functionality.

## Features
- User registration and authentication (Signup, Login, Logout)
- Add new recipes to the system
- Search for recipes based on keywords, ingredients, or categories
- User-friendly interface using Bootstrap and CSS

## Technologies Used
The Recipe Project is built using the following technologies:
- Python Django: A powerful web framework for building web applications using Python.
- Bootstrap: A front-end framework for designing responsive and visually appealing web pages.
- CSS: Used to style the web pages and enhance the user interface.

## Setup Instructions
To run this project locally, follow these steps:

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/amankumar1222/Recipes-project.git
   ```

2. Navigate to the project directory.
   ```
   cd recipe-project
   ```

3. Create a virtual environment (optional but recommended).
   ```
   python -m venv venv
   ```

4. Activate the virtual environment (if created).
   - On Windows:
   ```
   venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```
   source venv/bin/activate
   ```

5. Install the required dependencies.
   ```
   pip install -r  requirements.txt
   ```

6. Perform database migrations.
   ```
   python manage.py migrate
   ```

7. Create a superuser to access the Django admin panel (optional).
   ```
   python manage.py createsuperuser
   ```

8. Start the development server.
   ```
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://localhost:8000/`.

## Usage
1. Register a new account on the website by clicking on "Sign Up."
2. Log in using your credentials after successful registration.
3. Once logged in, you can add your recipes using the "Add Recipe" option.
4. To search for recipes, use the search bar and enter keywords, ingredients, or categories related to the recipe you are looking for.
5. Enjoy managing and discovering new recipes!

## Contributing
We welcome contributions to the Recipe Project! If you find any bugs or want to add new features, please open an issue or submit a pull request.


## License
The Recipe Project is open-source software licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.