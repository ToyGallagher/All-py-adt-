import pandas as pd
import numpy as np

df = pd.read_csv("result_20220202_202330.csv",encoding = "utf-8")
df = df.drop(df[df.VOTED == 1].index)

print(df)
df.to_csv("รายชือคนที่ไม่ใช้สิทธ์ ม.1และ3.csv")






