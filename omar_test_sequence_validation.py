import sbol3

sbol3.set_namespace('http://sbolstandard.org/testfiles')

gfp = sbol3.Component('GFP', sbol3.SBO_DNA)
gfp_seq = sbol3.Sequence('GFPSequence', elements='atgnnntaa', encoding=sbol3.IUPAC)

gfp.sequences = [ gfp_seq ]

print(gfp.sequences)