from django.urls import path
from traffic_flow import views as traffic_flow_views


urlpatterns = [
    path('', traffic_flow_views.home, name="home"),
    path('client/', traffic_flow_views.client, name="client"),
    path('client/loading/', traffic_flow_views.loading, name='loading'),
    path('client/unloading/', traffic_flow_views.unloading, name='unloading'),
    path('operator/table/', traffic_flow_views.operator, name='operator_table'),
    path('driver/table/', traffic_flow_views.driver, name='driver_table')
]