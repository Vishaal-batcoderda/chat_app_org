import json
from textblob import TextBlob  # Import TextBlob
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Create a unique room for each user (could use channels or room groups)
        self.room_name = 'chat_room'
        self.room_group_name = f'chat_{self.room_name}'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the incoming message
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Perform sentiment analysis
        sentiment = self.analyze_sentiment(message)

        # Send the message with sentiment to the group (all users in the room)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',  # Call the chat_message method
                'message': message,
                'sentiment': sentiment,
                'user': self.scope['user'].username,
            }
        )

    async def chat_message(self, event):
        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'user': event['user'],
            'message': event['message'],
            'sentiment': event['sentiment'],
        }))

    def analyze_sentiment(self, message):
        """
        Sentiment analysis using TextBlob.
        """
        blob = TextBlob(message)
        polarity = blob.sentiment.polarity
        if polarity > 0.2:
            return 'positive'
        elif polarity < -0.2:
            return 'negative'
        else:
            return 'neutral'
