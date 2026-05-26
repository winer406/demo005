import streamlit as st
import pandas as pd
import yfinance as yf
import json

st.title("Sample App:koala:")
st.title("這是一個sample app的應用程式")
st.title("這是一個sample app的應用程式", anchor="sample")


st.header("Header")
st.subheader("Subheader")

st.text("Text")

python_code = """
def hello():
    print("Hello, Streamlit!")
"""

st.code(python_code, language="python")

st.code(python_code, language="none", line_numbers=True)


st.caption("Caption: This is a sample caption for the app.")
st.caption("<center>Caption: This is a sample caption for the app.</center>", unsafe_allow_html=True)

data = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})

st.dataframe(data)

data = {
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8]
}

index = pd.Index(["a", "b", "c", "d"], name="index")

data2 = pd.DataFrame(data, index=index)

st.caption("這是用st.dataframe顯示的表格")
st.dataframe(data2)

st.caption("這是用st.table顯示的表格")
st.table(data2)

st.caption("這是用st.metric")
st.metric(label="溫度", value="25 °C", delta="1.2 °C")

stock_list = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 'TSM']
for ticker in stock_list:
    try:
        stock = yf.Ticker(ticker)

        # 取得即時價格
        todays_data = stock.history(period="5d")  # 最近兩天
        current_price = todays_data["Close"].iloc[-1]
        prev_close = todays_data["Close"].iloc[-2]

        # 計算漲跌幅
        change = current_price - prev_close
        pct_change = (change / prev_close) * 100

        # 顯示股價 + 漲跌幅
        st.metric(
            label=f"{ticker} 最新股價",
            value=f"{current_price:.2f} USD",
            delta=f"{change:+.2f} ({pct_change:+.2f}%)",
            delta_color="normal"  # 使用預設顏色
        )

    except Exception as e:
        st.error(f"取得股價資料失敗: {e}")

st.json(
    {
        "Name": "Streamlit",
        "Type": "Framework",
        "Language": "Python"
    },
    expanded=True
) 

with open("abc.json", "r") as f:
    my_data = json.load(f)

search=st.text_input("Search in JSON", "")
if search:
    # 搜尋 JSON 結構
    if search in my_data:
        st.success(f"Found: {search} -> {my_data[search]}")
    else:
        st.error(f"{search} not found in JSON")
# 顯示 JSON 結構 
    
st.json(my_data, expanded=True) 