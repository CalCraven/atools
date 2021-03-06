import mbuild as mb
import numpy as np


class Pentafluorophenyl(mb.Compound):
    """ A fully fluorinated phenyl group. """
    def __init__(self):
        super(Pentafluorophenyl, self).__init__()

        mb.load('pentafluorophenyl.pdb', compound=self, relative_to_module=self.__module__)
        self.translate(-self[0].pos)

        self.add(mb.Port(anchor=self[0], orientation=[0, -1, 0], separation=0.07), 
            'down')

if __name__ == '__main__':
    pentafluorophenyl = Pentafluorophenyl()
    pentafluorophenyl.save('pentafluorophenyl-test.mol2', overwrite=True)
