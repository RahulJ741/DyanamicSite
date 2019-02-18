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
