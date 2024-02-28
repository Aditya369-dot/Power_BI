import streamlit as st

st.set_page_config(layout="wide")

st.sidebar.info("lets Connect")
st.sidebar.markdown("""
[![GitHub](https://img.icons8.com/ios-glyphs/45/FFFFFF/github.png)](https://github.com/Aditya369-dot)
[![LinkedIn](https://img.icons8.com/ios-glyphs/45/FFFFFF/linkedin-circled--v2.png)](https://www.linkedin.com/in/aditya-b-231a0a194/)
[![Twitter](https://img.icons8.com/ios-glyphs/40/FFFFFF/twitter.png)](https://twitter.com/adibholla21)
[![Instagram](https://img.icons8.com/ios-glyphs/45/FFFFFF/instagram-new.png)](https://www.instagram.com/aditya_4real/?next=%2Foauth%2Foidc%2F%3Fapp_id%3D1289884158313322%26scope%3Dopenid%26response_type%3Dcode%26state%3DATB3TBXUaFJLKVN4dV5PYrDMQbVb4gYfCo_NtC7hKYeXi_xGSJiosSqUdnYymaMoKJCIQ-uoXpCCDDfHA95spC5vL_FHjyYUfkdMmj9igbQgB-ULu0BNLWW_VlXz7cGbGkSqtdg-Hl5PNAFvQ3Q4T4KkG1A%26redirect_uri%3Dhttps%3A%2F%2Fwww.threads.net%2Flogin%2Foidc%2F%26logger_id%3D31423f7a-6b01-4808-91a7-32c2a0b89ead)
""",unsafe_allow_html=True)
def gradient(color1, color2, color3):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:40x;border-radius:3%".'
                f'<span style="color:{color3};">Creating Simple and Powerful Power BI Dashboard using E-commerce data</span><br>',unsafe_allow_html=True)


with st.container():
    col1,col2 = st.columns([4,0.5])

with col1:
    gradient("#32CD32", "#00FF00", "#FFFF")
    st.header("")
    import streamlit as st

    st.markdown(
        "**In the fast-paced world of e-commerce, data is king. It informs every decision, from marketing strategies to inventory management, and in the digital age, the ability to quickly interpret and act on this data sets successful businesses apart. This is where our step-by-step tutorial comes into play, guiding you through the process of building an executive dashboard for your e-commerce platform using Microsoft Power BI.**")

    st.markdown(
        "**Our journey will begin with the basics of acquiring data, specifically focusing on datasets available through Kaggle—a treasure trove of information ready to be harnessed. From there, we'll dive into the creation of dynamic data models and flows, ensuring your dashboard not only presents data but tells a story. The art of creating sensible and impactful visuals will be our next focus, turning numbers and figures into insights at a glance.**")

    st.markdown(
        "**But we won’t stop there. The real magic happens when we introduce DAX (Data Analysis Expressions). These powerful formulas allow for deep dives and drill-downs into your data, uncovering trends and details that could easily be missed at first glance. Whether you're a seasoned Power BI user looking to refine your skills or a newcomer eager to make your mark in the e-commerce world, this tutorial is designed to equip you with the knowledge and tools you need to create a dashboard that not only meets but exceeds executive expectations.**")

    st.markdown(
        "**Stay tuned as we embark on this journey, transforming raw data into a sleek, insightful dashboard that will propel your e-commerce platform to new heights.**")



