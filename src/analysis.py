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
