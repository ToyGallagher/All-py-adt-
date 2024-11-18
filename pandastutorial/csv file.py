import pandas as pd
name=["คีย์บอร์ด","เมาส์","ตุ้กตา"]
category=["อุปกรณ์คอม","อุปกรณ์คอม","ของเล่น"]
price = [500,300,900]

nameseries = pd.Series(name)
categoryseries = pd.Series(category)
priceseries = pd.Series(price)

all = {"ชื่อสินค้า":nameseries,"หมวดหมู่":categoryseries,"ราคา":priceseries}
df = pd.DataFrame(all)
df.set_index(["ชื่อสินค้า"],inplace=True)
print(df)
df.to_csv("products.csv")

    
