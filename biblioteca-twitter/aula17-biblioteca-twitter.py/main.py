from conexoes import Twitter

cosumer_key = 'dVNVPWUub6ed00Y8t7aYQkdXk'
consumer_secret = 'YRYr4PBGoAl5FrjGAXMwClsh41slSDZG8NZMjNUvgbU2Rtlz7N'

token_key = '1218013983451570176-zyrpRwey7Oi18yPjHsswTqUyyLd0zR'
token_secret = 'ObZoWVRfhvvyDoCah2y3qexfrgDHYxCVMnZZfQkIgW8g1'

twitter = Twitter(cosumer_key, consumer_secret, token_key, token_secret)

tweetar = twitter.tweet()

# O texto colocado dentro dos parênteses será postado no Twitter

pesquisar = twitter.search()
for resultado in pesquisar:
    print (resultado['user']['screen_name'])
    print (resultado['text'])
    print ('')
# O texto colocado dentro dos parênteses será pesquisado no Twitter

