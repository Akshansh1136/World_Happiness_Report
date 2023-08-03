# Importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("World Happiness Report")

st.image('happiness.png')

st.markdown('''
A Web App to visualize and analyze the World Happiness Report data in 2019.
* **Libraries Used:** Streamlit, Pandas, Plotly
* **Data Source:** Kaggle
''')


# Reading csv data
data = pd.read_csv('happiness_19.csv')  

# Displaying Data and its Shape
st.write("**World Happiness Report dataset**", data)
st.write("Shape of data", data.shape)

# Header of sidebar
st.sidebar.header("Select")

# Creating selectbox for Graphs & Plots
graphs = st.sidebar.selectbox("Graphs & Plots", ("Bar Graph", "Scatter Plot", "HeatMap", "Pie Chart"))

# Sorting the columns
index = sorted(data.columns.unique())

# Setting default value for x, y, and color
default_index_x = index.index('Country or region')
default_index_y = index.index('Score')
default_index_col = index.index('GDP per capita')

# Creating selectbox for x, y and color label and setting default value
x_label = st.sidebar.selectbox("X label Parameter", index, index=default_index_x)
y_label = st.sidebar.selectbox("Y label Parameter", index, index=default_index_y)
col = st.sidebar.selectbox("Color", index, index=default_index_col)

st.markdown('''
## **Visualization**
''')

# function to plot graphs
def visualize_plotly(graph):
    if graph == "Bar Graph":
        st.write(graph)
        fig = px.bar(data, x=x_label, y=y_label, color=col)

    elif graph == "Scatter Plot":
        st.write(graph)
        fig = px.scatter(data, x=x_label, y=y_label, color=col)

    elif graph == "HeatMap":
        st.write(graph)
        fig = px.density_heatmap(data, x=x_label, y=y_label, nbinsx=20, nbinsy=20)

    else:
        st.write(graph)
        fig = px.pie(data, values=x_label, names=data[y_label])

    return fig

figure = visualize_plotly(graphs)
st.plotly_chart(figure)

st.markdown('''
## **Report**
''')

# Creating buttons to display reports
if st.button("Highest Score"):
    st.header("Country with Highest Happiness Score")
    highest_score = data[data['Score'] == max(data['Score'])]
    st.write(highest_score)

if st.button("Lowest Score"):
    st.header("Country with Lowest Happiness Score")
    lowest_score = data[data['Score'] == min(data['Score'])]
    st.write(lowest_score)

# Creating buttons to display complex insights
if st.button("High GDP and Social Support"):
    st.header("Country with High GDP per capita and Social Support")
    median_social_support = data['Social support'].median()
    high_gdp_support = data[(data['GDP per capita'] == max(data['GDP per capita'])) & (data['Social support'] > median_social_support)]
    st.write(high_gdp_support)



