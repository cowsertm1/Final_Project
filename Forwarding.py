from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
from base64 import b64decode
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser




SCOPES = 'https://www.googleapis.com/auth/gmail.modify'  # we are using modify and not readonly, as we will be marking the messages Read
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

user_id = 'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

# Getting all the unread messages from Inbox
# labelIds can be changed accordingly
unread_msgs = GMAIL.users().messages().list(userId='me', labelIds=[label_id_one, label_id_two]).execute()

label_id = 'Label_14' # ID of user label to add
filter = {
    'criteria': {
        'from': 'cat-enthusiasts@example.com'
    },
    'action': {
        'addLabelIds': [label_id],
        'removeLabelIds': ['INBOX']
    }
}
result = gmail_service.users().settings().filters().\
    create(userId='me', body=filter).execute()
print 'Created filter: %s' % result.get('id')