import sbol3

sbol3.set_namespace('http://sbolstandard.org/testfiles')

gfp_seq1 = sbol3.Sequence('GFPSequence', elements='atgnnntaa', encoding=sbol3.IUPAC_DNA_ENCODING)
gfp_seq2 = sbol3.Sequence('GFPSequence', elements='atgnnntaa', encoding='https://identifiers.org/edam:format_1207')
gfp_seq3 = sbol3.Sequence('GFPSequence', elements='atgnnntaa', encoding='DNA')
gfp_seq4 = sbol3.Sequence('GFPSequence', elements='atgnnntaa')


print(f'gfp_seq1 -> {gfp_seq1.validate()}')
print(f'gfp_seq2 -> {gfp_seq2.validate()}')
print(f'gfp_seq3 -> {gfp_seq3.validate()}')
print(f'gfp_seq4 -> {gfp_seq4.validate()}')
