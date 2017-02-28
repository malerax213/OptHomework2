#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Optional HomeWork2
Created on 28/02/2017
@author: Alexandru Matinas
'''
import sys
import urllib2
from bs4 import BeautifulSoup

api_key = None

class WeatherClient(object):
    '''
    Docstring for WeatherClient
    '''
    url_base = "http://api.wunderground.com/api/"
    url_service = {
    "hourly": "/hourly/q/CA/"
    }
    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def hourly(self, location):
        '''
        Baixar-se la web
        '''
        url = WeatherClient.url_base + self.api_key + WeatherClient.url_service["hourly"] + location + ".xml"
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()
        '''
        Llegir la web
        '''
        soup = BeautifulSoup(data, 'lxml')

        forecast = soup.find("forecast")
        data = forecast.find("pretty").text
        weekday = forecast.find("weekday_name").text
        hour = forecast.find("civil").text
        condicio = forecast.find("condition").text
        temp = forecast.find("temp").find("metric").text
        humidity = forecast.find("humidity").text
        '''
        Retornar resultats
        '''
        resultats = {}
        resultats["actual"]={}
        resultats["futur1"]={}
        resultats["futur2"]={}
        resultats["actual"]["data"] = data
        resultats["actual"]["weekday"] = weekday
        resultats["actual"]["hour"] = hour
        resultats["actual"]["temp"] = temp
        resultats["actual"]["humidity"] = humidity
        resultats["actual"]["condicio"] = condicio

        print resultats["actual"]["weekday"] + "'s forecast at",resultats["actual"]["hour"]+":"
        print "*-----------------------------*"
        print "Temp:",resultats["actual"]["temp"]
        print "Humidity:",resultats["actual"]["humidity"]
        print "Condition:",resultats["actual"]["condicio"]

if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print"API key must be in CLI Option"

    WC = WeatherClient(api_key)
    resultat = WC.hourly("Lleida")
