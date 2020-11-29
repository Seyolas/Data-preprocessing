import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#cleaning data...

data=pd.read_csv("datasets_27_792993_timesData.csv")
data.drop(["female_male_ratio","student_staff_ratio"],axis=1,inplace=True)

data=data[data["total_score"]!="-"]

#data=data.dropna(how="all")

data["total_score"]=pd.to_numeric(data["total_score"])


# what is the best 10 university in 2016?

print(data[(data["total_score"]>=82) & (data["year"] ==2016)].head(20))

# what is the best 10 university in 2014?
print(data[(data["total_score"]>=70) & (data["year"] ==2014)].head(10))


# what is the most succesful countries ?

plt.style.use("ggplot")
ülkeler = data['country'].value_counts().keys().tolist()
counts = data['country'].value_counts().tolist()
plt.figure(figsize=(10,9))
plt.xlabel("Countries")
plt.ylabel("Number of universities",weight="bold")
plt.title("Most succesful countries in all years",weight="bold")
plt.bar(ülkeler,counts)
plt.xticks(ülkeler,rotation="vertical",size=8,weight='bold')
plt.show()


# what is the number of students best 20 universities in 2016  ?

best=data[(data["total_score"]>=82) & (data["year"] ==2016)].head(20)

num_student=best["num_students"].tolist()
dizi=[]
for i in num_student:
    i=i.replace(",","")
    i=int(i)
    dizi.append(i)

liste=best["university_name"].tolist()
plt.bar(liste,dizi)
plt.show()

#Which Turkish universities are in the ranking?

print(data[data["country"]=="Turkey"])

#The relationship between the number of international students and the total score
