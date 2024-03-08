import streamlit as st
import os


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

file_path = "C:/Users/adity/OneDrive/Desktop/Power BI Course files/adventure works.zip"
if os.path.exists(file_path):
    # Open the file in binary read mode
    with open(file_path, "rb") as file:
        # Read the file's content
        bytes_data = file.read()

    # Create a download button and provide the file's content as bytes
    st.sidebar.info("Download CSV to follow along ⬇️ ")
    st.sidebar.download_button(
        label="Download CSV Zip",
        data=bytes_data,
        file_name="adventure_works.zip",
        mime="application/zip"
    )
else:
    st.error("File not found. Please check the file path.")


st.sidebar.info("Learn DAX in detail from Microsoft itself ⬇️ ")
st.sidebar.link_button(
    label="Link to DAX",
    url="https://learn.microsoft.com/en-us/dax/dax-overview"
)

def gradient(color1, color2, color3):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:40x;border-radius:3%".'
                f'<span style="color:{color3};">Creating Simple and Powerful Power BI Dashboard using E-commerce data</span><br>',unsafe_allow_html=True)


with st.container():
    col1,col2 = st.columns([4,0.5])

with col1:
    gradient("#808000", "#FFD700", "#FFDAB9")

    st.header("")

    st.markdown("""
    In a project designed to harness the power of e-commerce analytics, I have leveraged Microsoft Power BI to construct an executive dashboard that synthesizes complexity into clarity. This dashboard was built upon a rich dataset from Kaggle, meticulously molded to create a dynamic and informative narrative of the e-commerce business landscape.

    My approach was methodical: I began by sculpting a robust data model that set the stage for insightful analytics. The focus was on creating a storytelling flow within the dashboard that guides the viewer through different facets of business performance, from sales to customer engagement.

    Visualizations played a crucial role; each chart and graph was strategically placed to offer immediate business insights at a glance. From gauging customer order trends across income levels to tracking average revenue per customer, the dashboard transformed data points into actionable intelligence.

    With DAX expressions at my disposal, I added a layer of depth, enabling the dashboard to not only display static data but also to offer interactive exploration. The result was a compelling, user-friendly dashboard that distills vast amounts of data into understandable metrics that drive strategic business decisions.

    This project epitomizes the transformative potential of data visualization in Power BI, turning raw data into a streamlined, efficient dashboard poised to elevate any e-commerce platform's analytical capabilities.
    """, unsafe_allow_html=False)

    st.markdown("""
        <style>
        .stVideo {
            width: 5%;
            height: 10%;
        }
        </style>
        """, unsafe_allow_html=True)

    st.video('final.mp4')

st.header("🛠️➡️ Understanding the Architecture of Power BI and Fabric with Power Apps and Azure")
st.info("Power BI stands out for its ability to connect effortlessly with a wide range of data sources, including CSV files, APIs,databases and much more. "
        "It simplifies the process of turning raw data into insights through its integrated ETL (Extract, Transform, Load) capabilities."
        " However, it's just one of many tools available. Each tool brings its own strengths, and the choice often depends on specific project needs, data types, and the technical comfort of the team. "
        "By leveraging these tools wisely, you can ensure that your project benefits from a diverse set of data inputs, making your analyses richer and more comprehensive. "
        "This approach opens up analytics to a wider audience, ensuring that your project can harness the full potential of data-driven insights.")
st.image("images/architecture.png")




st.header("🛠️➡️ Understanding each Analysis on the Dashboard individually for a better understanding ")
st.subheader("Choose options below to select one analysis and learn more about it")

options = ["Exec Dashboard", "Map", "Product Detail", "Customer Detail","Data Model and Table View", "DAX integrations for Drill-downs"]

# Create radio buttons in a horizontal layout
selected_option = st.radio("Choose an option:", options, horizontal=True)

# Conditional block to show image and description based on selection

if selected_option == "Exec Dashboard":
        st.write("Description for Exec Dashboard")
        st.image("images/20240304175209-ezgif.com-video-to-gif-converter.gif", width=800)  # Replace with your image path or URL
        st.title('Executive Dashboard Analysis')

        st.markdown("""
        <style>
        .neon-orange { color: #FFA07A; } /* Adjust the color code for neon orange */
        .neon-green { color: #7FFF00; } /* Adjust the color code for neon green */
        .neon-blue { color: #00FFFF; } /* Adjust the color code for neon blue */
        .neon-pink { color: #FF69B4; } /* Adjust the color code for neon pink */
        </style>

        Upon analyzing the <span class='neon-orange'>**Adventure Works Cycles Executive Dashboard**</span>, we uncover a comprehensive snapshot of the company's performance in the cycling equipment market.

        #### <span class='neon-green'>Core Financial Indicators:</span>
        - <span class='neon-blue'>**Total Revenue ($24.9M)**</span>: This key figure is a testament to the company's strong market presence and effective sales strategies.
        - <span class='neon-blue'>**Total Profit ($10.5M)**</span>: A reflection of operational efficiency, this number highlights the company's ability to convert revenue into actual profit.
        - <span class='neon-blue'>**Total Orders (25.2K)**</span>: Indicative of customer demand and sales effectiveness, the volume of orders processed is a vital metric for operational scalability.
        - <span class='neon-blue'>**Return Rate (2.2%)**</span>: This metric warrants attention as it affects customer trust and impacts net revenue. A low rate is indicative of high product quality and customer satisfaction.

        #### <span class='neon-green'>Trend Analysis and Forecasting:</span>
        - The line graph detailing <span class='neon-pink'>**Revenue Trending**</span> allows us to identify temporal patterns, market responses to campaigns, and potentially, to forecast future revenue through its predictive dotted line.

        #### <span class='neon-green'>Monthly Business Health Check:</span>
        - <span class='neon-blue'>**Monthly Revenue ($1.83M)**</span>: Observed against the backdrop of previous performance, this provides a near real-time health check of the business's earning capacity.
        - <span class='neon-blue'>**Monthly Orders (2146)**</span>: A crucial indicator of market penetration and customer acquisition efforts.
        - <span class='neon-blue'>**Monthly Returns (166)**</span>: Monitoring this figure closely can inform product quality and customer service policies.

        #### <span class='neon-green'>Product Performance Deep Dive:</span>
        - The <span class='neon-pink'>**Orders by Category**</span> bar chart dissects the order volume into categories such as Accessories, Bikes, and Clothing, allowing for targeted analysis of product lines.

        #### <span class='neon-green'>Sales and Return Metrics:</span>
        - <span class='neon-blue'>**Top 10 performers**</span>: This table offers strategic insights into product strengths and informs inventory and marketing focus.
        - <span class='neon-blue'>**Most Ordered Product**</span>: This quick glance metric indicates market preference and product success.
        - <span class='neon-blue'>**Most Returned Product**</span>: An essential alert to potential issues in product or service quality that could be detrimental to the brand's reputation.

        The dashboard's design effectively incorporates visual aids and comparative analysis to empower executives with actionable insights, ensuring that strategic decisions are data-driven and timely.

        In summary, the <span class='neon-orange'>**Adventure Works Cycles Executive Dashboard**</span> is a strategic tool that not only provides a holistic view of the company’s current market standing but also serves as a compass for future business direction.
        """, unsafe_allow_html=True)




elif selected_option == "Map":
        st.image("images/20240304175313-ezgif.com-video-to-gif-converter.gif",width=900)  # Replace with your image path or URL
        st.title("Interactive Bubble Map")
        st.markdown("""
            <style>
            .neonHeading {color: #D39FFC;}  /* Neon Purple */
            .neonText {color: #FF4500;} /* Neon Orange */
            .neonHighlight {color: #39FF14;} /* Neon Green */
            .neonSubText {color: #00FFFF;} /* Neon Blue */
            </style>

            <span class='neonHeading'>Interactive Map Visualization Analysis in Power BI</span><br><br>

            <span class='neonText'>The Power BI dashboard presents an interactive map visualization that is pivotal for geospatial analysis. The displayed map highlights total orders by country with proportional bubble sizes that intuitively indicate order volumes. Through this visualization:</span><br>

            - <span class='neonHighlight'>Regions:</span> Different continents such as Europe, North America, and the Pacific are clearly demarcated, offering insights into regional market distribution.<br>
            - <span class='neonHighlight'>Bubbles:</span> The varying sizes of the bubbles provide an immediate visual cue to the user about the volume of orders from different countries, enabling quick comparative analysis.<br>
            - <span class='neonHighlight'>Interactivity:</span> Users can interact with the visualization to drill down into specific countries or regions, facilitating a deeper understanding of localized trends.<br>
            - <span class='neonHighlight'>Filtering:</span> The map includes a filtering feature, allowing stakeholders to view data for selected regions, aiding in targeted analysis and decision-making.<br><br>

            <span class='neonSubText'>Types of Maps in Power BI:</span><br>
            Power BI offers a variety of map visualizations to cater to different analytical needs:<br>
            - <span class='neonSubText'>Bubble Map:</span> Ideal for emphasizing points of interest with size-based indicators.<br>
            - <span class='neonSubText'>Filled Map:</span> Excellent for demographic and density distribution analysis through color-coded regions.<br>
            - <span class='neonSubText'>Shape Map:</span> Suited for custom layouts and non-geographical shapes.<br>
            - <span class='neonSubText'>ArcGIS Maps:</span> Advanced geographic analysis with enhanced features like heat maps, drive times, and clustering.<br><br>

            <span class='neonText'>In summary, the map visualization in Power BI shown in the image provides a strategic overview of global operations, enabling businesses to pinpoint areas of high performance and identify regions that may require additional attention or resources.</span>
            """, unsafe_allow_html=True)

elif selected_option == "Product Detail":
    st.image("images/20240304175401-ezgif.com-video-to-gif-converter.gif",width=900)  # Replace with your image path or URL
    st.title("Analyzing Individual Product Performance With Product Detail View ")
    st.markdown("""
        <style>
        .neonHeading {color: #39FF14;} /* Neon Green */
        .whiteText {color: #FFFFFF;} /* White */
        </style>

        <span class='neonHeading'>In-Depth Analysis of the Product Detail Dashboard</span><br><br>

        <span class='whiteText'>The dashboard we're examining goes beyond basic reporting to provide a rich, data-driven story about the 'All-Purpose Bike Stand'. By leveraging a suite of interactive visualizations and filters, it grants comprehensive insights into the product's performance.</span><br><br>

        <span class='neonHeading'>Monthly Orders vs. Order Target Gauge</span><br>
        <span class='whiteText'>
        The gauge is an intuitive tool for tracking sales efficiency. By showing the actual orders as a proportion of the target, it quickly communicates whether sales initiatives are hitting their mark. This can be particularly helpful in sales meetings to visually underscore areas needing attention and to prompt discussion around tactics for improvement.
        </span><br><br>

        <span class='neonHeading'>Profit Analysis Line Chart</span><br>
        <span class='whiteText'>
        Profitability is a vital sign of a product's success. The line chart traces profit over time, revealing the financial journey of the product. It’s critical for spotting trends, such as an increase in profit following a marketing campaign or a decrease that might correlate with external market pressures. By placing actual and adjusted profits side by side, the chart guides managers in evaluating the effectiveness of their pricing strategies and cost control measures.
        </span><br><br>

        <span class='neonHeading'>Revenue Targets Bar Chart</span><br>
        <span class='whiteText'>
        This bar chart is crucial for assessing how well the product is doing against revenue goals. It helps in understanding if the product is a strong contributor to the company's bottom line or if there are market challenges that need to be addressed. A consistent shortfall against targets might indicate the need for a product refresh or a pivot in strategy.
        </span><br><br>

        <span class='neonHeading'>Trend Analysis and Metric Selection</span><br>
        <span class='whiteText'>
        The trend analysis section dives into the selected product's sales, returns, and revenue over time. This multi-metric approach allows for a balanced view of success and areas for improvement. For example, a high return rate might point to quality issues, while fluctuating sales could indicate seasonal demand or supply chain challenges.
        </span><br><br>

        <span class='neonHeading'>Discount Filter Impact</span><br>
        <span class='whiteText'>
        The discount filter is a powerful feature that simulates how price adjustments could affect sales volume and profitability. It’s an excellent tool for understanding the price sensitivity of the product and can guide pricing strategies to optimize for market competitiveness and profitability. Analyzing how discounts impact total revenue and profit can inform promotional campaigns and discount limits.
        </span><br><br>

        <span class='whiteText'>
        Overall, this dashboard exemplifies the use of Power BI for strategic analysis. The interactive components encourage active exploration of the data, fostering a deeper understanding of the product’s market behavior. Such insights are invaluable for crafting strategies that capitalize on strengths and address weaknesses, thereby driving business growth.
        </span>
        """, unsafe_allow_html=True)





elif selected_option == "Customer Detail":
    st.image("images/20240304175439-ezgif.com-video-to-gif-converter.gif",width=900)  # Replace with your image path or URL
    st.title("Analyzing Our Customers Through Customer Detail Dashboard")
    st.markdown("""
        <style>
        .neonHeading {color: #39FF14;} /* Neon Green */
        .whiteText {color: #FFFFFF;} /* White */
        .neonBlue {color: #00FFFF;} /* Neon Blue */
        </style>

        <span class='neonHeading'>In-Depth Analysis and Key Findings from Customer Detail Dashboard</span><br><br>

        <span class='whiteText'>
        The customer detail dashboard is a treasure trove of insights, crafted with a range of visual elements that provide both an overarching and granular perspective on customer engagement and sales metrics.

        <span class='neonHeading'>Key Metrics and Their Implications</span><br>
        - The <span class='neonBlue'>Average Revenue Per Customer</span> at the top-left is a pivotal gauge of the value that each customer brings to the company. A robust average suggests that customer acquisition and upselling strategies are bearing fruit.
        - The <span class='neonBlue'>Unique Customer Orders</span> counter reflects the company's market reach and is indicative of its ability to attract and retain customers, which is essential for long-term viability.

        <span class='neonHeading'>Segmentation Analysis</span><br>
        - The <span class='neonBlue'>Income Level Distribution Donut Chart</span> showcases the variety within the customer base. A sizeable high-income segment could indicate success in capturing the premium market segment.
        - The <span class='neonBlue'>Occupation by Customer Donut Chart</span> provides valuable insights into the customers' professional backgrounds, information that can drive targeted product development and marketing strategies.

        <span class='neonHeading'>Revenue Trends and Patterns</span><br>
        - The <span class='neonBlue'>Revenue Trend Line Chart</span> reveals the revenue fluctuations over time, which can help identify the effects of seasonal trends or the impact of promotional activities.

        <span class='neonHeading'>Customer Revenue Contributions</span><br>
        - The <span class='neonBlue'>Customer Revenue Table</span> effectively pinpoints the customers who are significant revenue drivers and may be suitable for focused relationship-building initiatives like loyalty programs.

        <span class='neonHeading'>Customer Spotlight</span><br>
        - The <span class='neonBlue'>Featured Customer Card</span> highlights individual customer contributions, demonstrating the high lifetime value of certain customers and emphasizing the importance of personalized customer engagement strategies.

        <span class='neonHeading'>Overall Findings</span><br>
        The analysis of the dashboard reveals:
        - The diversified customer base regarding income and occupation hints at a broad appeal of the company's offerings.
        - There appears to be a substantial opportunity to augment customer retention strategies, particularly for those who are pivotal to the company's revenue stream.
        - A closer look at sales trends might uncover strategic periods for optimizing marketing initiatives and sales operations.

        In sum, this dashboard acts as a critical strategic asset for guiding future business directions and fostering an environment of informed decision-making practices.
        </span>
        """, unsafe_allow_html=True)



elif selected_option == "Data Model and Table View":
    colm, colt = st.columns([1,1])
    with colm:
        st.image("images/20240305151416-ezgif.com-video-to-gif-converter.gif",width=800)
    with colt:
        st.image("images/20240305151604-ezgif.com-video-to-gif-converter.gif",width=800)
    st.subheader("➡️ Understanding modelling with Model view and Table view")
    st.info("Data modeling in Power BI is a critical process that involves structuring your data in a way that makes it"
            " easy to create visuals, reports, and dashboards. "
            "A well-designed data model allows for efficient data analysis "
            "and helps uncover insights more effectively. "
            "Here's a concise overview of key concepts in data modeling within Power BI.")
    st.markdown("""
        <style>
        .neonHeading {color: #FF4500;}  /* Neon Orange */
        .neonSubHeading {color: #39FF14;} /* Neon Green */
        .neonHighlight {color: #00FFFF;} /* Neon Blue */
        </style>

        <span class='neonHeading'>Creating efficient data models requires first understanding the type of data stored in tables.</span><br><br>

        <span class='neonSubHeading'>👉 Building the Model:</span>
        <span class='neonHighlight'>In Power BI, after importing the data, you define relationships between tables,</span>
        typically connecting fact tables to related dimension tables through primary and foreign keys.
        This setup enables analyzing facts in the context of the dimensions, like time, geography, or product characteristics.<br><br>

        <span class='neonSubHeading'>👉 Lookup Tables:</span>
        <span class='neonHighlight'>Lookup tables, or dimension tables, store descriptive information about the entities in the fact tables.</span>
        They help in providing context to the numeric metrics in the fact tables, such as product details, customer information, or time dimensions.
        In Power BI, lookup tables are crucial for creating meaningful relationships and enabling rich data exploration.<br><br>

        <span class='neonSubHeading'>👉 Facts and Events Tables:</span>
        <span class='neonHighlight'>Fact tables store quantitative data for analysis and reporting,</span>
        such as sales amount, transaction count, etc. Event tables, a type of fact table, specifically track events over time,
        providing valuable insights into the temporal aspects of the data.<br><br>

        <span class='neonSubHeading'>👉 Joins:</span>
        <span class='neonHighlight'>Joins are used in Power BI to merge data from different sources based on common columns.</span>
        The main types of joins include Inner Join, Left Outer Join, Right Outer Join, and Full Outer Join,
        each serving a unique purpose in combining data sets to enrich the model.<br><br>

        <span class='neonSubHeading'>👉 Flows and Snowflake Schema:</span>
        <span class='neonHighlight'>The downward flow in data modeling refers to the hierarchy of data from high-level summaries to more detailed data.</span>
        In Power BI, this allows users to drill down through layers of data in visualizations,
        starting from a general overview down to more specific data points. The Snowflake Schema in Power BI is a data modeling technique where the data is organized in a way that resembles a snowflake.
        It involves a central fact table linked to multiple dimension tables, which can also be linked to other dimension tables.
        This schema is beneficial for complex data models, reducing data redundancy and improving query performance.
        """, unsafe_allow_html=True)


elif selected_option == "DAX integrations for Drill-downs":
    coldax, colinfo = st.columns([1 ,1])
    with coldax:
        st.image("images/20240305151812-ezgif.com-video-to-gif-converter.gif", width= 700)
    with colinfo:
       st.image("images/new.gif",width=700)
    st.title("Implicit Measures vs Explicit Measures")
    st.markdown("<span style='color: #FF4500;'> Implicit Measures </span> are automatically created by the software when a field is added to a report. They apply default aggregations like sum or count without the need for a user-defined formula." +
                    "<span style='color: #FF4500;'> Explicit Measures </span> are custom calculations created by the user using DAX formulas. These allow for more complex and precise data analysis.",unsafe_allow_html=True)
    st.markdown("<span style='color: #FF4500;'>Key Differences</span>",unsafe_allow_html=True)
    st.markdown(
            "<span style='color: #FF4500;'>Creation:</span> Implicit measures are auto-generated; explicit measures are user-defined.<br>" +
            "<span style='color: #FF4500;'>Flexibility:</span> Explicit measures offer greater flexibility and complexity.<br>" +
            "<span style='color: #FF4500;'>Performance:</span> Explicit measures can be optimized for better performance.<br>" +
            "<span style='color: #FF4500;'>Reusability:</span> Explicit measures can be reused across reports, ensuring consistency.",unsafe_allow_html=True)
    st.title("Using Implicit measures in Visualizations")
    st.markdown("""
        <style>
        .neonGreen {color: #39FF14;} /* Neon Green */
        </style>

        Implicit measures in Power BI are created automatically when you drag and drop fields into visualizations. These measures are typically straightforward aggregations of your data.<br><br>

        <span class='neonGreen'>Total Sales:</span> The sum of all sales transactions. This measure is automatically calculated when you drag the sales amount field into a visualization, summing up the total sales revenue.<br>

        <span class='neonGreen'>Total Orders:</span> The count of all orders. By dragging the order ID field into a visualization, Power BI can count the total number of orders placed within the selected timeframe.<br>

        <span class='neonGreen'>Average Order Value (AOV):</span> The average value of sales transactions. When you drag the sales amount field into a visualization and set the aggregation to average, Power BI calculates the AOV.
        """, unsafe_allow_html=True)

    st.title("Using Explicit Measures in Visualization")
    st.markdown("Explicit measures are created using DAX to define complex calculations. They offer flexibility and precision, tailored to specific analytical needs.",
            unsafe_allow_html=True)
    st.info("CLV = SUMX(Customers, [Total Sales] * [Profit Margin] * [Retention Rate])")
    st.write("This measure calculates the predicted net profit attributed to the entire future relationship with a customer. It considers total sales, profit margin, and retention rate for each customer.")
    st.info("YoY Sales Growth = (CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date])) - [Total Sales]) / CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))")
    st.write("This measure calculates the growth in sales compared to the same period in the previous year, giving insight into the business's growth trajectory.")
    st.info("TenDayRollingAverageSales = CALCULATE(AVERAGE(Sales[TotalSales]),DATESINPERIOD(Sales[SalesDate], LASTDATE(Sales[SalesDate]), -10, DAY))")
    st.write("This calculates the average total sales (AVERAGE(Sales[TotalSales])) over a rolling period of 10 days ending with the last date in Sales[SalesDate]. The period is dynamically calculated for each row in the data, making it a 'rolling' or 'moving'' average.")
    st.write("In brief, explicit measures provide more control and versatility for complex data analysis, whereas implicit measures are suitable for quick, straightforward aggregations.")

