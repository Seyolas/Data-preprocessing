import pandas as pd


df=pd.read_csv("USvideos.csv")

ilk5=df.head(5)
print(ilk5)

df.drop(["thumbnail_link","video_id","trending_date","publish_time","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1,inplace=True)
print(df)

satirSayisi=len(df.index)
print(satirSayisi)

sütunSayisi=len(df.columns)
print(sütunSayisi)

LikesOrt=df["likes"].mean()
print(LikesOrt)

DisLikesOrt=df["dislikes"].mean()
print(DisLikesOrt)

EnYüksekGörüntülenme=df["views"].max()
print(EnYüksekGörüntülenme)

EnYüksekGörüntülenmeyeSahipBaşlık=df[df["views"]==EnYüksekGörüntülenme]["title"].iloc[0]
print(EnYüksekGörüntülenmeyeSahipBaşlık)

EnDüşükGörüntülenme=df["views"].min()
print(EnDüşükGörüntülenme)

EnDüşükGörüntülenmeyeSahipBaşlık=df[df["views"]==EnDüşükGörüntülenme]["title"].iloc[0]
print(EnDüşükGörüntülenmeyeSahipBaşlık)

KategoriyeGöreYorumSayısı=df.groupby("category_id").mean()["comment_count"]
print(KategoriyeGöreYorumSayısı)

KategorilerdeKaçAdetVideo=df["category_id"].value_counts()
print(KategorilerdeKaçAdetVideo)

df["title_length"]=df["title"].apply(len)
print(df)


def countTag(tag):
    tagList=tag.split("|")
    return len(tagList)

df["tag_count"]=df["tags"].apply(countTag)
print(df)

print(df.sort_values("likes",ascending=True))

df["oran"] =df["likes"]/(df["likes"]+df["dislikes"])

df.fillna(0,inplace=True)

df.sort_values(by=["oran"],ascending=False)
print(df)