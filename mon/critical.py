from webpush import send_user_notification
from .models import ReceiveNotifications


# Critical params
TEMP_WARN = 45
TEMP_CRIT = 50
VIBE_WARN = 0.75
VIBE_CRIT = 1
WATT_WARN = 0.65
WATT_CRIT = 0.7
LOAD_WARN = 80
LOAD_CRIT = 95
TIME_WARN = 70000
TIME_CRIT = 85000


def check_data(data):
    if data.temperature > TEMP_CRIT:
        payload = {"head": "Medis Group LLC",
                   "body": f"Критическая температура на машине {data.machine_id}",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > VIBE_CRIT:
        payload = {"head": "Medis Group LLC",
                   "body": f"Критическая вибрация на машине {data.machine_id}",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > WATT_CRIT:
        payload = {"head": "Medis Group LLC",
                   "body": f"Критическое потребление на машине {data.machine_id}",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > LOAD_CRIT:
        payload = {"head": "Medis Group LLC",
                   "body": f"Критическая нагрузка на машине {data.machine_id}",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > TIME_CRIT:
        payload = {"head": "Medis Group LLC",
                   "body": f"Критическое время работы на машине {data.machine_id}",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > TEMP_WARN:
        payload = {"head": "Medis Group LLC",
                   "body": f"Температура на машине {data.machine_id} приближается к критической",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > VIBE_WARN:
        payload = {"head": "Medis Group LLC",
                   "body": f"Вибрация на машине {data.machine_id} приближается к критической",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > WATT_WARN:
        payload = {"head": "Medis Group LLC",
                   "body": f"Потребление на машине {data.machine_id} приближается к критическому",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > LOAD_WARN:
        payload = {"head": "Medis Group LLC",
                   "body": f"Нагрузка на машине {data.machine_id} приближается к критической",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
    if data.temperature > TIME_WARN:
        payload = {"head": "Medis Group LLC",
                   "body": f"Время работы на машине {data.machine_id} приближается к критическому",
                   "url": f"https://api.antares.nullteam.info/mon/record/{data.id}"}
        for user in ReceiveNotifications.objects.all():
            send_user_notification(user=user.user, payload=payload, ttl=1000)
