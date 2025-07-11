# 지하철 승하차 인원과 상권 활성화의 관계 분석

## 프로젝트 개요

이 프로젝트는 서울 지하철역 인근의 유동 인구 데이터를 기반으로 지역별 상권의 특성을 분석하고, 그에 맞는 전략적 제안을 도출하는 것을 목표로 한다. 특히 대학가, 직장가, 주거지 등으로 지역을 분류한 후, 시간대별 승하차 인원 데이터를 활용하여 상권의 활성화 양상을 비교·분석하였다.

## 분석 목적

- 지하철역 주변 상권을 유형별로 분류하여 특성 파악
- 시간대별 유동 인구 흐름을 기반으로 주요 이용자층과 이용 시간대 분석
- 각 유형별 지역에 맞는 상권 활성화 전략 제시

## 사용 데이터 및 분석 방법

- 서울교통공사 시간대별 지하철 승하차 인원 데이터
- 서울 열린데이터 광장의 상권 분석 자료
- Python(pandas, matplotlib 등)을 활용한 시각화 및 데이터 전처리
- 유형별 비교 분석을 위한 정성적 분류 기준 활용

## 지역 유형별 분석 및 전략 제안

### 1. 대학가 중심역

**특징**
- 평일 유동 인구는 대부분 학생으로 구성되어 있음
- 주말 유입 인구가 급감해 요일 간 유동 인구 차이가 큼
- 낮 시간대와 저녁 시간대에 상권이 주로 활성화됨

**전략 제안**
- 점심 및 저녁 시간대에 학생 대상 할인 혜택, 행사, 쿠폰 제공
- 외부 방문객 유입을 위한 빈 강의실 활용 문화행사 개최
- 대학 특성에 맞춘 테마 거리 조성

### 2. 직장생활 중심역

**특징**
- 출퇴근 시간대 유동 인구가 집중되어 있음
- 점심시간에는 이동이 많아 유동 인구가 급증함
- 주말 매출 및 유동 인구는 상대적으로 낮음

**전략 제안**
- 점심시간 중심의 프로모션 및 회사 대상 식사 장소 마케팅 강화
- 기업과 협력한 축제 개최, 회식 수요를 반영한 저녁 메뉴 구성
- 주말에는 가족 단위 대상 체험 행사 또는 마켓 기획

### 3. 주거 밀집 지역

**특징**
- 출근 전(오전)과 퇴근 후(저녁)에 유동 인구가 집중됨
- 낮 시간대에는 주부 및 고령층이 주요 이용자층
- 저녁 및 주말 시간대에 상권이 가장 활발함

**전략 제안**
- 저녁 및 주말 시간대에 가족 단위 이벤트 개최
- 오전 시간대에는 학생 및 직장인 대상 할인 광고 운영
- 지하철역 내 광고 공간 활용, 지역 기반 커뮤니티 앱과 연계

## 주요 인사이트

- 단순한 유동 인구 숫자보다, 시간대별 이용자층의 특성이 상권 운영에 더 큰 영향을 미친다.
- 각 역세권은 기능적 성격이 다르기 때문에, 획일적인 마케팅보다는 맞춤형 전략이 필요하다.
- 데이터를 통해 확인한 시간대별 유동 흐름은 매출과 직접적으로 연결되어 있으며, 이를 기반으로 한 전략 수립이 효과적이다.

## 결론

지하철 승하차 데이터는 단순한 이동 정보 이상으로 상권의 흐름을 이해하는 데 유용한 도구이다. 본 분석을 통해 상권의 시간적, 공간적 특성을 이해하고, 유형별 전략을 수립함으로써 실질적인 마케팅 방향을 제시할 수 있었다. 향후에는 카드매출, 상점 분포, 부동산 데이터 등과 연계한 추가 분석이 가능하며, 실시간 데이터 연동을 통해 더 정밀한 예측 시스템도 개발할 수 있을 것이다.

## 팀 구성

- 박성철 (2021092460)
- 황원준 (2021078031)
- 강정원 (2023040755)
