import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.write("Personalized Dashboard containing the most Important data goes here")


# Add a title to the sidebar
st.sidebar.title('Various Kinds Of Analytics')

# Add a button to the sidebar
Pie_button_clicked = st.sidebar.button('Pie Chart')
Bar_button_clicked = st.sidebar.button('Bar Chart')

# Display a pie chart when the button is clicked
if Pie_button_clicked:
    st.write('There could be text here which talks about the Pie Chart below')
    data = np.random.rand(5)
    fig, ax = plt.subplots()
    ax.pie(data, labels=[f'x{i}' for i in range(1, 6)])
    #st.pyplot(fig)

    # Set the width of the chart to fit the screen
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig, clear_figure=True)


if Bar_button_clicked:
    st.write('There could be text here which talks about the bar chart below')

    
    data = np.random.rand(5)
    labels = [f'x{i}' for i in range(1, 6)]
    fig, ax = plt.subplots()
    ax.bar(labels, data)
    #st.pyplot(fig)

    # Set the width of the chart to fit the screen
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig, clear_figure=True)
