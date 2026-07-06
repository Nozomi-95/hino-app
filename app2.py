import streamlit as st
import random as rd
import streamlit as st

options = [ '薮野', '金松', '大塚', '森岡', '田中', 
            '河本', '城内', '林黎', '林隆太', '内泉', 
            '重住', '松本', '稻船', '近藤', '高見', 
            '塩貝', '神村', '城戸', '高倉', '堤', 
            '瀬口', '出尾', '新熊', '小段', '越智',
            '廣津', '南浦', '奥野', '宮本', '長内',
            '寺中', '松元', '門脇', '竹田', '阿久津', 
            '喜多', '森本', '松石', '平野', '廣澤', 
            '上村', '打谷', '水野', '江口', '小西', 
            '市原', '竹本', '浅山', '小笠原', '當宮',
            '永井', '友部']

if "default" not in st.session_state:
    st.session_state.default = []

if st.button("全選択"):
    st.session_state.default = options

with st.form("form"):

    selected = st.multiselect(
        "なまえ",
        options,
        default=st.session_state.default
    )
    text = st.text_input("すうじ(カンマ区切り)")

    ok = st.form_submit_button("OK")

if ok:
    nums = [int(x.strip()) for x in text.split(",") if x.strip() != ""]

    st.write(len(selected), "人")

    if len(selected) != sum(nums):
        st.write("人数が合わない")

    rd.shuffle(selected)

    for i in nums:
        st.write(" ".join(selected[:i]))
        del selected[:i]