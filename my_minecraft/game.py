from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionRay, CollisionHandlerQueue, CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionTube, CollisionNode, CollisionHandlerEvent
from mapmanager import Mapmanager
from hero import Hero
import pickle
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camLens.setFov(120)
        self.land.loadLand('land.txt')
        self.hero = Hero((10,29,2), self.land)
        self.man = self.loader.loadModel('FinalBaseMesh.obj')
        self.man.setPos(15 ,29,1)
        self.man.setScale(0.1)
        self.man.setP(90)
        self.man.reparentTo(self.render)
        colliderNodePlayer = CollisionNode("playerSphere")
        colliderNodePlayer.addSolid(CollisionSphere(0, 0, 1, 2))
        colliderPlayer = self.hero.hero.attachNewNode(colliderNodePlayer)
        colliderPlayer.show()

        colliderNodeMan = CollisionNode("ManSphere")
        colliderNodeMan.addSolid(CollisionSphere(0, 0, 3, 10))
        colliderMan = self.man.attachNewNode(colliderNodeMan)
        colliderMan.show()
        colliderMan.setPythonTag("Man", self.man)

        self.handler = CollisionHandlerEvent()
        self.handler.add_in_pattern("%fn-into-%in")
        self.handler.add_out_pattern("%fn-out-%in")

        self.accept("playerSphere-into-ManSphere", self.touchMan)
        self.accept("playerSphere-out-ManSphere", self.leaveMan)
        self.cTrav = CollisionTraverser()
        self.cTrav.addCollider(colliderPlayer, self.handler)

    def touchMan(self, entry):
        collider = entry.getIntoNodePath()
        manModel = collider.getPythonTag("Man")
        manModel.setZ(1)
        print('😏🙄😶')
    def leaveMan(self, entry):
        collider = entry.getIntoNodePath()
        manModel = collider.getPythonTag("Man")
        print('🤬')
game = Game()
game.run()

# class Game(ShowBase):

#         colliderNodePlayer = CollisionNode("playerSphere")
#         colliderNodePlayer.addSolid(CollisionSphere(0, 0, 0, 2))
#         colliderPlayer = self.hero.hero.attachNewNode(colliderNodePlayer)
#         colliderPlayer.show()

#         colliderNodeMan = CollisionNode("ManSphere")
#         colliderNodeMan.addSolid(CollisionSphere(0, 0, 0, 10))
#         colliderMan = self.man.attachNewNode(colliderNodeMan)
#         colliderMan.show()
#         colliderMan.setPythonTag("Man", self.man)

#         self.handler = CollisionHandlerEvent()
#         self.handler.add_in_pattern("%fn-into-%in")

#         self.accept("playerSphere-into-manSphere", self.touchMan)
#         self.cTrav = CollisionTraverser()
#         self.cTrav.addCollider(colliderPlayer, self.handler)

#     def touchMan(self, entry):
#         collider = entry.getIntoNodePath()
#         manModel = collider.getPythonTag("Man")
#         mantModel.setZ(5)
#         print('😏🙄😶')
#     def leaveMan(self, entry):
#         collider = entry.getIntoNodePath()
#         manModel = collider.getPythonTag("Man")
#         print('🤬')