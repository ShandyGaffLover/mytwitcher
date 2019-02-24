import requests
from bs4 import BeautifulSoup

def get_auth_token(html:str)->str:
    soup=BeautifulSoup(html,'html.parser')
    return soup.find(attrs={'name':'authenticity_token'}).get('value')


username=''
password=''
payload={
    'session[username_or_email]':username
    ,'session[password]':password
    ,'return_to_ssl':'true'
    ,'redirect_after_login':'/'
}

s=requests.Session()
response=s.get('https://twitter.com/')
authenticity_token=get_auth_token(response.text)
payload['authenticity_token']=authenticity_token
response = s.post('https://twitter.com/sessions', data=payload)
response.raise_for_status()
print(response.text)
