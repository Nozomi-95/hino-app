import streamlit as st
import random as rd
import streamlit as st

options = ["林", "森", "森木", "森林","樹木","希林","木森","森樹"]

if "default" not in st.session_state:
    st.session_state.default = []

if st.button("全選択"):
    st.session_state.default = options

with st.form("form"):

    selected = st.multiselect(
        "選択してください",
        options,
        default=st.session_state.default
    )

    text = st.text_input("数字をカンマ区切りで入力")

    ok = st.form_submit_button("OK")

if ok:
    nums = [int(x.strip()) for x in text.split(",") if x.strip() != ""]

    st.write(nums)
    st.write(selected)
    st.write(len(selected), "人")

    if len(selected) != sum(nums):
        st.write("人数が合わない")

    rd.shuffle(selected)

    for i in nums:
        st.write(" ".join(selected[:i]))
        del selected[:i]