import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Baca File csv
data_day_df = pd.read_csv("https://raw.githubusercontent.com/alifya15/Rental-Bike-Data/main/dashboard/main_data.csv")

# mengolah data
data_day_df.sort_values(by="rental_date", inplace=True)
data_day_df['rental_date'] = pd.to_datetime(data_day_df['rental_date'])

# Dashboard
st.title("Selamat datang di Rental Bike Nusantara")
st.markdown("""---""")

# membuat sidebar
option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home', 'Pertanyaan 1', 'Pertanyaan 2')
)
with st.sidebar:
    st.image("https://raw.githubusercontent.com/alifya15/Rental-Bike-Data/main/dashboard/logo.jpg")

if option == 'Home':
    st.write("# Rental Bike Dataset")
    st.write(data_day_df)
    
elif option == 'Pertanyaan 1':
    st.write("# Korelasi antara Suhu, Kelembaban Udara, dan Jumlah Rental Sepeda")
    
    # Scatter plot untuk korelasi suhu dan jumlah sewa sepeda
    plt.figure(figsize=(7, 5))
    sns.scatterplot(x='temp', y='count', data=data_day_df)
    plt.xlabel('Suhu')
    plt.ylabel('Jumlah Rental Sepeda')
    plt.title('Korelasi antara Suhu dan Jumlah Rental Sepeda')
    scatter_fig = plt.gcf()  # Mendapatkan objek gambar
    st.pyplot(scatter_fig)  # Menyertakan objek gambar saat memanggil st.pyplot()

    # Scatter plot untuk korelasi kelembaban udara dan jumlah sewa sepeda
    plt.figure(figsize=(7, 5))
    sns.scatterplot(x='hum', y='count', data=data_day_df)
    plt.xlabel('Kelembaban Udara')
    plt.ylabel('Jumlah Rental Sepeda')
    plt.title('Korelasi antara Kelembaban Udara dan Jumlah Rental Sepeda')
    scatter_fig2 = plt.gcf()  # Mendapatkan objek gambar
    st.pyplot(scatter_fig2)  # Menyertakan objek gambar saat memanggil st.pyplot()

    correlation_temp_count = data_day_df['temp'].corr(data_day_df['count'])
    st.write("Korelasi antara suhu ('temp') dan jumlah Rental sepeda ('count'): ", correlation_temp_count)

    correlation_hum_count = data_day_df['hum'].corr(data_day_df['count'])
    st.write("Korelasi antara kelembaban udara ('hum') dan jumlah Rental sepeda ('count'): ", correlation_hum_count)

    correlation_matrix = data_day_df[['temp', 'hum', 'count']].corr()

    # Heatmap
    st.title('Korelasi antara Suhu, Kelembaban Udara, dan Jumlah Rental Sepeda')
    st.write('Heatmap korelasi antara variabel suhu, kelembaban udara, dan jumlah Rental sepeda')

    # Display heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Korelasi antara Suhu, Kelembaban Udara, dan Jumlah Rental Sepeda')
    st.pyplot(fig)
    st.write('Tabel Korelasi:')
    st.write(correlation_matrix)
    

    #Conclusion
    st.subheader("Conclusion")
    st.write("Dilihat dari hasil korelasi di peroleh bahwa temperatur sangat mempengaruhi jumlah rental sepeda dengan nilai 0.62 sedangkan kelembaban udara memperoleh hasil -0.10 yang berarti kelembaban udara tidak mempengaruhi jumlah rental sepeda")

elif option == 'Pertanyaan 2':
    st.write("# Perbedaan Jumlah Rental Sepeda antara working day dan holiday")

    # Total rental sepeda berdasarkan hari kerja
    st.subheader('Total rental sepeda berdasarkan working day:')
    workingday_rental = data_day_df[['workingday','casual','registered','count']].groupby(by='workingday').sum().reset_index()
    st.write(workingday_rental)

    # Plot jumlah rental sepeda berdasarkan hari kerja
    st.subheader('Plot jumlah rental sepeda berdasarkan working day:')
    fig, ax = plt.subplots(figsize=(8, 6))
    workingday_rental.plot(kind='bar', x='workingday', y=['casual', 'registered', 'count'], ax=ax)
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    plt.xlabel('Holiday')
    plt.ylabel('Total')
    plt.title('Number of Rentals in Holiday')
    plt.xticks([1, 0], ['Hari Kerja', 'Hari libur'], rotation=0)
    plt.legend(['Casual', 'Registered', 'count'])
    bar_fig = plt.gcf()  # Mendapatkan objek gambar
    st.pyplot(bar_fig)  # Menyertakan objek gambar saat memanggil st.pyplot()

    # Total rental sepeda berdasarkan hari libur
    st.subheader('Total rental sepeda berdasarkan holiday:')
    holiday_rental = data_day_df[['holiday','casual','registered','count']].groupby(by='holiday').sum().reset_index()
    st.write(holiday_rental)

    # Plot jumlah sewa sepeda berdasarkan hari libur
    st.subheader('Plot jumlah rental sepeda berdasarkan holiday:')
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    holiday_rental.plot(kind='bar', x='holiday', y=['casual', 'registered', 'count'], ax=ax2)
    for p in ax2.patches:
        ax2.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    plt.xlabel('Holiday')
    plt.ylabel('Total')
    plt.title('Number of Rentals in Holiday')
    plt.xticks([0, 1], ['Tidak Libur', 'Libur'], rotation=0)
    plt.legend(['Casual', 'Registered', 'count'])
    bar_fig2 = plt.gcf()  # Mendapatkan objek gambar
    st.pyplot(bar_fig2)  # Menyertakan objek gambar saat memanggil st.pyplot()

    st.subheader("Conclusion")
    st.write("dilihat dari hasil yang diperoleh dapat di simpulkan bahwa jumlah rental sepeda mencapai 3.292.679. Rental sepeda paling banyak di lakukan saat working day dibandingkan pada saat holiday. Variabel yang banyak melakukan rental saat working day adalah register dengan total mencapai 1.989.125")
