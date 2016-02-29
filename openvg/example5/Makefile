# Makefile pro preklad pateho prikladu ukazujiciho
# praci s OpenVG a EGL.

# Parametry prekladace.
CFLAGS=-Wall

# Dalsi parametry prekladace, zde adresare, kde se maji 
# hledat hlavickove soubory.
INCLUDES=-I/opt/vc/include/ -I/opt/vc/include/interface/vcos/pthreads -I/opt/vc/include/interface/vmcs_host/linux

# Parametry linkeru.
LDFLAGS=-L/opt/vc/lib/ -lGLESv2 -lEGL -lopenmaxil -lbcm_host -lvcos -lvchiq_arm -lpthread -lrt -lm

PROGNAME=example5

# Vychozi pravidlo pro vytvoreni vysledne spustitelne aplikace.
all:	$(PROGNAME)

clean:
	rm -f *.o
	rm -f $(PROGNAME)

# Pravidlo pro slinkovani vsech objektovych souboru a vytvoreni
# vysledne spustitelne aplikace.
$(PROGNAME):	$(PROGNAME).o
	$(CC) -o $@ $(LDFLAGS) $<

# Pravidlo pro preklad kazdeho zdrojoveho souboru do prislusneho
# objektoveho souboru.
%.o:	%.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

