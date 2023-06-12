from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
from datetime import datetime
 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)
    country=my_dict.get('country')
    capital=my_dict.get('capital')
    r1=""
    r2=""
    
    if country:
      try:
        url1= 'https://restcountries.com/v3.1/name/'
        res1 = requests.get(url1+country)
        data1 = res1.json()
        data1=list(data1)
        respo1=str(data1[0]["capital"][0])
        r1=f"The capital of {country} is {respo1}"
      except:
        r1=f"{country} country dose not exist in our databases"

    if capital:
      try:
        url2= 'https://restcountries.com/v3.1/capital/'
        res2 = requests.get(url2+capital)
        data2 = res2.json()
        data2=list(data2)
        respo2=str(data2[0]["name"]["common"])
        r2=f"{capital} is the capital of {respo2}"
      except:
        r2=f"{capital} capital dose not exist in our databases"

    if len(r1)>0 and len(r2)>0:
      final=r1+"\n"+r2
    elif len(r2)==0:
      final=r1
    elif len(r1)==0:
      final=r2
  
    self.wfile.write(final.encode())
    return