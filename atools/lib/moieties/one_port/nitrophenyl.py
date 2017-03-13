import mbuild as mb


class Nitrophenyl(mb.Compound):
    """ A nitrophenyl group. """
    def __init__(self):
        super(Nitrophenyl, self).__init__()

        phenyl = Phenyl()
        nitro = Nitro()

        phenyl.remove(phenyl[6])
        phenyl.add(mb.Port(anchor=phenyl[5]), 'up')
        mb.translate(phenyl['up'], [0, 0.07, 0])

        self.add(phenyl, 'phenyl')
        self.add(nitro, 'nitro')
        mb.equivalence_transform(self['nitro'], self['nitro']['down'], self['phenyl']['up'])

        self.add(phenyl['down'], 'down', containment=False)

if __name__ == '__main__':
    nitrophenyl = Nitrophenyl()
    nitrophenyl.save('nitrophenyl-test.mol2', overwrite=True)