CC=gcc
CFLAGS=-ffast-math -O9 -Wall -pedantic -std=c89
LFLAGS=-lSDLmain -lSDL

SRCDIR=src
OBJDIR=obj
EXENAME=main.exe

all:	$(EXENAME)

$(EXENAME):	$(OBJDIR)/main.o
	gcc -o $(EXENAME) $? $(LFLAGS)

$(OBJDIR)/main.o:	$(SRCDIR)/main.c
	$(CC) $(CFLAGS) -c -o $@ $<

