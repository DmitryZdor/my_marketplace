import uuid
from datetime import timedelta

from django.core.mail import send_mail

from common.utils import client_message

from celery import shared_task
from django.utils.timezone import now

from marketplace import settings
from .models import EmailVerification, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(),
                                              user=user,
                                              expiration=expiration)
    record.send_verification_email()


@shared_task
def send_email_client_order(obj):
    send_mail(
        subject='TOPS_CROPS_заказ',
        message=client_message(obj),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[obj.email, settings.EMAIL_HOST_USER],
        fail_silently=False,
    )