from neo_mcpi import *
from neo_mcpi.locals import *
import time

mc = minecraft.Minecraft.create()
mc.setBlock(mc.player.getPos().x, mc.player.getPos().y, mc.player.getPos().z, NETHER_REACTOR_CORE)
