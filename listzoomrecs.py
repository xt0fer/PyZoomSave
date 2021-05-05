import json
import os, sys
from zoomus import ZoomClient
from datetime import date
import calendar
import wget
import uuid
import unicodedata
import re

testtopic = "Zip Code Wilmington 'Meet the Experts' w/ Ben DuPont on - A Brief History & Future of Tech"

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def zcwxform(topic: str) -> str:
    #return topic.replace('w/', '').replace('-', '').replace('&', '').replace(',', ' ').replace('\'', '').replace('/','')
    return slugify(topic)

def topicxform(topic: str) -> str:
    return topic.replace("zip-code-wilmington", "zcw").replace("meet-the-experts", "mte").replace(" ", "_")
    
#print(topicxform(zcwxform(testtopic)))

zoomkey = os.environ.get('ZM_API_KEY')
zoomsecret = os.environ.get('ZM_API_SECRET')
lossie_id = os.environ.get('LOSSIE_ID')
kris_id = os.environ.get('KRIS_ID')
jwtoken = os.environ.get('JWT_TOKEN')

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
def download_mp4(f, fname):
    #print('> ', f['id'])
    #print('> ', f['download_url']+'?access_token='+jwtoken)
    durl = f['download_url']+'?access_token='+jwtoken
    if not os.path.exists('files/'+fname):
        wget.download(durl, 'files/'+fname)
        print("\n*** done with ", fname)
    else:
        print("\n*** Already Downloaded ", fname)



def getmeetings(yearis: int, monthis: int) :
    st_date = date(yearis, monthis, 1)
    en_date = date(yearis, monthis, calendar.monthrange(yearis,monthis)[1])
    rec_list = client.recording.list(user_id=lossie_id, start=st_date, end=en_date)
    reclist_json = json.loads(rec_list.content)
    #print(json.dumps(reclist_json, indent=2))

    recording_list = reclist_json['meetings']
    print("***", yearis, monthis)
    for rec in recording_list:
        # print(json.dumps(rec, indent=2))
        ttmp = rec['topic']
        ttime = "_"+rec['start_time']
        fname = topicxform(zcwxform(ttmp)) # + '_'+str(uuid.uuid4())[:8]
        print(fname)
        rec_files = rec['recording_files']
        for f in rec_files :
            if f['file_type'] == 'MP4' :
                download_mp4(f, fname+'.mp4')

        

for yr in range(2020,2022) :
    for mon in range(1,13) :
        getmeetings(yr,mon)