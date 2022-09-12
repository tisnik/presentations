CC=gcc
CFLAGS=-ffast-math -O9 -Wall -pedantic -std=c89
LFLAGS=-lSDL2

EMCC=emcc

all:	sdl_demo_1A sdl_demo_2A sdl_demo_1B.html sdl_demo_2B.html

clean:
	rm sdl_demo_1A
	rm sdl_demo_2A
	rm *.o

sdl_demo_1A:	sdl_demo_1A.o
	gcc -o $@ $< $(LFLAGS)

sdl_demo_1A.o:	sdl_demo_1A.c
	$(CC) $(CFLAGS) -c -o $@ $<

sdl_demo_2A:	sdl_demo_2A.o
	gcc -o $@ $< $(LFLAGS)

sdl_demo_2A.o:	sdl_demo_2A.c
	$(CC) $(CFLAGS) -c -o $@ $<

sdl_demo_1B.html:	sdl_demo_1B.o
	$(EMCC) $< -o $@ -s USE_SDL=2

sdl_demo_1B.o:	sdl_demo_1B.c
	$(EMCC) -c $< -o $@ -s USE_SDL=2

sdl_demo_2B.html:	sdl_demo_2B.o
	$(EMCC) $< -o $@ -s USE_SDL=2

sdl_demo_2B.o:	sdl_demo_2B.c
	$(EMCC) -c $< -o $@ -s USE_SDL=2
