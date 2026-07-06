import streamlit as st
import random as rd

options = ["りんご", "みかん", "バナナ", "ぶどう"]

if "default" not in st.session_state:
    st.session_state.default = []

with st.form("form"):
    if st.form_submit_button("全選択"):
        st.session_state.default = options

    selected = st.multiselect(
        options,
        default=st.session_state.default
    )

    text = st.text_input("数字をカンマ区切りで入力")

    ok = st.form_submit_button("OK")

if ok:
    nums = [int(x.strip()) for x in text.split(",") if x.strip() != ""]
    st.write(nums)
    st.write(selected)
    st.write(len(selected),"人")

"""
if len(selected) != sum(nums):
    st.write("人数が合わない")

rd.shuffle(selected)

for i in nums:
    st.write(" ".join(selected[:i]))
    selected."""