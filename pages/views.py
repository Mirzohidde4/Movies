from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def HomePage(request):
    user = request.user
    return render(request, 'pages/home.html', {'user': user})


def Admin(request):
    if request.user.is_superuser:
        return render(request, '/admin/')


def UserSetting(request):
    password = request.user.password
    parol = len(str(password)) * '#'
    return render(request, 'pages/user_setting.html', {'parol': parol})


def UpdateName(request): 
    if request.method == 'POST':
        # password = request.POST.get('password')
        users = User.objects.filter(username=request.user)
        for i in users:
            # if i.password == str(password):
            users.update(username=request.POST.get("username"))
            return redirect('user_setting')
            # else:
            #     hato = 'password error'
            #     return render(request, 'pages/update_name.html', {'hato': hato}) 
    return render(request, 'pages/update_name.html')


def UpdatePassword(request):
    return render(request, 'pages/update_pass.html')
