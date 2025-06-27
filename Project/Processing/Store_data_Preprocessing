import pandas as pd
import re

store_data = pd.read_csv("/Users/parksung-cheol/Desktop/subway_store_relation/정리/2023년 상권.csv")
subway_time = pd.read_csv("/Users/parksung-cheol/Desktop/subway_store_relation/EDA/clean_subway.csv")

#'역'으로 끝나는 이름을 추출하는 함수
def extract_station_name(location_name):
    match = re.match(r'(.+?역)', location_name)
    if match:
        return match.group(1)
    return None
store_data['역여부'] = store_data['상권_코드_명'].apply(extract_station_name)

# '역여부'가 None이 아닌 행만 필터링
store_data = store_data[store_data['역여부'].notna()]

#필요없는 열 제거
columns_to_drop = list(range(24, 32)) + list(range(47, 55))
store_data = store_data.drop(store_data.columns[columns_to_drop], axis=1)

#호선 열의 각 종류와 개수 계산
line_counts = subway_time['호선'].value_counts()
line_counts_df = line_counts.reset_index()
line_counts_df.columns = ['호선', '개수']

# 호선별 지하철역 리스트 생성
lines = subway_time['호선'].unique()  # 호선 목록 추출
line_stations = {line: subway_time[subway_time['호선'] == line]['역명'].unique() for line in lines}

# 가장 역이 많은 호선 기준으로 행 길이 설정
max_stations = max(len(stations) for stations in line_stations.values())
result_df = pd.DataFrame({
    line: pd.Series(stations).reindex(range(max_stations))
    for line, stations in line_stations.items()
})

# result_df에서 모든 호선의 역 이름 추출
stations_in_result = pd.unique(result_df.values.ravel())
stations_in_result = [station for station in stations_in_result if pd.notna(station)]  # NaN 제거

# filtered_subway_name에서 역여부가 stations_in_result에 있는 행만 필터링
store_data = store_data[store_data['역여부'].isin(stations_in_result)]

# 두 번째와 세 번째 열 삭제
store_data = store_data.drop(store_data.columns[[1, 1]], axis=1)
store_data = store_data.drop(store_data.columns[[1, 1]], axis=1)

# 열 이름 변경
store_data = store_data.rename(columns={'역여부': '역명'})

# 역명을 네 번째 열로 이동
columns = list(store_data.columns)
columns.insert(3, columns.pop(columns.index('역명')))  # '역명' 열을 네 번째 위치로 이동
store_data = store_data[columns]

filtered_values = [20231, 20232, 20233, 20234]
store_data = store_data[store_data.iloc[:, 0].isin(filtered_values)]

store_data.to_csv('store_data.csv', index=False, encoding='utf-8-sig')
