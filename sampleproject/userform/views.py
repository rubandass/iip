from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .serializers import RequestSerializer
from .models import Request
from datetime import datetime
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    userdata = Request.objects.all()
    return render(request, 'index.html', {'userdata': userdata})


def pagelogout(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    logout(request)
    return render(request, 'userform/logout.html')


def pagelogin(request):
    return redirect('/accounts/login/')


def formvalues(request):
    date_now = datetime.now()
    obj, status = Request.objects.update_or_create(
        user=request.user,
        defaults={'server': request.POST['server'],
                  'location': request.POST['location'], 'contact_person': request.POST['contact_person'], 'contact_number': request.POST['contact_number'], 'date': date_now, 'status': 'Initial contact'})
    return render(request, 'userform/thankyou.html')


def update_status(request):
    date_now = datetime.now()
    data = json.loads(request.body)
    user_object = Request.objects.get(user=data['user'])
    user_object.date = date_now
    user_object.status = data['status']
    user_object.save()
    data_all_users = Request.objects.all().values()
    data_json = list(data_all_users)
    return JsonResponse({'status': 'success', 'data': data_json})


def get_status(request):
    data = Request.objects.filter(user=request.user).values()
    data_json = list(data)
    return JsonResponse({'data': data_json})


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.all()

    def perform_create(self, serializer):
        date_now = datetime.now()
        serializer.save(user=self.request.user, date=date_now)
