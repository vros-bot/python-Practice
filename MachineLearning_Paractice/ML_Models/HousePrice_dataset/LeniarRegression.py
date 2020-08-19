import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lm

#Cleaning data
df = pd.read_csv('housePractice.csv')
df['date'] = pd.to_datetime(df.date)
df.head()

#Splitting Data into training and test
y=df['price']
x=df[['bedrooms', 'bathrooms', 'floors', 'sqft_living', 'sqft_lot', 'waterfront', 'view', 'condition','grade','sqft_above', 'sqft_basement', 'yr_built', 'sqft_living15', 'sqft_lot15']]
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2)

#Fitting into a linear regression model
model =lm()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
df1= pd.DataFrame({'Actual': y_test,
     'predicted': predictions,})

#Calculating test error
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

#Buliding a model for different splits
x1_train,x1_test,y1_train,y1_test =train_test_split(x,y,test_size=0.3)
model =lm()
model.fit(x1_train,y1_train)
predictions=model.predict(x1_test)
r_sq = model.score(x, y)
print('test error when data is split in 70-30 ratio',  r_sq)

x2_train,x2_test,y2_train,y2_test =train_test_split(x,y,test_size=0.4)
model =lm()
model.fit(x2_train,y2_train)
predictions=model.predict(x2_test)
r_sq = model.score(x, y)
print('test error when data is split in 60-40 ratio', r_sq)

x3_train,x3_test,y3_train,y3_test =train_test_split(x,y,test_size=0.1)
model =lm()
model.fit(x3_train,y3_train)
predictions=model.predict(x3_test)
r_sq = model.score(x, y)
print('test error when data is split in 90-10 ratio', r_sq)

#Finiding colinear variables
df1 = df[['id', 'date','bedrooms', 'bathrooms', 'floors', 'sqft_living', 'sqft_lot', 'waterfront', 'view', 'condition','grade','sqft_above', 'sqft_basement', 'yr_built', 'sqft_living15', 'sqft_lot15','zipcode','yr_renovated','lat','long']]
df2 = df1.corr()

#Finding 3 best predictors
y=df['price']
x=df[['condition', 'yr_built', 'sqft_living']]
x1_train,x1_test,y1_train,y1_test =train_test_split(x,y,test_size=0.2)
model =lm()
model.fit(x1_train,y1_train)
predictions=model.predict(x1_test)
r_sq = model.score(x, y)
print('test error1:' ,r_sq)

y=df['price']
x=df[['grade', 'yr_renovated', 'sqft_living']]
x1_train,x1_test,y1_train,y1_test =train_test_split(x,y,test_size=0.2)
model =lm()
model.fit(x1_train,y1_train)
predictions=model.predict(x1_test)
r_sq = model.score(x, y)
print('test error 2:', r_sq)

y=df['price']
x=df[['view', 'yr_built', 'sqft_living']]
x1_train,x1_test,y1_train,y1_test =train_test_split(x,y,test_size=0.2)
model =lm()
model.fit(x1_train,y1_train)
predictions=model.predict(x1_test)
r_sq = model.score(x, y)
print('test error3', r_sq)


#Building linear model using 3 predictors found in the previous step
y=df['price']
x=df[['grade', 'yr_built', 'sqft_living']]
x1_train,x1_test,y1_train,y1_test =train_test_split(x,y,test_size=0.2)
df2= x1_test.sample(100)
model =lm()
model.fit(x1_train,y1_train)
predictions=model.predict(df2)
r_sq = model.score(x, y)
print('test error when used 3 predictors', r_sq)
