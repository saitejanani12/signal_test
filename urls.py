"""
URL configuration for Signal_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# signal_demo/urls.py
from django.contrib import admin
from django.urls import path
from testapp.views import test_signal,test_signal_2,test_signal_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_signal/', test_signal, name='test_signal'),
    path('test_signal_2/',test_signal_2,name='test_signal_2'),
    path('test_signal_transaction/', test_signal_transaction, name='test_signal_transaction'),
]
