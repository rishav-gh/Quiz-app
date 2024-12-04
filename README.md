# Quiz App Project
This is a Quiz Application built with Django, providing features like taking quizzes, viewing quiz results, and managing quiz attempts. It includes user authentication for the quiz.

## Features
User Authentication: Users can sign up, log in, and log out.
Take Quizzes: Users can take quizzes, submit answers, and view their scores.
View Results: After completing a quiz, users can view their score and see the details of previous quiz attempts.
Profile Page: Users can view their total correct answers and attempted questions.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Django
Database: SQLite (by default, can be configured to PostgreSQL, MySQL, etc.)
Authentication: Django's built-in user authentication system
Static Assets: Images and CSS handled by Django's static files system

## Follow these instructions to set up the project locally.

# Prerequisites
Python (3.6 or higher)
pip (Python package installer)
Git (for version control)
Installation
Clone the Repository

## Open a terminal/command prompt and run the following command to clone the repository:
git clone https://github.com/rishav-gh/Quiz-app
- cd quiz-app

## Next install all the dependencies

## Set Up the Database
# Run the following Django command to set up your database:
python manage.py migrate

## Create a Superuser
### To access the Django admin panel, create a superuser:
python manage.py createsuperuser

## Add questions you want for the quiz
Run the Development Server

## Start the Django development server:
python manage.py runserver

## Access the Application:
Open your web browser and visit http://127.0.0.1:8000/ to access the landing page. You can log in, sign up, and start using the app.

Contact
For questions or suggestions, please feel free to open an issue or contact the project maintainer at rishavghatak@gmail.com.

Let me know if you need any additional sections or further customizations for the README!
