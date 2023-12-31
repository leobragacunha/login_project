from django.shortcuts import render
from django.contrib.auth.views import LoginView


# Create your views here.
def indexview(request):
    return render(request, "index.html")


class SiteLogin(LoginView):
    template_name = "login_app/login.html"
    next_page = "login_app/login_index.html"