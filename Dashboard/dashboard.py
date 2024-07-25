import streamlit as st
import pandas as pd

# Membuat header sebagai judul, subheader sebagai subjudul, dan caption
st.header('Dashboard of Facility of Bike Sharing')
st.subheader('Number of Users by Season and Time of Day')
st.caption('Copyright (c) 2024 | Dimas Septo Nugroho')

# Menotasikan angka menjadi musim yang dimaksud sesuai data
mapped_season = {
    "springer": 1,
    "summer": 2,
    "fall": 3,
    "winter": 4
}

# Membuat list untuk opsi interaktif dengan pengguna
season_list = [
    "springer",
    "summer",
    "fall",
    "winter"
]

# Mengelompokkan data berdasarkan kolom 'season' dan menjumlahkan kolom 'cnt'
def get_grouped_by_season(df):
    grouped_df = df.groupby('season', as_index=False)['cnt'].sum()
    return grouped_df

# Mengelompokkan data berdasarkan kolom 'hr' dan menjumlahkan kolom 'cnt'
def get_grouped_by_hour(df):
    grouped_df = df.groupby('hr', as_index=False)['cnt'].sum()
    return grouped_df

# Membaca file dataset CSV dan menyimpannya ke dalam DataFrame
def get_df_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

def get_chosen_seasons(df, options):
    tmp_season_list = season_list # List semua musim
    for option in options:
        tmp_season_list.remove(option)  # Menghapus musim yang dipilih dari list musim temporary
    for season in tmp_season_list:
        df = df[df['season'] != mapped_season[season]]  # Menghapus data untuk musim yang tidak dipilih
    return df

# Mengubah nama musim
def change_season_name(df):
    df.loc[df['season'] == 1, 'season'] = "springer"
    df.loc[df['season'] == 2, 'season'] = "summer"
    df.loc[df['season'] == 3, 'season'] = "fall"
    df.loc[df['season'] == 4, 'season'] = "winter"
    return df

# 
def main():
    csv_file = "hour.csv"
    df = get_df_from_csv(csv_file)
    

    options = st.multiselect(
        "What do you want to show?",
        season_list,
    )   # Mempersilakan pengguna untuk memilih musim yang ingin ditampilkan

    if options:
        # st.write("You selected:", options)
        df = get_chosen_seasons(df, options)
        df = change_season_name(df)

        # Mengelompokkan data berdasarkan musim dan jam sekaligus
        grouped_by_season = get_grouped_by_season(df)
        grouped_by_hour = get_grouped_by_hour(df)

        # Menampilkan bar chart sesuai permintaan pengguna
        st.bar_chart(grouped_by_season, x="season", y="cnt")
        st.bar_chart(grouped_by_hour, x="hr", y="cnt")
    else:
        st.write('Please select seasons to display the chart!')

main()