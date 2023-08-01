import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pathlib import Path


def by_workingday(df):
    byworkingday_bike = day_bike.groupby(by="workingday").instant.nunique().reset_index()
    byworkingday_bike.rename(columns={"instant": "sum"}, inplace=True)
    byworkingday_bike

    return byworkingday_bike


def by_weather(df):
    byseason_bike = day_bike.groupby(by="weathersit").instant.nunique().reset_index()
    byseason_bike.rename(columns={"instant": "sum"}, inplace=True)
    byseason_bike

    return byseason_bike


day_bike = pd.read_csv("dashboard.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://www.brandcrowd.com/blog/wp-content/uploads/2019/06/bike-share.png")


def workingday(df):
    st.subheader("Working Day")
    fig, ax = plt.figure(figsize=(10, 5))
    sns.barplot(
        y="sum",
        x="workingday",
        data=byworkingday_bike.sort_values(by="workingday", ascending=False),
        ax=ax
    )
    ax.set_title("Bagaimana pengaruh hari kerja mempengeruhi pengunaan bike sharing?", loc="center", fontsize=15)
    ax.set_ylabel("Jumlah Pengguna")
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=15)
    st.pyplot(fig)


def weather(df):
    st.subheader("Weather")

    fig, ax = plt.figure(figsize=(10, 5))
    sns.barplot(
        y="sum",
        x="weathersit",
        data=byseason_bike.sort_values(by="weathersit", ascending=False),
    )
    ax.set_title("Bagaimana kondisi cuaca terhadap banyaknya pengguna bike sharing?", loc="center", fontsize=15)
    ax.set_ylabel("Jumlah Pengguna")
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=15)
    st.pyplot(fig)


if __name__ == "__main__":
    sns.set(style="white")

    st.header("Bike Sharing Dashboard: bike: ")

    copyright = "Copyright © " + "2023 | Bike Sharing Dashboard | All Rights Reserved | " + "Made by : by [@Dinar Wahyu Rahman](https://https://www.linkedin.com/in/dinar-wahyu-rahman-00a405162/)"
    st.caption(copyright)
