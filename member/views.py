from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic import FormView
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from board.views import MainView
from member import models

from member.models import IdDefaultInfo, UserInfo


# Create your views here.
class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("member/login.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template("board/main.html")
        user_id = request.POST["user_id"]
        user_passwd = request.POST["user_passwd"]
        dto = models.IdDefaultInfo.objects.get(user_id=user_id)
        if user_passwd == dto.user_passwd:
            request.session["user_token"] = user_id
            return redirect("/board/main")
            # token = request.session["user_token"]
            # context = {"token": token}
            # return HttpResponse(template.render(context, request))


class RegistView(FormView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("member/regist_form.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template("member/login.html")

        dto = IdDefaultInfo(
            user_id=request.POST["user_id"],
            user_passwd=request.POST["user_passwd"],
            user_email=request.POST["user_email"],
        )
        dto.save()
        dto = UserInfo(
            user_favorite=request.POST["user_favorite"],
        )
        dto.save()
        context = {}
        return redirect("login")
