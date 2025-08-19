import random 
choice=input()
hand={'グー','チョキ','パー'}
C_choice=random.choice()
print('あなた：',choice)
print('相手：',C_choice)
if(choice==C_choice):
    print('->あいこ')
elif(choice=='グー'&&C_choice=='チョキ'||choice=='チョキ'&&C_choice=='パー'||choice=='パー'&&C_choice=='グー'):
    print('->勝ち!')    
elif(choice=='グー'&&C_choice=='パー'||choice=='チョキ'&&C_choice=='グー'||choice=='パー'&&C_choice=='チョキ'):
    print('->負け!')    
else:
    print("error")    