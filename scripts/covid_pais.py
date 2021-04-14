import requests

def api_call(url):
	return requests.get(url).json()

def pais(info, pais, fecha):
	equivalents = {
		'infectados': 'confirmed',
		'recuperados': 'recovered',
		'fallecidos': 'deaths'
	}
	url = 'https://api.covid19api.com/total/country/' + pais + '/status/' + equivalents[info]
	response = api_call(url)
	if not fecha:
		number = '{:.}'.format(response[-1]['Cases'])
		return number

	for count, register in enumerate(response):
		entered_date = "2020-"+fecha+"T00:00:00Z" 
		if register['Date'] == entered_date:
			number = int(register['Cases']) - int(response[count]['Cases'])
	#number = '{:.}'.format(number)
	return '{:.}'.format(str(number))


print(pais('fallecidos', 'argentina', '07-19'))
