# PyZoomSave

Need a way to copy recording on Zoom to Google Drive

You need a series of env vars to make this work.

- zoom userid
- zoom keys
- google id and keys

## What's the big idea?

Log into zoom, list all the available recordings for a given user.
Copy each one done to  a/tmp location.
Copy it up to a Google drive location.

after being sure they all went to google, have a means to delete from zoom.

see the Makefile for phases.

python 3.8.2 was used for development.

### Zoom API interaction

Found this
```
https://github.com/prschmid/zoomus
```

Looks like a good project to use for getting the recordings from Zoom.

stuck at 

> https://devforum.zoom.us/t/finding-your-api-key-secret-credentials-in-marketplace/3471


### Google Client Lib

Quickstart was here. 
https://developers.google.com/drive/api/v3/quickstart/python

```
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Google Upload stuff

https://developers.google.com/drive/api/v3/manage-uploads