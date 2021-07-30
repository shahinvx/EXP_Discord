from django.conf import settings
from prac_discord_6.settings import BASE_DIR, app_token
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics, serializers


from .models import Discord_Apps_List  ,NLP_Models
from .serializers import Discord_Serializer, Nlp_Serializer

from Discord_Model import my_discord

print('Base dir', BASE_DIR)
class Home(APIView):                                                # Class Based
    def get(self, request):
        return Response({"message": "App Start"})

class Discord_Home(APIView):                                        # Class Based
    def get(self, request):
        return Response({"message": "Doscord inside"})

# http://127.0.0.1:8000/discord/list/
class Discord_list(generics.ListAPIView):
    queryset = Discord_Apps_List.objects.all()
    serializer_class = Discord_Serializer

# http://127.0.0.1:8000/discord/add_discord/
class Discord_Add(generics.CreateAPIView):
    serializer_class = Discord_Serializer

# http://127.0.0.1:8000/discord/add_nlp/
class Nlp_Model_Add(generics.CreateAPIView):
    serializer_class = Nlp_Serializer

# http://127.0.0.1:8000/discord/model_list/
class Nlp_list(generics.ListAPIView):
    queryset = NLP_Models.objects.all()
    serializer_class = Nlp_Serializer


# http://127.0.0.1:8000/discord/discord_start/test_1/
from threading import Thread
import asyncio
#global My_TOKEN
My_TOKEN = ''
class Discord_App_Start(generics.ListAPIView):                     # Just [Get] all read only + qry
    def get_queryset(self):
        self.p_name = self.kwargs['name']

        if self.p_name:

            self.My_TOKEN = Discord_Apps_List.objects.get(App_name=self.p_name).App_Token
            print('\t\tAl data',self.My_TOKEN)
            global m_token 
            m_token = self.My_TOKEN
            

            return Discord_Apps_List.objects.filter(App_name=self.p_name)
        else:
            return Discord_Apps_List.objects.all()

    serializer_class = Discord_Serializer
#'''
    if 'm_token' not in globals():
        My_TOKEN = 'ODcwMTg0MjIzNzI0NjgzMjY0.YQJENg.JUEfIBv-eVCeIAZjDJ146hO8DYw'
        client = my_discord.MyClient()
        loop = asyncio.get_event_loop()
        loop.create_task(client.start(My_TOKEN))
        Thread(target=loop.run_forever).start()
    else:
        print('Token Not Found')
#'''


def start_discord(token):
    client = my_discord.MyClient()
    loop = asyncio.new_event_loop()
    loop = asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    #loop = asyncio.set_event_loop()
    loop.create_task(client.start(token))
    Thread(target=loop.run_forever).start()

class Discord_alt(APIView):
    global token
    def get(self, request, *args, **kwargs):
        global p_name 
        p_name = kwargs['name']
        qry = Discord_Apps_List.objects.get(App_name=p_name)
        print('\t\tAl data',qry.App_Token)
        
        if qry.App_Token!='':
            print('\t\tToken data',qry.App_Token)
            my_discord.set_model(qry.NLP_Model)

        serializer = Discord_Serializer(qry)
        return Response(serializer.data)

    try:
        print('\t\t\t\t\t name : ',p_name)
    except:
        print('pname not found')
    # My_TOKEN = 'ODcwMTg0MjIzNzI0NjgzMjY0.YQJENg.JUEfIBv-eVCeIAZjDJ146hO8DYw'
    # client = my_discord.MyClient()
    # loop = asyncio.get_event_loop()
    # loop.create_task(client.start(My_TOKEN))
    # Thread(target=loop.run_forever).start()

