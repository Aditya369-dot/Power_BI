import streamlit as st
import os
import imageio


st.set_page_config(layout="wide")

st.sidebar.info("lets Connect")



st.sidebar.markdown("""
[![GitHub](https://img.icons8.com/ios-glyphs/45/FFFFFF/github.png)](https://github.com/Aditya369-dot)
[![LinkedIn](https://img.icons8.com/ios-glyphs/45/FFFFFF/linkedin-circled--v2.png)](https://www.linkedin.com/in/aditya-b-231a0a194/)
[![Twitter](https://img.icons8.com/ios-glyphs/40/FFFFFF/twitter.png)](https://twitter.com/adibholla21)
[![Instagram](https://img.icons8.com/ios-glyphs/45/FFFFFF/instagram-new.png)](https://www.instagram.com/aditya_4real/?next=%2Foauth%2Foidc%2F%3Fapp_id%3D1289884158313322%26scope%3Dopenid%26response_type%3Dcode%26state%3DATB3TBXUaFJLKVN4dV5PYrDMQbVb4gYfCo_NtC7hKYeXi_xGSJiosSqUdnYymaMoKJCIQ-uoXpCCDDfHA95spC5vL_FHjyYUfkdMmj9igbQgB-ULu0BNLWW_VlXz7cGbGkSqtdg-Hl5PNAFvQ3Q4T4KkG1A%26redirect_uri%3Dhttps%3A%2F%2Fwww.threads.net%2Flogin%2Foidc%2F%26logger_id%3D31423f7a-6b01-4808-91a7-32c2a0b89ead)
""",unsafe_allow_html=True)

filepath = "Power_bi_resume.pdf"

with open(filepath,"rb") as file:
    btn = st.sidebar.download_button(
        label="Download Resume",
        data=file,
        mime="application/pdf"
    )

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
        "**Stay tuned as we embark on this journey, transforming raw data into a simple, insightful dashboard that will informative and functional.**")

    st.markdown("""
        <style>
        .stVideo {
            width: 10%;
            height: 10%;
        }
        </style>
        """, unsafe_allow_html=True)

    st.video('C:/Users/adity/Videos/Screen Recorder/final.mp4')

st.header(" 🛠️ STEP 1 ➡️ Connecting to a Data source by using Get data")
with st.container():
    col3 , col4 = st.columns([1,1])



with col3:
    st.write("")
    st.info("Power BI stands out for its ability to connect effortlessly with a wide range of data sources, including CSV files, APIs,databases and much more. "
        "It simplifies the process of turning raw data into insights through its integrated ETL (Extract, Transform, Load) capabilities."
        " However, it's just one of many tools available. Each tool brings its own strengths, and the choice often depends on specific project needs, data types, and the technical comfort of the team. "
        "By leveraging these tools wisely, you can ensure that your project benefits from a diverse set of data inputs, making your analyses richer and more comprehensive. "
        "This approach opens up analytics to a wider audience, ensuring that your project can harness the full potential of data-driven insights.")

    st.markdown(
        "<span style='color: #FF4500;'>In my role, we leverage cloud connectors and <span style='color:#00008B;'>APIs for data integration, primarily with Oracle Fusion Cloud and Azure Cloud. For Human Capital Management (HCM) data, I generate XML files using HCM extracts. For data from other business units,"
        " I connect to an Azure SQL database.</span> This approach highlights the importance of adaptability in managing data across different cloud platforms."
        " But we will keep it simple. If you are following me, please download the CSV (Comma Separated Values) file</span>",
        unsafe_allow_html=True)

    file_path = "C:/Users/adity/OneDrive/Desktop/Power BI Course files/adventure works.zip"

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in binary read mode
        with open(file_path, "rb") as file:
            # Read the file's content
            bytes_data = file.read()

        # Create a download button and provide the file's content as bytes
        st.write("Download here ⬇️ ")
        st.download_button(
            label="Download ZIP",
            data=bytes_data,
            file_name="adventure_works.zip",
            mime="application/zip"
        )
    else:
        st.error("File not found. Please check the file path.")


with col4:
    st.image("Screenshot (334).png", width= 700)


st.header("🛠️ STEP 2 ➡️ We model the data and clean it, also creating some calculated fields")
with st.container():
    col5, col6 = st.columns([1,1])

with col5:
    st.subheader("Description")
    st.info("Data modeling in Power BI is a critical process that involves structuring your data in a way that makes it"
             " easy to create visuals, reports, and dashboards. "
             "A well-designed data model allows for efficient data analysis "
             "and helps uncover insights more effectively. "
             "Here's a concise overview of key concepts in data modeling within Power BI.")
    st.markdown("<span style='color: #FF4500;'> Creating an efficient data models but first understanding type of data stored in tables</span>",unsafe_allow_html=True)
    st.markdown("<span style='color: #FF4500;'>👉 Building the Model:</span> In Power BI, after importing the data, you define relationships between tables, "
        "typically connecting fact tables to related dimension tables through primary and foreign keys. "
        "This setup enables analyzing facts in the context of the dimensions, like time, geography, or product characteristics."
        , unsafe_allow_html=True)

    st.write("")

    st.markdown(
        "<span style='color: #FF4500;'>👉 Lookup Tables:</span> Lookup tables, or dimension tables, store descriptive information about the entities in the fact tables. "
        "They help in providing context to the numeric metrics in the fact tables, such as product details, customer information, or time dimensions. "
        "In Power BI, lookup tables are crucial for creating meaningful relationships and enabling rich data exploration."
        , unsafe_allow_html=True)

    st.write("")
    st.markdown("<span style='color: #FF4500;'>👉 Facts and Events Tables:</span>Fact tables store quantitative data for analysis and reporting,"
                " such as sales amount, transaction count, etc. Event tables, a type of fact table, specifically track events over time, "
                "providing valuable insights into the temporal aspects of the data.",unsafe_allow_html=True )
    st.write("")
    st.markdown("<span style='color: #FF4500;'>👉 Joins :</span>Joins are used in Power BI to merge data from different sources based on common columns. "
                "The main types of joins include Inner Join, Left Outer Join, Right Outer Join, and Full Outer Join, "
                "each serving a unique purpose in combining data sets to enrich the model.",unsafe_allow_html=True)
    st.write("")
    st.markdown("<span style='color: #FF4500;'>👉 Flows and Snowflake Schema :</span>The downward flow in data modeling refers to the hierarchy of data from high-level summaries to more detailed data. "
                "In Power BI, this allows users to drill down through layers of data in visualizations, "
                "starting from a general overview down to more specific data points.The Snowflake Schema in Power BI is a data modeling technique where the data is organized in a way that resembles a snowflake. "
                "It involves a central fact table linked to multiple dimension tables, which can also be linked to other dimension tables. "
                "This schema is beneficial for complex data models, reducing data redundancy and improving query performance.",unsafe_allow_html=True)
with col6:
    st.image("Screenshot model).png", width=1200)


st.header("🛠️ STEP 1 ➡️ Understanding each Analysis on the Dashboard individually for a better understanding ")
st.subheader("Choose options below to select one analysis and learn more about it")

options = ["Exec Dashboard", "Model and Calculated Fields",  "Map", "Product Detail", "Customer Detail", "DAX integrations for Drill-downs"]

# Create radio buttons in a horizontal layout
selected_option = st.radio("Choose an option:", options, horizontal=True)

# Conditional block to show image and description based on selection
if selected_option == "Exec Dashboard":
    st.image("path_to_exec_dashboard_image.jpg")  # Replace with your image path or URL
    st.write("Description for Exec Dashboard")
elif selected_option == "Model and Calculated Fields":
    st.image("path_to_model_and_calculated_fields_image.jpg")  # Replace with your image path or URL
    st.write("Description for Model and Calculated Fields")
elif selected_option == "Map":
    st.image("path_to_map_image.jpg")  # Replace with your image path or URL
    st.write("Description for Map")
elif selected_option == "Product Detail":
    st.image("path_to_product_detail_image.jpg")  # Replace with your image path or URL
    st.write("Description for Product Detail")
elif selected_option == "Customer Detail":
    st.image("path_to_customer_detail_image.jpg")  # Replace with your image path or URL
    st.write("Description for Customer Detail")
elif selected_option == "DAX integrations for Drill-downs":
    st.image("")
    st.write("")




