import oauth2
import urllib.parse
import json

class Twitter: 
    def __init__(self, cosumer_key, consumer_secret, token_key, token_secret):
        self.conexao(cosumer_key, consumer_secret, token_key, token_secret)
            
    def conexao(self, cosumer_key, consumer_secret, token_key, token_secret):
        self.Consumer = oauth2.Consumer(cosumer_key, consumer_secret)               #
        self.Token = oauth2.Token(token_key, token_secret)                          # São atribbutos do objeto
        self.Cliente = oauth2.Client(self.Consumer, self.Token)                     #

    def tweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='') 
        requisicao = self.Cliente.request('https://api.twitter.com/1.1/statuses/update.json?statuses=' + query_codificada, method = 'POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def search(self, query):
        query_codificada = urllib.parse.quote(query, safe='') 
        requisicao = self.Cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+ query_codificada)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweets = objeto['statuses']
        return tweets