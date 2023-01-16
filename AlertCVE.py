import json
import requests
import tweepy
import time
from datetime import datetime

###############################
### Defina as configurações ###
###############################

# Bearer Token da conta de desenvolvedor no Twitter
TwitterToken = ''

# Token do bot do Telegran
TelegranToken = ''

# ID do grupo do Telegram que receberá os alertas OBS: começa com sinal de -
GroupTelegram = ''

#############################
### Fim das configurações ###
#############################

client = tweepy.Client(bearer_token=TwitterToken)
token = TelegranToken
chat_id = GroupTelegram  
tweeter_id = '821806287461740544'  # ID da conta que buscamos as CVEs no Twitter
num_max_result = 100     # Maximum results
timeout = 5      # seconds

# abre o arquivo com a lista de aplicativos
with open('aplications.json') as app:
    app_db = json.load(app)
    app.close()

# função de envio para o telegran
def AlertCVE(token, chat_id, message):
    try:
        data2 = {"chat_id": chat_id, "text": message}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data2)
    except Exception as e:
        print("Erro no sendMessage:", e)
    return


def fetch_app_is_match(text):
    result = [False,""]
    with open('aplications.json','r') as vendor:
        app_db = json.load(vendor)
        vendor.close()
    for app in app_db['Aplication']:
        if app in text:
            result = [True,app]
    return result


def Export_Logs_To_SIEM(tweeter):
    with open('logs_to_siem.csv','a') as siem:
        now = datetime.now()
        cvename = tweeter['text'].split(' ')[0]
        datetimegenerated = now.strftime('%Y/%m/%d %H:%M:%S')
        tweeter_id = tweeter['id']
        devicevendor = 'ORG' #sua organização
        deviceproductor = 'CVE'
        text = tweeter['text']
        siem.write(f'{datetimegenerated},{tweeter_id},{cvename},{devicevendor},{deviceproductor},{text}\n')
        siem.close()
    return

# Inicio do processo
while True:
    # abertutra do arquivo de controle
    with open('controle.txt', 'r') as config:
        last_id = config.readline()
        config.close()

    try:
        tweets = client.get_users_tweets(id=tweeter_id, since_id=last_id, max_results=num_max_result, tweet_fields=['context_annotations', 'created_at', 'geo'],)

        for tweet in reversed(tweets.data):
             last_id = str(tweet['id'])
             fetch_app = fetch_app_is_match(str(tweet['text']).lower())
             app_match = fetch_app[0]
             app_name = fetch_app[1].upper()
             if app_match:
                 AlertCVE(token, chat_id, '!!! ATENÇÃO !!! \nA tecnologia:  ' + '-- ' + app_name.upper().strip() + ' --\n' + 'foi encontrada em uma nova CVE.')
                 AlertCVE(token, chat_id, tweet['text'])
                 Export_Logs_To_SIEM(tweet)
                 print(tweet['text'])

    except Exception as e:
        print("Não existem novas CVEs:", e)
    # Gravar no arquivo de controle a ultima numeracao de twitter
    with open('controle.txt', 'w') as config:
        config.write(last_id)
        config.close()

    print("Press Ctrl+C to abort ... ")
    time.sleep(timeout)
