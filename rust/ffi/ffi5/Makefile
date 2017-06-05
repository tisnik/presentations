CC=gcc
CFLAGS=-Wall -ansi -fPIC
RUSTC=rustc

APP=ffi5
PROGNAME=$(APP)
LIBNAME=lib$(APP).so

RUST_SRC=$(APP).rs
LIB_SRC=$(APP).c
OBJ_FILE=$(APP).o

# Vychozi pravidlo pro vytvoreni vysledne spustitelne aplikace.
all:	$(LIBNAME) $(PROGNAME)

# Pravidlo pro slinkovani vsech objektovych souboru a vytvoreni
# vysledne spustitelne aplikace.
$(PROGNAME):	$(RUST_SRC) $(LIBNAME)
	$(RUSTC) -L . $<

# Pravidlo pro preklad knihovny
$(LIBNAME):	$(OBJ_FILE)
	$(CC) -shared -Wl,-soname,$(LIBNAME) -o $(LIBNAME) $<

%.o:    %.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f *.o
	rm -f *.so
	rm -f $(PROGNAME)

run:
	export LD_LIBRARY_PATH=.;./$(APP)
