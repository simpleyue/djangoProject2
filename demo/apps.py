from django.apps import AppConfig
from utils import g
g._init() #初始化


class DemoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "demo"
