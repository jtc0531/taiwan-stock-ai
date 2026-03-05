import streamlit as st
import pandas as pd
import requests

st.title("📈 AI 台股潛力飆股雷達")

st.write("正在抓取台股最新資料...")

# 台灣證交所 PER / 殖利率資料
url = "https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

# 數值轉換
df["PE"] = pd.to_numeric(df["PEratio"], errors="coerce")
df["Yield"] = pd.to_numeric(df["DividendYield"], errors="coerce")

# 篩選條件
filtered = df[
    (df["PE"] < 20) &
    (df["Yield"] > 3)
]

filtered = filtered.sort_values(by="Yield", ascending=False)

st.subheader("符合條件的股票")

st.dataframe(filtered[["Code", "Name", "PE", "Yield"]])