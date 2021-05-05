# Zvukový čip SID v osmibitových domácích mikropočítačích společnosti Commodore

Velkým konkurentem společnosti Atari v oblasti vývoje a prodeje osmibitových domácích mikropočítačů byla firma Commodore Business Machines (CBM), která mj. stála za vývojem i prodejem osmibitových domácích počítačů Commodore, včetně slavného počítače C64. Jak bývalo v minulosti zvykem, i firma Commodore (ostatně naprosto stejně, jako tomu bylo v případě konkurenční Atari) si pro čipovou sadu (chipset) svých domácích mikropočítačů vyvinula vlastní zákaznické čipy, včetně úspěšného grafického čipu VIC II a dnes popisovaného zvukového čipu SID.

Zkratka SID je odvozena z plného anglického názvu Sound Interface Device, tento integrovaný obvod je však také známý pod svým číselným označením – původní série vyráběná v technologii N-MOS nesla číslo 6581 a novější verze vyráběná na základě technologie H-MOS se označovala číslem 6582, popř. 8580 (tato série se však zvukově poněkud liší od série původní). Počáteční číslice 65 pochopitelně odkazují na mikroprocesor MOS 6502.

## Vyvinuté série SIDu

V následující tabulce jsou vypsány všechny vyvinuté série čipu SID:

Série      Označení na čipu Technologie
6581 R2    6581             N-MOS
6581 R3    6581 R3          N-MOS
6581 R4    6581 R4          N-MOS
6581 R4 AR 6581 R4          N-MOS
6582 A     6582 A           H-MOS
8580 R5    8580R5           H-MOS

## Poznámky k jednotlivým čipům

6581     původní dostupná varianta, R1 se neprodávala (není tedy ani v tabulce)            
6581 R3  vyráběna do roku 1986, někdy též označena jako 6581 CBM 
6581 R4  vyráběna v průběhu roku 1986                            
6581 R4  vyráběna od konce roku 1986 do roku 1990                
6582 A   vyráběna okolo roku 1992 (některé kusy i později)       
8580R5   vyráběna v letech 1987 až 1992                          

## Zapojení vývodů SIDu

Podívejme se nyní na zapojení vývodů čipu SID:

Obrázek 1

Zde můžeme vidět, že se jedná o poměrně malý integrovaný obvod s 28 piny, na rozdíl od "konkurenčního" čtyřicetipinového čipu POKEY, jenž měl poměrně velké množství pinů určených pro připojení klávesnice, sériové sběrnice a pro další veskrze "neakustické" účely. Část pinů čipu SID je digitální (dvoustavová), například část určená pro připojení k adresové a datové sběrnici (úrovně odpovídají technologii N-MOS a H-MOS), další piny jsou analogové – vstup zvuku, výstup zvuku, připojení kondenzátorů pro filtry atd. Navíc SID vyžaduje dvoje napájecí napětí – standardních 5 V a poměrně nestandardních 9 V pro analogovou část (novější verze mají toto napětí snížené, takže čip vyzařuje méně tepla).

## Vývoj zvukového čipu SID

## Bloková struktura čipu SID

## Generování akustických signálů
