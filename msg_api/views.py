from msg_api import models
from msg_api import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from datetime import datetime, timezone

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# Messages handeled by this View
class Messages(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Add New message to database
    def post(self, request):
        msg_in_hour=0   # for count messages in one hour
        hour_countdown=0    # for count time of last 10 messages
        last_msgs = models.Create_message.objects.filter(userid = request.user.id)[::-1][:10]  # getting last 10 messages
        print(last_msgs)
        # counting msg_in_hour and time for 10 messages
        for msg in last_msgs:   
            hour_countdown = (datetime.now().replace(tzinfo=timezone.utc)-msg.updated_at).total_seconds()-19800
            if hour_countdown<=3600:
                msg_in_hour+=1
                if msg_in_hour==10:
                    return Response({'Error':'You Reached Your Hourly limit!'}, status = 400)
            else:
                # This method will called if length of last_msgs > 0
                return Messages.processed_msg(request, hour_countdown,msg_in_hour) 

        # This method will called if length of last_msgs is 0
        return Messages.processed_msg(request)
        
    # processed_msg, method used for add the message to database if limit is not excessed
    @staticmethod
    def processed_msg(request, hour_countdown = 0, msg_in_hour = 0):
        if hour_countdown<3600 and msg_in_hour<10:    # if less the 10 messages have sent in  one hour duration
            newdata =  dict(request.data)
            newdata.update({'message':newdata['message'][0],'userid':request.user.id})
            print(newdata)
            data = serializers.MsgSerializer(data=newdata) # adding the message to database using serializer

            if data.is_valid():
                data.save()
                response=dict(data.data)    #convering data to dictionary
                userid = request.user.id
                username = request.user.username
                email = request.user.email
                # adding the user data who sent the message
                response.update({'createdby':{
                    'id': userid,
                    'username':username,
                    'email': email
                }})
                return Response(response, status=201)

            return Response(data.errors)

        return Response({'Error':'You Reached Your Hourly limit!'}, status = 400)
        
# Getting the valid user and genrating Token
class TokenAuthantication(ObtainAuthToken):

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request}) # Getting the valid user and token from authtoken
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']    # validating the user 
        token, _ = Token.objects.get_or_create(user=user)   # storing the token in variable
        return Response({'token': token.key}, status = 200)


