# -*- coding: utf-8 -*-
# @Author : TY Ren
# @Email : ren.tiany@northeastern.edu
# @Software : PyCharm
# @Time : 9/25/2023 9:50 PM
# @File : Assemble Sequence.py
# -------------------------------
import matplotlib.pyplot as plt

# Set the parameters
k = 10
output_file = 'youroutputfilepath/contigs.fasta'
input_file = 'yourinputfilepath/seqReadFile2023.txt'

def findOverlap(a, b, k):
    """
    This function finds the overlap between two sequences a and b, given the minimum overlap k.
    """
    findSeq = b[0:k]
    lp = a.find(findSeq)
    if (lp == -1):
        return -1
    elif (lp + len(b) > len(a)):
        if (a[lp:] == b[:len(a[lp:])]):
            return lp
        else:
            return -1
    else:
        return -2

def mergeOverlaps(reads, k):
    """
    This function iteratively merges reads with an overlap of at least k bases.
    """
    merged = False
    i = 0
    while i < len(reads):
        if reads[i] == "":  # Skip empty (already merged) reads
            i += 1
            continue
        j = 0
        while j < len(reads):
            if i != j and reads[j] and (len(reads[i]) >= k) and (len(reads[j]) >= k):
                ovlp = findOverlap(reads[i], reads[j], k)
                if ovlp > -1:  # Valid overlap found
                    reads[i] = reads[i][:ovlp] + reads[j]  # Merge the sequences
                    reads[j] = ""  # Mark the merged sequence as empty
                    merged = True
                    break  # Break to restart the merging process with the new extended read
                elif ovlp == -2:  # No possible overlap
                    reads[j] = ""
            j += 1
        if not merged:  # If no merge occurred for reads[i], move to the next read
            i += 1
        else:
            i = 0  # Restart the merging process with the new extended read
            merged = False  # Reset the merged flag for the next iteration

    # Filter out empty reads and return the list of merged sequences
    return [read for read in reads if read]

def writeContigs(sequences, output_file):
    """
    Writes the contigs to an output file in FASTA format with numerical labels.
    """
    with open(output_file, 'w') as f:
        for i, seq in enumerate(sequences):
            f.write(f">contig{i+1}\n{seq}\n")

def assembleReads(input_file, output_file, k):
    """
    Main function to assemble reads into contigs.
    """
    # Read the sequences from the input file and print the input sequence
    with open(input_file, 'r') as file:
        reads = [line.strip() for line in file]

    # print("Sequences loaded from the file:")
    # for seq in reads:
    #     print(seq)

    # Merge the reads with overlaps and print them
    merged_reads = mergeOverlaps(reads, k)
    print("\nSequences after merging:")
    # for n in merged_reads:
    #     print(n)
    for idx, seq in enumerate(merged_reads, 1):
        print(f"Contig {idx}: {seq}")

    # Write the resulting contigs to the output file
    writeContigs(merged_reads, output_file)

    return reads, merged_reads

# Run the assembly process
# assembleReads(input_file, output_file, k)
original_reads, merged_reads = assembleReads(input_file, output_file, k)

# Return the path to the output file to download it if necessary
output_file

def calculate_coverage(reads):
    """
    Calculates the coverage for each base position in the reads.
    """
    coverage = [0] * max(len(read) for read in reads)  # Initialize coverage list
    for read in reads:
        for i in range(len(read)):
            coverage[i] += 1  # Increment coverage for each base position
    return coverage

# Calculate coverage from the original reads before assembly
coverage = calculate_coverage(original_reads)
# Plot the coverage
plt.figure(figsize=(10, 6))
plt.bar(range(len(coverage)), coverage, color='skyblue')
plt.title('Coverage across Each Base Position')
plt.xlabel('Base Position')
plt.ylabel('Coverage')
plt.show()

# Let's reload the input file and take a look at the sequences
input_file_path = 'D:/学校/6400/6400-HW1/seqReadFile2023.txt'

# Read the sequences from the input file
with open(input_file_path, 'r') as file:
    original_reads = [line.strip() for line in file]

# Check the first few reads to understand their length and content
sample_sequences = original_reads[:10]
sample_sequences

# Since we have confirmed that the reads are of length 20, let's calculate the coverage correctly.
# We will use the original_reads for this calculation and not the merged_reads.

# Calculate coverage from the original reads
coverage = calculate_coverage(original_reads)

# Plot the coverage
plt.figure(figsize=(10, 6))
plt.bar(range(len(coverage)), coverage, color='skyblue')
plt.title('Coverage across Each Base Position')
plt.xlabel('Base Position')
plt.ylabel('Coverage')
plt.xlim(0, 20)  # Set the limit of x-axis to 20, as the maximum length of reads is 20
plt.show()
