from fun import *

seq1 = "ACGCNCTTTTCTCGCGTACCTTTACTAATAGAATGCAAAGACGTCCCCCG"
seq2 = "CTCGCGTACCTTTACTAAGAGAATGCGNAGACGTCCCCCGGNGGACCGAT"

#list = function.seqAlign(seq1,seq2)
list = smithWaterman.water(seq1,seq2)
#list [align1,align2,symbol,maxscore]
seqExpand1 = ""
seqExpand2 = ""
sign = ""

seqExpand1+="-"*seq2.find(list[1])
seqExpand2+="-"*seq1.find(list[0])
seqExpand1 += seq1
seqExpand2 += seq2
sign += "-"*(seq2.find(list[1])+seq1.find(list[0]))
sign += list[2]

maxLength = max(len(seqExpand1),len(seqExpand2))
seqExpand1 +="-"*(maxLength-len(seqExpand1))
seqExpand2 +="-"*(maxLength-len(seqExpand2))
sign += "-"*(maxLength-len(sign))

print(seqExpand1)
print(seqExpand2)
print(sign)