# coding=utf-8
"""
BDSPyRunner插件开发模板

作者：student_2333

根据pyr源代码编写，如有错误请指正
"""
import mc


def listener(event: str):
    """设置监听器的装饰器函数"""

    def function(func):
        mc.setListener(event, func)
        return func

    return function


@listener('onPreJoin')
def onPreJoin(data):
    """
    玩家加入服务器(前) 监听 --> 建议初始化数据操作、无法发送消息及表单
    """
    print(f'事件名：{data["Event"]}')
    print(f'玩家IP地址：{data["IP"]}')
    print(f'玩家：{data["Player"]}')
    print(f'玩家的XUID值（相当于唯一标识符）：{data["XUID"]}')
    # return False  # 拦截此事件


@listener('onJoin')
def onJoin(data):
    """
    玩家加入服务器（后）监听 --> 可发送消息表单
    """
    print(f'事件名：{data["Event"]}')
    print(f'玩家：{data["Player"]}')
    # 无法拦截此事件


@listener('onLeft')
def onLeft(data):
    """
    玩家离开服务器监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'玩家：{data["Player"]}')
    print(f'玩家的XUID值（相当于唯一标识符）：{data["XUID"]}')
    # 无法拦截此事件


@listener('onPlayerCmd')
def onPlayerCmd(data):
    """
    玩家输入指令监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'指令文本：{data["Command"]}')
    print(f'玩家：{data["Player"]}')
    print(f'是否执行成功：{data["isSuccess"]}')
    # return False  # 拦截此事件


@listener('onChat')
def onChat(data):
    """
    聊天监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'聊天内容：{data["Message"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onPlayerDie')
def onPlayerDie(data):
    """
    玩家死亡监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'死亡的玩家：{data["Player"]}')
    print(f'死亡原因：{data["Cause"]}')
    print(f'导致玩家死亡的实体 （可能为NULL）：{data["Entity"]}')
    # 无法拦截此事件


@listener('onRespawn')
def onRespawn(data):
    """
    玩家重生监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'重生的玩家：{data["Player"]}')
    # 无法拦截此事件


@listener('onChangeDim')
def onChangeDim(data):
    """
    玩家切换维度监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'切换维度的玩家：{data["Player"]}')
    print(f'维度ID （0：主世界）（1：下界）（2：末地）：{data["ToDimensionId"]}')
    # 无法拦截此事件


@listener('onJump')
def onJump(data):
    """
    玩家跳跃监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onSneak')
def onSneak(data):
    """
    玩家潜伏监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'玩家：{data["Player"]}')
    print(f'潜伏ID （0:站立）（1：潜伏中）：{data["IsSneaking"]}')
    # return False  # 拦截此事件


@listener('onAttack')
def onAttack(data):
    """
    玩家攻击监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'造成的伤害值：{data["AttackDamage"]}')
    print(f'玩家：{data["Player"]}')
    print(f'被攻击目标：{data["Target"]}')
    # return False  # 拦截此事件


@listener('onEat')
def onEat(data):
    """
    玩家吃食物监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'食物：{data["FoodItem"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 未知是否可拦截此事件


@listener('onMove')
def onMove(data):
    """
    玩家移动监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'玩家：{data["Player"]}')
    print(f'玩家坐标 【list[float]类型】：{data["Pos"]}')
    # return False  # 未知是否可拦截此事件


@listener('onChangeSprinting')
def onChangeSprinting(data):
    """
    玩家疾跑状态切换监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'是否正在疾跑：{data["IsSprinting"]}')
    print(f'：{data["Player"]}')
    # return False  # 未知是否可拦截此事件


@listener('onSpawnProjectile')
def onSpawnProjectile(data):
    """
    投射物生成监听
    """
    print(f'事件名：{data["Event"]}')
    # print(f'{data["Identifier"]}')
    print(f'来源：{data["Shooter"]}')
    print(f'投射物：{data["Type"]}')
    # return False  # 未知是否可拦截此事件


@listener('onSetArmor')
def onSetArmor(data):
    """
    玩家装备改变监听【进入服务器会优先调用此监听-->和onPreJoin等级一样】
    """
    print(f'事件名：{data["Event"]}')
    print(f'装备名：{data["ArmorItem"]}')
    print(f'玩家：{data["Player"]}')
    print(f'格子ID：{data["Slot"]}')
    # 无法拦截此事件


@listener('onRide')
def onRide(data):
    """
    骑乘监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'骑乘者：{data["Rider"]}')
    print(f'被骑乘者：{data["Vehicle"]}')
    # return False  # 拦截此事件


@listener('onUseItem')
def onUseItem(data):
    """
    玩家右键使用物品监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'物品：{data["ItemStack"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onTakeItem')
def onTakeItem(data):
    """
    玩家拿起物品监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'物品对象：{data["ItemEntity"]}')
    print(f'物品：{data["ItemStack"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onDropItem')
def onDropItem(data):
    """
    玩家丢弃物品监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'物品：{data["ItemStack"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onUseItemOn')
def onUseItemOn(data):
    """
    玩家对方块右键使用物品监听

    注：Win10、Win11客户端玩家右键会在服务端连续多次激发这个事件
    """
    print(f'事件名：{data["Event"]}')
    print(f'目标方块：{data["BlockInstance"]}')
    print(f'物品：{data["ItemStack"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 未知是否可拦截此事件


@listener('onInventoryChange')
def onInventoryChange(data):
    """
    玩家背包物品改变监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'新放入的物品：{data["NewItemStack"]}')
    print(f'玩家：{data["Player"]}')
    print(f'原来的物品：{data["PreviousItemStack"]}')
    print(f'背包格子ID：{data["Slot"]}')
    # 无法拦截此事件


@listener('onChangeArmorStand')
def onChangeArmorStand(data):
    """
    盔甲架装备改变监听
    """
    print(f'事件名：{data["Event"]}')
    # print(f'{data["ArmorStand"]}')
    print(f'玩家：{data["Player"]}')
    print(f'玩家格子ID：{data["Slot"]}')
    # 无法拦截此事件


@listener('onStartDestroyBlock')
def onStartDestroyBlock(data):
    """
    开始挖掘方块监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'方块对象：{data["BlockInstance"]}')
    print(f'玩家：{data["Player"]}')
    # 无法拦截此事件


@listener('onDestroyBlock')
def onDestroyBlock(data):
    """
    方块被破坏监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'方块对象：{data["BlockInstance"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onPlaceBlock')
def onPlaceBlock(data):
    """
    放置方块监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'方块对象：{data["BlockInstance"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onOpenContainer')
def onOpenContainer(data):
    """
    打开容器监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'容器名称：{data["BlockInstance"]}')
    # print(f'{data["Container"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onCloseContainer')
def onCloseContainer(data):
    """
    关闭容器监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'容器名称：{data["BlockInstance"]}')
    # print(f'{data["Container"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onContainerChange')
def onContainerChange(data):
    """
    容器内容改变
    """
    print(f'事件名：{data["Event"]}')
    print(f'操作实体：{data["Actor"]}')
    print(f'被操作容器：{data["BlockInstance"]}')
    # print(f'：{data["Container"]}')
    print(f'新物品：{data["NewItemStack"]}')
    print(f'操作玩家：{data["Player"]}')
    print(f'旧物品：{data["PreviousItemStack"]}')
    print(f'格子ID：{data["Slot"]}')
    # 无法拦截此事件


# @listener('onBlockExplode')
# def onBlockExplode(data):
#    """
#    方块被爆炸破坏
#    """
#    print(f'事件名：{data["Event"]}')
#    print(f'：{data["BlockInstance"]}')
#    print(f'：{data["Breaking"]}')
#    print(f'：{data["Fire"]}')
#    print(f'：{data["MaxResistance"]}')
#    print(f'：{data["Radius"]}')
#    # return False  # 拦截此事件


@listener('onMobDie')
def onMobDie(data):
    """
    生物死亡监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'死亡的实体对象：{data["Mob"]}')
    print(f'：{data["Cause"]}')
    print(f'伤害来源的实体对象（可能为Null）：{data["Entity"]}')
    # 无法拦截此事件


@listener('onMobHurt')
def onMobHurt(data):
    """
    生物受伤（包括玩家）
    """
    print(f'事件名：{data["Event"]}')
    print(f'受伤的实体对象：{data["Mob"]}')
    print(f'受伤原因：{data["Cause"]}')
    print(f'伤害来源的实体对象（可能为Null）：{data["Entity"]}')
    # return False  # 拦截此事件


@listener('onCmdBlockExecute')
def onCmdBlockExecute(data):
    """
    命令方块执行监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'方块对象：{data["BlockInstance"]}')
    print(f'指令文本：{data["Command"]}')
    print(f'命令是否由命令方块矿车执行：{data["IsMinecart"]}')
    print(f'命令方块矿车对象：{data["Minecart"]}')
    # return False  # 拦截此事件


@listener('onRedStoneUpdate')
def onRedStoneUpdate(data):
    """
    红石更新监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'被更新方块：{data["BlockInstance"]}')
    print(f'是否被激活：{data["IsActivated"]}')
    print(f'红石能量等级：{data["RedStonePower"]}')
    # 未知是否可拦截此事件


@listener('onProjectileHitEntity')
def onProjectileHitEntity(data):
    """

    """
    print(f'事件名：{data["Event"]}')
    print(f'发射的弹射物实体：{data["Source"]}')
    print(f'被击中的实体对象：{data["Target"]}')
    # 无法拦截此事件


@listener('onProjectileHitBlock')
def onProjectileHitBlock(data):
    """
    方块被弹射物击中
    """
    print(f'事件名：{data["Event"]}')
    print(f'被击中的方块：{data["BlockInstance"]}')
    print(f'发射的弹射物实体：{data["Source"]}')
    # 未知是否可拦截此事件


@listener('onBlockInteracted')
def onBlockInteracted(data):
    """
    方块交互监听
    """
    print(f'事件名：{data["Event"]}')
    print(f'方块名称：{data["BlockInstance"]}')
    print(f'玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onUseRespawnAnchor')
def onUseRespawnAnchor(data):
    """
    玩家使用重生锚
    """
    print(f'事件名：{data["Event"]}')
    print(f'被使用的重生锚：{data["BlockInstance"]}')
    print(f'使用重生锚的玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onFarmLandDecay')
def onFarmLandDecay(data):
    """
    耕地退化
    """
    print(f'事件名：{data["Event"]}')
    print(f'造成耕地退化的实体：{data["Actor"]}')
    print(f'退化的耕地：{data["BlockInstance"]}')
    # return False  # 拦截此事件


@listener('onUseFrameBlock')
def onUseFrameBlock(data):
    """
    操作物品展示框
    """
    print(f'事件名：{data["Event"]}')
    print(f'被操作的物品展示框：{data["BlockInstance"]}')
    print(f'操作物品展示框的玩家：{data["Player"]}')
    print(f'操作类型：{data["Type"]}')
    # return False  # 拦截此事件


@listener('onPistonPush')
def onPistonPush(data):
    """
    活塞推动
    """
    print(f'事件名：{data["Event"]}')
    print(f'正在工作的活塞：{data["PistonBlockInstance"]}')
    print(f'被推动的方块：{data["TargetBlockInstance"]}')
    # return False  # 拦截此事件


@listener('onHopperSearchItem')
def onHopperSearchItem(data):
    """
    漏斗（漏斗矿车）检测可否吸取物品
    """
    print(f'事件名：{data["Event"]}')
    print(f'维度ID：{data["DimensionId"]}')
    print(f'目标漏斗：{data["HopperBlock"]}')
    print(f'漏斗矿车坐标：{data["MinecartPos"]}')
    # return False  # 拦截此事件


@listener('onHopperPushOut')
def onHopperPushOut(data):
    """
    漏斗输出物品
    """
    print(f'事件名：{data["Event"]}')
    print(f'维度ID：{data["DimensionId"]}')
    print(f'漏斗所在的位置：{data["Pos"]}')
    # return False  # 拦截此事件


@listener('onFireSpread')
def onFireSpread(data):
    """
    火焰蔓延
    """
    print(f'事件名：{data["Event"]}')
    print(f'维度ID：{data["DimensionId"]}')
    print(f'蔓延到的方块：{data["Target"]}')
    # return False  # 拦截此事件


@listener('onBlockChanged')
def onBlockChanged(data):
    """
    方块改变
    """
    print(f'事件名：{data["Event"]}')
    print(f'改变后的方块：{data["NewBlockInstance"]}')
    print(f'改变前的方块：{data["PreviousBlockInstance"]}')

    # 拦截此事件需要注意以下问题
    # 1.部分事件导致的方块变化无法拦截, 比如玩家挖掘，放置
    # 2.对于方块与方块之间关系导致的变化，部分不可拦截，比如爆炸摧毁周围方块
    #  （实际上，客户端看起来那边还是存在方块的，但是已经是假方块了）
    # 3.但是对于火把这种需要附着在其他方块上的方块，如果因为附着方块被摧毁，那么火把不会随之被破坏
    # 4.具体某些特性可以自行测试
    # return False  # 拦截此事件


@listener('onNpcCmd')
def onNpcCmd(data):
    """
    NPC 执行命令
    """
    print(f'事件名：{data["Event"]}')
    print(f'NPC 执行的命令：{data["Command"]}')
    print(f'执行命令的 NPC：{data["Npc"]}')
    print(f'触发 NPC 命令执行的玩家：{data["Player"]}')
    # return False  # 拦截此事件


@listener('onScoreChanged')
def onScoreChanged(data):
    """
    玩家计分板数值改变
    """
    print(f'事件名：{data["Event"]}')
    print(f'计分板计分项名称：{data["ObjectiveName"]}')
    print(f'计分板数值改变的玩家：{data["Player"]}')
    print(f'改变后的计分板数值：{data["Score"]}')
    # 无法拦截此事件


@listener('onConsoleCmd')
def onConsoleCmd(data):
    """
    服务端执行后台命令
    """
    print(f'事件名：{data["Event"]}')
    print(f'执行的后台命令：{data["Command"]}')
    # return False  # 拦截此事件


@listener('onConsoleOutput')
def onConsoleOutput(data):
    """
    控制台产生命令输出
    """
    print(f'事件名：{data["Event"]}')
    print(f'输出的命令结果信息：{data["Output"]}')
    # return False  # 拦截此事件


@listener('onEffectChanged')
def onEffectChanged(data):
    """
    玩家改变药水效果
    """
    print(f'事件名：{data["Event"]}')
    print(f'被改变的效果名称：{data["Effect"]}')
    print(f'改变效果的玩家：{data["Player"]}')
    print(f'改变类型：{data["Type"]}')
    # return False  # 拦截此事件


@listener('onServerStarted')
def onServerStarted(data):
    """
    服务器启动
    """
    print(f'事件名：{data["Event"]}')
    # 无法拦截此事件
