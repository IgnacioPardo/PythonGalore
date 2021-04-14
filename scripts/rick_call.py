from twilio.rest import Client

account_sid = 'AC5a91b40dcbc7379b67771e52b8b8f1ec'
auth_token = '86bcbea73d539e3b083f04b5f869abc5'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+5491122806788',
                        from_='+14352535733'
                    )

print(call.sid)