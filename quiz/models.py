from django.db import models
from django.contrib.auth.models import User

# Student model to store information about each student
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    full_name = models.CharField(max_length=100)
    enrolled_date = models.DateField(auto_now_add=True)  # Automatically set when the student is created
    score = models.IntegerField(default=0)  # To track the student's total score
    total_questions_attempted = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)  # Added this field to track correct answers

    def __str__(self):
        return self.user.username

# Quiz model to represent a quiz
class Quiz(models.Model):
    title = models.CharField(max_length=200)  # Title of the quiz
    description = models.TextField(blank=True, null=True)  # Optional description of the quiz
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the quiz is created

    def __str__(self):
        return self.title

# Question model to represent questions in a quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')  # Link to a quiz
    question_text = models.TextField()  # The text of the question
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the question is created

    def __str__(self):
        return self.question_text

# Answer model to represent answers to a question
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # Link to a question
    answer_text = models.CharField(max_length=200)  # The text of the answer
    is_correct = models.BooleanField(default=False)  # True if this is the correct answer

    def __str__(self):
        return self.answer_text

# Model to track a student's quiz attempts
class StudentQuizAttempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # The student who attempted the quiz
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)  # The quiz that was attempted
    score = models.IntegerField()  # Score obtained in the quiz
    completed_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the quiz is completed

    def __str__(self):
        return f"{self.student.user.username} - {self.quiz.title}"
