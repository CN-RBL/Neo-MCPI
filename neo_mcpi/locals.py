try:
    from block import *
    from entity import *
    from vec3 import Vec3
except ImportError:
    from neo_mcpi.block import *
    from neo_mcpi.entity import *
    from neo_mcpi.minecraft import Vec3

START_POSITION: Vec3 = Vec3(0, 0, 0)
