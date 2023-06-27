from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader

# Create your views here.


class MainView(View):
    def get(self, request):
        template = loader.get_template("board/main.html")
        context = {"token": request.session["user_token"]}

        return HttpResponse(template.render(context, request))
