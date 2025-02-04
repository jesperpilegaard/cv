import streamlit as st

pg = st.navigation([st.Page("about_me.py", title="🙋‍♂️ Om mig"), st.Page("work.py", title="💼 Erhvervserfaring"), 
                    st.Page("education.py", title="🎓 Uddannelse"), st.Page("portfolio.py", title="📊 Dashboard Scape")])
pg.run()