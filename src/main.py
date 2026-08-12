def analyze_dna(dna):
    dna = dna.upper()

    valid_bases = {"A", "T", "G", "C"}

    if not set(dna).issubset(valid_bases):
        print("Invalid DNA sequence")
        return

    length = len(dna)
    
    a_count = dna.count("A")
    t_count = dna.count("T")
    g_count = dna.count("G")
    c_count = dna.count("C")

    gc_content = (g_count + c_count) / length * 100
    at_content = (a_count + t_count) / length * 100
    total_content = at_content + gc_content

    print("DNA sequence:", dna)
    print("Sequence length:", length)
    print("A:", a_count)
    print("T:", t_count)
    print("G:", g_count)
    print("C:", c_count)
    print("GC content:", gc_content, "%")
    print("AT content:", at_content, "%")
    print("Total AT + GC:", total_content, "%")

analyze_dna("ATGCGGTAAC")
analyze_dna("AAAAAAAAAA")
analyze_dna("ATGCGXTAAC")
analyze_dna("atgcggtaac")