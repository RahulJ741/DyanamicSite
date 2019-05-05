from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import LoginForm
from django.contrib.auth import authenticate , login, logout
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from dynamic_site.forms import ProjectForm
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
                response = redirect('project_list')
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




class ProjectList(ListView):
    context_object_name = 'project_list'
    model = Project
    # page_kwarg = 'page'
    # paginate_by =
    template_name = 'project_list.html'

    def get_queryset(self):
        return Project.objects.filter(user = self.request.user)

    def get_context_data(self, **kwargs):
        # kwargs['test'] = "this is test text just to see if this is rendered in template"
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['new_text'] = "this is test text just to see if this is rendered in template"
        return context




class ProjectDetails(DetailView):
    model = Project
    context_object_name = 'project'
    http_method_names = ['get']
    # slug_field = 'SLUG_FIELD'
    # slug_url_kwarg = 'SLUG_URL_KWARG'
    # success_url = 'SUCCESS_URL'
    template_name = 'project_details.html'

    def http_method_not_allowed(self, *arg, **kwargs):
        super(ProjectDetails, self).http_method_not_allowed(*arg, **kwargs)
        return HttpResponse('Only get method is allowed')




class ProjectCreation(CreateView):
    model = Project
    form_class = ProjectForm
    # success_url = 'SUCCESS_URL'
    template_name = 'create_project.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectCreation, self).get_context_data(**kwargs)
        context['templates'] = TemplateList.objects.all()
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        return HttpResponse('asdfasdfadf')




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
