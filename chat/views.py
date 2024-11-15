from transformers import pipeline
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

# Load the pre-trained model for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis")


def analyze_sentiment(text):
    analysis = sentiment_analyzer(text)
    print(analysis)  # Debugging: Check the raw analysis output
    return analysis[0]['label'], analysis[0]['score']



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        # Get message content from the serializer data
        message_content = serializer.validated_data['content']

        # Analyze sentiment
        sentiment_label, sentiment_score = analyze_sentiment(message_content)

        # Create the message object and include sentiment analysis data
        message = serializer.save()
        message.sentiment = sentiment_label  # Store sentiment
        message.sentiment_score = sentiment_score  # Store sentiment score
        message.save()
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensure only logged-in users can access this view
def profile(request):
    return render(request, 'profile.html')  # Render the profile page template


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensure only logged-in users can access this view
def chat_view(request):
    return render(request, 'chat.html')  # Render the chat page template
