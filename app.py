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
    fig, ax = plt.subplots()
    ax.pie(data, labels=[f'x{i}' for i in range(1, 6)])
    st.pyplot(fig)

    # Set the width of the chart to fit the screen
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig, clear_figure=True)
