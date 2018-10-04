import pandas as pd
import p1
p1.wfile()


dataset = pd.read_csv('cdoc.txt', header = None,sep=" ", delimiter="\n")

import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
review=[]
for i in range(0, 1):
    review = re.sub('[^a-zA-Z]', ' ', dataset[0][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)

f= open("ndoc.txt","w")
f.write(review)
print(review)