from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Quiz, Question, Answer, StudentQuizAttempt, Student
from django.contrib.auth.decorators import login_required

def home(request):
    fname = None
    if request.user.is_authenticated:
        # Assuming the user profile has a 'fname' attribute
        fname = request.user.first_name 
    return render(request,"home.html",{'fname': fname})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        # Create a new Student record for the user
        Student.objects.create(user=myuser)

        messages.success(request, "Success! Account Created")
        return redirect('signin')
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"home.html", {'fname':fname})
        else:
            messages.error(request,"Incorrect username or password!")
            return redirect('home')
    return render(request,"signin.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('home')

def quiz_list(request):
    quizzes=None
    if request.user.is_authenticated:
        quizzes = Quiz.objects.all()  # Fetch all quizzes
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# View to display questions for a specific quiz
@login_required
def quiz_detail(request, quiz_id):
    # Fetch the quiz by its ID
    quiz = Quiz.objects.get(id=quiz_id)
    # Fetch a random question for the quiz
    question = Question.objects.order_by('?').first()  # Get a random question
    return render(request, "quiz_detail.html", {'quiz': quiz, 'question': question})

# View to handle quiz submission
@login_required
def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        # Ensure the student exists
        student = get_object_or_404(Student, user=request.user)

        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()
        score = 0

        for question in questions:
            selected_answer_id = request.POST.get(str(question.id))
            if selected_answer_id:
                selected_answer = get_object_or_404(Answer, id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1

        # Update student's total attempted questions and correct answers
        student.total_questions_attempted += questions.count()
        student.correct_answers += score
        student.save()

        # Create a StudentQuizAttempt entry
        StudentQuizAttempt.objects.create(
            student=student,
            quiz=quiz,
            score=score
        )

        return render(request, 'quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total_questions': questions.count()
        })

def quiz_result(request):
    student = request.user.student
    total_questions = student.questions_attempted
    correct_answers = student.correct_answers
    score = round((correct_answers / total_questions) * 100, 2) if total_questions > 0 else 0
    return render(request, 'quiz_results.html', {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'score': score
    })

# View to display student dashboard
def student_dashboard(request):
    student=None
    attempts=None
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        attempts = StudentQuizAttempt.objects.filter(student=student)  # Fetch all quiz attempts
    return render(request, 'dashboard.html', {'student': student, 'attempts': attempts})