from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

#Using the Everypixel API
class QualityAppraiser:
    def __init__(self, clientId, clientSecret):
        self.tokenUrl = 'https://api.everypixel.com/oauth/token'
        try:
            oAuth = OAuth2Session(client = BackendApplicationClient(clientId))
            token = oAuth.fetch_token(token_url=self.tokenUrl,
                                      auth=(clientId, clientSecret))
        except:
            print("Whoops!")
        self.finalToken = OAuth2Session(clientId, token=token)

    def get_token(self):
        return self.finalToken
