from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

def members(request):
    members = Member.objects.all().values()
    
    return render(request, 'all_members.html', {
        'data': members
    })
    
def details(request, id):
    #id = request.GET.get('id')
    
    member = Member.objects.get(id=id)
    
    return render(request, 'details.html', {
        'member': member
    })
    
def main(request):
  return render(request, 'main.html')


def testing(request):
    # pega todos
    # members = Member.objects.all().values()
    
    # page = apenas as colunas informadas
    #members = Member.objects.values_list('firstname')
    
    # pega somente os registros de acordo com o filtro
    # mais sobre filter https://www.w3schools.com/django/django_queryset_filter.php
    members = Member.objects.filter(firstname='Tobias').values()
    
    print(members)
    return render(request, 'template.html', {
        "members": members
    })
