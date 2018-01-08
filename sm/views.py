from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import ObjectDoesNotExist
from rest_framework import viewsets
from .serializers import ProcesadosSerializer, TendenciasSerializer
from .models import Procesados, Tendencias, Usuario
import hashlib


class IndexView(View):
    template_name = 'sm/pages/index.html'

    def get(self, request):
        context = {}
        context['num_procesados_es_count'] = Procesados.objects.filter(idioma="ES").count()
        context['num_procesados_en_count'] = Procesados.objects.filter(idioma="EN").count()
        context['num_procesados_ca_count'] = Procesados.objects.filter(idioma="CA").count()

        if 'user' in request.session:
            context['username'] = request.session['user']
        return render(request, self.template_name, context)

class PrivateView(View):
    template_name = 'sm/pages/private.html'

    def get(self, request):
        if 'user' in request.session:
            username = request.session['user']
        else:
            username = None

        if self.__can_access(username):
            return render(request, self.template_name, {})
        else:
            return HttpResponseRedirect(reverse('home'))

    def __can_access(self, username):
        if username is None: return False

        try:
            user = Usuario.objects.get(username=username)
            user_exists = True
        except ObjectDoesNotExist:
            user_exists =  False

        has_enough_level = user.level >= 1

        return user_exists and has_enough_level

class LoginView(View):
    template_name = 'sm/pages/login.html'

    def get(self, request):
        if 'user' in request.session:
            del request.session['user']
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST['username']
        password = hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest()
        error_msg = ""

        try:
            user = Usuario.objects.get(username=username)
            authenticated = (user.password == password)
            if not authenticated:
                error_msg = 'Contraseña incorrecta.'

        except ObjectDoesNotExist:
            authenticated = False
            error_msg = 'El usuario no existe.'

        if authenticated:
            request.session['user'] = username
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, self.template_name, {'error': error_msg})



class ProcesadosViewSet(viewsets.ModelViewSet):
    queryset = Procesados.objects.all()
    serializer_class = ProcesadosSerializer

class TendenciasViewSet(viewsets.ModelViewSet):
    queryset = Tendencias.objects.all()
    serializer_class = TendenciasSerializer
