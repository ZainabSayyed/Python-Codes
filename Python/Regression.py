import pandas as pd
import quandl
import math
import datetime
import calendar
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
style.use('ggplot')

df=quandl.get("WIKI/GOOGL", authtoken="4pvJWW528cuqpH4aqCvx")
#we are not interested in all features so just read relevant fetaure.
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
print(df.head())
#the relation between open and close , high and low is very important but
#regression will not find by itself , so calulcate those features to feed into 
#regression algorithm
#Caluclate %change between high and low, create new column 'HL_PCT' and store in it.
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.0
df['PCT_Change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.0
df=df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]
forecast_col='Adj. Close'
df.fillna(-99999,inplace=True)
forecast_out=int(math.ceil(0.01*len(df)))
print(df.tail())

df['label']=df[forecast_col].shift(-forecast_out)
X=np.array(df.drop(['label'],1))
X=preprocessing.scale(X)
X=X[:-forecast_out]
X_lately=X[-forecast_out:]
df.dropna(inplace=True)
#print(df.head())
#X=X[:-forecast_out+1]
#df.dropna(inplace=True)
y=np.array(df['label'])
#print (len (X),len (y))
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)
clf=LinearRegression(n_jobs=-1)
clf.fit(X_train,y_train)
with open('linearregression.pickle','wb') as f:
    pickle.dump(clf,f)
    
pickle_in=open('linearregression.pickle','rb')
clf=pickle.load(pickle_in)

accuracy= clf.score(X_test,y_test)
#print(accuracy)
#Just for Testing try different algorithms, SVM default is linear
#clf=svm.SVR()
#clf.fit(X_train,y_train)
#accuracy= clf.score(X_test,y_test)
#print(accuracy)
# Try svm with Kernel Polynomial
#Just for Testing try different algorithms, SVM default is linear
forecast_set=clf.predict(X_lately)
#clf=svm.SVR(kernel='poly')
#clf.fit(X_train,y_train)
#accuracy= clf.score(X_test,y_test)
print(forecast_set,accuracy,forecast_out)
#Accuracy is not improving hence will stick to linear regression.
#print(-forecast_out)
df['Forecast']=np.nan
last_date=df.iloc[-1].name
last_unix=last_date.utctimetuple()
#datetime.strptime(last_date, "%B %d, %Y")
one_day=86400
next_unix=calendar.timegm(last_unix)+one_day
for i in forecast_set:
    next_date=datetime.date.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]=[np.nan for i in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
