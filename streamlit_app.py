import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to render a line plot


def render_line_plot(data, x_col, y_cols):
    plt.figure(figsize=(10, 6))
    for col in y_cols:
        plt.plot(data[x_col], data[col], label=col)
    plt.xlabel(x_col)
    plt.ylabel('Values')
    plt.legend()
    plt.title('Line Plot')
    st.pyplot()

# Function to render a bar plot


def render_bar_plot(data, x_col, y_cols):
    plt.figure(figsize=(10, 6))
    x = data[x_col]
    width = 0.8 / len(y_cols)
    for i, col in enumerate(y_cols):
        x_shift = x - 0.4 + i * width
        plt.bar(x_shift, data[col], width=width, align='center', label=col)
    plt.xlabel(x_col)
    plt.ylabel('Values')
    plt.legend()
    plt.title('Bar Plot')
    st.pyplot()

# Function to render a scatter plot


def render_scatter_plot(data, x_col, y_cols):
    plt.figure(figsize=(10, 6))
    for col in y_cols:
        plt.scatter(data[x_col], data[col], label=col)
    plt.xlabel(x_col)
    plt.ylabel('Values')
    plt.legend()
    plt.title('Scatter Plot')
    st.pyplot()

# Main function


def main():
    st.title("Dataset Visualization App")

    # Upload dataset
    uploaded_file = st.file_uploader("Upload dataset (CSV)", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Display dataset
        st.subheader("Dataset")
        st.write(data)

        # Choose columns for visualization
        columns = data.columns.tolist()
        selected_cols = st.multiselect(
            "Select columns for visualization", columns)

        if selected_cols:
            plot_type = st.selectbox("Select plot type", [
                                     "Line Plot", "Bar Plot", "Scatter Plot"])

            if plot_type == "Line Plot":
                x_col = st.selectbox("Select x-axis column", selected_cols)
                render_line_plot(data, x_col, selected_cols)

            elif plot_type == "Bar Plot":
                x_col = st.selectbox("Select x-axis column", selected_cols)
                render_bar_plot(data, x_col, selected_cols)

            elif plot_type == "Scatter Plot":
                x_col = st.selectbox("Select x-axis column", selected_cols)
                render_scatter_plot(data, x_col, selected_cols)


# Run the app
if __name__ == "__main__":
    main()
