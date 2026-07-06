import streamlit as st
import streamlit as st
st.title("タイトル")
st.header("見出し")
st.subheader("小見出し")
st.write("こんにちは")

import streamlit as st

options = ["りんご", "みかん", "バナナ", "ぶどう"]

if "selected" not in st.session_state:
    st.session_state.selected = []

# 全選択ボタン
if st.button("全選択"):
    st.session_state.selected = options

# 解除ボタン（おまけ）
if st.button("全解除"):
    st.session_state.selected = []

selected = st.multiselect(
    "果物を選択",
    options,
    default=st.session_state.selected
)

st.session_state.selected = selected

st.write("選択中:", selected)