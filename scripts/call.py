import nexmo
from pprint import pprint

client = nexmo.Client(
  application_id='950cb90c-3848-49c6-b472-7f6a1335d101',
  private_key='private.key'
)

ncco = [
  {
    'action': 'talk',
    'voiceName': 'Joey',
    'text': 'This is a text-to-speech test message.'
  }
]

response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '5491144015439'
  }],
  'from': {
    'type': 'phone',
    'number': '5491154026445'
  },
  'ncco': ncco
})

pprint(response)