dna = "AAAAAAAAAA"

length = len(dna)

a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

gc_content = (g_count + c_count) / length * 100

print("DNA sequence:", dna)
print("Sequence length:", length)
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
print("GC content:", gc_content, "%")
at_content = (a_count + t_count) / length * 100
print("AT content:", at_content, "%")
total_content = at_content + gc_content
print("Total AT + GC:", total_content, "%")