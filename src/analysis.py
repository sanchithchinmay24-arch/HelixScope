def analyze_dna(dna):
    dna = dna.upper()

    valid_bases = {"A", "T", "G", "C"}

    if not set(dna).issubset(valid_bases):
        return None

    length = len(dna)

    a_count = dna.count("A")
    t_count = dna.count("T")
    g_count = dna.count("G")
    c_count = dna.count("C")

    gc_content = (g_count + c_count) / length * 100
    at_content = (a_count + t_count) / length * 100
    total_content = at_content + gc_content

    return {
        "sequence": dna,
        "length": length,
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "GC_content": gc_content,
        "AT_content": at_content,
        "total_content": total_content
    }
def reverse_complement(dna):
    dna = dna.upper()

    valid_bases = {"A", "T", "G", "C"}

    if not set(dna).issubset(valid_bases):
        print("Invalid DNA sequence")
        return

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    result = ""

    for base in dna:
        result += complement[base]

    return result[::-1]
def transcribe_dna(dna):
    dna = dna.upper()

    valid_bases = {"A", "T", "G", "C"}

    if not set(dna).issubset(valid_bases):
        print("Invalid DNA sequence")
        return None

    rna = dna.replace("T", "U")

    return {
        "DNA": dna,
        "RNA": rna,
        "length": len(rna)
    }
def rna_to_codons(rna):
    rna = rna.upper()

    valid_bases = {"A", "U", "G", "C"}

    if not set(rna).issubset(valid_bases):
        print("Invalid RNA sequence")
        return None

    codons = []

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i + 3]
        codons.append(codon)

    return codons

CODON_TABLE = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",

    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*",

    "UGU": "C", "UGC": "C",
    "UGA": "*", "UGG": "W",

    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",

    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",

    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",

    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M",

    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",

    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",

    "AGU": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",

    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",

    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",

    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
def translate_codons(codons):
    protein = ""

    for codon in codons:
        amino_acid = CODON_TABLE.get(codon)

        if amino_acid is None:
            print("Invalid codon:", codon)
            return None

        protein += amino_acid

        if amino_acid == "*":
            break

    return protein

def find_orfs(dna):
    dna = dna.upper()

    valid_bases = {"A", "T", "G", "C"}

    if not set(dna).issubset(valid_bases):
        print("Invalid DNA sequence")
        return None

    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}

    orfs = []

    strands = {
        "forward": dna,
        "reverse": reverse_complement(dna)
    }

    for strand_name, sequence in strands.items():

        for frame in range(3):

            for i in range(frame, len(sequence) - 2, 3):

                codon = sequence[i:i + 3]

                if codon == start_codon:

                    for j in range(i + 3, len(sequence) - 2, 3):

                        next_codon = sequence[j:j + 3]

                        if next_codon in stop_codons:

                            orf = sequence[i:j + 3]

                            orfs.append({
                                "sequence": orf,
                                "start": i,
                                "end": j + 3,
                                "frame": frame,
                                "strand": strand_name
                            })

                            break

    return orfs

def annotate_orf(orf):
    sequence = orf["sequence"]

    length = len(sequence)

    rna = sequence.replace("T", "U")

    codons = rna_to_codons(rna)

    protein = translate_codons(codons)

    return {
        "sequence": sequence,
        "start": orf["start"],
        "end": orf["end"],
        "length": length,
        "frame": orf["frame"],
        "strand": orf["strand"],
        "protein": protein
    }

def simulate_mutation(dna, position, new_base):
    dna = dna.upper()
    new_base = new_base.upper()

    valid_bases = {"A", "T", "G", "C"}

    if not set(dna).issubset(valid_bases):
        print("Invalid DNA sequence")
        return None

    if new_base not in valid_bases:
        print("Invalid DNA base")
        return None

    if position < 0 or position >= len(dna):
        print("Invalid position")
        return None

    original_base = dna[position]

    mutated_dna = dna[:position] + new_base + dna[position + 1:]

    return {
        "original": dna,
        "mutated": mutated_dna,
        "position": position,
        "original_base": original_base,
        "new_base": new_base
    }