import json
import os, sys
from zoomus import ZoomClient
from datetime import date
import calendar

testtopic = "Zip Code Wilmington 'Meet the Experts' w/ Ben DuPont on - A Brief History & Future of Tech"

def zcwxform(topic: str) -> str:
    return topic.replace('w/', '').replace('-', '').replace('&', '').replace(',', ' ').replace('\'', '')

def topicxform(topic: str) -> str:
    return topic.replace("Zip Code Wilmington", "ZCW").replace("Meet the Experts", "MTE").replace(" ", "_")
    
#print(topicxform(zcwxform(testtopic)))

zoomkey = os.environ.get('ZM_API_KEY')
zoomsecret = os.environ.get('ZM_API_SECRET')
lossie_id = os.environ.get('LOSSIE_ID')
kris_id = os.environ.get('KRIS_ID')

# print(zoomkey, zoomsecret)
if zoomkey is None:
    print("Must set ENV VARS ZM_API_KEY and ZM_API_SECRET")
    sys.exit(1)
client = ZoomClient(zoomkey, zoomsecret)

# user_list_response = client.user.list()
# print(user_list_response)
# user_list = json.loads(user_list_response.content)
# print(user_list)

# for user in user_list['users']:
#     user_id = user['id']
#     print(json.loads(client.meeting.list(user_id=user_id).content))

# user_person = client.user.get(id=lossie_id)
# print(json.loads(user_person.content))


# yearis=2020
# monthis=7

def getmeetings(yearis: int, monthis: int) :
    st_date = date(yearis, monthis, 1)
    en_date = date(yearis, monthis, calendar.monthrange(yearis,monthis)[1])
    rec_list = client.recording.list(user_id=lossie_id, start=st_date, end=en_date)
    reclist_json = json.loads(rec_list.content)
    #print(json.dumps(reclist_json, indent=2))

    recording_list = reclist_json['meetings']
    print("***", yearis, monthis)
    for rec in recording_list:
        ttmp = rec['topic']
        ttime = "_"+rec['start_time']
        fname = topicxform(zcwxform(ttmp)) + ttime
        print(fname)

for yr in range(2020,2022) :
    for mon in range(1,13) :
        getmeetings(yr,mon)