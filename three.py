import json

url =  "jsons_file/file_js.json"

with open(url) as file_js:
    templates = json.load(file_js)



list_test = templates

pre_chanel = list_test['rss'] 
chanel = pre_chanel['channel']
news_items = chanel['items']

dict_for_descriptions = {}
i = 0
for news in news_items:
    id_news = news['_id']
    pub_date = news['pubDate']
    descriptions = news['description']
    dict_for_descriptions[i] = descriptions
    i = i+1

#max_word = max(dict_for_descriptions.values(), key=lambda i: i[1])[0]

value_list = list(dict_for_descriptions.values())

word_list = []
i = 0
for var in value_list:
    words = var.split(' ')
    for word in words:
        lenght = len(word)
        if lenght > 6:
            word_list.append(word)




