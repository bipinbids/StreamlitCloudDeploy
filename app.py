import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Add a title to the sidebar
st.sidebar.title('Sidebar Title')

# Add a button to the sidebar
button_clicked = st.sidebar.button('Show Pie Chart')

# Display a pie chart when the button is clicked
if button_clicked:
    st.write('Pie Chart:')
    data = np.random.rand(5)
    plt.pie(data, labels=[f'x{i}' for i in range(1, 6)])
    st.pyplot(plt)
