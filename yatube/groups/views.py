from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def group_index(request):
    return HttpResponse('Groups')


def group_posts(request, group_name):
    return HttpResponse(f'Group {group_name}')


