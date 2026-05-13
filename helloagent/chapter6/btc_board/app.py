import streamlit as st
import requests
import datetime
from streamlit_autorefresh import st_autorefresh

# -------------------- 页面配置 --------------------
st.set_page_config(
    page_title="比特币价格看板",
    page_icon="🪙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------- 会话状态初始化 --------------------
if 'btc_data' not in st.session_state:
    st.session_state.btc_data = None         # 存储上一次成功的数据（字典）
if 'last_update' not in st.session_state:
    st.session_state.last_update = None       # 上次更新时间
if 'error' not in st.session_state:
    st.session_state.error = None             # 错误消息
if 'manual_refresh' not in st.session_state:
    st.session_state.manual_refresh = False   # 手动刷新标志

# -------------------- 自动刷新（每60秒） --------------------
st_autorefresh(interval=60000, key="auto_refresh")

# -------------------- 手动刷新按钮 --------------------
col1, col2 = st.columns([1, 8])
with col1:
    if st.button("🔄 刷新", help="手动获取最新价格"):
        st.session_state.manual_refresh = True
        st.rerun()

# -------------------- 数据获取函数 --------------------
def fetch_bitcoin_data():
    """调用 CoinGecko 接口获取比特币当前价格、24h涨跌额、24h涨跌幅"""
    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        "?vs_currency=usd"
        "&ids=bitcoin"
        "&order=market_cap_desc"
        "&per_page=1"
        "&page=1"
        "&sparkline=false"
        "&price_change_percentage=24h"
    )
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            raise ValueError("API 返回空数据")
        item = data[0]
        return (
            item['current_price'],
            item['price_change_24h'],
            item['price_change_percentage_24h'],
            None  # 无错误
        )
    except Exception as e:
        return None, None, None, str(e)

# -------------------- 加载与数据更新逻辑 --------------------
if st.session_state.manual_refresh:
    # 手动刷新：显示 spinner 并获取数据
    with st.spinner("正在获取最新价格..."):
        price, change_amount, change_percent, error = fetch_bitcoin_data()
        st.session_state.manual_refresh = False
else:
    # 自动刷新或首次加载：不显示 spinner
    price, change_amount, change_percent, error = fetch_bitcoin_data()

# 错误处理：若获取失败，使用旧数据并提示用户
if error:
    st.session_state.error = error
    if st.session_state.btc_data is not None:
        price = st.session_state.btc_data['price']
        change_amount = st.session_state.btc_data['change_amount']
        change_percent = st.session_state.btc_data['change_percent']
        st.warning(f"⚠️ 数据获取失败: {error}，显示上次缓存数据")
    else:
        st.error(f"❌ 无法获取比特币价格: {error}")
        st.stop()  # 没有旧数据时停止渲染
else:
    # 成功：更新会话状态
    st.session_state.btc_data = {
        'price': price,
        'change_amount': change_amount,
        'change_percent': change_percent
    }
    st.session_state.last_update = datetime.datetime.now()
    st.session_state.error = None

# -------------------- UI 展示 --------------------
st.markdown("# 🪙 比特币价格看板")

# 当前价格（大号、加粗）
st.markdown(
    f"<h1 style='text-align: center; font-size: 60px;'>${price:,.2f}</h1>",
    unsafe_allow_html=True
)

# 24h 涨跌额与涨跌幅并排显示
col_a, col_b, col_c = st.columns(3)
with col_a:
    delta_amount = f"+${change_amount:,.2f}" if change_amount >= 0 else f"-${abs(change_amount):,.2f}"
    delta_amount_color = "green" if change_amount >= 0 else "red"
    st.markdown(
        f"<h5 style='text-align: center;'>24h 涨跌额</h5>"
        f"<h3 style='text-align: center; color: {delta_amount_color};'>{delta_amount}</h3>",
        unsafe_allow_html=True
    )

with col_b:
    delta_percent = f"+{change_percent:.2f}%" if change_percent >= 0 else f"{change_percent:.2f}%"
    delta_percent_color = "green" if change_percent >= 0 else "red"
    st.markdown(
        f"<h5 style='text-align: center;'>24h 涨跌幅</h5>"
        f"<h3 style='text-align: center; color: {delta_percent_color};'>{delta_percent}</h3>",
        unsafe_allow_html=True
    )

with col_c:
    if st.session_state.last_update:
        update_time = st.session_state.last_update.strftime("%Y-%m-%d %H:%M:%S")
        st.markdown(
            f"<h5 style='text-align: center;'>最近更新</h5>"
            f"<h5 style='text-align: center; color: gray;'>{update_time}</h5>",
            unsafe_allow_html=True
        )

# 底部说明
st.caption("数据来源：CoinGecko（免费 API） | 自动刷新：每 60 秒")