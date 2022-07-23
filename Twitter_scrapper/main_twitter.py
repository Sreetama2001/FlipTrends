import tweets
import time
# run script every 2 times a day
# Categories we have divided into are Fashion, Electronics, Home and Furniture, Beauty, Babies/Kids and Games, Books & Stationaries, Home and Furniture, Sports and more
tweets.books_Stationaries()
time.sleep(20*60)
tweets.electronics()
time.sleep(20*60)
tweets.home_Funiture()
time.sleep(20*60)
tweets.sports_More()
time.sleep(20*60)
tweets.beauTy()
time.sleep(20*60)
tweets.kids_Babies()                                    
time.sleep(20*60)
tweets.Fashion()
print("Execution Completed sucessfully!!")

