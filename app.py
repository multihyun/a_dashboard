import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the dashboard
st.title('Sample Streamlit Dashboard')
st.title('집에 재발 보내주십쇼...')


# barain bahrain grand prix
import pandas as pd

# CSV 파일을 로드합니다.
qualifying_df = pd.read_csv('./data2/qualifying.csv')
circuits = pd.read_csv('./data2/circuits.csv')
constructors_df = pd.read_csv('./data2/constructors.csv')
drivers_df = pd.read_csv('./data2/drivers.csv')
races_df = pd.read_csv('./data2/races.csv')

# qualifying을 races와 raceId로 병합합니다.
merged_df1 = pd.merge(qualifying_df, races_df, on='raceId', how='left')

# 결과를 constructors와 constructorId로 병합합니다.
merged_df2 = pd.merge(merged_df1, constructors_df, on='constructorId', how='left')

# 결과를 drivers와 driverId로 병합합니다.
merged_df3 = pd.merge(merged_df2, drivers_df, on='driverId', how='left')

# circuitId가 3인 행만 포함하도록 필터링합니다.
filtered_df = merged_df3[merged_df3['circuitId'] == 3]

# 필요한 열을 선택합니다.
result_df = filtered_df[['year', 'raceId', 'name_x', 'name_y', 'surname', 'q3']]

# 명확성을 위해 열 이름을 변경합니다.
result_df.columns = ['year', 'raceId', 'race_name', 'constructor_name', 'driver_surname', 'q3']

# q3 열이 숫자가 아닌 값을 포함할 수 있으므로 이를 처리합니다.
# 'q3' 값을 숫자로 변환 (예: '01:30.6' 형식에서 초 단위로 변환)
def convert_time_to_seconds(time_str):
    if time_str == 'NULL' or pd.isnull(time_str):
        return np.nan
    try:
        mins, secs = map(float, time_str.split(':'))
        return mins * 60 + secs
    except ValueError:
        return np.nan

result_df['q3'] = result_df['q3'].apply(convert_time_to_seconds)

# null 값을 제거합니다.
result_df = result_df.dropna(subset=['q3'])

# 'year'와 'raceId'를 기준으로 정렬합니다.
result_df = result_df.sort_values(by=['year', 'raceId'])

# x, y 데이터를 준비합니다.
bahrain_x = result_df['year']
bahrain_y = result_df['q3']

# 데이터프레임 시각화
st.write('### Chart')
if option == 'Line Chart':
    st.line_chart(data.set_index('x'))
elif option == 'Bar Chart':
    fig, ax = plt.subplots()
    ax.bar(bahrain_x, bahrain_y)
    st.pyplot(fig)

# Sidebar for user input
st.sidebar.header('User Input Parameters')
n = st.sidebar.slider('Number of data points', 10, 100, 50)
option = st.sidebar.selectbox('Select a chart type', ('Line Chart', 'Bar Chart'))

# Generate random data
data = pd.DataFrame({
    'x': np.arange(n),
    'y': np.random.randn(n).cumsum()
})

# Display the data
st.write('### Generated Data', data)

# Plot the data
st.write('### Chart')
if option == 'Line Chart':
    st.line_chart(data.set_index('x'))
elif option == 'Bar Chart':
    fig, ax = plt.subplots()
    ax.bar(data['x'], data['y'])
    st.pyplot(fig)

# Adding a map
st.write('### Map')
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

titanic = pd.read_csv('./data/titanic.csv')
st.write(titanic)
qualifying_df = pd.read_csv('./data2/qualifying.csv')
circuits = pd.read_csv('./data2/circuits.csv')
constructors_df = pd.read_csv('./data2/constructors.csv')
drivers_df = pd.read_csv('./data2/drivers.csv')
races_df = pd.read_csv('./data2/races.csv')


#streamlit run app.py