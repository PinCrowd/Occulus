#!/bin/bash
for z in {a..z}
do
    for i in {0..31}
    do
    n=$((RANDOM%200+100))
    opencv_createsamples \
      -img images/positives/$i.png \
      -vec vectors-31/$z-$i.vec \
      -bg negatives_2x.dat \
      -num 30 \
      -bgcolor 0 \
      -bgthresh 80 \
      -maxidev 40 \
      -maxxangle 0.0$n \
      -maxyangle 0.0$n \
      -maxzangle 0.0$n \
      -w 24 \
      -h 24
    done
done

