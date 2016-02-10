#!/bin/bash

WORDFILE="/usr/share/dict/words"
NUMWORDS=1

#Number of lines in $wordfile
tL='awk 'NF!=0{++c} END ' $WORDFILE'

#for i in 'seq $NUMWORDS'
#do
#rnum= $(($RANDOM%$tL+1))
sed -n $(RANDOM%tl+1) P  $WORDFILE
#done
