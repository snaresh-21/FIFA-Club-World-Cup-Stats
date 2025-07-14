import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("team_stats_club_world_cup.csv")



# Clean and rename columns
df.columns = df.columns.str.strip()

df.rename(columns={
    'Squad': 'Team',
    'Standard Gls': 'Goals',
    'Standard Sh': 'Shots',
    'Standard SoT': 'Shots on Target',
    'Standard SoT%': 'SoT%',
    'Standard Sh/90': 'Shots/90',
    'Standard SoT/90': 'SoT/90',
    'Standard G/Sh': 'Goals per Shot',
    'Standard G/SoT': 'Goals per SoT',
    'Standard Dist': 'Avg Shot Dist',
    'Standard PK': 'Penalties',
    'Standard PKatt': 'Penalties Attempted'
}, inplace=True)


st.set_page_config(page_title="Club World Cup Dashboard", layout="wide")

st.title("⚽ FIFA Club World Cup Team Stats")

# Sidebar filters
teams = st.sidebar.multiselect("Select Teams", df['Team'].unique(), default=df['Team'].unique())
stats = st.sidebar.multiselect("Select Stats to Display", df.columns[2:], default=['Goals', 'Shots'])

# Filtered Data
filtered_df = df[df['Team'].isin(teams)]

# Show dataframe
st.subheader("📊 Raw Data")
st.dataframe(filtered_df)

# Bar Chart
if stats:
    for stat in stats:
        fig = px.bar(filtered_df, x='Team', y=stat, title=f'{stat} by Team', text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

# Optional scatter
if 'Shots' in df.columns and 'Goals' in df.columns:
    st.subheader("🎯 Goals vs Shots")
    fig2 = px.scatter(filtered_df, x='Shots', y='Goals', color='Team', hover_name='Team',
                      size='Goals', title="Goals vs Shots")
    st.plotly_chart(fig2, use_container_width=True)
