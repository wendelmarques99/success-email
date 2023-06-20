from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage 
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        data = {"user": email}
        template = render_to_string("email.html", data)

        email = EmailMessage(
        "Login - portal", 
        template, 
        settings.EMAIL_HOST_USER,
        ['toemailuser']
        )
        email.send()
        return render(request, "habilitado.html", data)