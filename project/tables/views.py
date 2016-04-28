from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
# from django.db.models import Q

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

import json
import pprint


from .forms import UserForm, LoginForm, SearchForm
from .models import Neighborhood, Ages, Economic, SchoolEducation, Building, Demographic, UnitValue, UnitDescription


class Index(View):
    def get(self, request):
        context = {}
        # check to see if someone is already logged in
        if request.user.is_authenticated(): 
            # get their username  
            username = request.user.username
            context = {
                'username': username,
            }
        user_form = UserForm()
        login_form = AuthenticationForm()
        context ["user_form"] = user_form
        context ["login_form"] = login_form
        return render(request, "index.html", context)


class Register(View):
    def post(self, request):
        body = request.body.decode()
        if not body: 
            return JsonResponse ({"response":"Missing Body"})
        data = json.loads(body)

        user_form = UserForm(data)
        if user_form.is_valid():
            user = user_form.save()
            return JsonResponse({"Message": "Register succesfull", "success": True})
        else:
            return JsonResponse ({"response":"Invalid information", 'success' : False, 'errors': user_form.errors })


class Login(View):
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session.set_expiry(30000)
            return JsonResponse({"username":username, "success": True})
        else:
            return JsonResponse({'errors': form.errors})


class Logout(View):
    def post(self, request):
        print(request)
        logout(request) # django built in logout 
        return JsonResponse ({"Message":"Logout Successful"})


class Search(View):
    def post(self,request):
        print(request.POST)
        form = SearchForm(request.POST)
        form.is_valid()
        print(form.errors)
        pprint.pprint(form.cleaned_data)
        results = form.cleaned_data
        # return results
        return JsonResponse({"success": True})

        # if form.is_valid():
        #   # form.execute_queries()
        #   Algorithm(form)

class Results(View):
    def post(self,request):
        pass










