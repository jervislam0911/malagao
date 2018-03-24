from django.shortcuts import render
from message.models import UserMessage
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "malagao.settings")
django.setup()

# Create your views here.

def getform(request):
    if request.method == "POST":
        first_name = request.POST.get('first-name', '')
        last_name = request.POST.get('last-name', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone', '')

    # all_messages = UserMessage.objects.filter(first_name='zhuzhu', last_name='ga')
    # for message in all_messages:
    #     print(message)
    #
    user_message = UserMessage()
    user_message.first_name = first_name
    user_message.last_name = last_name
    user_message.message = message
    user_message.email = email
    user_message.phone_number = phone_number
    user_message.object_id = "dwad"
    user_message.save()

    return render(request, 'message_form.html')