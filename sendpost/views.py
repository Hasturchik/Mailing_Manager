from rest_framework import viewsets, status
from .models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mailing, Message, Client
from .serializers import MessageSerializer
import requests

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# @api_view(['POST'])
# def start_mailing(request, mailing_id):
#     try:
#         mailing = Mailing.objects.get(id=mailing_id)
#
#         # Logic to filter and get targeted clients for the mailing
#         targeted_clients = get_targeted_clients(mailing)  # Implement this function
#
#         # Send messages to targeted clients
#         for client in targeted_clients:
#             # Your logic here for sending messages to clients
#             message = Message(client=client, mailing=mailing, status="Pending")  # Create message object
#             message.save()  # Save message to start collecting stats
#
#             # Assume you have a function to send the message externally
#             send_message_to_external_service(message)  # Implement this function
#
#         return Response({"message": "Mailing started."}, status=status.HTTP_200_OK)
#
#     except Mailing.DoesNotExist:
#         return Response({"message": "Mailing not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# # Assuming you have the JWT token available in a variable called jwt_token
# def send_message_to_external_service(message):
#     headers = {
#         'Authorization': f'Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA5MTAwMzcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9OaXlhcmxhdGhvdGVwIn0.cAK7PV6uJLORH5yPWj3WnHChiKQbORpNau2YoKhYCVI}',
#         'Content-Type': 'application/json'
#     }
#     data = {
#         'id': message.id,
#         'phone': message.client.phone_number,
#         'text': message.mailing.message_text
#     }
#     response = requests.post('http://external-service-url/send/{msgId}'.format(msgId=message.id), json=data,
#                              headers=headers)
#
#     # Handle response from the external service
#     if response.status_code == 200:
#         message.status = "Sent"
#     else:
#         message.status = "Failed"
#
#     message.save()  # Update the status of the message