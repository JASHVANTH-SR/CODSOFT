import pandas as pd
import streamlit as st
import plotly.express as px

# Load Titanic dataset
titanic_data = pd.read_csv('titanic dataset.csv')

# Prepare data for visualization
data = titanic_data.dropna()

# Create Streamlit app
def main():
    st.title("Titanic Passenger Analysis")

    st.markdown(
        """
        Explore the Titanic dataset and gain insights through visualizations.
        """
    )

    # Display basic statistics
    st.header("Basic Statistics")
    st.write("Total passengers:", len(data))
    st.write("Survival rate:", data['Survived'].mean())

    # Display age distribution
    st.header("Age Distribution")
    fig_age = px.histogram(data_frame=data, x='Age', title="Age Distribution")
    st.plotly_chart(fig_age)

    # Display fare distribution
    st.header("Fare Distribution")
    fig_fare = px.histogram(data_frame=data, x='Fare', title="Fare Distribution")
    st.plotly_chart(fig_fare)

    # Display survival by sex and class
    st.header("Survival by Sex and Class")
    fig_sex_class = px.histogram(data_frame=data, x='Pclass', color='Survived', barmode='group',
                                 title="Survival by Sex and Class")
    st.plotly_chart(fig_sex_class)

    # Display survival by embarkation port
    st.header("Survival by Embarkation Port")
    fig_embarked = px.histogram(data_frame=data, x='Embarked', color='Survived', barmode='group',
                                title="Survival by Embarkation Port")
    st.plotly_chart(fig_embarked)

    st.markdown(
        """
        This interactive scatter plot compares the age and fare of Titanic passengers based on their sex and survival status.
        - Green circles represent female passengers.
        - Blue circles represent male passengers.
        - Symbol 'x' indicates passengers who survived.
        - Symbol 'o' indicates passengers who did not survive.
        """
    )

    # Filter data for survived and not survived passengers
    survived = data[data['Survived'] == 1]
    not_survived = data[data['Survived'] == 0]

    # Create an interactive scatter plot using Plotly Express
    fig = px.scatter(
        data_frame=data,
        x='Age',
        y='Fare',
        color='Sex',
        symbol='Survived',
        title="Age vs Fare by Sex (Survival)",
        labels={'Age': 'Age', 'Fare': 'Fare'},
        template='plotly',
        hover_name='Sex',
        hover_data=['Survived']
    )

    # Display the Plotly figure using Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
