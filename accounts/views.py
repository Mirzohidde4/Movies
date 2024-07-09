from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .form import CaptchaTestForm
import time
from django.core.paginator import Paginator


# Create your views here.
def Captcha(request):
    if request.method=="POST":
        form=CaptchaTestForm(request.POST)
        if form.is_valid():
            print("Captcha validation success")
            return redirect('home')
        else:
            print("Captcha validation failed")
    form=CaptchaTestForm()
    return render(request, "accounts/captcha.html", {"form": form})

    
def SignPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                name = 'username exists!'
                return render(request, 'accounts/sign.html', {'name': name})
            if User.objects.filter(email=email).exists():
                pochta = 'email address exists!'
                return render(request, 'accounts/sign.html', {'pochta': pochta})
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            hato = 'passwords didn\'t match!'
            return render(request, 'accounts/sign.html', {'hato': hato})
    return render(request, 'accounts/sign.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            hato = 'username or password error!'
            return render(request, 'accounts/login.html', {'hato': hato})
    return render(request, 'accounts/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('home')


# def EmailSend(email, username, code):
#     import smtplib
#     from email.mime.multipart import MIMEMultipart
#     from email.mime.text import MIMEText

#     from_email = "mmaqsad004@gmail.com"
#     from_password = "spfd vubt yvgs odoj"
#     to_email = f"{email}"

#     msg = MIMEMultipart("alternative")
#     msg["Subject"] = "Parolni tiklash"
#     msg['From'] = 'Onlayn Kutubxona'
#     msg["To"] = to_email
#     user = f"{username}"

#     html = f"""\
#         <div style="color: black !important;">
#             <h2>Salom {user}</h2>
#             <p>Siz saytda parolingizni tiklash uchun so'rov yubordingiz, parolni tiklash uchun pastdagi tugma orqali saytda kiring.</p>
#             <a href="http://127.0.0.1:8000/resetpassword/{code}" target="_blank" style="display: inline-block; width: 150px; height: 50px; background-color: aqua; text-align: center; line-height: 50px; text-decoration: none; color: black; font-size: 35px">Kirish</a>
#         </div>
#     """

#     part2 = MIMEText(html, "html")

#     msg.attach(part2)

#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587

#     try:
#         s = smtplib.SMTP(smtp_server, smtp_port)
#         s.starttls()
#         s.login(from_email, from_password)
#         s.sendmail(from_email, to_email, msg.as_string())
#         return True
#     except Exception as e:
#         print(e)
#         return False


# def PasswordResetPage(request):
#     all = Category.objects.all()

#     paginator3 = Paginator(all, 3)
#     page_number3 = 1
#     page_obj3 = paginator3.get_page(page_number3)
#     if request.user.is_authenticated == False:
#         if request.method == "POST":
#             em = request.POST.get("email")
#             email = User.objects.filter(email=em)
#             s = uniqid()
#             if email.exists() == True:
#                 for i in email:
#                     try:
#                         EmailSend(i.email, i.username, s)
#                         ResetPassword.objects.create(user=i, code=s)
#                         break
#                     except Exception as e:
#                         print(e)
#                         return render(
#                             request,
#                             "reset-password.html",
#                             {
#                                 "color": "red",
#                                 "sign": "true",
#                                 "text": "Emailga xabar yuborishda xatolik yuz berdi, iltimos keyinroq urinib ko'ring.",
#                                 "category": page_obj3 if page_obj3.exists() else False,
#                             },
#                         )
#                 return render(
#                     request,
#                     "reset-password.html",
#                     {
#                         "color": "red",
#                         "sign": "true",
#                         "text": "Parolni tiklash uchun xabar elektron pochtangizga yuborildi.",
#                         "page_obj3": page_obj3,
#                     },
#                 )
#             else:
#                 return render(
#                     request,
#                     "reset-password.html",
#                     {
#                         "color": "red",
#                         "sign": "true",
#                         "text": "Siz kiritga email orqali xech kim ro'yhatdan o'tmagan.",
#                         "page_obj3": page_obj3,
#                     },
#                 )

#         else:
#             return render(
#                 request,
#                 "reset-password.html",
#                 {
#                     "color": "black",
#                     "sign": "true",
#                     "text": "Parolingizni tiklash uchun elektron pochta manzilingizni kiriting.",
#                     "page_obj3": page_obj3,
#                 },
#             )
            
#     else:
#         return redirect("home")
        
# def ResetPasswordConfirmPage(request, code):
#     all = Category.objects.all()
#     paginator3 = Paginator(all, 3)
#     page_number3 = 1
#     page_obj3 = paginator3.get_page(page_number3)
    
#     x = ResetPassword.objects.filter(code=code)
#     if request.method == "POST":
#         p1 = request.POST.get("p1")
#         p2 = request.POST.get("p2")
#         if p1 == p2:
#             user = User.objects.get(username=x[0].user.username)
#             user.set_password(p2)
#             user.save()
#             userc = User.objects.get(email=x[0].user.email)
#             ResetPassword.objects.filter(user=userc).delete()
#             return redirect("home")
#         else:
#             return render(
#                     request,
#                     "reset-password-confirm.html",
#                     {
#                         "color": "red",
#                         "sign": "true",
#                         "text": f"Parollar bir biriga mos emas.",
#                         "page_obj3": page_obj3,
#                     },
#                 )
#     else:
#         if x.exists() == True:
#             for i in x:
#                 return render(
#                     request,
#                     "reset-password-confirm.html",
#                     {
#                         "color": "black",
#                         "sign": "true",
#                         "text": f"User: {i.user.username}. Yangi parolni kiriting.",
#                         "page_obj3": page_obj3,
#                     },
#                 )
#         else:
#             return redirect("home")


# def uniqid(prefix="", more_entropy=False):
#     m_time = time.time()
#     base = "%8x%05x" % (int(m_time), int((m_time - int(m_time)) * 10000000))

#     if more_entropy:
#         import random

#         base += "%.8f" % random.random()

#     return prefix + base
