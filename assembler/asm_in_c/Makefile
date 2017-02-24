# Parametry prekladace.
CFLAGS=-Wall -O9

# Vychozi pravidlo pro vytvoreni vysledne spustitelne aplikace.
all:	asm_in_c_1.s asm_in_c_1 \
	asm_in_c_2.s asm_in_c_2 \
	asm_in_c_3.s asm_in_c_3 \
	asm_in_c_4.s asm_in_c_4 \
	asm_in_c_5.s asm_in_c_5 \
	asm_in_c_6.s asm_in_c_6 \
	asm_in_c_7.s asm_in_c_7 \
	asm_in_c_8.s asm_in_c_8 \
	asm_in_c_9.s asm_in_c_9

clean:
	rm -f *.o
	rm -f *.s
	rm -f asm_in_c_[0-9]

# Pravidlo pro slinkovani vsech objektovych souboru a vytvoreni
# vysledne spustitelne aplikace.
$(PROGNAME):	$(PROGNAME).o
	$(CC) -o $@ $(LDFLAGS) $<

# Pravidlo pro preklad kazdeho zdrojoveho souboru do prislusneho
# objektoveho souboru.
%.o:	%.c
	$(CC) $(CFLAGS) -c $< -o $@

# Pravidlo pro preklad kazdeho zdrojoveho souboru do prislusneho
# assemblerovskeho vysledku.
%.s:	%.c
	$(CC) $(CFLAGS) -S -c $< -o $@

