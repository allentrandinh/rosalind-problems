import fasta_manipulation as fm

possible_codon = { 'F':'2', 'L':'6', 'S':'6', 'Y':'2' , 'C':'2', 'W':'1' ,
'P':'4' , 'H' : '2' , 'Q' : '2' , 'R':'6' , 'I' : '3' , 'M' :'1' , 'T':'4',
'N':'2' , 'K' : '2' , 'V' :'4' , 'A' : '4', 'D' : '2' , 'E' : '2' , 'G':'4'}

def num_rna(PROTEIN):
    '''
    :param PROTEIN: protein seq
    :return: number of mRNA can give rise to that protein module 1e6
    '''
    #take into account stop codon
    rna_count = 3
    for i in range(len(PROTEIN)):
        rna_count *= int(possible_codon[PROTEIN[i]])
    return(rna_count%1000000)

aa_mass = {
"A" : "71.03711", "C" : "103.00919", "D" : "115.02694", "E" : "129.04259",
"F" : "147.06841", "G": "57.02146", "H" : "137.05891", "I": "113.08406",
"K" : "128.09496", "L" : "113.08406", "M" : "131.04049", "N" : "114.04293",
"P" : "97.05276", "Q" : "128.05858", "R" : "156.10111", "S": "87.03203",
"T" : "101.04768", "V" : "99.06841", "W" : "186.07931", "Y" : "163.06333" }

def protein_mass(PROTEIN):
    '''
    :param PROTEIN: protein seq
    :return: mass of protein
    '''
    mass = 0
    for aa in PROTEIN:
        mass += float(aa_mass[aa])
    return(mass)

#fm.single_seq_noheading('/Users/apd20500/Desktop/rosalind_prtm.txt')
