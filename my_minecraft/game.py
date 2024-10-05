from direct.showbase.ShowBase import ShowBase
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
game = Game()
game.run()
