from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sola = SentimentIntensityAnalyzer()

sentence = input("Sentence: ")

score = sola.polarity_scores(sentence)["compound"]
print(f'The sentiment value of the sentence :"{sentence}" is : {score}')

polarity = sola.polarity_scores(sentence)
pos = polarity["pos"]
neu = polarity["neu"]
neg = polarity["neg"]
print("="*50)
print(f'The percententage of positive sentiment in :"{sentence}" is : {round(pos*100,2)} %')
print(f'The percententage of neutral sentiment in :"{sentence}" is : {round(neu*100,2)} %')
print(f'The percententage of negative sentiment in :"{sentence}" is : {round(neg*100,2)} %')
print("="*50)