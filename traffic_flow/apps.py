from django.apps import AppConfig


class TrafficFlowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'traffic_flow'
    verbose_name = "Система управления потоками транспорта"