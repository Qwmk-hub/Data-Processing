import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = '/Users/parksung-cheol/Desktop/데이터처리 프로젝트 데이터/나눔 글꼴/나눔명조/NanumFontSetup_TTF_MYUNGJO/NanumMyeongjoExtraBold.ttf'
fontprop = fm.FontProperties(fname=font_path)

real_subway = pd.read_csv("/Users/parksung-cheol/Desktop/데이터처리 프로젝트 데이터/진짜 지하철.csv")

data_cols = [col for col in real_subway.columns if '승차인원' in col or '하차인원' in col]
time_intervals = list(set(col.split(' ')[0] for col in data_cols))

reshaped_data = []
for _, row in real_subway.iterrows():
    for time in time_intervals:
        if f'{time} 승차인원' in row:
            reshaped_data.append({
                '사용월': row['사용월'],
                '호선명': row['호선명'],
                '지하철역': row['지하철역'],
                '시간대': time,
                '인원수': row[f'{time} 승차인원'],
                '승하차여부': '승차'
            })
        if f'{time} 하차인원' in row:
            reshaped_data.append({
                '사용월': row['사용월'],
                '호선명': row['호선명'],
                '지하철역': row['지하철역'],
                '시간대': time,
                '인원수': row[f'{time} 하차인원'],
                '승하차여부': '하차'
            })

reshaped_df = pd.DataFrame(reshaped_data)
reshaped_df['지하철역'] = reshaped_df['지하철역'].str.replace(r'\(.*?\)', '', regex=True)

clean_subway = pd.read_csv("/Users/parksung-cheol/Desktop/데이터처리 프로젝트 데이터/EDA/clean_subway.csv")
line_2_data = clean_subway[clean_subway['호선'] == '2호선']
aggregated_line_2 = (
    line_2_data
    .drop(columns=['승하차구분'])
    .groupby(['호선', '역명'], as_index=False)
    .sum()
)

time_labels = ['00~06', '06~11', '11~14', '14~17', '17~21', '21~24']
gangnam_data = aggregated_line_2[aggregated_line_2['역명'] == '강남역']
y_values = gangnam_data[time_labels].values.flatten()

plt.figure(figsize=(10, 6))
plt.plot(time_labels, y_values, marker='o', label='강남역')
plt.title('강남역 시간대별 탑승객 수', fontproperties=fontprop)
plt.xlabel('시간대', fontproperties=fontprop)
plt.ylabel('탑승객 수', fontproperties=fontprop)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(prop=fontprop)
plt.show()

stations = ['강남역', '잠실역', '홍대입구역', '신설동역', '한양대역', '충정로역']
station_data = aggregated_line_2[aggregated_line_2['역명'].isin(stations)]

plt.figure(figsize=(12, 8))
colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']
for idx, station in enumerate(stations):
    y_vals = station_data[station_data['역명'] == station][time_labels].values.flatten()
    plt.plot(time_labels, y_vals, marker='o', color=colors[idx], label=station)

plt.title('시간대별 탑승객 수 (6개 역 비교)', fontproperties=fontprop)
plt.xlabel('시간대', fontproperties=fontprop)
plt.ylabel('탑승객 수', fontproperties=fontprop)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(prop=fontprop)
plt.show()

labels = ['한식', '카페', '의류', '편의점']
sizes = [25, 30, 20, 25]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('강남역 주요 업종 비율 (예시)', fontproperties=fontprop)
plt.show()
