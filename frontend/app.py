import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui_category import analytics_tab_by_category
from analytics_ui_months import analytics_tab_by_months

st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics Monthly"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab_by_category()
with tab3:
    analytics_tab_by_months()