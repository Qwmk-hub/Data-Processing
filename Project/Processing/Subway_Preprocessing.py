#라이브러리 불러오기
import pandas as pd

subway_time = pd.read_csv("original_dataset/subway_data.csv")

#각 시간대에 열들을 합쳐 새로운 열 생성
subway_time['06~11시간대'] = subway_time.iloc[:, 7:12].sum(axis=1)
subway_time['11~14시간대'] = subway_time.iloc[:, 12:15].sum(axis=1)
subway_time['14~17시간대'] = subway_time.iloc[:, 15:18].sum(axis=1)
subway_time['17~21시간대'] = subway_time.iloc[:, 18:22].sum(axis=1)
subway_time['21~24시간대'] = subway_time.iloc[:, 22:25].sum(axis=1)

#필요없는 열 삭제, 전날24시이후 열 생성
subway_time = subway_time.drop(subway_time.columns[list(range(7, 25))], axis=1)
subway_time = subway_time.sort_values(by=['호선', '역번호', '역명', '승하차구분', '수송일자']).reset_index(drop=True)
subway_time['전날24시이후'] = None

#전날24시이후 값 할당
subway_time['수송일자'] = pd.to_datetime(subway_time['수송일자'])
for i in range(1, len(subway_time)):
    if (subway_time.loc[i, '수송일자'] == subway_time.loc[i-1, '수송일자'] + pd.Timedelta(days=1) and
        subway_time.loc[i, '호선'] == subway_time.loc[i-1, '호선'] and
        subway_time.loc[i, '역번호'] == subway_time.loc[i-1, '역번호'] and
        subway_time.loc[i, '역명'] == subway_time.loc[i-1, '역명'] and
        subway_time.loc[i, '승하차구분'] == subway_time.loc[i-1, '승하차구분']):
        subway_time.loc[i, '전날24시이후'] = subway_time.loc[i-1, '24시이후']

# '00~06시간대' 열 생성 (06시이전 + 전날24시이후)
subway_time['00~06시간대'] = subway_time['06시이전'] + subway_time['전날24시이후'].fillna(0)
cols = list(subway_time.columns)
new_position = 8
cols.insert(new_position, cols.pop(cols.index('00~06시간대')))
subway_time = subway_time[cols]
subway_time = subway_time.drop(subway_time.columns[[6,7, 14]], axis=1)

# 역명 열의 고유한 값(종류) 추출
unique_station_names = subway_time['역명'].unique()

# 괄호와 괄호 안의 내용 제거
subway_time['역명'] = subway_time['역명'].str.replace(r'\(.*?\)', '', regex=True).str.strip()
subway_time['역명'] = subway_time['역명'].replace({'서울역': '서울'})
subway_time['역명'] = subway_time['역명'] + '역'

#저장
subway_time.to_csv("/Users/parksung-cheol/Desktop/real/Preprocessing_data/subway_preprocessing.csv", index=False, encoding='utf-8-sig')
