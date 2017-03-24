FILE=mandelbrot.c
OUTPUT=mandelbrot

IMAGE=.ppm
LOGS=.log

CC=gcc
CC_OPT=

CC_OMP=-fopenmp
CC_PTH=-pthread

.PHONY: all
all:  mandelbrot_omp mandelbrot_pthread mandelbrot_seq

mandelbrot_omp: $(FILE)
	$(CC) -o $(OUTPUT)_omp $(CC_OPT) $(CC_OMP) $(FILE)

mandelbrot_pthread: $(FILE)
	$(CC) -o $(OUTPUT)_pthread $(CC_OPT) $(CC_PTH) $(FILE)

mandelbrot_seq: $(FILE)
	$(CC) -o $(OUTPUT)_seq $(CC_OPT) $(FILE)

.PHONY: clean
clean:
	rm $(OUTPUT)_* *$(IMAGE) *$(LOGS)
