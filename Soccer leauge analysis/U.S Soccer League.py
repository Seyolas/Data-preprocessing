import pandas as pd

df=pd.read_csv("mls-salaries-2017.csv")
print(df)

first10Value=df.head(10)
print(first10Value)

toplamSatir=len(df.index)
print(toplamSatir)

MaaşOrt=df["base_salary"].mean()
print(MaaşOrt)

EnYüksekMaaş=df["base_salary"].max()
print(EnYüksekMaaş)

EnYüksekTazminat=df["guaranteed_compensation"].max()
print(EnYüksekTazminat)

print(df[df["guaranteed_compensation"]==EnYüksekTazminat]["last_name"].iloc[0])

Gonzalez=df[df["last_name"]=="Gonzalez Pirez"]
print(Gonzalez)

GonzalezMevkii=df[df["last_name"]=="Gonzalez Pirez"]["position"].iloc[0]
print(GonzalezMevkii)

MevkiiGrupla=df.groupby("position").mean()
print(MevkiiGrupla)

KaçFarklıMevkii=df["position"].nunique()
print(KaçFarklıMevkii)

HerMevkiideKaçOyuncu=(df["position"].value_counts())
print(HerMevkiideKaçOyuncu)

HerTakımdaKaçOyuncu=df["club"].value_counts()
print(HerTakımdaKaçOyuncu)

def son_find(last_name):
    if "son" in last_name.lower():
        return True
    return False

print(df[df["last_name"].apply(son_find)])
