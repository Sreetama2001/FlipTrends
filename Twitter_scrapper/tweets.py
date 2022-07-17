import tweepy as tp
import credentials as dta
import scrape2 as sc

auth = tp.OAuth1UserHandler(consumer_key=dta.API_Key, consumer_secret=dta.API_Key_Secret)   
auth.set_access_token(dta.access_token,dta.access_token_secret)
API=tp.API(auth,retry_delay=2,retry_count=2)

def Fashion(name="Fashion"):        
    fashion_keywords=["#apparel" ,"#clothes" ,"#clothing" ,"#clothingbrand", "#clothingstyle" ,"#design","#fashion" ,"#fashionstyle","#instafashion" ,"#lifestyle" ,"#mensfashion" ,"#model" ,"#outfit" ,"#streetstyle" ,"#streetwear" ,"#style" ,"#tshirt","#Jackets","#handbags"]
    fashion_tweet=[]
    count=0
    date_since="2022-04--01"
    for fashion in fashion_keywords:
        tweets_fashion = tp.Cursor(API.search_tweets,fashion,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_fashion:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                        # if h not in fashion_keywords:
                        #     fashion_keywords.append(h)
                        # else:
                        #     fashion_keywords
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
                # tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                # #     # Get direct video link
                # if(len(tweet_media) == 0):
                #     line['video_url']=tweet_media
            except Exception as e:
                print(str(e))
            except StopIteration:
                print("Error occured !!")
                break
            try:
                if trend_score>=2:
                    fashion_tweet.append(line)
                else:
                    print("Tweet rejected since very less popular")
            except:
                fashion_tweet.append(line)
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new_fashion_tweet=sc.sort__(fashion_tweet,'trend_score')
    sc.write_json_file(new_fashion_tweet,f"{name}")


def electronics(name="Electronics"):
    Electronics_keywords=["#phone","#computers","#android","#cell","#tech","#innovation","tablets","#Deals","#watch"]
    Electronics_tweet=[]
    count=0
    date_since="2022-04--01"
    for electronic in Electronics_keywords:
        tweets_electronics = tp.Cursor(API.search_tweets,electronic,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_electronics:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                        # if h not in fashion_keywords:
                        #     fashion_keywords.append(h)
                        # else:
                        #     fashion_keywords
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
                # tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                # #     # Get direct video link
                # if(len(tweet_media) == 0):
                #     line['video_url']=tweet_media
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            try:
                if trend_score >=2:
                    Electronics_tweet.append(line)
                else:
                    print("Tweet rejected since very less popular")
            except:
                Electronics_tweet.append(line)
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new_Electronics_tweet=sc.sort__(Electronics_tweet,'trend_score')
    sc.write_json_file(new_Electronics_tweet,f"{name}")



def home_Funiture(name='Home_And_Furniture'):
    Home_Funiture_keywords=["#art","#artist","#wallpaper","#flowers","#summer","#home","#beach","#homedecor","#luxury","#property","#Rumah","#lamps","#tea","#coffee","#mugs","#gifts","#giftideas","#design","#homedesign"]
    Home_Funiture_tweet=[]
    count=0
    date_since="2022-04--01"
    for Home_Funiture in Home_Funiture_keywords:
        tweets_Home_Funiture = tp.Cursor(API.search_tweets,Home_Funiture,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_Home_Funiture:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                        # if h not in fashion_keywords:
                        #     fashion_keywords.append(h)
                        # else:
                        #     fashion_keywords
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
                # tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                # #     # Get direct video link
                # if(len(tweet_media) == 0):
                #     line['video_url']=tweet_media
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            try:
                if trend_score >=2:
                    Home_Funiture_tweet.append(line)
                else:
                    print("Tweet rejected since very less popular")    
            except:
                Home_Funiture_tweet.append(line)
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new_Home_Funiture_tweet=sc.sort__(Home_Funiture_tweet,'trend_score')
    sc.write_json_file(new_Home_Funiture_tweet,f"{name}")

def sports_More(name='Sports_And_MoRE'):
    Sports_More_keywords=["#workness","#fitness","#health","#diet","#yoga","#gym","#weightloss","#training","#fit","#tennis","#cricket","#badminton","#squash","#NowPlaying","#shuttles","#skateboard","#skater","#skate","#camping","#travel","#outdoors","#vlog","#pool","#swimwear","#swim"]
    Sports_More_tweet=[]
    count=0
    date_since="2022-04--01"
    for Sports_More in Sports_More_keywords:
        tweets_Sports_More = tp.Cursor(API.search_tweets,Sports_More,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(60)
        tweet_count=0
        for tweet in tweets_Sports_More:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                        # if h not in fashion_keywords:
                        #     fashion_keywords.append(h)
                        # else:
                        #     fashion_keywords
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
                # tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                # #     # Get direct video link
                # if(len(tweet_media) == 0):
                #     line['video_url']=tweet_media
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score >=2:
                Sports_More_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new_Sports_More_tweet=sc.sort__(Sports_More_tweet,'trend_score')
    sc.write_json_file(new_Sports_More_tweet,f"{name}")

def kids_Babies(name="Kids_And_toys"):
    kids_babies_keywords=["#cutebaby","#games","#Marvel","#kids","#toys","#kindergarden","#newborn","#schools"]
    kids_babies_tweet=[]
    count=0
    date_since="2022-04--01"
    for kids_babies in kids_babies_keywords:
        tweets_kids_babies = tp.Cursor(API.search_tweets,kids_babies,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(75)
        tweet_count=0
        for tweet in tweets_kids_babies:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                        # if h not in fashion_keywords:
                        #     fashion_keywords.append(h)
                        # else:
                        #     fashion_keywords
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
                # tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                # #     # Get direct video link
                # if(len(tweet_media) == 0):
                #     line['video_url']=tweet_media
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score>=2:
                kids_babies_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new_kids_babies_tweet=sc.sort__(kids_babies_tweet,'trend_score')
    sc.write_json_file(new_kids_babies_tweet,f"{name}")

def beauTy(name="Skincare_And_Beauty"):
    beauty_keywords=["#makeup","#glamour","#cosmetics","#lips","#eyeshadow","#model","#skincare","#checkitout","#instamakeup","#dental"]
    beauty_tweet=[]
    count=0
    date_since="2022-04--01"
    for beauty in beauty_keywords:
        tweets_beauty = tp.Cursor(API.search_tweets,beauty,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(75)
        tweet_count=0
        for tweet in tweets_beauty:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                        # if h not in fashion_keywords:
                        #     fashion_keywords.append(h)
                        # else:
                        #     fashion_keywords
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
                # tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                # #     # Get direct video link
                # if(len(tweet_media) == 0):
                #     line['video_url']=tweet_media
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score>=2:
                beauty_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new_beauty_tweet=sc.sort__(beauty_tweet,'trend_score')
    sc.write_json_file(new_beauty_tweet,f"{name}")

def books_Stationaries(name="Books_AND_Stationaries"):
    books_stationaries_keywords=["#book","#fantasy","#reading","#Amazon","#amreading","#authors","#bookworm","#Kindle","#books","#writing","#read","#chemistry","#poetry","#Statistics","#Nursing","#biology","#English","#Pens","#pencil","#comics"]
    books_stationaries_tweet=[]
    count=0
    date_since="2022-04--01"
    for books_stationaries in books_stationaries_keywords:
        tweets_books_stationaries = tp.Cursor(API.search_tweets,books_stationaries,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_books_stationaries:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                        # if h not in fashion_keywords:
                        #     fashion_keywords.append(h)
                        # else:
                        #     fashion_keywords
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
                # tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                # #     # Get direct video link
                # if(len(tweet_media) == 0):
                #     line['video_url']=tweet_media
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score>=2:
                books_stationaries_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new_books_stationaries_tweet=sc.sort__(books_stationaries_tweet,'trend_score')
    sc.write_json_file(new_books_stationaries_tweet,f"{name}")


def top_trends(name='Top_Trends'):
    trend_result=API.get_place_trends(dta.i_woeid)
    list=[]
    try:
        for trend in trend_result[0]["trends"]:
            a= trend['name']
            # write_json(trends)
            list.append(a)
    except:                                          
        print("Somethng went wrong")
    trending_keywords=list
    trending_tweet=[]
    count=0
    date_since="2022-04--01"
    for tre in trending_keywords:
        tweets_ = tp.Cursor(API.search_tweets,tre,since_id=date_since,tweet_mode='extended', lang='en',include_entities=True).items(15)
        tweet_count=0
        for tweet in tweets_:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                    else:
                        line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                else:
                    line=line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':"null"}
                
                # Access video info
            #     tweet_media = tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
            #     #     # Get direct video link
            #     if(len(tweet_media) != 0):
            #         line['video_url']=tweet_media

            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score>=2:
                trending_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets :=> {count}")
    new__tweet=sc.sort__(trending_tweet,'trend_score')
    sc.write_json_file(new__tweet,f"{name}")


