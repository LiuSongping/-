print('-'*30,'欢迎','-'*30)

print('请选择你的性别:')
print('\t 1.男')
print('\t 2.女')
print('-'*82)
player_chocie=input('请选择[1,2]:')
if player_chocie=='1':
    print('你是男性')
elif player_chocie=='2':
    print('你是女性')
else:
    print('对不起，没有这个选项，默认男性！')

x=2 #能量
y=2 #战斗力
lv=1 #级别

boss_x=100 #boss能量
boss_y=100 #boss战斗力

print('-'*82)
print(f'你的级别为{lv},你的能量为{x}，你的战斗力为{y}')
while True:
    print('-'*82)
    print('请选择你要进行的操作:')
    print('\t 1.练级')
    print('\t 2.打怪')
    print('\t 3.撤退')
    c=input('请选择你的操作[1-3]:')
    if c=='1':
        x+=2
        y+=2
        lv+=1
        print('-'*82)
        print(f'恭喜升级，你现在的级别为{lv},能量为{x}，战斗力为{y}')
    elif c=='2':
        print('发现妖怪并攻击')
        boss_x-=y
        if boss_x<=0:
            print(f'妖怪受到{y}点伤害，死，你赢了！GAME OVER')
            break
        x-=boss_y
        print(f'妖怪攻击你')
        if x<=0:
            print(f'你受到了{妖怪_y}点伤害，死！GAME OVER')
            break
    elif c=='3':
        print('-'*82)
        print('你选择撤退，但被打死！GAME OVER')
        break
    else:
        print('-'*82)
        print('输入有误，重新输入')
input('回车键退出：')
