from SequenceParcer import *
from FilenameHolder import *
from SequenceSampler import *
from SequenceAligner import *
from AffinityPropagationClusterer import *
segment = 'NA'
species = 'Human'
strain = 'A'

fnh = FilenameHolder(segment, species, strain)
fnh.name_all_files()

parser = SequenceParser(fnh)
parser.start_standard_workflow()

sampler = SequenceSampler(fnh)
sampler.start_standard_workflow(100)

aligner = SequenceAligner(fnh)
aligner.start_standard_workflow()

clusterer = AffinityPropagationClusterer(fnh)
clusterer.fetch_distmat()
clusterer.sanitize_distmat()
clusterer.write_sanDistmat()
clusterer.compute_affmat()
clusterer.write_affmat()
clusterer.get_distmat_stdev()
clusterer.compute_affinity_propagation()
clusterer.write_txt_report()
clusterer.plot_clusters()