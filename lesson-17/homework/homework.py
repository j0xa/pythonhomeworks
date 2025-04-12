import pandas as pd
import sqlite3
import os
import openpyxl
os.chdir(r"C:\Users\User\Documents\GitHub\python_homework\lesson-17\homework")

with sqlite3.connect("../data/chinook.db") as connection:
    df_customers = pd.read_sql(
        "SELECT * FROM customers",
        con=connection
    )
    df_invoices = pd.read_sql(
        "SELECT * FROM invoices",
        con=connection
    )

inner_join = pd.merge(df_customers, df_invoices, on="CustomerId", how="inner")
total_invoices = inner_join.groupby(["CustomerId", "FirstName", "LastName"]).size().reset_index(name="TotalInvoices")
total_invoices.head()

df_movie = pd.read_csv("../data/movie.csv")
df_movie_1 = df_movie[["director_name", "color"]]
df_movie_2 = df_movie[["director_name", "num_critic_for_reviews"]]
left_join = pd.merge(df_movie_1, df_movie_2, on="director_name", how="left")
outer_join = pd.merge(df_movie_1, df_movie_2, on="director_name", how="outer")
print(f"Left join rows: {left_join.shape[0]}")
print(f"Outer join rows: {outer_join.shape[0]}")

df_titanic = pd.read_excel("../data/titanic.xlsx")
df_titanic_info = df_titanic.groupby("Pclass").agg({
    "Age":"mean",
    "Fare":"sum",
    "PassengerId":"count"
}).reset_index()
df_titanic_info.columns = ["Pclass", "Age", "Fare", "TotalPassengers"]
df_titanic_info

df_multi_level_grouping = df_movie.groupby(["color", "director_name"]).agg(
    {
        "num_critic_for_reviews":"sum",
        "duration":"mean"
    }
).reset_index()
df_multi_level_grouping


df_flights = pd.read_parquet("../data/flights")
df_nested_group_flights =df_flights.groupby(["Year", "Month"]).agg(
    {
        "FlightId":"count",
        "ArrDelay":"mean",
        "DepDelay":"max"

    }
)

def child_or_adult(age):
    if not (age>0): return
    elif age<18: return "Child"
    else: return "Adult"
df_titanic["Age_Group"] = df_titanic["Age"].transform(child_or_adult)
df_titanic.sample(4)

df_employee = pd.read_csv("../data/employee.csv")
def min_max_normalize(series):
    return (series-series.min())/(series.max()-series.min())
df_employee["NORMALIZED_SALARY"] = df_employee.groupby("DEPARTMENT")["BASE_SALARY"].transform(min_max_normalize)
df_employee.head(5)

def movie_duration(duration):
    if not duration>=0: return
    elif duration<60: return "Short"
    elif duration<120: return "Medium"
    else: return "Long"

df_movie["duration_type"] = df_movie["duration"].apply(movie_duration)
df_movie[["duration", "duration_type"]].sample(5)

def filter_passengers(df):
    return df[df["Survived"]==1].copy()
def fill_ages(df):
    df.loc[:,"Age"] = df["Age"].fillna(df["Age"].mean())
    return df
def new_column(df):
    df.loc[:,"Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

df_titanic_pipe = (df_titanic.pipe(filter_passengers).pipe(fill_ages).pipe(new_column))
df_titanic_pipe.sample(5)

def filter_departure_delay(df):
    return df[df["Delay"]>30]
def delay_per_hour(df):
    df["Delay_Per_Hour"] = df["Delay"]/df["Duration"]
    return df
df_flights.pipe(filter_departure_delay).pipe(delay_per_hour)