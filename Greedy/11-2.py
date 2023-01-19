s = input()
split_s = s.split()
# 원소를 문자열에서 정수로 변경한 리스트
s_list = list(map(int, split_s))

for i in range(s):
  # 0이나 1이면 덧셈 연산자
  if s[i] == 0 or s[i] == 1:
    
    split_s.insert(i+1, '+')
  # 나머지 값들은 곱셈 연산자
  else:
    split_s.insert(i+1, '*')