from fun import *

seq1 = "ACGCNCTTTTCTCGCGTACCTTTACTAATAGAATGCAAAGACGTCCCCCG"
seq2 = "CTCGCGTACCTTTACTAAGAGAATGCGNAGACGTCCCCCGGNGGACCGAT"
seqOri = "ACGCNCTTTCCTCGCGTATCTNTACTAAMAGAATGCMNAGAGGTCCCCCGGNGGACCGAT"

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

seqConsensus = ""
#将两个seqExpand 合并成一个seqConsensus：
for i,j in zip(seqExpand1,seqExpand2):
    if (i==j):
        seqConsensus +=i
    elif (i == '-'):
        seqConsensus += j
    elif (j == '-'):
        seqConsensus += i
    elif (i == 'N' or j == 'N'):
        seqConsensus += "N"
    else:
        seqConsensus += "M"

print(seqConsensus)
list2 = smithWaterman.water(seqConsensus,seqOri)
print(list2[0])
print(list2[1])
print(list2[2])