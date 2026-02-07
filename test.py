import random
import time

from neo_mcpi import *
from neo_mcpi.event import ChatEvent
from neo_mcpi.locals import *

mc = minecraft.Minecraft.create()
mc.player.setPos(0, 0, 0)  # 出生原点
mc.postToChat("余翊涵你好！")

for i in range(0, 2000):
    mc.setBlock(i, 0, 0, i)

