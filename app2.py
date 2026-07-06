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

    ok = st.form_submit_button("OK")

if ok:
    st.write(selected)

    