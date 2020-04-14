#Import statements
import re

#Open the file and read it in
fileIn = open("unknown_blast.xml")
blastRecord = NCBIXML.read(fileIn)

alignCount = 0

#Iterate through all the alignments
for alignment in blastRecord.alignments:
    hspNo = 0
    print(alignment.title)
    if(alignment.hsps):
        if(re.search('PREDICTED',alignment.title)):
            print('\n***ALIGNMENT ',alignCount,'***')
            titleArr = alignment.title.split('|')
            print("RefSeq ID: ",titleArr[4])
            print('HSP#\tScore\tBitSc\tGaps\tEval')
            for hsp in alignment.hsps:
                hspNo += 1
                print(str(hspNo) + ":\t" + str(hsp.score) + \ 
                      "\t" + str(hsp.bits) + "\t" + str(hsp.gaps) + \
                      "\t" + str(hsp.expect))
    #print('\n')
fileIn.close()
