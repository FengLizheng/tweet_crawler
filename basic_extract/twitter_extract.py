# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 05:25:50 2020

@author: FENG Lizheng The University of Hong Kong

"""
import time
def tweets_basic_excract(tweets,i,screen_name):
        screen_name=screen_name
        created_at=tweets[i]['created_at']
        id=tweets[i]['id']
        id_str=tweets[i]['id_str']
        text=tweets[i]['text']
        truncated=tweets[i]['truncated']
        source=tweets[i]['source']      
        in_reply_to_status_id=tweets[i]['in_reply_to_status_id']
        in_reply_to_status_id_str=tweets[i]['in_reply_to_status_id_str']
        in_reply_to_user_id=tweets[i]['in_reply_to_user_id']
        in_reply_to_user_id_str=tweets[i]['in_reply_to_user_id_str']
        in_reply_to_screen_name=tweets[i]['in_reply_to_screen_name']       
        user=str(tweets[i]['user'])     
        geo=str(tweets[i]['geo'])
        coordinates=tweets[i]['coordinates']
        place=tweets[i]['place']
        contributors=str(tweets[i]['contributors'])
        is_quote_status=tweets[i]['is_quote_status']
        try:
            quoted_status_id=tweets[i]['quoted_status_id']
        except:
            quoted_status_id=""
            
        try:
            quoted_status_id_str=tweets[i]['quoted_status_id_str']
        except:
            quoted_status_id_str=""
        try:    
            quote_status=str(tweets[i]['quoted_status'])
            quote_label=1
        except:
            quote_label=0
            quote_status=""
        try:    
            retweeted_status=str(tweets[i]['retweeted_status'])
            retweeted_label=1
        except:
            retweeted_label=0
            retweeted_status=""
        try:  
            quote_count=tweets[i]['quote_count']  
        except:
            quote_count=None
        try:
            reply_count=tweets[i]['reply_count']  
        except:
            reply_count=None
        retweet_count=tweets[i]['retweet_count']
        favorite_count=tweets[i]['favorite_count']
        favorited=tweets[i]['favorited']
        retweeted=tweets[i]['retweeted']
        lang=tweets[i]['lang']
        entities=str(tweets[i]['entities'])
        try:
            extended_entities=str(tweets[i]['extended_entities'])
        except:
            extended_entities=None
        try:
            possibly_sensitive=tweets[i]['possibly_sensitive']
        except:
            possibly_sensitive=None
        try:
            filter_level=tweets[i]['filter_level']
        except:
            filter_level=None
        try:
            matching_rules=tweets[i]['matching_rules']
        except:
            matching_rules=None
            
        try:
            current_user_retweet=tweets[i]['current_user_retweet']
        except:
            current_user_retweet=None
            
        try:
            scopes=tweets[i]['scopes']
        except:
            scopes=None
            
        try:
            withheld_copyright=tweets[i]['withheld_copyright']
        except:
            withheld_copyright=None
        try:
            withheld_in_countries=tweets[i]['withheld_in_countries']
        except:
            withheld_in_countries=None
        try:
            withheld_scope=tweets[i]['withheld_scope']
        except:
            withheld_scope=None
            
        sample_collection_time = time.asctime( time.localtime(time.time()) )
        
        record={
                "screen_name":screen_name,
                "created_at":created_at,
                "id":id,
                "id_str":id_str,
                "text":text,
                "truncated":truncated,
                "source":source,
                "in_reply_to_status_id":in_reply_to_status_id,
                "in_reply_to_status_id_str":in_reply_to_status_id_str,
                "in_reply_to_user_id":in_reply_to_user_id,
                "in_reply_to_user_id_str":in_reply_to_user_id_str,
                "in_reply_to_screen_name":in_reply_to_screen_name,
                "user":user,
                "geo":geo,
                "coordinates":coordinates,
                "place":place,
                "contributors":contributors,
                "is_quote_status":is_quote_status,
                "quoted_status_id":quoted_status_id,
                "quoted_status_id_str":quoted_status_id_str,
                "quote_status":quote_status,
                "quote_label":quote_label,
                "retweeted_label":retweeted_label,
                "retweeted_status":retweeted_status,
                "quote_count":quote_count,
                "reply_count":reply_count,
                "retweet_count":retweet_count,
                "favorite_count":favorite_count,
                "favorited":favorited,
                "retweeted":retweeted,
                "lang":lang,
                "entities":entities,
                "extended_entities":extended_entities,
                "possibly_sensitive":possibly_sensitive,
                "filter_level":filter_level,
                "matching_rules":matching_rules,
                "current_user_retweet":current_user_retweet,
                "scopes":scopes,
                "withheld_copyright":withheld_copyright,
                "withheld_in_countries":withheld_in_countries,
                "withheld_scope":withheld_scope,
                "sample_collection_time":sample_collection_time                                                
            }
   
        
        return record
   
        
     
            
        