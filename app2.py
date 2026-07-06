import streamlit as st
import streamlit as st
st.title("タイトル")
st.header("見出し")
st.subheader("小見出し")
st.write("こんにちは")

import streamlit as st

options = ["りんご", "みかん", "バナナ", "ぶどう"]

if "default" not in st.session_state:
    st.session_state.default = []

with st.form("my_form"):
    col1, col2 = st.columns(2)

    with col1:
        if st.form_submit_button("全選択"):
            st.session_state.default = options

    with col2:
        if st.form_submit_button("全解除"):
            st.session_state.default = []

    selected = st.multiselect(
        "果物を選択",
        options,
        default=st.session_state.default
    )

    ok = st.form_submit_button("OK")

if ok:
    st.write("確定:", selected)