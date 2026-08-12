from analysis import (analyze_dna,reverse_complement, transcribe_dna, rna_to_codons, translate_codons, find_orfs, annotate_orf)
if __name__ == "__main__":

    result = analyze_dna("ATGCGGTAAC")
    print("GC percentage from result:", result["GC_content"])

    print("Reverse complement:", reverse_complement("ATGCGGTAAC"))

    rna_result = transcribe_dna("ATGCGGTAAC")

    print("RNA:", rna_result["RNA"])
    print("RNA length:", rna_result["length"])
    rna_result = transcribe_dna("ATGCGGTAAC")

print("RNA:", rna_result["RNA"])

codons = rna_to_codons(rna_result["RNA"])

print("Codons:", codons)
rna_result = transcribe_dna("ATGCGGTAAC")

codons = rna_to_codons(rna_result["RNA"])

protein = translate_codons(codons)

print("Protein:", protein)
dna = "CCCATGAAAGGGTAAACCC"

orfs = find_orfs(dna)

print("ORFs:", orfs)
print("ORFs 2:", find_orfs("AAAAAAAAAAAA"))
print("ORFs 3:", find_orfs("ATGCXTA"))
print("ORFs 4:", find_orfs("ATGAAATAG"))
reverse_test = "CTATTTCAT"

print("Reverse strand test:", find_orfs(reverse_test))

dna = "CCCATGAAAGGGTAAACCC"

orfs = find_orfs(dna)

for orf in orfs:
    annotation = annotate_orf(orf)
    print("Annotated ORF:", annotation)