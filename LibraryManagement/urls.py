"""bibliotheksverwaltung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [

    path('login/', views.login_page),
    path('logout/', views.logout_route),
    path('', views.overview_page),
    path('profile/', views.profile_page),
    path('borrow/', views.borrow_route),
    path('return/', views.return_route),
    path('detail/<int:id>/', views.detail_page),
    path('print/', views.print_codes_page),

    path('imprint/', views.imprint),
    path('privacy/', views.privacy)
]
