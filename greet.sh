espeak "good night "
if [ $(date +%H) -gt 0 -a $(date +%H) -le 5 ]
then
espeak "time is $(date +%H) hours $(date +%M) MINUTES and date is $(date +%d)"
espeak "good night "
fi
if [ $(date +%H) -gt 5 -a $(date +%H) -le 12 ]
then
espeak "time is $(date +%H) hours $(date +%M) MINUTES and date is $(date +%d)"
espeak "good morning "
fi
if [ $(date +%H) -gt 12 -a $(date +%H) -le 16 ]
then
espeak "time is $(date +%H) hours $(date +%M) MINUTES and date is $(date +%d)"
espeak "good afternoon "
fi
if [ $(date +%H) -gt 16 -a $(date +%H) -le 22 ]
then
espeak "time is $(date +%H) hours $(date +%M) MINUTES and date is $(date +%d)"
espeak "good evening "
fi

