import json
import requests
positions = []
with open('portfolio.txt', 'r') as cur_portfolio:
	for p in cur_portfolio:
		positions.append(p.strip())
print(positions)
position_news_mapping = {}
for position in positions:
	results = requests.get('http://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+position+'%20stock&start=10').text
	parsed_json = json.loads(results)
	response_json = parsed_json['responseData']['results']
	urls = [x['unescapedUrl'] for x in parsed_json['responseData']['results']]
	position_news_mapping[position] = urls
print(position_news_mapping)

# Google Search Results API: http://ajax.googleapis.com/ajax/services/search/news?v=1.0&q=goog&start=10