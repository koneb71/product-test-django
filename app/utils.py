from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def confirm_order_email(payload):
    subject = 'Order Confirmation'
    context = {
        'customer_name': payload['customer_name'],
        'order_id': payload['order_number'],
        'order_date': payload['created_at'],
        'items': payload['items']
    }

    html_message = render_to_string('email/order_confirmation_email.html', context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [payload['customer_email']],
        html_message=html_message,
        fail_silently=False,
    )
