from django.core.mail import send_mail
from R4C.settings import EMAIL_HOST_USER
from orders.models import Order


def send_email(robot):
    orders = Order.objects.filter(robot_serial=robot.serial)
    if orders:
        for order in orders:
            subject = 'Робот доступен в наличии'
            message = (f'Добрый день!\nНедавно вы интересовались нашим роботом модели {robot.model}, '
                       f'версии {robot.version}.\nЭтот робот теперь в наличии. '
                       f'Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.')
            send_mail(subject, message, EMAIL_HOST_USER, [order.customer.email])
