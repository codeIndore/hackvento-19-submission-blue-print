from googleapiclient.discovery import build
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', ]
path = 'home/vedang/Downloads/learn5/email/main/credentials.json'
path1 = 'home/vedang/Downloads/learn5/email/main/credentials.dat'


def read():
    with open('main/credentials.dat', 'rb') as credentials_dat:
        credentials = pickle.load(credentials_dat)

    if credentials.expired:
        credentials.refresh(Request())

    service = build('gmail', 'v1', credentials=credentials)
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")
        strin = ''
        j = 0
        for message in messages[:10]:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            if msg['payload']['headers'][6]['value'] == '<18bcs061@ietdavv.edu.in>':
                j+=1
                strin += "{\"id\":"+str(j)+",\"message\":"+"\""+msg['snippet']+"\""+"}\n"
        f = open('res.json', 'w')
        f.write(strin)
        f.close()
