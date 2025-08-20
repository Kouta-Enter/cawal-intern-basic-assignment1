"""プレイヤー vs コンピュータのじゃんけん"""
import random
choice=input("input")
hand=['グー','チョキ','パー']
C_choice=random.choice(hand)
print('あなた：',choice)
print('相手：',C_choice)
if choice==C_choice:
    print('->あいこ')
elif choice=='グー' and C_choice=='チョキ'\
    or choice=='チョキ' and C_choice=='パー' \
    or choice=='パー'and C_choice=='グー':
    print('->勝ち!')
elif choice=='グー' and C_choice=='パー' \
    or choice=='チョキ' and C_choice=='グー' \
    or choice=='パー' and C_choice=='チョキ':
    print('->負け!')
else:
    print("error")
