import tweepy
auth=tweepy.OAuthHandler('Xx4KwYcD9gblOs8UdYB8kIzRe','v6xyqHuZAVawglowBN1Q69MKd0Hpk9WBvaKBwckyGgb2itiPPa')
auth.set_access_token('1050916640005578753-edhFgvnvHCb90owGxovHdM1hyWu3ln','FyXs0mMFDr4VQWsbnFsLBHOpeD9qOU3dZtmhuKNSbfpdf' )
api=tweepy.API(auth)
x=input("Write your tweet:")
api.update_status(x)
print("Tweeted successfully")
