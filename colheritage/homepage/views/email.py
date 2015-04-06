__author__ = 'cjpowers'
from django.core.mail import send_mail


# SEND EMAIL
send_mail(
    'Overdue Items',
    'Content goes here.',
    'cjpwrs@gmail.com',
    'cjpwrs@gmail.com',
)

#msg.attach_alternative(get_template('email.html').render(Context()), "text/html")
#msg.send()