from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')


class ContactView(APIView):
    def post(self, request):
        form = ContactForm(request.data)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'Message from {name}',
                message=message,
                from_email=email,
                recipient_list=['your.email@example.com'],
                fail_silently=False,
            )
            return Response({'message': 'Message sent successfully!'}, status=status.HTTP_200_OK)

        return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)