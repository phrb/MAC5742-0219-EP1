FILE=mandelbrot.c
OUTPUT=mandelbrot

IMAGE=.ppm
LOGS=.log

CC=clang
CC_OPT=

all: $(FILE)
	$(CC) -o $(OUTPUT) $(CC_OPT) $(FILE)

clean:
	rm $(OUTPUT) *$(IMAGE) *$(LOGS)
