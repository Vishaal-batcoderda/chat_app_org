import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from .views import analyze_sentiment

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Handle WebSocket disconnection
        pass

    async def receive(self, text_data):
        try:
            # Parse the incoming message from the client
            data = json.loads(text_data)
            message_content = data["message"]

            # Retrieve the authenticated user
            user = self.scope.get("user")
            if user.is_authenticated:
                username = user.username
            else:
                username = "Anonymous"

            # Perform sentiment analysis on the message content
            sentiment_label, score = analyze_sentiment(message_content)

            # Save the message to the database
            message = Message.objects.create(
                user=user,
                content=message_content
            )

            # Send the message along with sentiment analysis results to the client
            await self.send(text_data=json.dumps({
                'message': message_content,
                'user': username,
                'sentiment': sentiment_label,
                'score': score  # If needed to display the sentiment score
            }))

        except Exception as e:
            # Handle any exceptions (e.g., print the error)
            print(f"Error in processing message: {e}")
            # Optionally send an error message back to the client
            await self.send(text_data=json.dumps({
                'error': 'There was an error processing your message.'
            }))
