import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
all_data=pd.read_csv("Bütün_aylar.csv")

# Cleaning Data...
nandf=all_data[all_data.isna().any(axis=1)] # NAN olan sütunları görmek...

all_data["Month"]=all_data["Order Date"].str[0:2] #Month kolonuna order date'in ilk 2 değerini ata
all_data=all_data.dropna(how="all")               #NAN olan bütün satırları sil

all_data=all_data[all_data["Order Date"].str[0:2]!="Or"]

all_data["Month"]=all_data["Order Date"].str[0:2]
all_data["Month"]=all_data["Month"].astype("int32")

all_data["Quantity Ordered"]=pd.to_numeric(all_data["Quantity Ordered"]) # miktarı inte çevirdik
all_data["Price Each"]=pd.to_numeric(all_data["Price Each"])       # price eachı inte çevirdik



# Question1: What was the best month for sales ? how much was earned that month ?

all_data["Sales"]=all_data["Quantity Ordered"]*all_data["Price Each"]

result=all_data.groupby("Month").sum()

aylar=range(1,13)

plt.bar(aylar,result["Sales"])
plt.xticks(aylar)
plt.xlabel("Month number")
plt.ylabel("Sales in USD $")
plt.show()

#Question2 : Which city had the highest number of sales ?


def hesapla(adres):
    list=adres.split(",")
    return list[1]

all_data["City"]=all_data["Purchase Address"].apply(hesapla)

result2=all_data.groupby("City").sum()

şehirler=[şehirler for şehirler,df in all_data.groupby("City")]

plt.bar(şehirler,result2["Sales"])
plt.xticks(şehirler,rotation="vertical",size=8)
plt.xlabel("City name")
plt.ylabel("Sales in USD $")
plt.show()

#Question 3 What time should we display advertisement to maximize likelihood of customer's buying product ?


all_data["Order Date"]=pd.to_datetime(all_data["Order Date"])

all_data["Hour"]=all_data["Order Date"].dt.hour
all_data["Minute"]=all_data["Order Date"].dt.minute



times=[times for times,df in all_data.groupby("Hour")]

plt.plot(times,all_data.groupby("Hour").count())
plt.xticks(times)
plt.xlabel("Hour")
plt.ylabel("Number of orders")
plt.grid()
plt.show()

#Question 4 : What products are most often sold together ?

product_group=all_data.groupby("Product")

quantity_ordered=product_group.sum()["Quantity Ordered"]

product=[product for product, df in product_group]
plt.bar(product,quantity_ordered)
plt.xticks(product,rotation="vertical",size=7)
plt.show()