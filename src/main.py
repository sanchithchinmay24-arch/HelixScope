from analysis import analyze_dna, reverse_complement


if __name__ == "__main__":
    result = analyze_dna("ATGCGGTAAC")
print("GC percentage from result:", result["GC_content"])

print("Reverse complement:", reverse_complement("ATGCGGTAAC"))
print("Reverse complement 1:", reverse_complement("ATGCGGTAAC"))
print("Reverse complement 2:", reverse_complement("AAAAAAAAAA"))
print("Reverse complement 3:", reverse_complement("atgc"))
print("Reverse complement 4:", reverse_complement("ATGCX"))