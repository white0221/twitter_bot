import tweepy
import datetime
 
CK=""
CS=""
AT=""
AS=""
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
 
api = tweepy.API(auth)
 
class Listener(tweepy.StreamListener):
  print("コンストラクタの生成")

  def on_status(self, status):
	# リプライが来たら返信
    if (status.in_reply_to_screen_name) == api.me().screen_name:
      status_id = status.id
      tweet = "リプありがとう！自動返信しているよ"
      tweet_rep = "@" + str(status.user.screen_name) + " " + str(tweet)
      api.update_status(status=tweet_rep,in_reply_to_status_id=status_id)
      print("リプライしました: "+ tweet_rep)
      return True

  def on_error(self, status_code):
    print('Got an error with status code: ' + str(status_code))
    return True

  def on_timeout(self):
    print('Timeout...')
    return True
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
 
listener = Listener()
print("コンストラクタ生成完了")
stream = tweepy.Stream(auth, listener)
stream.userstream()

