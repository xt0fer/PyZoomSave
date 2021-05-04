import json
import os, sys
from zoomus import ZoomClient
from datetime import datetime

zoomkey = os.environ.get('ZM_API_KEY')
zoomsecret = os.environ.get('ZM_API_SECRET')
lossie_id = os.environ.get('LOSSIE_ID')
kris_id = os.environ.get('KRIS_ID')

print(zoomkey, zoomsecret)
if zoomkey is None:
    print("Must set ENV VARS ZM_API_KEY and ZM_API_SECRET")
    sys.exit(1)
client = ZoomClient(zoomkey, zoomsecret) #, base_uri="https://api.zoom.us/v2")

# user_list_response = client.user.list()
# print(user_list_response)
# user_list = json.loads(user_list_response.content)
# print(user_list)

# for user in user_list['users']:
#     user_id = user['id']
#     print(json.loads(client.meeting.list(user_id=user_id).content))
user_person = client.user.get(id=lossie_id)
print(json.loads(user_person.content))
print("***")
st_date = datetime(2021, 1, 3)
#en_date = datetime(2021, 5, 4, 0, 0, 0, 0)
rec_list = client.recording.list(user_id=lossie_id, start=st_date)
print(json.loads(rec_list.content))
