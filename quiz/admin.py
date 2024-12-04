from django.contrib import admin
from .models import Student, Quiz, Question, Answer, StudentQuizAttempt

# Inline model to display answers within questions
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Number of blank answer fields to display by default

# Admin class for the Question model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz')  # Fields to display in the admin list view
    inlines = [AnswerInline]

# Admin class for the Quiz model
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Fields to display in the admin list view

# Admin class for the Student model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'enrolled_date', 'score')

# Admin class for StudentQuizAttempt model
class StudentQuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'completed_at')

# Register models with their respective admin classes
admin.site.register(Student, StudentAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(StudentQuizAttempt, StudentQuizAttemptAdmin)
