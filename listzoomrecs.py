import json
import os, sys
from zoomus import ZoomClient

zoomkey = os.environ.get('ZM_API_KEY')
zoomsecret = os.environ.get('ZM_API_SECRET')
if zoomkey is None:
    print("Must set ENV VARS ZM_API_KEY and ZM_API_SECRET")
    sys.exit(1)
client = ZoomClient(zoomkey, zoomsecret)

user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)

for user in user_list['users']:
    user_id = user['id']
    print(json.loads(client.meeting.list(user_id=user_id).content))
