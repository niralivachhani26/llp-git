# app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Import the chatbot processor from the local chatbot directory
from .chatbot.chatbot_processor import get_chatbot_response

def clients(request):
    return render(request, 'clients.html')

@api_view(['POST'])
def chatbot_endpoint(request):
    try:
        # Get message from request data
        user_message = request.data.get('message')
        
        if not user_message:
            return Response({
                'status': 'error',
                'message': 'No message provided'
            }, status=400)

        # Get response from chatbot
        chatbot_response = get_chatbot_response(user_message)

        # Return response
        return Response({
            'status': 'success',
            'response': chatbot_response
        })

    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=500)
