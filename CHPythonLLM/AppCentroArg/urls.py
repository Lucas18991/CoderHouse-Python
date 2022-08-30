"""CHPythonLLM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from CHPythonLLM.views import probando_html, ano_nacimiento, saludo, segunda_vista, dia_de_hoy, saludo_con_nombre
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludar'),
    path('segunda_vista/', segunda_vista, name='Segunda_vista'),
    path('dia_de_hoy/', dia_de_hoy, name='dia_de_hoy'),
    path('saludo_con_nombre/<nombre>',
         saludo_con_nombre, name='saludo_con_nombre'),
    path('ano_nacimiento/<edad>',
         ano_nacimiento, name='ano_nacimiento'),
    path('probando_html/',
         probando_html, name='probando_html'),
    path('AppCentroArg/', include('AppCentroArg.urls')),
]
