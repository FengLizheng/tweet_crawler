# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:02:59 2020

@author: FENG Lizheng The University of Hong Kong
"""
from user_information.user import get_user_profile
from api.twitter_api import oauth_login
from database import Database
import time
import pandas as pd

def extract_user_profile(screen_name):
      
        user=get_user_profile(twitter_api, screen_names=[screen_name])
        print(user)
        id=user[screen_name]['id']
        id_str=user[screen_name]['id_str']
        name=user[screen_name]['name']
        location=user[screen_name]['location']
        description=user[screen_name]['description']
        url=user[screen_name]['url']
        protected=user[screen_name]['protected']
        followers_count=user[screen_name]['followers_count']
        friends_count=user[screen_name]['friends_count']
        listed_count=user[screen_name]['listed_count']
        created_at=user[screen_name]['created_at']
        favourites_count=user[screen_name]['favourites_count']
        utc_offset=str(user[screen_name]['utc_offset'])
        time_zone=str(user[screen_name]['time_zone'])
        geo_enabled=user[screen_name]['geo_enabled']
        verified=user[screen_name]['verified']
        statuses_count=user[screen_name]['statuses_count']
        lang=str(user[screen_name]['lang'])
        contributors_enabled=user[screen_name]['contributors_enabled']
        is_translator=user[screen_name]['is_translator']
        is_translation_enabled=user[screen_name]['is_translation_enabled']
        profile_background_color=user[screen_name]['profile_background_color']
        profile_background_image_url=user[screen_name]['profile_background_image_url']
        profile_background_image_url_https=user[screen_name]['profile_background_image_url_https']
        profile_background_tile=user[screen_name]['profile_background_tile']
        profile_image_url=user[screen_name]['profile_image_url']
        profile_image_url_https=user[screen_name]['profile_image_url_https']
        profile_link_color=user[screen_name]['profile_link_color']
        profile_sidebar_border_color=user[screen_name]['profile_sidebar_border_color']
        profile_sidebar_fill_color=user[screen_name]['profile_sidebar_fill_color']
        profile_text_color=user[screen_name]['profile_text_color']
        profile_use_background_image=user[screen_name]['profile_use_background_image']
        has_extended_profile=user[screen_name]['has_extended_profile']
        default_profile=user[screen_name]['default_profile']
        default_profile_image=user[screen_name]['default_profile_image']
        following=user[screen_name]['following']
        follow_request_sent=user[screen_name]['follow_request_sent']
        notifications=user[screen_name]['notifications']
        translator_type=user[screen_name]['translator_type']
        
        entities=user[screen_name]['entities']
        status=user[screen_name]['status']
        sample_collection_time = time.asctime( time.localtime(time.time()) )
        
        try:
            profile_banner_url=user[screen_name]['profile_banner_url']
        except:
            profile_banner_url=""
            
        try:
            withheld_in_countries=user[screen_name]['withheld_in_countries']
        except:
            withheld_in_countries=""
        
        try:
            withheld_scope=user[screen_name]['withheld_scope']
        except:
            withheld_scope=""
            
        record = {
                          "screen_name":screen_name,
                          "id":id,
                          
                          "id_str": id_str,
                          "name": name,
                          "location":location,
                          "description":description,
                          "url":url,
                          "protected":protected,
                          "followers_count":followers_count,
                          "friends_count":friends_count,
                          "listed_count":listed_count,                         
                          "created_at":created_at,
                          "favourites_count":favourites_count,
                          "utc_offset":utc_offset,
                          "time_zone":time_zone,
                          "geo_enabled":geo_enabled,
                          "verified":verified,
                          "statuses_count":statuses_count,
                          "lang":lang,
                          "contributors_enabled":contributors_enabled,
                          "is_translator":is_translator,
                          "is_translation_enabled":is_translation_enabled,
                          "profile_background_color":profile_background_color,
                          "profile_background_image_url":profile_background_image_url,
                          "profile_background_image_url_https":profile_background_image_url_https,
                          "profile_background_tile":profile_background_tile,
                          "profile_image_url":profile_image_url,
                          "profile_image_url_https":profile_image_url_https,
                          "profile_link_color":profile_link_color,
                          "profile_sidebar_border_color":profile_sidebar_border_color,
                          "profile_sidebar_fill_color":profile_sidebar_fill_color,
                          "profile_text_color":profile_text_color,
                          "profile_use_background_image":profile_use_background_image,
                          "has_extended_profile":has_extended_profile,
                          "default_profile":default_profile,
                          "default_profile_image":default_profile_image,
                          "following":following,
                          "follow_request_sent":follow_request_sent,
                          "notifications":notifications,
                          "translator_type":translator_type,
                          "entities":str(entities),
                          "status":str(status),
                          "profile_banner_url":profile_banner_url,
                          "withheld_in_countries":withheld_in_countries,
                          "withheld_scope":withheld_scope,
                          "sample_collection_time":sample_collection_time
                       
                         }
        return record
            
def cut_screen_name(url,i):    
    screen_name=url[i].split('/')[3]
    return screen_name 
            
          
if __name__=="__main__":
                
                twitter_api = oauth_login()
                db = Database()
                db.connect()
                df=pd.read_csv(r'twitter_url.csv')
                url=df['twitter_url']
                
                for i in range(15):
                    try:
                        screen_name=cut_screen_name(url,i)
                        record=extract_user_profile(screen_name)            
                        table_name = 'twitter.user_profile'
                        db.insert_dict(record, table_name)
                    except:
                         continue                  
                       
                db.close()
                