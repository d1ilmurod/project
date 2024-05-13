from django.shortcuts import render

# Create your views here.


def index_page_view(request):
    return render(request, 'main/index.html')


def about_page_view(request):
    return render(request,'main/about.html')



def service_page_view(request):
    return render(request,'main/service.html')



def team_page_view(request):
    return render(request,'main/team.html')



def why_page_view(request):
    return render(request,'main/why.html')


