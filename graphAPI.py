import requests

class api(object):
        def __init__(self, endpoint=None, access_token=None):
            self.api_url="https://graph.facebook.com/v2.8/"+endpoint+'/'
            self.access_token=access_token
            self.urls=[]

        def request(self, fields=None):
            url=self.api_url+'?fields='+fields+'&access_token='+self.access_token;
            self.getUrls(url)
            print self.urls


        def getUrls(self,url):
            response = requests.get(url)
            content=response.json();
            data=content['data'];
            for d in data:
                try:
                    self.urls.append(d['full_picture'])
                except:
                    print 'Node with no pic found'

                
