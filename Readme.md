# PyZoomSave

Need a way to copy recording on Zoom to Google Drive

You need a series of env vars to make this work.

- zoom userid
- zoom ZM_API_KEY, ZM_API_SECRET
- zoom ids for LOSSIE_ID, KRIS_ID, LIZ_ID
- zoom JWT_TOKEN (I made one with one week's validity)
- a way to mount Google Drive and copy files to it
- enough disk space to hold the downloaded mp4 files

## What's the big idea?

Log into zoom, list all the available recordings for a given user.
Download each one done to  `./files/` location.
Copy it up to a Google drive location.

after being sure they all went to google, have a means to delete from zoom.

see the Makefile for phases.

python 3.8.2 was used for development.

Create a `venv` and make sure you install all the `requirements.txt` into it.
Use Python3 and Pip3.

### Zoom API interaction

Found this
```
https://github.com/prschmid/zoomus
```

Looks like a good project to use for getting the recordings from Zoom.

You need to have ADMIN access to your zoom account for this to work.

I used `CloudMounter` to mount the Google Drive using my work email. That gave me access
to the company folders.
