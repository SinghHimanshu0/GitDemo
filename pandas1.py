import pandas as pd




# Different ways to create df:
# 1-read_csv---->df=pd.read_csv('/Users/himanshusingh/Documents/Pandas/weather.csv')
# 2-read_excel---->df=pd.read_csv('/Users/himanshusingh/Documents/Pandas/weather.xlsx','Sheet1')
# 3-using dict------>df=pd.DataFrame(student)
# 4-using tuple








# df=pd.read_csv('/Users/himanshusingh/Documents/Pandas/weather.csv')
# print(df)





# 3a-using dict------>df=pd.DataFrame(student)
student={
    'Name':['Himanshu','Kushagra','Akshat','Shubham','Shivam'],
    'score':['100','90','90','95','88'],
    'Location':['PRYJ','PRYJ','PRYJ','CHG','CHG']
}

df=pd.DataFrame(student )
g=df.groupby('Location')
# print(g)
# for a,b in g:
#     print(a)
#     print(b)


# print(g.get_group('PRYJ'))
print(g.min()['score'].loc['CHG'])










# 3b-using dict------>df=pd.DataFrame(student)
# student=[
#     {'Name':'Himanshu','Subject':'CSE','Location':'PRYJ'},
#      {'Name':'Kushagra','Subject':'LAW','Location':'PRYJ'},
#       {'Name':'Akshat','Subject':'CSE','Location':'PRYJ'},
#        {'Name':'Shubham','Subject':'CSE','Location':'CHG'}]

# df=pd.DataFrame(student)
# print(df)

# print()



# 4-using tuple
# weather_data=[
#     ('1/1/2017',32,6,'Rain'),
#     ('2/1/2017',28,8,'Sunny'),
#     ('3/1/2017',31,9,'Rain'),
#     ('4/1/2017',37,4,'Sunny')
# ]
# df=pd.DataFrame(weather_data,columns=['Date','Temp','Windspeed','Event'])
# print(df)
