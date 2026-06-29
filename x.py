import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("churn.csv")



from sqlalchemy import create_engine
engine=create_engine('sqlite:///churn.db',echo=False)

df.to_sql(name="exp",con=engine,if_exists="replace")



df.to_sql(name="customers1",con=engine,if_exists="replace",index=False)

r=pd.read_sql("select *from customers1 limit 5",con=engine)
print(r)

r1=pd.read_sql('''select churn, count(*) from customers1 group by Churn''',con=engine)
print(r1)


r2=pd.read_sql('''select churn,avg(MonthlyCharges) as average_charges from customers1 group by Churn''',con=engine)
print(r2)

r3 = pd.read_sql("SELECT Contract, Churn, COUNT(*) FROM customers1 GROUP BY Contract, Churn", con=engine)
print(r3)

r4= pd.read_sql("select churn,avg(tenure) from customers1 group by churn",con=engine)
print(r4)

r5= pd.read_sql("select count(*) from customers1 group by Churn",con=engine)
 




'''
sns.countplot(x="Contract",hue="Churn",data=df)
plt.show()
plt.figure()

sns.histplot(x="tenure",hue="Churn",data=df)
plt.show()

plt.figure()
sns.boxplot(x="Churn",y="MonthlyCharges",data=df)
plt.show()

plt.figure()
sns.countplot(x="InternetService",hue="Churn",data=df)
plt.show()
'''


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()
print(df.isnull().sum())
print(df.dtypes)


df=df.drop("customerID",axis=1)


for col in df.select_dtypes(include='object').columns:
    print(col, df[col].unique())

df["gender"]=df["gender"].map({'Female':0,'Male':1})
df["Partner"]=df["Partner"].map({'Yes':0,'No':1})
df["Dependents"]=df["Dependents"].map({'Yes':0,'No':1})
df["PhoneService"]=df["PhoneService"].map({'Yes':0,'No':1})
df["PaperlessBilling"]=df["PaperlessBilling"].map({'Yes':0,'No':1})
df["Churn"]=df["Churn"].map({'Yes':1,'No':0})


df=pd.get_dummies(df,drop_first=True,columns=["MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaymentMethod"])
print(df.columns)
print(df.shape)

x=df.drop('Churn',axis=1)
y=df['Churn']

print(x.shape)
print(y.shape)

from sklearn.preprocessing import StandardScaler
scale=StandardScaler()
x[['tenure', 'MonthlyCharges', 'TotalCharges']] = scale.fit_transform(x[['tenure', 'MonthlyCharges', 'TotalCharges']])

print(x[['tenure', 'MonthlyCharges', 'TotalCharges']].head())

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=104,shuffle=True,train_size=0.8)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LogisticRegression

reg=LogisticRegression()
reg.fit(x_train,y_train)

y_pred=reg.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier

re=RandomForestClassifier(class_weight='balanced')
re.fit(x_train,y_train)
y_pre=re.predict(x_test)

print(accuracy_score(y_pre,y_test))

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pre))
print(confusion_matrix(y_test, y_pre))

from sklearn.model_selection import GridSearchCV
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [5, 10, None],
    'min_samples_leaf': [1, 2, 4]
}

clf = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_grid, cv=5, scoring="recall")
clf.fit(x_train,y_train)
print(clf.best_params_)
print(clf.best_score_)

best_rf = RandomForestClassifier(max_depth=10, min_samples_leaf=1, n_estimators=100, class_weight='balanced')
best_rf.fit(x_train, y_train)
y_pred_best = best_rf.predict(x_test)
print(classification_report(y_test, y_pred_best))

import joblib
joblib.dump(best_rf,'best_rf.pkl')
joblib.dump(scale, 'scaler.pkl')

'''print(x.columns.tolist())'''

'''from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=42)
x_train_sm, y_train_sm = sm.fit_resample(x_train, y_train)

from xgboost import XGBClassifier
xg=XGBClassifier()
xg.fit(x_train_sm, y_train_sm)
y_pred_xg = xg.predict(x_test)
print(classification_report(y_test, y_pred_xg))'''

pd.read_sql("SELECT * FROM predictions_log", con=engine)