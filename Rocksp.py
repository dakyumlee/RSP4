import random

a = print(input("가위 바위 보 >>> "))

com = random.randint(1,3)

win = 0
lose = 0
tie = 0

while(True):
  def Rocksp():
    a = print(input("가위 바위 보 >>> "))
    if (a == "가위"):
      a = 1
    elif (a == "바위"):
      a = 2
    elif (a == "보"):
      a = 3
  
  if (a == com):
    print("비겼습니다!")
    tie+=1
  elif (a == 1 and com == 3) or (a == 2 and com == 1) or (a == 3 and com == 2):
    print("이겼습니다!")
    win+=1
  else:
    print("졌습니다!")
    lose+=1

  Q = input("다시 실행하시겠습니까? 네/ 아니오 >>>")
  if Q != "네":
    break
  Rocksp()

print("당신이 이긴 횟수: ", win)
print("당신이 진 횟수: ", lose)
print("당신이 비긴 횟수: ",tie)
