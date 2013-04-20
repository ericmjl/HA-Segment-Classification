from SequenceParcer import *
from FilenameHolder import *
from SequenceSampler import *
from SequenceAligner import *
from AffinityPropagationClusterer import *

segments = ['HA', 'NA', 'PB1', 'PB2', 'PA', 'M2', 'M1', ]
species = 'Human'
strain = 'A'

for segment in segments:

	fnh = FilenameHolder(segment, species, strain)
	fnh.name_all_files()

	parser = SequenceParser(fnh)
	parser.start_standard_workflow()

	sampler = SequenceSampler(fnh)
	sampler.start_standard_workflow(50)

	aligner = SequenceAligner(fnh)
	aligner.start_standard_workflow()

	clusterer = AffinityPropagationClusterer(fnh)
	clusterer.start_standard_workflow()