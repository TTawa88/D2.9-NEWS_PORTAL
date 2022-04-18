from django.apps import AppConfig
import redis


class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointments'


red = redis.Redis(
    host='redis-17367.c250.eu-central-1-1.ec2.cloud.redislabs.com',
    port=17367,
    password='OFxBll8t7Iz5yh86bAWeCksVBNYiB3Kd'
)