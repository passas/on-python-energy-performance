NTIMES=10

export NTIMES

measure:
	sudo modprobe msr
	sudo ../../../RAPL/main "/home/miguel/.codon/bin/codon run -release bubble_sort_codon.py" Codon "Bubble Sort 30 000" $(NTIMES)

run:
	/home/miguel/.codon/bin/codon run -release bubble_sort_codon.py

mem: 
	{ /usr/bin/time -v /home/miguel/.codon/bin/codon run -release bubble_sort_codon.py > /dev/null; } 2>&1 | grep "Maximum resident" #| sed "s/[^0-9]\+\([0-9]\+\).*/\1/"
