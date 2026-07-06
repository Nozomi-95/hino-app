import streamlit as st

options = ["りんご", "みかん", "バナナ", "ぶどう"]

if "default" not in st.session_state:
    st.session_state.default = []

with st.form("form"):
    if st.form_submit_button("全選択"):
        st.session_state.default = options

    selected = st.multiselect(
        "選択",
        options,
        default=st.session_state.default
    )

    text = st.text_input("数字をカンマ区切りで入力（例: 1,2,3）")

    ok = st.form_submit_button("OK")

if ok:
    nums = [int(x.strip()) for x in text.split(",") if x.strip() != ""]
    st.write("確定:", nums)
    
    st.error("数字以外が含まれています")

    st.write(selected)