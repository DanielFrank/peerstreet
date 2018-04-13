#In reality, we'd have the msa/year/population as a separate data item. Made it part of MSA class to speed up finishing.
import simplejson

class MSA:
    
    def __init__(self, msa_name):
        self.msa_name = msa_name
        self.populations = dict()
    
    def encode(self):
        return self.__dict__
    
    @classmethod
    def decode(cls, d):
        msa = MSA("")
        msa.__dict__ = d
        return msa
        
    def set_population(self, year, pop):
            self.populations[year] = pop
    
    def get_population(self, year):
        try:
            return self.populations[year]
        except KeyError:
            return 0