def solution(s):
  result = 1e9
  modified_str = ""
  # 맨 앞부터 시작해 1개씩 분할부터 n개 분할까지 반복 진행 : 절반개수가 넘어간 분할은 의미가 없음
  for split in range(1, (len(s) // 2) + 1):
    prev = s[0:split]
    cnt = 1
    # 첫분할된 지점 이후부터 끝까지 분할개수만큼 증가하며 반복
    for j in range(split, len(s), split):
      # 이전 상태와 문자열이 같다면
      if prev == s[j:j + split]:
        cnt += 1
      # 이전과 문자열이 같지 않다면 = 더이상 압축X
      else:
        # 반복횟수가 있다면, 압축
        if cnt >= 2:
          modified_str += ( str(cnt) + prev )
        # 반복횟수가 없다면
        else:
          modified_str += prev
        
        # 변수 값들 초기화 : 분할한 이후에 다시 그 뒷 문자열들도 비교해야하기 때문 : 다시 11줄로 돌아감
        prev = s[j:j + split]
        cnt = 1
    # 남는 문자열들 처리 : 이해 안 가는 부분
    modified_str += str(cnt) + prev if cnt >= 2 else prev
    # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    result = min(result, len(modified_str))
  return result