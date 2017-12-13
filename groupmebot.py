#!/usr/bin/python
# -*- coding: utf-8 -*-

# GroupMeBot: A python framework for a GroupMe Bot
# See http://www.groupme.com for more details


# -*- coding: cp1252 -*-
import requests
import time

# Some variables that will be used in making calls to the APIs
location_name = 'Houston, TX'
location_coords = { 'x': '29.7199', 'y': '-95.3422' }
request_params = { 'token': 'GROUPMEtOKEN'}

def post(to_send):
    # Send the response to the group
        post_params = { 'bot_id' : 'INSERT YOUR BOT ID', 'text': to_send }
        requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
        request_params['since_id'] = message['id']

#change spicc stuff
#add leslie motivate
#yeh/nah when questions
#


while True:
    #INSERT GROUP ID
    response = requests.get('https://api.groupme.com/v3/groups/INSERT GROUP ID/messages', params = request_params)

    # If there are new messages, check whether any of them are making queries to the bot
    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']

        # Iterate through each message, checking its text
        for message in response_messages:
            mess = message['text'].lower()
            if(mess.find('she') > -1):
            
                to_send = 'S-H-E???!\n\nPlease use gender neutral pronouns like "Ze" or "Hir" as to not offend anyone here :)'
                # Send the response to the group
                post(to_send)
                print("sending message: " + to_send)
                break
            
            if(message['text'].lower() == 'he '):
            
                to_send = 'H-E???!\n\nPlease use gender neutral pronouns like "Ze" or "Hir" as to not offend anyone here :)'
                post(to_send)
                
                print("sending message: " + to_send)
                print(message['text'])
                break
            
            
            
            if(mess.find('nig') > -1 or mess.find('negroe') > -1):
            
                to_send = 'Woah there! Next time, please refrain from using this horribly racist word. Instead, please use the universally accepted term "Basketball American".\n\nThanks for understanding'
                # Send the response to the group
                post(to_send)
                print("sending message: " + to_send)
                break
        
            if(mess.find('spic') > -1 or mess.find('wetback') > -1):
            
                to_send = 'Woah there! Next time, please refrain from using this horribly racist word. Instead, please use the universally accepted term "Basketball American".\n\nThanks for understanding'
                # Send the response to the group
                post(to_send)
                print("sending message: " + to_send)
                break
        
            if(mess.find('kike') > -1 or mess.find('jew') > -1):
            
                to_send = 'Woah there! Next time, please refrain from using this horribly racist word. Instead, please use the universally accepted term "Sh3kel American".\n\nThank you for your understanding.'
                # Send the response to the group
                post(to_send)
                print("sending message: " + to_send)
                break
            
            if(mess.find('fag') > -1 or mess.find('queer') > -1 or mess.find('gay') > -1):
            
                to_send = 'Woah there! Next time, please refrain from using this horribly racist word. Instead, please use the universally accepted term "Fanny Bandit".\n\nThanks for understanding'
                # Send the response to the group
                post(to_send)
                print("sending message: " + to_send)
                break
        
            if (mess.find('walk') > -1 or mess.find('weather') > -1):
            
                # Construct a response to send to the group
                weather_response = requests.get('https://api.weather.gov/points/' + location_coords['x'] + ',' + location_coords['y'] + '/forecast').json()
                current_weather = weather_response['properties']['periods'][0]['detailedForecast']
                to_send = 'The current We@ther in ' + location_name + ': ' + current_weather
            
                # Send the response to the group
                post(to_send)
                print("sending message: " + to_send)
                break

    time.sleep(5)
