import gmail

POST https://www.googleapis.com/gmail/v1/users/userId/settings/filters
filter = {
    'criteria': {
        'from': 'cowsertm1@gmail.com'
    },
    'action': {
        'forward': "cowsertm1.73dd1@m.evernote.com"
    }
}
result = gmail_service.users().settings().filters().\
    create(userId='me', body=filter).execute()
print 'Created filter: %s' % result.get('id')