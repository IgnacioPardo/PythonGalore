from pprint import pprint
def get_bars_filtered(bars, _filter):
	results = {}
	for _filter_key in _filter.keys():
		for _id in bars.keys():
			if _filter[_filter_key] in bars[_id][_filter_key]:
				results[_id] = bars[_id]
				#break
	return results


bars = {1 : 
			{
				"name" : "Chona´s",
				"tags" : "se, buenardo, outside",
				"categoria" : "bar, night-out",
				"hood" : "nuñez",
				"vibe" : "chill, relax"

			}, 
		2 : 
			{
				"name" : "Lo de Chona",
				"tags" : "casa, drogas",
				"categoria" : "rancho",
				"hood" : "nuñez, belgrano",
				"vibe" : "party, proyecto-x"

			}, 
		3 : 
			{
				"name" : "honas",
				"tags" : "fake, casa",
				"categoria" : "",
				"hood" : "nuñez",
				"vibe" : "embole"

			}, 
		4 : 
			{
				"name" : "aaaaa",
				"tags" : "drogas, outside",
				"categoria" : "casa-tomada",
				"hood" : "lanus",
				"vibe" : ""

			} }

filters = {"tags" : "drogas"}