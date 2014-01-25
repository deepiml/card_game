class Card(object):
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite
    def __repr__(self):
        return '%s%s' %(self.rank, self.suite)
c0 = Card(5, 'd')
print c0
