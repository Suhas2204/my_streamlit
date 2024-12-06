import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Concrete Dataset Analyzer")
st.write("Upload your concrete dataset to analyze for outliers and visualize data using boxplots.")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File successfully uploaded!")
        st.write("### Dataset Preview")
        st.write(df.head())

        # Check for numerical columns
        num_columns = df.select_dtypes(include=["float64", "int64"]).columns

        if not num_columns.empty:
            st.write("### Outlier Analysis")

            # Generate Boxplots for Numerical Columns
            for col in num_columns:
                st.write(f"#### Boxplot for `{col}`")
                fig, ax = plt.subplots()
                sns.boxplot(data=df, x=col, ax=ax)
                ax.set_title(f"Boxplot of {col}")
                st.pyplot(fig)

            # Display Summary Statistics
            st.write("### Summary Statistics")
            st.write(df[num_columns].describe())
        else:
            st.warning("The uploaded dataset contains no numerical columns for analysis.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a CSV file to start the analysis.")
