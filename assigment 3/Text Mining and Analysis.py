from twython import Twython
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Replace the following strings with your own keys and secrets
TOKEN = '722625872432349185-toIl982dbBsRttXHf8UfkUPVCk1NE2t'
TOKEN_SECRET = 'cN2dDApVIIQ31EFnIjKf5ZDkYsvcVJUSnrxfqX60MSnAG'
CONSUMER_KEY = '5A6Ai4gPH4o90mIGxzXENitbe'
CONSUMER_SECRET = 'vPnYWkR4JqCAdVEor13VF12AeJEJaF5SQRGOe7LGTSe7bjIiaM'

t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="dollar tree", count=2500)
data1 = t.search(q="family dollar", count=2500)
data2 = t.search(q= "dollar general", count =5000)
dollartree = 0
dollartreepos = 0
dollartreeneg = 0
dollargeneral = 0
dollargeneralpos = 0
dollargeneralneg = 0
familydollar = 0
familydollarpos = 0
familydollarneg = 0



for status in data['statuses']:
    score = SentimentIntensityAnalyzer().polarity_scores(status['text'])
    dollartree += score['compound']
    dollartreepos += score['pos']
    dollartreeneg += score['neg']

for status in data1['statuses']:
    score = SentimentIntensityAnalyzer().polarity_scores(status['text'])
    familydollar += score['compound']
    familydollarpos += score['pos']
    familydollarneg += score['neg']

for status in data2['statuses']:
    score = SentimentIntensityAnalyzer().polarity_scores(status['text'])
    dollargeneral += score['compound']
    dollargeneralpos += score['pos']
    dollargeneralneg += score['neg']


dollarsum = familydollar +dollartree
dollarsumpos = familydollarpos +dollartreepos
dollarsumneg = familydollarneg +dollartreeneg

print ('the Compound Score for Dollar Tree segment on Twitter for the most recent 5,000 twitt is {:2f}, pos: {:1f}, neg: {:01f}'.format(dollartree, dollartreepos, dollartreeneg))
print ('the Compound Score for Family Tree segment on Twitter for the most recent 5,000 twitt is {:2f}, pos: {:1f}, neg: {:01f}'.format(familydollar, familydollarpos, familydollarneg))
print ('the Compound Score for Dollar Tree, inc. on Twitter for the most recent 5,000 twitt is {:2f}, pos: {:1f}, neg: {:01f}'.format(dollarsum, dollarsumpos, dollarsumneg))
print ('the Compound Score for Dollar General,inc. on Twitter for the most recent 5,000 twitt is {:2f}, pos: {:1f}, neg: {:01f}'.format(dollargeneral, dollargeneralpos, dollargeneralneg))



# for status in data1['statuses']:
#      print(status['text'])


# # Save data to a file (will be part of your data fetching script)
# f = open('dickens_texts.pickle','w')
# pickle.dump(charles_dickens_texts,f)
# f.close()

# # Load data from a file (will be part of your data processing script)
# input_file = open('dickens_texts.pickle','r')
# reloaded_copy_of_texts = pickle.load(input_file)  

# Sample Use of sentiment analysis
# sentence = 'Software Design is my favorite class because learning Python is so cool!'
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)