# 백준 1546 평균구하기

# 입력
# 1번째 줄에 시험을 본 과목의 개수 N이 주어진다. 해당 값은 1000보다 작거나 같다
# 2번째 줄에 세준이의 현재 성적이 주어진다. 해당 값은 100보다 작거나 같은, 음이 아닌 정수이고, 적어도 1개의 값은 0보다 크다

# 출력
# 1번째 줄에 새로운 평균을 출력한다.
# 실제 정답과 출력값의 절대 오차 또는 상대 오차가 10^-2 면 정답

n = int(input()) # 0 < n <= 1000
grade = list(map(float,input().split()))
max_grade = max(grade)
sum_grade = 0
for i in grade:
    new_grade = (i/max_grade) * 100
    sum_grade += float(new_grade)
new_avg = sum_grade/n
print(new_avg)


