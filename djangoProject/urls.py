"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from traffic_flow import views as traffic_flow_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', traffic_flow_views.home, name="home"),
    path('client/', traffic_flow_views.client, name="client"),
    path('client/loading/', traffic_flow_views.loading, name='loading'),
    path('client/unloading/', traffic_flow_views.unloading, name='unloading'),
    path('operator/table/', traffic_flow_views.operator, name='operator_table'),
    path('driver/table/', traffic_flow_views.driver, name='driver_table')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
