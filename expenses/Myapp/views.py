from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def dashboard(request):
    return render(request, 'dashboard.html')

def add_expense(request):
    if request.method == "POST":
        # Logic สำหรับบันทึกข้อมูล
        pass
    return render(request, 'add_expense.html')

def about(request):
    return render(request, 'about.html')

