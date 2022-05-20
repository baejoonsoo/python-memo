pw=input()

if not pw.islower() or  not pw.isalnum():
  print('오류! 비밀번혹 규칙에 맞지 않습니다')
else:
  print('비밀번호가 설정되었습니다')


