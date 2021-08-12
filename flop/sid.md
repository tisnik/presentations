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

Frekvence těchto signálů je odvozena od frekvence hodin (hodinový signál je přiváděn na pin fi2) a šestnáctibitového čísla ukládaného do dvojice řídicích registrů – každý zvukový kanál samozřejmě může mít nastavenou odlišnou frekvenci. Při použití hodinového signálu s frekvencí 1 MHz (přibližně tato frekvence je použita i u osmibitových domácích počítačů Commodore) je rozsah generovaných tónů roven téměř osmi oktávám s velmi malým krokem, který umožňuje plynule přecházet od jedné noty k notě druhé (portamento). V rozsahu zmíněných osmi oktáv lze pro každý zvukový kanál zvolit jeden ze 65536 různých tónů (2^16=65536).

## Střída obdélníkového signálu

Obdélníkový signál, který obsahuje největší podíl vyšších harmonických (nejméně jich má signál trojúhelníkový, jehož tvar je nejvíce "podobný" sinusovce), je zvláštní tím, že je u něj možné volit jeho střídu, tj. poměr mezi dobou trvání nízké a vysoké úrovně. Střída neovlivňuje základní frekvenci signálu ale spektrální charakteristiku vyšších harmonických. V případě SIDu se střída nastavuje v rozsahu 0 až 100% pomocí dvanáctibitového čísla uloženého do dvojice řídicích osmibitových registrů (vyšší čtyři bity druhého registru zůstávají nevyužity).

Při nastavení hodnoty 2047 se generuje obdélníkový signál se střídou 1:1, naopak nejvyšší hodnota (4095) vede k tomu, že z generátoru signálu vychází pouze stejnosměrná složka (DC). Ta sama o sobě samozřejmě není slyšitelná, lze ji však přesto využít, například pro sampling nebo pro netradiční generování tónů pouze pomocí změny tvaru obálky (viz další kapitoly). Střídu je možné měnit velmi rychle, čehož se někdy využívá například ve hrách pro napodobení zvuků některých zbraní.

## Tvarování obálky

Důležitou součást řetězce generujícího zvuk tvoří dva bloky, pomocí nichž je možné tvarovat takzvanou obálku. Obálkou se řídí amplituda signálu na výstupu z bloku označeného Amplitude Modulator. Do tohoto bloku vstupují dva signály – první signál je vytvářený ve výše popsaných generátorech signálů, tj. jedná se buď o periodický obdélníkový, trojúhelníkový či pilový signál, popř. šum. Druhý signál představuje vlastní obálka. Tento signál není obecně periodický (je "spouštěný" programově a jeho střední část označená symbolem S může být libovolně dlouhá) a při porovnání s periodou prvního signálu bývá i mnohem delší, řádově v desítkách milisekund až jednotkách sekund.

S využitím  obálky je možné zvukový signál upravit tak, aby se do značné míry podobal tónu reálného hudebního nástroje, což je i jeden z důvodů, proč se obálky stejného typu (nazývané ADSR – důvod je uveden v dalším odstavci) používají i v mnoha hudebních syntetizérech a některých dalších zvukových čipech (z těch známějších se jedná o OPL-2/Yamaha YM 3812 a OPL-3/Yamaha YMF 262).

Základní tvar obálky je určen čtveřicí parametrů – attack (doba či strmost náběhu první hrany), decay (doba či strmost druhé – klesající/sestupné – hrany), sustain (stabilní úroveň signálu obálky po prvotním vzrůstu a poklesu, většinou vyjadřovaná v procentech amplitudy) a release (doba či strmost poslední – klesající – hrany). Pro každý z těchto parametrů je v řídicích registrech zvukového čipu SID vyhrazena čtveřice bitů.

Čtyřbitová hodnota parametru attack určuje dobu náběhu v rozsahu 2 ms až 8 sekund (předpokládá se, že na vstup hodin fi2 je připojen hodinový signál s frekvencí 1 MHz; v případě odlišné frekvence se pochopitelně budou lišit i uvedené časy). Hodnoty parametrů decay a release určují dobu trvání sestupných hran v rozsahu 6 ms až 24 sekund, tj. sice se u nich též používá pouze čtyřbitová hodnota, ale všechny časy jsou třikrát delší. Hodnota parametru sustain představuje zlomek amplitudy v rozsahu 0/15 (tj. ticho – na výstupu z bloku Amplitude Modulator je stále signál s nulovou amplitudou) až 15/15 (odpovídá 100%).

## Řízení doby sustain i amplitudy obálky

Povšimněte si, že čtyři výše uvedené parametry nejsou pro úplné popsání tvaru obálky dostatečné. Především chybí určení doby, po kterou si obálka drží úroveň sustain a taktéž amplituda, tj. maximální úroveň signálu obálky v bodě, kde se náběžná hrana attack láme a mění se v sestupnou hranu decay. Tyto dva parametry jsou totiž nastavovány samostatně.

Maximální úroveň signálu obálky je vždy nastavena na 100%, ovšem s tím, že výstupní úroveň z celého řetězce pro generování zvuků je globálně ovlivnitelná čtyřmi bity jednoho řídicího registru. Doba trvání úrovně sustain je určena bitem GATE ukládaným do jednoho z řídicích registrů, zvlášť pro každý zvukový kanál. Ve chvíli, kdy je tento bit nastaven na logickou jedničku, spustí se cyklus attack (obálka se začne měnit dle náběžné hrany), za nímž automaticky následuje cyklus release (první sestupná hrana) až do chvíle, kdy se úroveň obálky ustálí na hodnotě sustain. Tato hodnota se udržuje tak dlouho, dokud má bit GATE hodnotu logické jedničky. Ve chvíli, kdy se programově tento bit vynuluje, začne probíhat cyklus release, tj. úroveň obálky se snižuje až k nule.

Poznámka: například u čipů OPL2 a OPL3 se namísto bitu GATE používá bit nazvaný KEY-ON, ovšem s velmi podobným významem.

## Přehrávání samplů

V případě, že se čip SID používá pro přehrávání samplovaných zvuků, je možné hodnotu jednotlivých vzorků (samplů) převádět na čtyřbitové číslo, které ovlivňuje úroveň sustain. Samotná obálka se změní tak, že hodnoty attack, decay i release jsou nastaveny na nulovou hodnotu (to odpovídá nejstrmějším hranám), hodnota bitu GATE zůstává nastavená na logickou jedničku a pouze se programově mění úroveň sustain.

## Bit GATE ve chvíli fází ATTACK a RELEASE

SID taktéž umožňuje změnu hodnoty bitu GATE v kterémkoli okamžiku. Pokud se například tento bit vynuluje ještě v době, kdy probíhá cyklus attack, začne ihned probíhat cyklus release, tj. z obálky zmizí její prostřední část. Taktéž již před doběhnutím cyklu release je možné bit GATE znovu nastavit na úroveň logické jedničky, čímž se ihned nastartuje další cyklus attack (některé hudební syntetizéry, které taktéž obálku ADSR využívají, tento "zrychlený" přechod mezi cykly attack a release, neumožňují).

## Další části řetězce zpracování zvuku

Generátory signálů a tvarovače obálek (tedy ADSR) jsou základními bloky, kterými je možné generovat zvuky napodobující různé hudební nástroje. Ovšem to není zdaleka vše, co SID dokáže. Především je možné ovlivnit výstup z jednoho generátoru signálů výstupem z generátoru dalšího s využitím takzvané kruhové modulace (ring modulation – název této modulace je odvozen od způsobu zapojení polovodičových diod v analogovém obvodu, který tuto modulaci prováděl například u superheterodynů – FM přijímačů), vzájemně synchronizovat jednotlivé generátory signálů, používat analogové výstupní filtry typu dolní propust, horní propust a pásmová propust, přimixovat externí zvukový signál, navzájem zkombinovat signály vytvářené v generátorech signálů aj.

Těmito technikami, které mj. značnou měrou přispěly k velké oblibě SIDu, se budeme podrobněji zabývat v následujících kapitolách.

## Kruhová modulace (ring modulation)

Před vstupem signálu vytvářeného v generátoru signálů do amplitudového modulátoru lze dva vybrané zvukové signály podrobit kruhové modulaci (ring modulation), jejíž použití vede k syntéze unikátních a pro SID typických zvuků. SID je ostatně jedním z mála zvukových čipů, který kruhovou modulaci používá; například na čipech s OPL-2 či OPL-3 ji lze napodobit jen velmi složitě. Kruhovou modulaci je možné zapnout vždy pro dvojici vybraných zvukových kanálů: kanál 1 může být modulovaný výstupem z oscilátoru kanálu 3, kanál 2 může být modulovaný výstupem z oscilátoru kanálu 1 a konečně kanál 3 lze modulovat výstupem z oscilátoru zvukového kanálu číslo 2 (viz čtvrtý obrázek s modrými šipkami, jimiž je naznačeno, čím je který signál modulován).

Aby byl vliv kruhové modulace slyšitelný, musí být na modulovaném zvukovém kanálu povolen oscilátor vytvářející trojúhelníkový signál (jeho vzestupná i sestupná hrana má stejný sklon). Z modulačního kanálu je vždy využit obdélníkový signál o zadané frekvenci, který "sampluje" (násobí) signál trojúhelníkový na modulovaném zvukovém kanálu, který má většinou poněkud nižší frekvenci, než signál obdélníkový.

Frekvence obou kanálů, jejichž signály vstupují do kruhového modulátoru, mohou být soudělné či nesoudělné – pokaždé se syntetizuje tón s odlišným zabarvením (zajímavě zní například poměr frekvencí 3:2 či 5:4). Násobení v časové oblasti vede ke vzniku celého širokého spektra neharmonických frekvencí v oblasti frekvenční čehož je možné využít při tvorbě zabarvených tónů typických pro hudbu SIDu. Zabarvení je při použití kruhové modulace zcela odlišné od zabarvení získaného pomocí frekvenční či fázové modulace (FM – frequency modulation, PM – phase modulation), i když i při použití těchto modulací dochází ke vzniku dalších vyšších a nižších frekvencí ve výsledném zvuku.

## Výstupní filtry

SID je hybridním čipem obsahujícím jak digitální obvody (jedná se například o již dříve popisované generátory signálů nebo část, která zajišťuje připojení čipu na adresovou a datovou sběrnici i logiku pro výběr řídicích a stavových registrů), tak i obvody čistě analogové. Na základě analogových obvodů jsou vytvořeny i výstupní filtry, do kterých je možné selektivně přivádět jak výstupy z jednotlivých zvukových kanálů (po aplikaci kruhové modulace a amplitudové modulace pomocí obálky ADSR), tak i externí zvukový signál.

Výstupní filtry jsou tří typů – dolní propust (LP – low pass), horní propust (HP – high pass) a pásmová propust (BP – band pass). Filtry ve své podstatě tvoří samostatnou část zvukové syntézy, která není aditivní (do signálu se nepřidávají další složky), ale naopak subtraktivní (dochází k odstranění či zmenšení vybraných frekvencí). Jednotlivé filtry je možné navzájem kombinovat a vytvořit tak například z dolní a horní propusti pásmovou zádrž, popř. z dolní propusti a pásmové propusti vytvořit dolní propust s odlišnou charakteristikou. Pomocí dvou osmibitových řídicích registrů se nastavuje mezní frekvence všech filtrů (jedná se o jedinou frekvenci platnou pro všechny tři typy filtrů, její význam je ovšem u každého filtru jiný).

V případě, že jsou mezi piny pojmenované CAP1A a CAP1B i CAP2A a CAP2B připojeny dva kondenzátory s kapacitou 6,8 mikrofaradů, lze mezní frekvenci filtrů měnit v rozsahu přibližně 30 Hz až 12 kHz (počítače Commodore C64 obsahovaly kondenzátory právě o této kapacitě, ovšem SID lze použít i v dalších systémech,
kde mohou být kapacity odlišné podle toho, k jakému účelu je tento čip určen). Samotná frekvence je reprezentována jako jedenáctibitové bezrozměrné
číslo, skutečná frekvence je na této hodnotě lineárně závislá.

Útlum zvukového signálu procházejícího dolní či horní propustí je po překročení mezní frekvence roven přibližně 12 decibelům na oktávu. U pásmové propusti je útlum (v obou směrech od mezní frekvence) roven šesti decibelům na oktávu. Připomeňme si, ze zvýšení tónu o jednu oktávu znamená zdvojnásobení jeho frekvence a snížení o jednu oktávu naopak frekvenci poloviční. Utlum je udávaný v decibelech, tj. logaritmickém poměru mezi naměřenou (vypočtenou) amplitudou a amplitudou maximální (výsledek je navíc vynásoben deseti či dvaceti podle toho, zda jde o napěťový či výkonový útlum popř. zesílení).

## Vstup externího signálu a regulace hlasitosti na výstupu

Na blokovém schématu zvukového čipu SID můžeme vidět i vstup externího signálu spolu s možnou cestou, kterou tento signál může být zpracováván – buď se externí signál přímo smísí s výstupy zvukových kanálů nebo je přiveden na vstup filtrů popsaných v předchozí kapitole. Na tento analogový vstup se vstupní impedancí přibližně 100 kiloohmů lze zapojit prakticky libovolný zvukový čip, například další SID nebo i AY-8910 či POKEY :-), popřípadě analogový výstup ze zvukového syntetizéru (elektronické varhany).

Počet "sériově" zapojených čipů je prakticky omezen pouze vzrůstající úrovní šumu. Tento vstup taktéž mnoho uživatelů využilo u série SID 8580 pro přivedení stejnosměrné složky do bloku VOLUME, čímž bylo umožněno přehrávání samplovaných zvuků, protože tato poslední série čipu SID byla upravena tak, aby docházelo k menšímu zašumění výstupu, což však mělo za následek absenci stejnosměrné složky (DC), která je při přehrávání samplů použita (viz následující kapitola). Posledním blokem na SIDu je blok nazvaný VOLUME, ve kterém se globálně mění hlasitost výsledného zvuku. Pro určení hlasitosti jsou rezervovány čtyři bity v jednom z řídicích registrů, čímž je vlastně i určen typický formát samplů při přehrávání digitalizovaných zvuků.

## Přehrávání digitalizovaného (samplovaného) zvuku

Na zvukovém čipu SID je možné poměrně snadno přehrávat i digitalizovaný (samplovaný) zvuk. Existuje několik možných způsobů přehrávání samplovaného zvuku; typicky se používá buď přímé řízení výstupní úrovně v bloku VOLUME, na jehož vstup je přivedena stejnosměrná složka (takto lze snadno pracovat se čtyřbitovými samply) nebo se používá PWM – pulse width modulation, tj. programová změna střídy obdélníkového signálu. V tomto případě není pro změnu střídy možné využít přímo možnosti SIDu, protože jeho zvukové generátory nemají tak vysokou frekvenci (pro PWM se musí používat časový krok odpovídající samplované frekvenci vynásobené dynamickým rozsahem samplu, tj. například 2^8).

S využitím PWM lze i na běžném počítači Commodore C64 bez dalších hardwarových úprav přehrávat digitalizovaný zvuk samplovaný na frekvenci cca 16 kHz se samply uloženými na šesti bitech, což odpovídá dynamickému rozsahu zhruba 36 dB (se SuperCPU lze dosáhnout vzorkovací frekvence až 19 kHz s plně osmibitovými vzorky). Podrobný popis jednotlivých způsobů přehrávání digitalizovaných zvuků (včetně praktických ukázek přehrávacích rutin) je uveden v článku The C64 Digi, jehož autory jsou Robin Harbron, Levente Harsfalvi a Stephen Judd. Nejjednodušší přehrávací rutina, která modifikuje přímo výstupní hlasitost v závislosti na nejvyšších čtyřech bitech osmibitového samplu, vypadá následovně:


## SID: minulost a současnost

## Ukázky hudby pro SID

