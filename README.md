# Genomics in Bioinformatics

### ⭐ DNA Read Assembly and Coverage Analysis Based on Sequence Overlap

### ⭐ Part 1
生物信息学中的序列拼接：基于序列重叠的DNA读段组装与覆盖度分析, 这个项目的逻辑是对序列进行组装。
首先，从输入文件中读取序列。对这些序列进行比较，找出至少有k个碱基重叠的序列。如果找到重叠，就将两个序列合并为一个更长的序列。
这个合并过程是迭代的，新合并的序列会用来继续查找可能的重叠。一旦一个序列不能再与其他任何序列合并，它就被视为一个完整的“contig”。
所有的“contigs”最终会被写入到一个FASTA格式的输出文件中，每个“contig”都有一个数字标签。

- 1.	对输入文件中的序列两两进行比较，查找是否存在至少k个碱基的重叠（在您的例子中k等于10）。
- 2.	如果序列A的末尾k个碱基与序列B的开头k个碱基相匹配，则认为这两个序列重叠。
- 3.	一旦发现重叠，将这两个序列合并为一个更长的序列，即将序列B的非重叠部分附加到序列A的末尾。
- 4.	然后，取这个新合并的长序列，用它的末尾k个碱基去查找其他序列的开头k个碱基是否重叠，如果是，继续合并。
- 5.	重复这个过程，直到没有更多的序列可以合并。这时，这个长序列就被认为是一个完整的contig。
- 6.	按照上述过程，处理所有序列，每个独立合并的结果都被标记为一个contig（例如：contig 1, contig 2, ...）。
- 7.	最后，所有的contig被写入到一个FASTA格式的输出文件中。

这个方法类似于生物信息学中用于基因组组装的某些简化算法。这种类型的算法可以用来将读取的序列（reads）组装成更长的序列（contigs），这在DNA测序中是常见的处理步骤。

### ⭐ Part 2
Evaluate the distribution of the reads across each sequence. Create a visualization of your choice that shows coverage of reads across each of your sequences.
为了评估reads在每个序列中的分布（coverage），我们可以执行以下步骤：
- 1.	对每个序列，计算每个碱基的覆盖度，即这个位置在多少reads中出现过。
- 2.	创建一个可视化图表，展示每个序列的每个位置的覆盖度。
- 3.	通过观察这个图表，我们可以判断测序方法是否存在偏差。

这里的上下文中，"coverage"（覆盖度）指的是在测序数据中，每一个碱基（A、C、G、T）在序列的每个位置出现的频率。具体来说：
- 1.	如果某个位置的覆盖度很高，这意味着有很多reads包含了这个位置的碱基。这通常表明该位置的数据质量好，测序信号强。
- 2.	如果某个位置的覆盖度很低，可能意味着很少的reads覆盖了这个位置，这可能是由于测序数据的局限性或者该位置本身就较为罕见。
- 3.	在基因组测序项目中，理想的情况是整个被测序的区域都有均匀且充分的覆盖度，这样可以确保数据的完整性和准确性。不均匀的覆盖度可能导致某些区域的信息缺失或不准确，这在解释测序结果时需要特别注意。
- 4.	从图上来说，要判断测序方法是否存在偏见（biased），我们需要分析覆盖度可视化图表。在理想情况下，如果测序方法没有偏见，我们期望看到的是相对均匀的覆盖度分布——即所有位置的碱基都有大致相同的覆盖频率。这个图是merge以后得distribution（当然我也可以用原始数据来做distribution，见图2）。
![image](https://github.com/rent01/Genomics/assets/88874618/31d46888-ea25-4afc-b8ab-a7a06d69b83e)
![image](https://github.com/rent01/Genomics/assets/88874618/69a1c809-f265-4752-b34b-ad29455916f3)

### ⭐ Part 3: Conclusion
- 1.	At what point does the program output change when you decrease k? 
When the overlap parameter k is decreased, you can expect to see more merges occurring, since reads will have a higher chance of overlapping with shorter required overlap lengths. This could potentially lead to a more connected assembly but also increases the risk of erroneous merges. The output of the program will change when k becomes small enough that incorrect overlaps are accepted, which might not be true overlaps.
- 2.	At what point does the program output change when you increase k? 
When the overlap parameter k is increased, fewer merges will occur since the requirement for overlap is stricter. The output of the program will change when k reaches a threshold where true overlaps are missed, and reads that should be merged remain separate.
- 3.	What is the relationship between how high k can go and sequencing coverage?
The relationship between the value of k and sequencing coverage can be quite direct: a higher k can require higher coverage to ensure that all true overlaps are found. If the coverage is low and k is high, it's possible that some true contigs won't be assembled because the necessary overlaps don't exist within the reads. Conversely, a lower k can tolerate lower coverage, as the shorter required overlap will be more common, but again, this increases the risk of false positives in the assembly.


