from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import LoginForm
from django.contrib.auth import authenticate , login, logout
# Create your views here.


class Login(View):
    """docstring for Login."""
    def __init__(self):
    #     super(Login, self).__init__()
        self.form = LoginForm

    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        form_data = self.form(request.POST)
        if form_data.is_valid():
            user = authenticate(username = form_data.data['email'], password = form_data.data['password'])
            if user and user.is_active:
                login(request,user)
                response = redirect('')
                return response

        return redirect('login')


class SignUP(View):
    """docstring for SignUP."""
    # def __init__(self):
        # super(SignUP, self).__init__()


    def get(self, request):
        return render(request, 'signup.html', {})

    def post(self, request):
        pass


class ProjectCreation(View):
    """docstring for ProjectCreation."""
    def __init__(self, arg):
        super(ProjectCreation, self).__init__()
        self.arg = arg

    def get(self, request):
        pass

    def post(self, request):
        pass





class HomePage(View):
    """docstring for HomePage."""
    # def __init__(self, arg):
    #     super(HomePage, self).__init__()
    #     self.arg = arg
    def __init__(self):
        self.header = HeaderData.objects.all()

    def get(self, request):
        # header = HeaderData.objects.all()
        return render(request,'index.html', {'header_content': self.header})


class RedirectPage(View):
    """docstring for RedirectPage."""
    # def __init__(self, arg):
    #     super(RedirectPage, self).__init__()
    #     self.arg = arg

    def __init__(self):
        self.header = HeaderData.objects.all()


    def get(self, request, *args, **kwargs):
        url_path = kwargs['url_path']

        return render(request, 'redirect_page.html', {'header_content': self.header})
