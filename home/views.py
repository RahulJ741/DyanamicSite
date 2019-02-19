from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class HomePage(View):
    """docstring for HomePage."""
    # def __init__(self, arg):
    #     super(HomePage, self).__init__()
    #     self.arg = arg
    def __init__(self):
        self.header = HeaderData.objects.all()

    def get(self, request):
        header = HeaderData.objects.all()
        return render(request,'index.html', {'header_content': header})


class RedirectPage(View):
    """docstring for RedirectPage."""
    # def __init__(self, arg):
    #     super(RedirectPage, self).__init__()
    #     self.arg = arg


    def get(self, request, *args, **kwargs):
        url_path = kwargs['url_path']

        return render(request, 'redirect_page.html', {})
