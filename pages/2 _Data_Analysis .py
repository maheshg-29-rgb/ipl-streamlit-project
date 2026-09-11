import streamlit as st
import pandas as pd

# -----------------------------------------
# 1. Load Dataset
# -----------------------------------------

df = pd.read_csv("IPL_Matches_Data_2008_2026.csv")

# -----------------------------------------
# 2. Title
# -----------------------------------------

st.title("IPL Data Analysis")

# -----------------------------------------
# 3. Dataset
# -----------------------------------------

st.subheader("Dataset")

st.dataframe(
    df,
    use_container_width=True
)

st.write("First 5 rows")
st.write(df.head())

st.write("Last 5 rows")
st.write(df.tail())

st.write("Dataset shape:", df.shape)

st.write("Columns:")
st.write(df.columns)

# -----------------------------------------
# 4. Dataset Shape
# -----------------------------------------

st.subheader("Dataset Shape")

rows, columns = df.shape

st.write("Rows:", rows)
st.write("Columns:", columns)

# -----------------------------------------
# 5. Missing Values
# -----------------------------------------

missing_values = df.isnull().sum()

st.subheader("Missing Values")

st.dataframe(missing_values)

# -----------------------------------------
# 6. Dataset Metrics
# -----------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Matches",
    len(df)
)

col2.metric(
    "Total Seasons",
    df["season"].nunique()
)

col3.metric(
    "Total Venues",
    df["venue"].nunique()
)

col4.metric(
    "Cities",
    df["city"].nunique()
)

# -----------------------------------------
# 7. Total Runs and Wickets
# -----------------------------------------

df["total_runs"] = (
    df["team1_runs"] +
    df["team2_runs"]
)

df["total_wickets"] = (
    df["team1_wickets"] +
    df["team2_wickets"]
)

# -----------------------------------------
# 8. Average Runs
# -----------------------------------------

average_runs = df["total_runs"].mean()

st.metric(
    "Average Match Runs",
    round(average_runs, 2)
)

# -----------------------------------------
# 9. Highest Combined Score
# -----------------------------------------

highest_score = df["total_runs"].max()

st.metric(
    "Highest Combined Score",
    highest_score
)

# -----------------------------------------
# 10. Prepare Season and Team Lists
# -----------------------------------------

seasons = sorted(
    df["season"].dropna().unique()
)

teams = sorted(
    pd.concat([
        df["team1"],
        df["team2"]
    ]).dropna().unique()
)

# -----------------------------------------
# 11. Sidebar Filters
# -----------------------------------------

st.sidebar.title("Filters")

selected_season = st.sidebar.selectbox(
    "Season",
    seasons
)

selected_team = st.sidebar.selectbox(
    "Team",
    teams
)

# -----------------------------------------
# 12. Filter Dataset
# -----------------------------------------

filtered_df = df[
    (df["season"] == selected_season) &
    (
        (df["team1"] == selected_team) |
        (df["team2"] == selected_team)
    )
]

st.subheader("Filtered Matches")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# -----------------------------------------
# 13. Matches by Season
# -----------------------------------------

st.subheader("Matches by Season")

matches_by_season = (
    df.groupby("season")
    .size()
    .reset_index(name="matches")
)

st.dataframe(matches_by_season)

# -----------------------------------------
# 14. Team Wins
# -----------------------------------------

st.subheader("Team Wins")

team_wins = (
    df["winner"]
    .value_counts()
    .reset_index()
)

team_wins.columns = [
    "Team",
    "Wins"
]

st.dataframe(team_wins)

# -----------------------------------------
# 15. Top 10 Winners
# -----------------------------------------

st.subheader("Top 10 Winning Teams")

top_winners = (
    df["winner"]
    .value_counts()
    .head(10)
)

st.dataframe(top_winners)