# coding=utf-8
"""
pyRunner插件开发模板

作者：student_2333

根据pyr的wiki编写

如有错误请指正

QQ:3076823485

E-mail:lgc2333@126.com

Telegram:@lgc2333
"""
import mc


def listener(event: str):
    """设置监听器的装饰器函数"""

    def function(func):
        mc.setListener(event, func)
        return func

    return function


@listener('onConsoleInput')  # 后台输入
def onConsoleInput(data):
    print(f'指令数据:{data}')
    # return False # 拦截该事件


@listener('onConsoleOutput')  # 后台输出
def onConsoleOutput(data):
    print(f'输出信息:{data}')
    # return False # 拦截该事件


@listener('onSelectForm')  # 选择表单
def onSelectForm(data):
    print(f'表单ID:{data["formid"]}')
    print(f'表单回传的选择项信息:{data["selected"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onUseItem')  # 使用物品
def onUseItem(data):
    # 注：Win10客户端使用物品事件会在单次点击内触发多次
    print(f'操作方块所在位置:{data["position"]}')
    print(f'物品ID:{data["itemid"]}')
    print(f'物品特殊值:{data["itemaux"]}')
    print(f'物品名称:{data["itemname"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onPlaceBlock')  # 放置方块
def onPlaceBlock(data):
    print(f'操作方块所在位置:{data["position"]}')
    print(f'方块ID:{data["blockid"]}')
    print(f'方块名称:{data["blockname"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onDestroyBlock')  # 破坏方块
def onDestroyBlock(data):
    print(f'操作方块所在位置:{data["position"]}')
    print(f'方块ID:{data["blockid"]}')
    print(f'方块名称:{data["blockname"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onOpenChest')  # 打开箱子
def onOpenChest(data):
    print(f'操作方块所在位置:{data["position"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onOpenBarrel')  # 打开木桶
def onOpenBarrel(data):
    print(f'操作方块所在位置:{data["position"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # 该事件不可拦截


@listener('onCloseChest')  # 关闭箱子
def onCloseChest(data):
    print(f'操作方块所在位置:{data["position"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # 该事件不可拦截


@listener('onCloseBarrel')  # 关闭木桶
def onCloseBarrel(data):
    print(f'操作方块所在位置:{data["position"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # 该事件不可拦截


@listener('onContainerChange')  # 放入取出
def onContainerChange(data):
    print(f'物品ID:{data["itemid"]}')
    print(f'物品数量:{data["itemcount"]}')
    print(f'物品名字:{data["itemname"]}')
    print(f'物品特殊值:{data["itemaux"]}')
    print(f'操作方块所在位置:{data["position"]}')
    print(f'方块ID:{data["blockid"]}')
    print(f'方块名称:{data["blockname"]}')
    print(f'操作格子位置:{data["slot"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # 该事件不可拦截


@listener('onChangeDimension')  # 切换维度
def onChangeDimension(data):
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onMobDie')  # 生物死亡
def onMobDie(data):
    print(f'伤害具体原因ID:{data["dmcase"]}')
    print(f'死亡实体Entity对象:{data["actor1"]}')
    print(f'伤害源实体Entity对象:{data["actor2"]}')
    # 该事件不可拦截


@listener('onMobHurt')  # 生物受伤
def onMobHurt(data):
    # 注：此监听存在相关组件setDamage用于设置伤害值
    print(f'伤害具体原因ID:{data["dmcase"]}')
    print(f'死亡实体Entity对象:{data["actor1"]}')
    print(f'伤害源实体Entity对象:{data["actor2"]}')
    print(f'理论伤害值:{data["damage"]}')
    # return False # 拦截该事件


@listener('onRespawn')  # 玩家重生
def onRespawn(data):
    print(f'玩家Entity对象:{data}')
    # 该事件不可拦截


@listener('onChat')  # 聊天消息
def onChat(data):
    print(f'发送者名字:{data["sender"]}')
    print(f'接收者名字:{data["target"]}')
    print(f'接收到的信息:{data["msg"]}')
    print(f'聊天类型:{data["style"]}')
    # 该事件不可拦截


@listener('onInputText')  # 输入文本
def onInputText(data):
    print(f'输入的文本:{data["msg"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onCommandBlockUpdate')  # 更新命令方块
def onCommandBlockUpdate(data):
    print(f'玩家Entity对象:{data["player"]}')
    print(f'将被更新的新指令:{data["cmd"]}')
    print(f'命令方块模式:{data["mode"]}')
    print(f'是否有条件:{data["condition"]}')
    print(f'是否要红石:{data["redstone"]}')
    print(f'上一次输出:{data["output"]}')
    print(f'命令方块名字:{data["rawname"]}')
    print(f'延迟:{data["delay"]}')
    print(f'命令方块所在位置:{data["position"]}')
    # return False # 拦截该事件


@listener('onInputCommand')  # 输入指令
def onInputCommand(data):
    print(f'玩家输入的指令:{data["cmd"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onCommandBlockPerform')  # 命令方块执行
def onCommandBlockPerform(data):
    print(f'将被执行的指令:{data["cmd"]}')
    print(f'命令方块名称:{data["rawname"]}')
    print(f'执行者所在位置:{data["position"]}')
    print(f'命令方块模式:{data["mode"]}')
    print(f'是否有条件:{data["condition"]}')
    # return False # 拦截该事件


@listener('onPlayerJoin')  # 加入游戏
def onPlayerJoin(data):
    print(f'玩家Entity对象:{data}')
    # 该事件不可拦截


@listener('onPlayerLeft')  # 离开游戏
def onPlayerLeft(data):
    print(f'玩家Entity对象:{data}')
    # 该事件不可拦截


@listener('onPlayerAttack')  # 玩家攻击
def onPlayerAttack(data):
    print(f'被攻击实体Entity对象:{data["actor"]}')
    print(f'玩家Entity对象:{data["player"]}')
    # return False # 拦截该事件


@listener('onLevelExplode')  # 世界爆炸
def onLevelExplode(data):
    print(f'爆炸者实体Entity对象:{data["actor"]}')
    print(f'爆炸点所在位置:{data["position"]}')
    print(f'爆炸者所处维度ID:{data["dimensionid"]}')
    print(f'爆炸强度:{data["power"]}')
    # return False # 拦截该事件


@listener('onSetArmor')  # 玩家穿戴
def onSetArmor(data):
    print(f'玩家Entity对象:{data["player"]}')
    print(f'物品ID:{data["itemid"]}')
    print(f'物品数量:{data["itemcount"]}')
    print(f'物品名字:{data["itemname"]}')
    print(f'物品特殊值:{data["itemaux"]}')
    print(f'操作格子位置:{data["slot"]}')
    # 该事件不可拦截


@listener('onFallBlockTransform')  # 耕地破坏
def onFallBlockTransform(data):
    print(f'玩家Entity对象:{data["player"]}')
    print(f'方块所在位置:{data["position"]}')
    print(f'所处维度ID:{data["dimensionid"]}')
    # return False # 拦截该事件


@listener('onUseRespawnAnchorBlock')  # 使用重生锚
def onUseRespawnAnchorBlock(data):
    print(f'玩家Entity对象:{data["player"]}')
    print(f'方块所在位置:{data["position"]}')
    print(f'所处维度ID:{data["dimensionid"]}')
    # return False # 拦截该事件


@listener('onScoreChanged')  # 计分板改变
def onScoreChanged(data):
    print(f'计分板ID:{data["scoreboardid"]}')
    print(f'玩家分数:{data["playersnum"]}')
    print(f'对象实际名称:{data["objectivename"]}')
    print(f'对象显示名称:{data["objectivedisname"]}')
    # 该事件不可拦截


@listener('onMove')  # 玩家移动
def onMove(data):
    print(f'玩家Entity对象:{data}')
    # 该事件不可拦截


@listener('onPistonPush')  # 活塞推动
def onPistonPush(data):
    print(f'方块名字:{data["blockname"]}')
    print(f'方块ID:{data["blockid"]}')
    print(f'方块坐标:{data["blockpos"]}')
    print(f'活塞坐标:{data["pistonpos"]}')
    print(f'维度ID:{data["dimensionid"]}')
    # 该事件不可拦截


@listener('onEndermanRandomTeleport')  # 末影人随机传送
def onEndermanRandomTeleport(data):
    print(f'末影人Entity对象:{data}')
    # return False # 拦截该事件


@listener('onServerStarted')  # 服务器启动
def onServerStarted():
    # 无参数
    pass  # 事件不可拦截


@listener('onDropItem')  # 物品扔出
def onDropItem(data):
    print(f'扔物品玩家Entity对象:{data["player"]}')
    print(f'物品id:{data["itemid"]}')
    print(f'物品数量:{data["itemcount"]}')
    print(f'物品名称:{data["itemname"]}')
    print(f'物品特殊值:{data["itemaux"]}')
    # return False # 拦截该事件


@listener('onTakeItem')  # 拾取物品
def onTakeItem(data):
    print(f'拾取玩家Entity对象:{data["player"]}')
    print(f'拾取物品Entity对象:{data["actor"]}')
    # return False # 拦截该事件


@listener('onRide')  # 乘坐坐骑
def onRide(data):
    print(f'乘坐玩家Entity对象:{data["actor1"]}')
    print(f'被乘坐生物Entity对象:{data["actor2"]}')
    # return False # 拦截该事件


@listener('onUseFrameBlock')  # 使用物品展示框
def onUseFrameBlock(data):
    print(f'玩家Entity对象:{data["player"]}')
    print(f'方块坐标:{data["blockpos"]}')
    print(f'维度id:{data["dimensionid"]}')
    # return False # 拦截该事件


@listener('onJump')  # 玩家跳跃
def onJump(data):
    print(f'玩家Entity对象:{data}')
    # 该事件不可拦截


@listener('onSneak')  # 玩家潜行
def onSneak(data):
    print(f'玩家Entity对象:{data}')
    # 该事件不可拦截


@listener('onBlockInteracted')  # 方块交互
def onBlockInteracted(data):
    print(f'玩家Entity对象:{data["player"]}')
    print(f'方块坐标:{data["blockpos"]}')
    print(f'方块名称:{data["blockname"]}')
    print(f'方块id:{data["blockid"]}')
    print(f'维度id:{data["dimensionid"]}')
    # 该事件不可拦截


@listener('onFireSpread')  # 火焰蔓延
def onFireSpread(data):
    print(f'方块坐标:{data["blockpos"]}')
    print(f'方块名称:{data["blockname"]}')
    print(f'方块id:{data["blockid"]}')
    print(f'维度id:{data["dimensionid"]}')
    # return False # 拦截该事件


@listener('onBlockExploded')  # 方块爆炸
def onBlockExploded(data):
    print(f'爆炸源实体Entity对象:{data["actor"]}')
    print(f'方块坐标:{data["blockpos"]}')
    print(f'方块名称:{data["blockname"]}')
    print(f'方块id:{data["blockid"]}')
    print(f'维度id:{data["dimensionid"]}')
    # 该事件不可拦截
