# Java로도 짜보기
# 성공

# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

import datetime

d = datetime.datetime.now()

year = d.year;
month = d.month;
day = d.day;

print("%d-%.2d-%d" %(year, month, day))