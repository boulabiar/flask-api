import requests
import mysecrets

twitch_headers = {
    'Authorization': 'Bearer ' + mysecrets.access_token,
    'Client-Id': mysecrets.client_id,
}

recordset = {}

'''
[
   {
      "id":"141981764",
      "login":"twitchdev",
      "display_name":"TwitchDev",
      "type":"",
      "broadcaster_type":"partner",
      "description":"Supporting third-party developers building Twitch integrations from chatbots to game integrations.",
      "profile_image_url":"https://static-cdn.jtvnw.net/jtv_user_pictures/8a6381c7-d0c0-4576-b179-38bd5ce1d6af-profile_image-300x300.png",
      "offline_image_url":"https://static-cdn.jtvnw.net/jtv_user_pictures/3f13ab61-ec78-4fe6-8481-8682cb3b0ac2-channel_offline_image-1920x1080.png",
      "view_count":7840624,
      "created_at":"2016-12-14T20:32:28Z"
   }
]
'''

def streamerBuilder(username, platform='Twitch'):
    if platform=='Twitch':
        twitchHandler(username)
    return recordset


def twitchHandler(username):
    params = (('login', username),)
    response = requests.get('https://api.twitch.tv/helix/users', headers=twitch_headers, params=params).json()['data'][0]
    if response != []:
        recordset['platform'] = "Twitch"
        recordset['username'] = username
        recordset['streamUrl'] = "https://twitch.tv/" + username
        recordset['profilePictureUrl'] = response['profile_image_url']

    return recordset

#print(streamerBuilder('twitchdev'))


