# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 07:08:46 2020

@author:Feng Lizheng The University of Hong Kong
"""
from api.twitter_api import oauth_login,harvest_user_timeline
from basic_extract.twitter_extract import tweets_basic_excract
import pandas as pd 
from database import Database

def cut_screen_name(url,i):    
    screen_name=url[i].split('/')[3]
    return screen_name 



if __name__=="__main__":
    twitter_api = oauth_login()
    db = Database()
    db.connect()
    df=pd.read_csv(r'twitter_url.csv')
    url=df['twitter_url']
    for i in range(len(url)):
        try:
            max_results=500
            screen_name=cut_screen_name(url,i)
            tweets = harvest_user_timeline(twitter_api, screen_name=screen_name, \
                                   max_results=max_results)
   
            for j in range(max_results-1):
                print(tweets[j])
                record=tweets_basic_excract(tweets,j,screen_name)
               
                table_name = 'twitter.twitter_data'
                db.insert_dict(record, table_name)
               
        except:
            continue   
      




  
   