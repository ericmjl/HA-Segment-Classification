from SequenceParcer import *
from FilenameHolder import *
from SequenceSampler import *
segment = 'HA'
species = 'Human'
strain = 'A'

fnh = FilenameHolder(segment, species, strain)

parser = SequenceParser(fnh)
parser.start_standard_workflow()

sampler = SequenceSampler(fnh)