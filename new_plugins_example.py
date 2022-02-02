# 由我什么都布吉岛编写
# 2022.2.2
import mc # 导入mc模块 必需！

def joinFunction(data): # 函数
    player = data['Player']
    print(f"玩家:{player} 加入了服务器")
    mc.explode(x, y, z, 0, 25, True, 25, True)


mc.setListener('onJoin', joinFunction)
