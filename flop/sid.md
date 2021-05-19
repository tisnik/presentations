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

## Vývoj zvukového čipu SID

Vývoj zvukového čipu SID vedl Robert "Bob" Yannes, který později založil firmu Ensoniq vyrábějící zvukové syntetizéry i zvukové karty určené pro profesionální a poloprofesionální použití. Vzhledem ke značně krátkému termínu, kdy měl být čip SID dokončený, došlo k poměrně nepříjemné věci známé například i ze softwarového vývoje – tvorba dokumentace k finální verzi čipu se odložila a ve skutečnosti nebyla nikdy ve své úplnosti dopsána. To vedlo k zajímavému paradoxu – zvukový čip sice pracoval (a to velmi dobře, zejména když vezmeme v úvahu jeho minimalistický hardware poplatný době vzniku a technologickým možnostem), ale existující dokumentace (platná pro vývojové verze) neodpovídala finálnímu výrobku, což pro mnoho lidí znamenalo určitou formu dobrodružství při hledání všech možností, které tento čip pro tvorbu hudby poskytoval.

SID se nicméně i přes tento malý handicap rozšířil, v neposlední řadě i díky úspěchu osmibitového domácího mikropočítače Commodore C64, kterého se prodalo několik desítek milionů kusů. Časopis Byte dokonce SID zařadil mezi dvacet nejdůležitějších čipů v historii počítačů. Unikátní zvukové možnosti SIDu jsou dodnes využívány v některých syntetizérech, především v SIDStation. Dále je SID použit v HardSIDu a MSSIAH, s velkou pravděpodobností pak ještě v dalších podobně koncipovaných zvukových zařízeních.

## Zapojení vývodů SIDu

Podívejme se nyní na zapojení vývodů čipu SID:

Obrázek 1

Na tomto zapojení můžeme vidět, že se jedná o poměrně malý integrovaný obvod s 28 piny, na rozdíl od "konkurenčního" čtyřicetipinového čipu POKEY (Atari), jenž měl poměrně velké množství pinů určených pro připojení klávesnice, sériové sběrnice a pro další veskrze "neakustické" účely. Část pinů čipu SID je digitální (dvoustavová), například část určená pro připojení k adresové a datové sběrnici (úrovně odpovídají technologii N-MOS a H-MOS). Další piny jsou ovšem analogové – vstup zvuku, výstup zvuku, připojení kondenzátorů pro filtry atd. Navíc SID vyžaduje dvoje napájecí napětí, a to konkrétně standardních 5 V a navíc i poměrně nestandardních 9 V pro analogovou část (novější verze mají toto napětí snížené, takže čip vyzařuje méně tepla, nehledě na jednodušší zapojení celého počítače či zvukového zařízení).

## Bloková struktura čipu SID

Na druhém obrázku je zobrazena bloková struktura zvukového čipu SID. Z tohoto obrázku je patrné, že existuje více navzájem propojených bloků, ve kterých se zvuky vytváří a modifikují. Některé bloky jsou sestaveny z digitálních prvků, další bloky jsou čistě analogové, což přispívá k unikátnímu (a mnohdy i snadno rozpoznatelnému) zvuku.

Obrázek 2

## Stručný popis celého zvukového řetězce

Základ celého řetězce, ve kterém zvuk vzniká, tvoří tři generátory periodického signálu, jehož tvar může být obdélníkový s nastavitelnou střídou, trojúhelníkový či pilový (SID nedokáže automaticky vygenerovat sinusovku, podobně jako mnoho dalších zvukových čipů osmibitové éry, na druhou stranu je tón generovaný sinusovkou plochý, tedy i bez vyšších harmonických). Tón, resp. přesněji řečeno periodický signál, který vychází z generátoru, je upraven v amplitudovém modulátoru, jenž dokáže amplitudu měnit na základě obálky specifikované čtveřicí hodnot známých pod souhrnným označením ADSR, neboli attack, decay, sustain a release. Před vstupem signálu do amplitudového modulátoru lze dva vybrané zvukové signály podrobit kruhové modulaci (ring modulation), jejíž použití taktéž vede k vytvoření unikátních a pro SID typických zvuků.

## Koncová analogová část - filtrace

Signál, který vznikne po aplikaci kruhové modulace a modulace amplitudové, může být buď přímo zesílen a poslán na výstup (taktéž k němu lze přičíst externí signál, například z dalšího SIDu, fajnšmekři dokonce mohou zkombinovat SID a POKEY nebo SID a AY-8910), nebo může být dále zpracován v bloku analogových filtrů. Podle aktuální konfigurace čipu lze použít filtr typu dolní propust, horní propust či pásmová propust.

Konkrétní rozsahy frekvencí pro zmíněné filtry jsou určeny kapacitou kondenzátorů připojených k čipu SID (vstupy CAP1A, CAP1B, CAP2A a CAP2B, používají se kondenzátory s přibližnou kapacitou 6,8 nF) a nastavením 11bitové hodnoty do dvojice řídicích registrů.

## Řídicí registry

Zvukový čip SID je možné ovládat s využitím 29 osmibitových registrů, které jsou rozděleny do pěti skupin. První skupina sedmi registrů slouží pro ovládání zvukového kanálu číslo 1, druhá skupina sedmi registrů k ovládání kanálu číslo 2, třetí skupina taktéž sedmi registrů je (překvapivě) rezervována pro kanál číslo 3, čtvrtá skupina, jež obsahuje čtyři registry, ovládá filtry zapojené v koncovém stupni řetězce zpracování zvuku a konečně pátá skupina, jež taktéž obsahuje čtyři osmibitové registry, je určena pro čtení některých údajů z čipu SID (jedná se o jedinou skupinu registrů, které je možné číst, do ostatních 25 registrů lze data pouze zapisovat).

## Generátory signálů

Generátory signálů tvoří první část celého řetězce vytvářejícího zvuk. Čip SID může pro každý zvukový kanál produkovat periodické signály tří typů (obdélníkový, trojúhelníkový, pilový), popř. lze použít zdroj šumu (noise), který se v praxi využívá, podobně jako v případě minule popsaného zvukového čipu POKEY, například na napodobení zvuku perkusních nástrojů (některé hudební skladby však místo toho využívají zdigitalizované vzorky skutečných perkusních nástrojů).
