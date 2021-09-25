import requests  # requests 라이브러리 설치 필요

# requests 를 사용해 요청(Request)하기
response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

# 응답(response) 데이터인 json을 쉽게 접근할 수 있게 만들어 city_air 에 담고
city_air = response_data.json()
# 값을 출력

gu_infos = city_air['RealtimeCityAir']['row']

for gu_info in gu_infos:
    if gu_info['PM10'] < 20 :
        print(gu_info['MSRSTE_NM'], gu_info['PM10'])


