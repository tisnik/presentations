V tomto článku se seznámíme se všemi důležitými zvukovými a hudebními čipy, které byly používány v osmibitových herních konzolích i v osmibitových domácích mikropočítačích, i když je nutné poznamenat, že některé z těchto čipů poměrně úspěšně přežily i do éry 16bitových a 32bitových strojů. U každého popisovaného čipu se budu snažit o porovnání s integrovaným obvodem POKEY, který nepochybně všichni čtenáři FLOPu velmi dobře znají (ostatně v čísle 39 vyšel velmi podrobný návod popisující všechny důležité vlastnosti tohoto čipu).

Integrované obvody určené pro generování zvuků a hudby tvoří nedílnou a současně i velmi důležitou součást historie vývoje herních konzolí a samozřejmě i osmibitových domácích mikropočítačů. Až na několik výjimek, mezi něž patří především původní ZX Spectrum a vlastně i všechny počítače vyráběné v ČSSR, byly těmito čipy osazeny prakticky všechny úspěšné herní konzole a mikropočítače vyráběné od konce sedmdesátých let minulého století až po začátek let devadesátých, kdy již na trhu začaly převažovat šestnáctibitové a 32bitové stroje. A právě vlastnosti a nabízené možnosti zvukových čipů do značné míry určovaly oblíbenost dané platformy.

V dalším textu budou popsány tyto čipy:

* Integrovaný obvod TIA použitý především v herních konzolích Atari 2600 i v Atari 7800

* Integrovaný obvod POKEY, který všichni nepochybně znáte

* Zvukový čip Texas Instruments SN76489 (DCSG)

* Zvukový čip Texas Instruments SN76496 (varianta DCSG)

* Do třetice zvukový čip Texas Instruments, tentokrát s označením SN76477

* Zvukový subsystém konzole NES založené na čipu Ricoh 2A03/2A07

* Integrovaný obvod AY-3-8910 neboli podomácku "áýčko" a jeho varianty (Yamaha YM2149 atd.)

* Na závěr nesmíme zapomenout na SID firmy MOS



# Úvodní informace

Ještě před popisem jednotlivých čipů si musíme ozřejmit, že pod termínem "zvukový čip" nebo "hudební čip" můžeme mít na mysli tři typy obvodů. Nejjednodušší jsou obvody označované zkratkou PSG neboli Programmable Sound Generator. Interně mnohem komplikovanější jsou čipy s FM syntézou a později, se zvyšující se kapacitou RAM, se začaly více prosazovat i obvody určené především pro přehrávání a mixování samplů (PCM). Nás bude v tomto článku zajímat především první skupina, která je v mnoha ohledech nejzajímavější a navíc nás PSG provázely prakticky celou érou osmibitových domácích mikropočítačů i konzolí.

Všechny PSG, které si popíšeme v navazujících odstavcích, jsou založeny na zpracování vstupního hodinového signálu, kterým jsou řízeny interní moduly PSG. PSG mohou generovat obdélníkové signály s volitelnou frekvencí (a někdy i s konfigurovatelnou střídou), dále pak šum s volitelnou frekvencí a některé PSG navíc generují i trojúhelníkový a/nebo pilový signál (pro zvuk hudebních nástrojů je vhodnější pilový signál). Podle typu PSG můžeme na čipu očekávat i takzvaný generátor obálky (envelope generator), popř. i různé typy filtrů a propustí.

V případě, že je hodinový signál přiveden na běžný čítač s výstupem propojeným s klopným obvodem T, bude takto zapojený modul generovat obdélníkový výstupní signál s frekvencí určenou počáteční hodnotou čítače (samotná konstrukce čítačů se od sebe může odlišovat, většinou však čítají směrem k nule a při podtečení se na výstupu objeví impuls přivedený do klopného obvodu). Takto vytvořené obdélníkové vlny asi není zapotřebí Ataristům zdlouhavě popisovat, ovšem zajímavé je zjistit, co se skrývá pod pojmem trojúhelníková vlna.

Několik PSG totiž používá pro generování trojúhelníkového nebo i pilového signálu čtyřbitový čítač (tedy 16 úrovní), jehož výstup je přes jednoduchý čtyřbitový D/A převodník přiváděn na reproduktor. To znamená, že na osciloskopu uvidíme spíše různé schůdky, ale určitě ne čistý trojúhelníkový průběh. Konkrétní tvar signálu je samozřejmě ovlivněn i filtry a zesilovačem, které "schůdky" trošku vyhladí.

Generování šumu je u naprosté většiny PSG založeno na použití posuvného registru se zpětnou vazbou (LSFR, též poly counter), přičemž bitová délka tohoto registru určuje, jak bude šum znít - zda bude skutečně "náhodný", nebo zda bude mít tak krátkou periodu, že vlastně vznikne pouze zkreslený tón. LSFR použité u zvukových generátorů mají mnoho podob a různou délku (od čtyř do sedmnácti bitů), takže se jim budeme samostatně věnovat u každého popisovaného čipu.



# Integrovaný obvod TIA použitý v Atari 2600 (VCS) i v Atari 7800

Nejprve si popíšeme zvukové možnosti čipu TIA neboli plným jménem Television Interface Adaptor. Jedná se o jeden z pouhých tří integrovaných obvodů tvořících ústřední prvky v minulosti velmi populární osmibitové herní konzole Atari 2600.

Čip TIA se kromě generování grafického obrazu stará i o zvukovou syntézu. Ta je z dnešního pohledu dosti zvláštní. Na jednu stranu je způsob zvukové syntézy velmi jednoduchý a v některých ohledech připomíná způsob zvukové syntézy použité o několik let později v čipu POKEY v osmibitových domácích mikropočítačích Atari. Jednoduchost spočívá v možnosti generování pouze obdélníkových signálů (pravidelných popř. sice nepravidelných, ale periodických), jejichž amplituda může být nastavena na hodnoty 0-15 (řídí se tedy čtyřmi bity).

Na druhou stranu však způsob interního zapojení posuvných registrů se zpětnou vazbou nabízí poměrně velké množství kombinací, které vlastně nenajdeme ani u čipu POKEY, který je jinak v oblasti generování zvuků a hudby nástupcem čipu TIA.

Vzhledem k tomu, že se čip TIA stará jak o vytváření video signálu, tak i pro syntézu zvuků a hudby, je v něm několik modulů společných. Zejména se to týká způsobu generování základního hodinového signálu (přesněji řečeno dvojice signálů), které vstupují do zvukového systému a od jejichž frekvence se odvíjí i frekvence přehrávaných tónů.

Základem všech signálů řídicích celou herní konzoli Atari 2600 je oscilátor, který u NTSC varianty generuje hodinový signál o frekvenci 3,579545 MHz a u PAL varianty poněkud nižší frekvenci 3,546894 MHz. Tento základní signál se nazývá pixel clock (v některých dokumentech též color clock), protože kromě dalších činností řídí i generování pixelů na obrazových řádcích (262 řádků a necelých 60 snímků za sekundu u NTSC, 312 řádků a necelých 50 snímků za sekundu u PAL). Současně se tento signál dělí třemi a výsledek o frekvencích 1,193182 MHz (NTSC) popř. 1,182298 MHz (PAL) slouží jako hlavní řídicí hodinový signál mikroprocesoru MOS 6507. Z tohoto důvodu se tento signál nazývá CPU clock a proto se dočteme, že hodinová frekvence konzole Atari 2600 je 1,19 MHz, což ovšem platí jen pro NTSC variantu.

Oba dva výše zmíněné signály, tj. jak pixel clock, tak i CPU clock, jsou dále děleny konstantou 114 použitou mj. video subsystémem pro vykreslení jednoho obrazového řádku. Současně však takto vydělené signály vstupují i do audio systému. Jejich frekvence je rovna 31399 Hz a 10466 Hz pro systém NTSC a 31113 Hz a 10371 Hz pro systém PAL. V původních originálních materiálech je ovšem jen lakonicky napsáno "na vstupu audio systému je signál o frekvenci přibližně 30 kHz", což je nepřesné a může se to negativně projevit při volbě konstant při přehrávání not.

V případě integrovaného obvodu TIA jsou programátorům k dispozici dva na sobě nezávislé programovatelné zvukové kanály. Každý z těchto kanálů je řízen trojicí řídicích registrů, celkem tedy může programátor modifikovat osm řídicích registrů: AUDF0, AUDF1, AUDC0, AUDC1, AUDV0 a AUDV1. Vzhledem k tomu, že možnosti obou zvukových kanálů jsou totožné (všechny obvody jsou zdvojeny), budeme v dalším textu popisovat pouze kanál první, který je řízený trojicí registrů AUDF0, AUDC0 a AUDV0.

První řídicí registr zvukového kanálu (AUDF0), přesněji řečeno pět bitů tohoto registru určuje konstantu 1 až 32 použitou při dělení vstupní frekvence. Buď se použije frekvence pixel_clock/114 nebo CPU_clock/114. Výsledkem dělení je obdélníkový signál o frekvenci přibližně 1 kHz až 30 kHz (popř. 300 Hz až 10 kHz, opět jen přibližně), který je přiváděn do dvojice konfigurovatelných posuvných registrů (LSFR) se zpětnou vazbou. První registr má délku pěti bitů, druhý délku čtyř bitů, ovšem je možné je spojit do jediného registru o délce devíti bitů (viz další text).

Tyto dva posuvné registry slouží jak pro generování čistého obdélníkového signálu, tak i pro vytváření šumu (noise generator) s různou charakteristikou. Konfigurace obou posuvných registrů je řízena registrem AUDC0, přičemž význam mají pouze čtyři spodní bity. Jednotlivé kombinace určují jak zdroj signálu (pixel_clock/114 či CPU_clock/114), tak i způsob zapojení zpětných vazeb v obou posuvných registrech.

Jedna z kombinací umožňuje generovat konstantní signál o hodnotě 1, což je výhodné, protože je možné zvuk jednoduše samplovat rychlou změnou obsahu registru AUDV0. Další dvě kombinace přepínají pětibitový posuvný registr do režimu, v němž se stále opakuje sekvence 0101010..., tj. posuvný registr zde slouží jako dělička vstupní frekvence dvěma (popř. šesti, protože CPU_clock=pixel_clock/3). Právě tento režim se používal při přehrávání čistých tónů (ovšem rozladěných).

Další dostupný režim taktéž používá posuvný registr, tentokrát ovšem takovým způsobem, že se vstupní signál dělí hodnotou 31. Opakuje se v něm totiž sekvence 31 bitů, z nichž 13 sousedních bitů je nulových, zbytek jedničkových (to, že počet jedniček a nul není zcela totožný, se projeví ve výsledném zvuku jen nepatrně). Opět platí, že CPU_clock má třetinovou frekvenci, takže v oficiálních materiálech se hovoří o dělení konstantou 93; ve skutečnosti tato "magická" konstanta odpovídá 3*31.

Další režimy již využívají oba posuvné registry pro tvorbu šumu. Pokud je použit jen čtyřbitový registr, je perioda opakování pouze 15 bitů, což je opět možné využít pro generování tónů, ovšem zkreslených. Podobně při použití pětibitového LSFR s periodou opakování 31. Spojením obou dvou registrů za sebe se generuje šum o periodě 511 bitů (podobného efektu lze docílit i u čipu POKEY).

Nejsložitější je režim, v němž pětibitový LSFR řídil čtyřbitový LSFR: pokud se na výstupu prvního LSFR objeví jednička, provede se posun i ve čtyřbitovém LSFR; v opačném případě se druhý LSFR ignoruje. Výsledkem je pseudonáhodný signál s periodou 15*31=465 bitů (další "magická" hodnota, která není v původních materiálech nijak vysvětlena a musela být až mnohem později vydedukována ze schémat čipu TIA).

Poznámka: se čtyřbitovým, pětibitovým i devítibitovým posuvným registrem se setkáme i v dále popsaném čipu POKEY, což není náhoda (ostatně i z teorie LSFR vychází, že například osmibitový posuvný registr vyžaduje mnohem složitější zapojení zpětné vazby, než registr sedmibitový nebo devítibitový, "výhodné" délky jsou 2-7 bitů, 9-11 bitů, 15 bitů a 17 bitů).

Výsledný signál, nezávisle na tom, zda se jedná o čistý obdélníkový průběh či o šum, je následně zesílen 1 až šestnáctkrát na základě hodnoty posledního řídicího registru (AUDV0, AUDV1). Interně se nejedná o nic složitého - čtyři bity, resp. přesněji řečeno čtyři logické úrovně, jsou přivedeny na jednoduchou odporovou síť se čtyřmi rezistory o hodnotách 3k7, 7k5, 15k a 30k (takže se vlastně nejedná o zesílení, ale naopak o konfigurovatelné zeslabení). Výsledné napětí, které na rezistorech vznikne, je vyvedeno na výstupní pin čipu TIA (ten tedy musí obsahovat dva piny s analogovým zvukovým výstupem, každý zvukový kanál má vyhrazen jeden pin).

Zvuk generovaný čipem TIA je možné poměrně jednoduše rozeznat od zvuku dalších herních konzolí nebo domácích mikropočítačů, už jen z toho důvodu, že prakticky všechny noty jsou kvůli velmi krátkému čítači, který je použitý pro dělení vstupní frekvence, rozladěny. Avšak i přesto pro TIA dodnes vznikají různá více či méně vážně míněná hudební díla, a to včetně poměrně úspěšných pokusů o čtyřbitový sampling (což ovšem vyžaduje použití "supercartridgí" s dostatečně velkou EPROM, protože interní RAM o kapacitě celých 128 bajtů je samozřejmě pro tyto účely nepoužitelná).



# Zvukový čip POKEY

Pro čtenáře tohoto článku (a vlastně i celého FLOPu) pravděpodobně nebude žádným tajemstvím, že typickým zástupcem osmibitových domácích mikropočítačů, které využívaly pro syntézu zvuku i hudby speciální integrovaný obvod, jsou všechny osmibitové mikropočítače firmy Atari. Pro syntézu zvuku (a také několik dalších důležitých operací popsaných na konci této kapitoly) byl firmou Atari vyvinut integrovaný obvod nazvaný POKEY, jehož jméno je odvozeno od sousloví POtentiometer and KEYboard (což je zvláštní, protože mnohem větší význam má generátor zvuku a taktéž modul určený pro ovládání sériové komunikace).

Tento čip není využitý pouze v domácích mikropočítačích, ale také v některých herních konzolích firmy Atari a taktéž herních automatech (ostatně pro firmu Atari představovala výroba herních konzolí i automatových her v jednu chvíli převážnou část zisků). V případě čipu POKEY se jedná o hybridní integrovaný obvod, který obsahuje jak digitální část (právě ta je použita i pro zvukovou syntézu), tak i část analogovou – tento obvod je totiž vybaven mj. i funkcí určenou pro (relativně pomalý) převod analogového signálu na osmibitové vzorky, čehož firma Atari využívala pro připojení ovladačů typu paddle ke svým počítačům i herním konzolím.

V úvodním odstavci této kapitoly jsme jsme si řekli, že integrovaný obvod POKEY slouží mj. i ke zvukové syntéze. Zvuk je možné generovat s využitím čtyř zvukových kanálů (lze tedy vytvářet až čtyřhlasou polyfonii), přičemž vždy dva kanály je možné v případě potřeby spojit do kanálu jednoho, u něhož lze přesněji řídit frekvenci zvuku (v podstatě to znamená, že se dva osmibitové čítače/děliče spojí do jednoho čítače šestnáctibitového a popř. se změní zdroj vstupních hodinových signálů – viz další text). Pro ovládání zvukového subsystému se používá devět osmibitových řídicích registrů: AUDF1 až AUDF4, AUDC1 až AUDC4 a společný řídicí registr AUDCTL.

Každý zvukový kanál produkuje obdélníkový signál s amplitudou, kterou je možné nastavit do jedné ze šestnácti úrovní (pro specifikaci amplitudy každého kanálu jsou vyhrazeny v ovládacích registrech pouze čtyři bity). Nulová logická hodnota obdélníkového signálu na vstupu vždy vede k nulovému napětí na výstupu zvukového kanálu; logická jednička je převedena na jednu ze šestnácti úrovní napětí (podobně jako u TIA a ostatně i u prakticky všech dalších PSG).

Závislost mezi zvolenou úrovní a napětím není přesně lineární; taktéž generovaný signál není (například po připojení na osciloskop) zcela přesně obdélníkový, čehož se dodnes využívá při tvorbě trojúhelníkových a pilových průběhů (ovšem nutno říci, že za značné pomoci mikroprocesoru, přesného časování, popř. s využitím dále zmíněného hi-pass filtru).

Na vstup zvukového subsystému je přiváděn hodinový signál procesoru, který má frekvenci cca 1,79 MHz pro počítače s televizní normou NTSC a 1,77 Hz pro počítače s normou PAL. Tento signál je pro další účely dělen konstantami 28 a 114, takže vzniknou další dva signály, z nichž první má frekvenci přibližně 63 kHz a druhý necelých 16 kHz. S využitím řídicích registrů lze zvolit, který z těchto signálů se bude používat pro řízení zvukových kanálů (ovšem ne všechny možnosti je možné vybrat současně, viz dále).

Frekvence zvuku v každém zvukovém kanálu je řízena děličem 1:N, který je interně implementovaný jako čítač (ostatně právě na základě čítačů obvod POKEY detekuje stlačené klávesy, generuje pseudonáhodná čísla, provádí A/D převod z ovladačů paddle a komunikuje se SIO). Pokud nejsou zvukové kanály spojeny do dvojic, je funkce čítače vlastně velmi jednoduchá: na vstup čítače je přiveden jeden ze tří hodinových signálů zmíněných výše a při každém taktu se hodnota čítače sníží o jedničku.

Při podtečení hodnoty čítače se na jeho výstupu objeví logická jednička a současně je hodnota v čítači resetována na uživatelem zvolenou hodnotu (ta je uložena v příslušném řídicím registru AUDF1 až AUDF4). Výstup čítače je použit v dalších obvodech. Například při generování čistého tónu se jedničkou, která se objeví na výstupu čítače, pouze překlopí jeden klopný obvod (takže se vlastně vstupní frekvence navíc dělí dvěma).

Změnou obsahu řídicího registru obvodu POKEY je možné nakonfigurovat jednu ze tří základních kombinací zvukových kanálů:

1. Čtyři samostatné zvukové kanály, přičemž frekvence každého z nich je vytvořena pomocí osmibitového děliče, na který se přivádí jeden ze dvou vstupních hodinových signálů (cca 16 kHz, cca 63 kHz). Tato konfigurace čipu POKEY je použita při práci se zvukem z Atari BASICu (známý příkaz SOUND a,b,c,d). V tomto režimu lze při standardním nastavení generovat tóny v rozsahu zhruba čtyř oktáv, ovšem výběrem odlišného hodinového signálu je možné celou škálu 256 různých tónů posunout.

2. Dva zvukové kanály, přičemž frekvence každého z nich je vytvořena pomocí šestnáctibitového děliče, který vznikl spojením dvou děličů osmibitových. V takovém případě je možné na vstup děliče přivádět přímo hodinovou frekvenci procesoru, tj. vybírat mezi třemi vstupními signály cca 16 kHz, cca 63 kHz a 1,77 popř. 1,79 MHz podle televizní normy). Tónový rozsah z obou stran v tomto případě přesahuje limity lidského sluchu (infrazvuk, ultrazvuk) i možnosti zesilovačů.

3. Jeden zvukový kanál řízený šestnáctibitovým děličem a dva kanály řízené děličem osmibitovým (tuto konfiguraci využívalo mnoho hudebníků, kteří přesněji řízený zvukový kanál použili pro basový hudební nástroj a další dva kanály pro perkusní nástroj – někdy samplovaný – a hlavní melodii hranou většinou na vyšších frekvencích).

Poznámka: v případě, že se dva zvukové kanály spojí za sebe, dojde ke snížení současně přehrávaných zvuků na 3 nebo dokonce jen na 2, ale zvýší se přesnost čítače, protože vstupní frekvence může být dělena hodnotou 1 až 2^16. V tomto případě se však volí vyšší frekvence hodinových signálů na vstupu obvodu: z cca 16 kHz na 63 kHz nebo na CPU clock, jinak by po vydělení příliš velkou hodnotou byl na výstupu zvukových kanálů infrazvuk, který se v případě obdélníkového průběhu projevuje pouze "lupáním" membrány reproduktoru při skokové změně amplitudy.

Zastavme se na chvíli u popisu subsystému pro generování šumu popř. zkreslených periodických signálů. Ten je založen na již zmíněných LSFR, tedy posuvných registrech se zpětnovazební smyčkou (dva vybrané bity se přes XOR hradlo vrací zpět na vstup čítače). LSFR se někdy označují termínem poly čítače. Připomeňme si, že na výstupu děličů (tvořených osmibitovými čítači popř. dvěma spojenými osmibitovými čítači) získáme po každých N cyklech vstupního signálu logickou úroveň 1. Pokud potřebujeme generovat čistý tón, je tato úroveň použita pro změnu (toggle) výstupní úrovně v klopném obvodu typu D (opět se zpětnou vazbou). Výsledkem je obdélníkový signál.

Ovšem je možná i další kombinace využívající zmíněné poly čítače. Obvod POKEY obsahuje celkem tři poly čítače (čtyřbitový, pětibitový, sedmnáctibitový), jejichž výstup může řídit vybraný zvukový kanál. Všechny čtyři zvukové kanály se dělí o stejné poly čítače, ovšem každý zvukový kanál může mít nastavenou jinou frekvenci, tj. i výsledný zvuk bude odlišný. U sedmnáctibitového poly čítače (viz další odstavce) je vzdálenost mezi stejnými vzorky (perioda) tak velká, že ho lze považovat za generátor náhodných impulsů, který vytváří bílý šum.

Princip řízení zvukového kanálu poly čítačem je ve skutečnosti velmi jednoduchý – řízení je prováděno obyčejným logickým hradlem a klopným obvodem typu D. Poly čítače sice mění hodnotu na svém výstupu velmi rychle (jsou totiž řízeny přímo hodinovým signálem mikroprocesoru, tj. cca 1,79 MHz pro počítače pracující v normě NTSC a 1,77 MHz pro počítače s televizní normou PAL), ale maximální frekvence na výstupu zvukového kanálu je kvůli zapojenému logickému hradlu a klopnému obvodu omezena frekvencí získanou pomocí děliče 1:N (neboli hodnota na výstupu klopného obvodu se nemůže měnit s větší frekvencí, než je frekvence přivedená na jeho vstup CLK).

Je to vlastně velmi elegantní řešení, kdy si tvůrci čipu POKEY vystačili s pouhými třemi poly čítači sdílenými všemi čtyřmi zvukovými kanály (ostatně stejný minimalismus a eleganci nalezneme v high-pass filtru popsaného níže).

Samotný poly čítač, tj. generátor pseudonáhodného šumu, je tvořen posuvným registrem řízeným externím hodinovým signálem. S každým taktem hodin dojde k posunu obsahu registru (tj. čtyř, pěti, sedmnácti a ve speciálním případě devíti bitů) o jednu pozici. Na vstup posuvného registru je zpětnovazební smyčkou přivedena binární hodnota získaná pomocí hradla typu XOR připojeného svými vstupy na třetí a poslední bit posuvného registru – hodnota, na výstupu hradla je tedy zapsána do první pozice.

Pokud vezmeme do úvahy logickou funkci, kterou hradlo typu XOR reprezentuje, dojdeme k závěru, že po inicializaci čipu POKEY může mít posuvný registr prakticky jakoukoli nenulovou hodnotu, protože i za této situace rychle dojde k jeho naplnění pseudonáhodnými daty, které se poté periodicky opakují s periodou, jejíž délka závisí na bitové délce samotného posuvného registru.

Pokud má registr délku n bitů, je perioda rovna 2^n-1 taktům, protože jeden zbývající stav – samé nulové bity – tvoří samostatný (nezajímavý) cyklus. Poslední bit posuvného registru představuje i jeho finální výstup, tj. sekvenci pseudonáhodných binárních hodnot, kterou po zpracování obvodem POKEY (zejména po nastavení amplitudy) slyšíme.

Zatímco čtyřbitové a pětibitové poly čítače produkují poměrně rychle se opakující pseudonáhodné sekvence (lze s nimi napodobit například zvuk leteckých motorů), sedmnáctibitový poly čítač již má délku sekvence tak dlouhou, že s ním lze generovat náhodný zvuk. Tento čítač lze také překonfigurovat tak, že se jeho délka sníží na devět bitů (což pravděpodobně souvisí se snahou přiblížit se zvukovým možnostem čipu TIA). Překonfigurování je snadné: zpětnovazební smyčka je přepojena do osmého bitu a nikoli do bitu prvního.

Poslední zajímavou funkcí čipu POKEY související s generováním zvuků, je možnost zařadit do řetězce zpracování i takzvaný high-pass filtr. Ovšem tento název nás nesmí zmást, protože se nejedná o skutečnou analogovou či digitální horní propust, ale o "pouhý" klopný obvod typu D doplněný o hradlo. Na vstup D (data) je přiváděn výstup z jednoho zvukového kanálu, na vstup CLK (hodiny, resp. přesněji zapamatování D) pak výstup z kanálu dalšího. Současně je výstup z prvního kanálu zkombinován hradlem XOR s výstupem Q z klopného obvodu D. Co to znamená v praxi? Každá hrana, která se objeví v kanálu 1 invertuje výstup z tohoto zapojení, zatímco hrana, která se objeví v kanálu 2 výstup vynuluje (na vstupu XOR se v daném okamžiku nachází dvě shodné hodnoty).

Výsledkem je tedy signál, jehož průběh vzdáleně připomíná výsledek PWM (pulsně-šířkovou modulaci) ve chvíli, kdy jsou si frekvence obou kanálů blízké. A právě k tomuto účelu je možné high-pass filtr použít, kromě dalších triků.

V případě potřeby (a také dostatečného výkonu mikroprocesoru) je možné generování obdélníkového signálu zcela vypnout a řídit pouze amplitudu na výstupu každého zvukového kanálu. Tímto způsobem lze přehrávat i nasamplované zvuky, ovšem kvůli výše uvedeným vlastnostem čipu POKEY je možné použít pouze šestnáct úrovní hlasitosti, tj. jedná se o čtyřbitový sampling s dynamickým rozsahem pouze 24 dB (naproti tomu CD-Audio využívá šestnáctibitový sampling s dynamickým rozsahem 96 dB a SID používá osmibitový sampling s dynamickým rozsahem cca 48 dB, což zhruba odpovídá magnetofonovému záznamu).

Ve skutečnosti je možné v případě, že je to nutné, digitalizovaný zvuk přehrávat současně na všech čtyřech zvukových kanálech, čímž se počet úrovní – a tím i dynamický rozsah – nepatrně zvyšuje (součet intenzit není lineární ale logaritmický). Nasamplovaná řeč byla na osmibitových počítačích Atari použita například ve hrách Ghostbusters či Berzerk, běžněji se setkáme s nasamplovanými bicími nástroji.

Kromě zvukové syntézy se integrovaný obvod POKEY používal i pro dat čtení klávesnice (přímá podpora pro maximálně 64 kláves + 3 speciálně zpracovávané klávesy Control, Shift a Break), komunikaci se zařízeními připojenými přes sériový port (jedná se o známé rozhraní SIO – Serial Input/Output), jako generátor pseudonáhodných čísel i ve funkci časovače (tři zvukové kanály bylo možné přepnout do funkce časovače, čehož se využívalo při práci s kazetovým magnetofonem).

Právě sloučení mnoha různých funkcí do jediného čtyřicetipinového integrovaného obvodu umožnilo snížit celkový počet obvodů ve všech osmibitových počítačích Atari, což samozřejmě – v mnohem větší míře než dnes – souvisí i s celkovou relativně nízkou výrobní cenou počítače či konzole, jeho nižší poruchovostí apod. Jen pro upřesnění: v klasických osmibitových Atari se nacházely čtyři "velké" obvody se čtyřiceti piny – mikroprocesor MOS 6502, grafický koprocesor ANTIC, grafický čip CTIA, později GTIA a taktéž v tomto článku popsaný multifunkční obvod POKEY.



# Zvukový čip Texas Instruments SN76489 (DCSG)

Třetím PSG, s nímž se v tomto článku seznámíme, je zvukový čip Texas Instruments SN76489, který je spíše známý pod zkratkou DCSG. Tento čip byl původně navržen pro osmibitový domácí mikropočítač TI-99/A, ovšem nakonec byl použit v mnohem známějších mikropočítačích počítačích BBC Micro či Sharp MZ-800, ale i v herních konzolích společnosti Sega, konkrétně v modelech SG-1000, Sega Master System, Sega Game Gear i v Sega Genesis (aka Sega Mega Drive).

I přesto, že zkratka DCSG znamená "Digital Complex Sound Generator", je čip SN76489 poměrně jednoduchý a v porovnání s POKEY nabízel hudebníkům menší možnosti konfigurace. Ostatně si sami můžete porovnat možnosti obou čipů porovnat po přečtení následujících odstavců.

Zvukový čip SN76489 byl dodávaný v pouzdru DIL o šestnácti vývodech a umožňuje generování (obdélníkových) zvukových signálů s volitelnou frekvencí a amplitudou. SN76489 obsahuje tři tónové generátory vytvářející periodický obdélníkový signál a jeden generátor šumu s pevně danou periodou 32767 (existuje ovšem i dále zmíněná varianta SN76489A, u níž je perioda zvětšena na 65535, takže šum na tomto čipu zní odlišně od originálu).

Frekvence každého tónového generátoru je určena desetibitovou konstantou uloženou do řídicího registru čipu SN76489. Tato konstanta je použita ve frekvenční děličce (běžném čítači), přičemž reálná frekvence vytvářeného obdélníkového signálu se vypočítá z frekvence hodinového signálu poděleného konstantou 32. Typická frekvence hodinového signálu přitom u herní konzole SG-100 byla nastavena na hodnotu 3,579545 MHz pro konzole určené pro normu NTSC a 3,546893 MHz pro konzole pro normu PAL. U dalších počítačů a konzolí může být frekvence odlišná, takže se hudba a zvuky musely při přenosu na jinou platformu přeprogramovat.

U každého tónového generátoru je taktéž možné určit amplitudu pomocí čtyřbitové hodnoty. Na výstupu se všechny zvukové signály sčítají, takže se rychlou změnou amplitudy a vhodným nastavením frekvencí jednotlivých zvukových kanálů dají generovat i poměrně složité melodie nebo zvuky ve hrách (v tom se od sebe TIA, POKEY ani DSCG příliš neodlišují).

Jak jsme se již řekli v předchozích odstavci, obsahuje tento čip navíc jeden generátor šumu, který je implementován pomocí posuvného registru o šířce patnácti bitů se zpětnou vazbou (bit, který se vrací na vstup posuvného registru, je získán logickou operací nonekvivalence (XOR) vybraných bitů posuvného registru). Pro generátor šumu je možné zvolit pouze tři frekvence: Fosc/64, Fosc/128 a Fosc/256. Poněkud nešikovné je to, že obsah generátoru šumu není možné přečíst mikroprocesorem, protože by se tato funkce mohla hodit ve hrách, které mnohdy vyžadují generátor (pseudo)náhodných čísel.

Generátor šumu zvukového čipu SN76489 může pracovat ve dvou režimech. V obou případech se používá již zmíněný posuvný registr o délce 15 či 16 bitů (podle verze čipu), jehož obsah je s každým taktem posunut doprava o jeden bit. Poslední bit posuvného registru představuje výstup z generátoru šumu. V prvním režimu je poslední bit posuvného registru spojen s bitem prvním, tj. sekvence bitů se neustále cyklicky opakuje. Původní sekvence obsahuje pouze jeden jedničkový bit, tj. výstupem je pravidelný obdélníkový signál se střídou 1:15 resp. 1:14.

V režimu druhém je zpětná vazba poněkud složitější – přes logické hradlo XOR jsou na vstup prvního bitu přiváděny výstupy z bitu posledního a třináctého (popř. dvanáctého), takže výsledkem je sekvence pseudonáhodných hodnot, jejichž opakování nastane až po proběhnutí 32767 resp. 65535 stavů (poslední stav je představován samými nulami a nepoužívá se). Jedná se o totožné chování, jakého je možné docílit s využitím již popsaného zvukového čipu POKEY či TIA (i když délka periody se liší).

Čip SN76489 obsahuje celkem osm interních řídicích registrů. Tři registry, každý o šířce deseti bitů, slouží pro uložení konstanty pro děličky frekvence tónových generátorů (určují tedy výšky tónů odvozených od vstupního hodinového signálu). Další tři registry, tentokrát o šířce čtyři bity, jsou určeny pro zápis amplitudy tónových generátorů. Sedmý registr má taktéž šířku čtyři bity a určuje amplitudu generátoru šumu. A konečně poslední registr je pouze tříbitový a je určen pro řízení generátoru šumu (volba ze tří frekvencí odvozených od Fosc + režim generátoru).

Vzhledem k tomu, že se do čipu SN76489 data přenáší po jednotlivých bajtech a není možné adresovat jednotlivé registry, neboť čip neobsahuje žádné piny pro zápis adresy!, je formát jednotlivých bajtů (zpráv) zvolen tak, aby bylo zcela přesně určeno, kterou hodnotu (či) hodnoty daný bajt představuje. Existují čtyři typy přenášených zpráv: nastavení spodních čtyř bitů děliče frekvence, nastavení vyšších šesti bitů děliče frekvence (dohromady tedy deset bitů), nastavení generátoru šumu a změna hlasitosti jednotlivých kanálů.

Jak je z tohoto popisu patrné, byly možnosti zvukového čipu SN76489 skutečně poněkud menší než možnosti konkurenčních čipů AY-3–8910 či POKEY, na druhou stranu ovšem lepší, než tomu bylo u čipu TIA použitého v námi oblíbené herní konzoli Atari 2600.



# Zvukový čip Texas Instruments SN76496

Výše popsaný čip SN76489 byl vyráběn v několika různých verzích. Původní verze byla označována pouze SN76489, popř. SN76489N v případě úzkého pouzdra DIP. Pozdější varianty, které byly označovány SN76489A a SN76489AN, se od původních verzí lišily především inverzními výstupními signály, což se projevilo na odlišném zapojení zesilovače (ale na výslednou podobu zvuku prakticky neměly žádný vliv). Maximální hodinová frekvence všech těchto čtyř čipů byla stanovena na 4 MHz, takže tyto čipy byly dobře využitelné ve všech mikropočítačích a konzolích, v nichž byly frekvence hodinového signálu odvozeny od televizních norem NTSC a PAL.

Kromě toho se ještě setkáme s variantami označovanými SN76494 popř. TMS9919, u nichž byla maximální hodinová frekvence snížena na 500 kHz (z označení TMS navíc můžeme vidět, že tyto čipy byly vyráběny i dalšími výrobci). Ve skutečnosti se jedná o prakticky shodné čipy s původním SN764789, ovšem chybí u nich vstupní dělička frekvence 1/8. Tyto varianty se používaly například i v herních automatech.

Mnohem zajímavější je čip nesoucí označení SN76496, který je sice postaven na původní variantě SN76489, ovšem navíc využívá pin číslo 9, který nebyl u původní řady SN76489 zapojen. U SN76496 slouží pro vstup audio signálu (AUDIO IN), což umožňovalo kombinaci většího množství zdrojů zvuků (připomeňme si, že na výstup těchto čipů byl vyveden analogový signál vzniklý součtem všech zvukových kanálů, na rozdíl od některých pozdějších čipů s FM syntézou, které vetšinou vyžadovaly speciální D/A převodník).



# Do třetice zvukový čip Texas Instruments, tentokrát SN76477

Čip pojmenovaný SN76477, který taktéž vyráběla společnost Texas Instruments, se hned v několika ohledech odlišuje od všech ostatních PSG, s nimiž jsme se v tomto článku prozatím setkali. Ostatní PSG jsou totiž skutečně programovatelné resp. přesněji řečeno konfigurovatelné mikroprocesorem, který může v reálném čase modifikovat obsah řídicích registrů popř. nastavovat parametry DMA. Z pohledu mikroprocesoru (a vlastně i programátora) je tedy PSG jedním z mnoha dalších čipů, které lze relativně snadno ovládat (v BASICu pomocí POKE, v assembleru zápisem do řídicích registrů nebo portů).

Čip TI SN76477 je při použití tohoto pohledu zcela odlišný, protože se generovaný zvuk řídí pomocí tlačítek, kondenzátorů, rezistorů (potenciometrů) a popř. vhodně zvoleného napětí přiloženého na zvolené piny tohoto integrovaného obvodu. Interně totiž SN76477 obsahuje klasický oscilátor, generátor šumu, generátor trojúhelníkového signálu, generátor obálky (envelope) a SLF (oscilátor s velmi nízkou frekvencí), jejichž parametry jsou řízeny zmíněnými elektronickými součástkami. Jedná se tedy spíše o čip vhodný pro bastlení popř. pro stavbu "alternativních" syntetizátorů, v nichž se kromě SN76477 použijí i další obvody (pro vytvoření smyčky atd. atd.).

Klasický oscilátor může být řízen již zmíněným SLF, takže výsledek je do značné míry podobný signálu získaného FM syntézou. Generátor obálky je poněkud omezen, protože namísto běžné ADSR obálky (attack, decay, sustain, release) má obálka jen tři fáze ASR (attack, sustain, release). Rychlost fází attack a decay se, stejně jako úroveň sustain, nastavují externími součástkami (zde konkrétně děličem napětí).

Důvodem, proč se o tomto poněkud neobvyklém čipu zmiňuji, je fakt, že byl použit v herních automatech, například ve slavných Space Invaders, Vanguard či Stratovox (zde společně s "ayčkem"). Mezi novější projekty založené na tomto čipu patří AxeSynth pocházející z roku 2004.



# Generování zvuků a hudby na osmibitové herní konzoli NES s čipem 2A03 nebo 2A07

Ústředním čipem, na němž je postavena slavná osmibitová herní konzole NES, je mikroprocesor Ricoh 2A03, popř. Ricoh 2A07 (tyto čipy se od sebe liší především odlišným časováním a jsou určeny pro různé televizní normy). Konstruktéři v případě mikroprocesoru 2A03/2A07 vsadili na osvědčenou jistotu, protože tento čip je založen na jádru oblíbeného osmibitového mikroprocesoru MOS 6502, který pravděpodobně není zapotřebí čtenářům FLOPu podrobněji představovat.

V případě čipů 2A03/2A07 však došlo k určitému zjednodušení jádra původního MOS 6502. Například byl odstraněn nepříliš často používaný režim pro práci s BCD čísly, kdy se do jednoho bajtu ukládají dvě dekadické číslice 0-9 (každá do čtyř bitů - nibblu), což znamená, že rozsah ukládaných hodnot byl 00 až 99 a nikoli 0 a 255. Původní mikroprocesor MOS 6502 a jeho varianty může být do tohoto režimu přepnut pomocí instrukce SED (set decimal), přepnutí zpět zajišťuje instrukce CLD (clear decimal).

Zatímco jádro mikroprocesoru bylo nepatrně zjednodušeno, byly na čip Ricoh 2A03/2A07 přidány další podpůrné moduly, díky jejichž existenci mohlo být redukováno celkové množství integrovaných obvodů, z nichž se herní konzole NES skládala. Jednalo se v první řadě o programovatelný "pomalý" časovač se základní frekvencí 240 Hz, z níž mohly být odvozeny další frekvence (48, 60, 96, 120 a 192 Hz). Dále byl na čip přidán modul pro přímý přístup do paměti a přenosy dat (DMA).

V kontextu tohoto článku je pro nás však mnohem zajímavější další část určená pro práci se zvukem: šlo o programovatelné generátory obdélníkového signálu, generátor trojúhelníkového signálu a taktéž o konfigurovatelný generátor šumu tvořený posuvným registrem se zpětnou vazbou. Zapomenout nesmíme ani na modul určený pro přehrávání samplů (napojený na D/A převodník). Celý zvukový subsystém se řídil pomocí devatenácti osmibitových registrů.

Zvuk či melodie mohly být tvořeny v pěti na sobě nezávislých kanálech. Jedná se o dva již zmíněné generátory obdélníkového signálu s volitelnou amplitudou, frekvencí a střídou, dále o (taktéž zmíněný) generátor trojúhelníkového signálu s volitelnou frekvencí a automaticky měněnou amplitudou, generátor šumu, u nějž bylo možné zvolit režim činnosti, amplitudu a frekvenci posunu a konečně o D/A převodník, který mohl být buď ovládán přímo programově, nebo bylo umožněno načítat zvukové vzorky (samply) uložené v paměti ROM či RAM. Zajímavé je, že zvukový subsystém neobsahoval žádné filtry, na rozdíl od (jednoduchých) filtrů nabízených čipem POKEY (Atari) či komplexnějších filtrů použitých v čipu SID (Commodore C64).

Taktéž podpora pro tvarování obálky generovaných signálů byla pouze dosti jednoduchá (tuto funkcionalitu však neměl ani POKEY, kde se musela řešit programovými cestami či trikem s high-pass filtry). Čip 2A03/2A07 obsahoval dva piny, na které byl přiváděn výstup ze všech pěti zvukových kanálů. Na pin číslo 1 (ROUT) byl přiváděn výstup z obou generátorů obdélníkových signálů, zatímco výstup z ostatních třech kanálů byl přiváděn na pin číslo 2 (COUT). V herní konzoli NES byl výstup z obou kanálů sloučen a analogově sečten s mikrofonním vstupem (ten se příliš často nepoužíval) a výsledný analogový signál byl zesílen a dále zpracován.

Z hlediska programátora-hudebníka se nejjednodušeji ovládaly oba generátory obdélníkových signálů, u nichž bylo možné měnit zejména tři základní parametry: amplitudu (4 bity = 16 nastavitelných úrovní), frekvenci (přibližně 54,6 Hz až 12,4 kHz podle použité televizní normy, frekvenci bylo možné měnit plynule díky použití šestnáctibitových čítačů) a střídu (1:8, 1:4, 1:2, 3:4). Každý z této dvojice kanálů se ovládal čtyřmi řídicími registry: SQx_VOL (hlasitost), SQx_SWEEP (střída), SQx_LO a SQx_HI (počáteční hodnota čítače, ze které se odvozuje frekvence zvuku). Poznámka: za "x" si doplňte číslo kanálu, tedy 1 nebo 2.

U generátoru trojúhelníkového signálu se měnila jeho úroveň (4 bity = 16 úrovní) automaticky, ale programově bylo možné nastavit frekvenci změn signálu v rozsahu 27,3 Hz až 55,9 kHz (opět v závislosti na použité televizní normě). Vše se ovládalo třemi registry nazvanými TRI_LINEAR (aktuální hodnota čítače pro generování "schodů" tvořících vzestupnou i sestupnou hranu trojúhelníkového signálu, zvyšuje se automaticky), TRI_LO a TRI_HI (počáteční hodnota čítače, z něhož se odvozuje frekvence trojúhelníkového signálu).

Podobně jako další popsané zvukové čipy POKEY či AY-3-8910, obsahoval i zvukový subsystém herní konzole NES generátor šumu. Ten byl vytvořen pomocí patnáctibitového posuvného registru se zpětnou vazbou: vybrané dva bity posuvného registru byly přes hradlo XOR přesunuty na jeho začátek, přičemž se obsah registru mezitím posunul o jeden bit doleva. Zvukový výstup byl generován na základě aktuálního obsahu bitu s indexem 14.

Posuvný registr mohl pracovat ve dvou režimech činnosti: "krátkém" a "dlouhém". Ve "dlouhém režimu" se generovala sekvence pseudonáhodných bitů s periodou 32767 vzorků (zbývající 32768 stav nemohl být použit, protože se jednalo o nulovou hodnotu spadající mimo generovanou sekvenci; to již ostatně známe). V "krátkém režimu" byla perioda pseudonáhodného signálu kratší: 93 bitů/vzorků. Samozřejmě bylo taktéž možné měnit frekvenci posunu, a to přibližně v rozsahu 29,3 Hz až 447 kHz (opět v závislosti na tom, jaká televizní norma byla použita). Pro řízení generátoru šumu byly použity tři registry: NOISE_VOL (hlasitost, 4 bity), NOISE_LO a NOISE_HI (frekvence + výběr krátkého nebo dlouhého režimu).

Zbývá nám si popsat už jen pátý kanál, jímž je D/A převodník. Ten bylo možné ovládat programově změnou jednoho řídicího registru (sedmibitová hodnota), popř. byla podporována funkce automatického přehrávání vzorků (samplů) z paměti ROM, přičemž při načítání samplu došlo k pozastavení mikroprocesoru. Při přehrávání vzorků byla frekvence nastavitelná v rozsahu 4,2 kHz až 33,5 kHz (ovšem zvolit bylo možné jen šestnáct přednastavených frekvencí). D/A převodník se ovládal čtyřmi registry nazvanými DMC_FREQ (frekvence přehrávání samplů), DMC_RAW (přímý sedmibitový výstup, pokud se nepoužije automatické přehrávání), DMC_START (adresa se vzorky, resp. konstanta, z níž se adresa vypočte) a DMC_LEN (počet vzorků).

Devatenáctý a současně i poslední řídicí registr se jmenuje SND_CHN. Slouží pro povolení zvukových kanálů a pro přečtení stavu zvukového subsystému.

Tento čip již nabízí v porovnání s POKEY zajímavé možnosti. Týká se to zejména 16bitových čítačů použitých při generování obdélníkových signálů (v POKEY naproti tomu bylo nutné spojit dva kanály) a generátoru trojúhelníkového signálu, který mohl být použitý pro basové linky popř. pro perkusní nástroje. Naproti tomu jsou možnosti konfigurace poly čítače mnohem omezenější.



# Integrovaný obvod AY-3-8910 neboli podomácku "áýčko" a jeho varianty (YM2149 atd.)

Předposledním zvukovým čipem z éry osmibitových počítačů, který si v tomto článku popíšeme, je čip AY-3-8910 firmy General Instrument (GI), později vyráběný i firmou Yamaha pod označením YM2149. Tento čip byl součástí osmibitového domácího mikropočítače ZX Spectrum 128K, herních konzolí Vectrex a Intellivision či 16/32bitového počítače Atari ST (YM2149) či CP1610. Samotné jádro čipu, které se stará o generování zvuku, firma Yamaha používala prakticky dodnes i v současných integrovaných obvodech určených pro video hry či mobilní telefony. Jedná se především o čip YM-2203 (označovaný též zkratkou OPN), který původní AY-3–8910 rozšiřuje o frekvenční modulaci (FM).

Samotný zvukový čip AY-3–8910 byl vyráběn ve třech variantách označovaných AY-3–8910, AY-3–8912 a AY-3–8913. Jednotlivé varianty čipu se však nelišily způsobem generování zvuků (funkční bloky pro práci se zvukem totiž zůstávaly nezměněné), ale především počtem osmibitových vstupně/výstupních portů ovládaných přes řídicí registry (viz navazující odstavce).

AY-3–8910 se totiž, podobně jako již popsaný čip POKEY, používal kromě práce se zvuky a hudbou také pro ovládání dalších zařízení; mohl například pracovat jako jednoduchý programově řízený paralelní port, rozhraní pro připojení digitálních joysticků, přepínač mezi bankami operační paměti atd. Počítače či herní konzole, které pro ovládání dalších zařízení využívaly jiný obvod (například Intel 8255), tak obsahovaly buď nejmenší a samozřejmě i nejlevnější čtyřiadvacetipinovou variantu AY-3–8913, popř. osmadvacetipinovou variantu AY-3–8912.

Základní vlastnosti všech tří variant čipu AY jsou vypsány v následující tabulce:

Označení čipu Počet I/O Pinů
AY-3–8910     2         40
AY-3–8912     1         28
AY-3–8913     žádný     24

Poslední zmíněný čip měl jeden pin nezapojený, další přidaný pin byl určen pro výběr obvodu (chip select) a navíc obsahoval testovací piny TEST IN a TEST OUT.

Osmibitový domácí počítač ZX Spectrum pravděpodobně není zapotřebí čtenářům blíže představovat. V Evropě se jednalo o nejrozšířenější domácí osmibitový počítač se silnou programátorskou i uživatelskou podporou. Tento počítač, který byl po hardwarové stránce velmi jednoduchý (v porovnání s Atari až primitivní :-), bylo také velmi snadné "klonovat". Z tohoto důvodu existuje několik desítek typů klonů vyráběných v různých zemích (u nás, resp. dnes spíše v SR, se jednalo například o typovou řadu Didaktik Gama a Didaktik M).

Původní ZX Spectrum sice bylo vybaveno pouze interním reproduktorem připojeným na jeden z pinů čipu ULA (bylo tedy možné vytvářet zvuk jen s využitím dvoustavového obdélníkového signálu, podobně jako později na PC-Speakeru), ale modernější verze ZX Spectra nazvaná ZX Spectrum 128K již obsahovala - kromě mnoha dalších vylepšení - i zvukový čip AY, což oproti původnímu řešení představovalo značný pokrok.

Zvukový čip AY-3–8912 byl použit i v herní konzoli Vectrex, která je zajímavá především tím, že pro zobrazování používá zabudovaný vektorový displej. Aby se alespoň z malé části nahradily některé nedostatky vektorové grafiky (například praktická nemožnost vyplňování ploch a také viditelné poblikávání zobrazovaných vektorů ve složitějších obrazech), byla ke každé hře dodávána poloprůhledná fólie, která se umístila před monitor. Na fólii byl většinou nakreslen okolní herní svět.

Přímo v herní konzoli byla zabudována i obrazovka Samsung 240RB40, která měla velikost cca 8×11 palců a byla postavena poněkud netradičně "nastojato". Za účelem dosažení co nejnižší ceny celé konzole byly použity černobílé výprodejové obrazovky. Ve druhé generaci se tvůrci pokoušeli použít i barevnou obrazovku, to však značným způsobem navyšovalo cenu celého systému, proto bylo od tohoto nápadu upuštěno.

Kromě mikroprocesoru, pamětí a D/A převodníku s multiplexerem byla konzole osazena i v článku popisovaným zvukovým čipem AY-3–8912 (tj. "prostřední" variantou s jedním osmibitovým portem), který sloužil pro generování zvukového doprovodu, dále obvod PIA pro řízení vstupů i výstupů a nakonec digitálně-analogový převodník MC1408 (ten byl v zařízení přítomen pouze jeden, i když ve skutečnosti přes multiplexer ovládal celkem tři analogové výstupy).

Další počítač, který obsahoval zvukový čip AY-3–8910 (resp. jeho variantu YM2149 od firmy Yamaha), již byl představitelem nové generace 16/32bitových strojů. Jednalo se o počítače řady Atari ST. Řada ST začínala modelem Atari 260 ST (přesněji, existoval ještě model Atari 130 ST, ten se však prakticky neprodával), který však byl poměrně rychle nahrazen třemi typy počítačů, jež svými vlastnostmi pokrývaly značnou část tehdejšího trhu s osobními počítači: Atari 520 ST, Atari 1040 ST a Atari Mega ST.

Čip AY-3–8910 i všechny jeho varianty používá pro tvorbu zvuků a hudby tři samostatně nastavitelné tónové generátory, které produkují obdélníkové signály o zadané frekvenci (rozsah je 8 oktáv, každý kanál přitom obsahuje dvanáctibitový dělič), jenž jsou dále zpracovávány. Každý tónový generátor vytváří zdroj zvukového signálu pro jeden ze zvukových kanálů – celkem jsou tedy k dispozici tři zvukové kanály, přičemž výstup každého z kanálů je vyveden na samostatný pin (jedná se o analogový výstup, na který lze například přímo zapojit zesilovač).

To je pro PSG velmi netypické zapojení, protože u většiny ostatních zvukových čipů jsou zvuky z jednotlivých kanálů namixovány přímo na čipu do jednoho výstupu; na druhou stranu je však možné velmi jednoduše i s pomocí pouze jediného AY-3–8910 vytvářet stereo hudbu. Kromě tónových generátorů je možné použít i generátor šumu, jehož výstup lze přivést do zvoleného (či zvolených) zvukových kanálů. Generátor šumu se často používá například pro napodobení zvuku perkusních nástrojů, podobně jako tomu je u již popsaných zvukových čipů POKEY či u dále zmíněného SIDu.

Obdélníkový signál vytvářený v tónových generátorech lze upravit pomocí obálky, která je však generována poněkud netypickým způsobem (například u SIDu je použita klasická obálka typu ADSR – attack, decay, sustain, release). Obálka má u ayčka tvar digitalizovaného periodického nebo neperiodického pilového či trojúhelníkového signálu. Taktéž je možné obálku ovládat programově, což vlastně znamená, že se pomocí zápisu do jednoho z řídicích registrů mění amplituda generovaného obdélníkového signálu.

Na výstupu se nachází nelineární digitálně/analogový převodník, který slouží k převodu čtyřbitové hodnoty získané modifikací obdélníkového signálu obálkou na napěťovou úroveň v rozsahu do 1,35 Voltů (při zatížení analogového výstupu obvodem s odporem 1 k). Díky použití nelineárního D/A převodníku se signál s původně lichoběžníkovým průběhem (výsledek změny amplitudy obdélníkového signálu pomocí obálky) mění na signál se "špičkami", které dodávají hudbě vytvářené na čipu AY-3–8910 typické zabarvení.

Nelinearita D/A převodníku způsobuje problémy při přehrávání samplované hudby, neboť ta je většinou uložena ve formě osmibitových či šestnáctibitových vzorků s lineární závislostí mezi uloženou hodnotou a zaznamenanou úrovní. Z tohoto důvodu se při přehrávání samplované hudby na AY-3–8910 musejí používat převodní tabulky (existuje jich větší množství, liší se jak způsobem uložení, tak i konkrétními hodnotami pro převod; nesmíme také zapomínat na to, že zesilovače zapojené za AY-3–8910 nemusí mít lineární průběh a tudíž se převodní tabulky mohou mezi jednotlivými typy počítačů odlišovat).

Podívejme se nyní na tento PSG z pohledu programátora. Zvukový čip AY-3–8910 je ovládán pomocí šestnácti osmibitových řídicích registrů, které jsou pojmenovány R0 až RF, jejichž stručný popis je uveden v tabulce pod odstavcem:

Registr Význam
R0  dolních osm bitů děliče frekvence hudebního kanálu A
R1  horní čtyři bity děliče frekvence hudebního kanálu A
R2  dolních osm bitů děliče frekvence hudebního kanálu B
R3  horní čtyři bity děliče frekvence hudebního kanálu B
R4  dolních osm bitů děliče frekvence hudebního kanálu C
R5  horní čtyři bity děliče frekvence hudebního kanálu C
R6  pět bitů děliče frekvence generátoru šumu
R7  nastavení zvukového mixéru i směru obou I/O portů
R8  nastavení úrovně hlasitosti hudebního kanálu A
R9  nastavení úrovně hlasitosti hudebního kanálu B
RA  nastavení úrovně hlasitosti hudebního kanálu C
RB  dolních osm bitů děliče frekvence generátoru obálky
RC  horních osm bitů děliče frekvence generátoru obálky
RD  nastavení tvaru obálky
RE  data I/O portu A (vstup či výstup)
RF  data I/O portu B (vstup či výstup)

Povšimněte si, že zatímco AY-3–8910 je řízen šestnácti registry, u čipu POKEY se vytvářený zvuk ovlivňoval registry devíti a čip SID měl pro stejný účel vyhrazeno dokonce 29 registrů. Řídicí registry je možné podle jejich funkce rozdělit do několika skupin. Prvních šest registrů R0 až R5 slouží pro nastavení frekvence obdélníkového signálu generovaného v každém hudebním kanálu (pro jeden hudební kanál jsou použity vždy dva sousední registry, do nichž se ukládá hodnota pro frekvenční dělič).

Následuje registr R6, kterým se nastavuje frekvence šumu, registr R7 pro řízení mixéru a vstupně-výstupních portů, trojice registrů R8, R9, RA pro nastavení hlasitosti jednotlivých hudebních kanálů, dvojice registrů RB a RC pro nastavení frekvence obálky, registr RD určující tvar obálky a konečně dvojice registrů RE a RF, které jsou použity při práci se vstupně-výstupními porty. Těmito dvěma registry se nebudeme dále zabývat, neboť nemají vliv na vytvářený zvuk, ostatní registry budou naopak popsány podrobněji.

Základ tónu je pro každý hudební kanál tvořen v generátoru obdélníkového signálu (square wave generator). Princip práce tohoto generátoru je velmi jednoduchý (ostatně právě proto ho můžeme nalézt jak v AY-3–8910, tak i v čipu POKEY). Frekvence pravidelného hodinového signálu přiváděného na vstup CLOCK, jenž se nachází na pinu číslo 22, je u YM2149 nejprve pomocí klopného obvodu typu T vydělena na polovinu. To, zda k vydělení skutečně dojde, závisí na stavu pinu SEL; naproti tomu u původního AY-3–8910 se toto vydělení frekvence na polovinu neprovádí nikdy. Výsledkem je signál nazvaný master clock.

Poté je hodinový signál přiveden do binárních čítačů, které pracují jako frekvenční děliče (pravděpodobně jsou v AY-3–8910 skutečně použity děliče založené na binárních čítačích, které s každým hodinovým taktem sníží svoji hodnotu o jedničku, přičemž po dosažení nuly je jejich výstup invertován a do čítače se dosadí původní hodnota). Frekvence obdélníkového signálu je pro každý hudební kanál ovládána zvlášť pomocí dvojice osmibitových řídicích registrů (R0+R1 pro kanál A, R2+R3 pro kanál B a R4+R5 pro kanál C), v nichž je uloženo dvanáctibitové číslo představující hodnotu, kterou se dělí hodinový signál.

Z celkem šestnácti bitů je možné nastavit pouze bitů dvanáct, což je však pro požadovaný frekvenční rozsah osmi oktáv dostatečné. Frekvence každé obdélníkové vlny se vypočte pomocí vztahu: f_square=f_master/16TP, kde TP je hodnota uložená ve dvojici řídicích registrů a f_master je frekvence hodinového signálu.

Dalším primárním zdrojem signálu pro tvorbu zvuku je generátor šumu (noise generator). Výstup z tohoto generátoru (opět se jedná o binární signál, v tomto případě o náhodné pulsy) může být přiveden do libovolného hudebního kanálu, v případě potřeby i do všech kanálů, ovšem šumový generátor je pouze jeden a i jeho frekvence je pro všechny tři hudební kanály vždy stejná. Pro nastavení frekvence šumového generátoru je určeno pět bitů řídicího registru R6.

Frekvence je vypočtena podle vztahu prakticky totožného se vztahem uvedeným v předchozím odstavci: f_noise=f_master/16NP, kde NP je hodnota uložená v řídicím registru R6. Vzhledem k menší maximální hodnotě, kterou lze uložit do pěti bitů (2^5-1=31 vs. 2^12-1=4095) je i frekvence vytvářeného šumu většinou mnohem vyšší než frekvence obdélníkového signálu (v případě šumu není zcela přesné hovořit o frekvenci, spíše se jedná o maximální mez frekvence).

Důležitou součástí zvukového čipu AY-3–8910 je takzvaný mixér. V něm se pro každý hudební kanál zvlášť nastavuje zdroj signálu, který má být dále zpracováván. Pro každý hudební kanál lze povolit vstup obdélníkového signálu o zvolené frekvenci a vstup z generátoru šumu. V případě, že jsou pro jeden hudební kanál povoleny oba zdroje zvuku, jsou korektně smíchány (tato operace je implementačně velmi jednoduchá, neboť obdélníkový i šumový signál je binární, tudíž lze mixér realizovat pomocí logických hradel). Nastavení mixéru se provádí pomocí řídicího registru R7. Pro každý kanál jsou v tomto registru vyhrazeny dva bity – zápis nuly do příslušného bitu povoluje vstup obdélníkového signálu či šumu. Pokud jsou oba bity nastaveny na logickou jedničku, je výstup pro zvolený zvukový kanál zakázán.

Nejvyšší dva bity řídicího registru R7 slouží k určení směru vstupně-výstupních portů – každý port může být nastaven buď do výstupního režimu (zápis dat) nebo do režimu vstupního (čtení dat).

Hlasitost hudebních kanálů lze nastavit buď programově na jednu ze šestnácti úrovní, nebo je možné hlasitost měnit pomocí generátoru obálky popsaného v následujících odstavcích. Pro řízení hlasitosti každého hudebního kanálu je určený jeden řídicí registr – R8 až RA. Amplituda je nastavena čtyřmi bity (rychlou programovou změnou amplitudy je možné přehrávat samplované zvuky), pátým bitem řídicího registru je určeno, zda má být amplituda skutečně řízena programově nebo zda se má použít generátor obálky. Nejvyšší tři bity tohoto řídicího registru zůstávají nevyužity.

Dalším funkčním blokem, který se podílí na tvarování výsledného zvuku, je takzvaný generátor obálky (envelope generator). Obálkou je možné (s využitím amplitudové modulace) ovlivnit maximální hodnoty původního obdélníkového a/nebo šumového signálu. Zatímco u dále popsaného čipu SID byly použity obálky typu ADSR (attack, decay, sustain, release), má u AY-3–8910 obálka tvar periodického či neperiodického trojúhelníkového nebo pilového signálu. Ve skutečnosti se však nejedná o analogový signál, ale o signál digitální se šestnácti úrovněmi, tj. na osciloskopu by místo čistých průběhů bylo na každé náběžné nebo sestupné patrných šestnáct "schodů".

Pro nastavení frekvence změny obálky (přesněji doby čítání stavů 0–15) slouží dvojice řídicích registrů RB a RC, do nichž lze zadat šestnáctibitovou konstantu, která je použita v následujícím vztahu: f_EP=f_master/256EP, kde EP je šestnáctibitová hodnota uložená do výše zmíněné dvojice řídicích registrů RB a RC. Vzhledem ke konstantě, která se v tomto vztahu vyskytuje, má signál představovaný obálkou výrazně delší periodu, než signál obdélníkový. To odpovídá významu obálky, protože v každém cyklu obálky (t_EP=1/f_EP) se vygeneruje trojúhelníková část vlny mající šestnáct kroků – vždy se projde všemi šestnácti úrovněmi.

Tvar obálky je určen nejnižšími čtyřmi bity řídicího registru RD, pomocí nichž je možné vybrat jeden z osmi tvarů obálky (ze šestnácti možných kombinací je tedy pouze osm kombinací unikátních). Tyto čtyři bity jsou pojmenovány CONT, ATT, ALT a HOLD. Bitem CONT (continue) se určuje, zda se bude obálka periodicky opakovat, bit ATT (attenuation) vybírá tvar náběžné části vlny (vzestupná či sestupná), nastavením bitu ALT (alternation) lze vynutit zrcadlové či naopak periodické opakování náběžné části vlny (tj. buď se vytváří pilový nebo trojúhelníkový signál) a konečně bitem HOLD lze zajistit "podržení" výstupu po první periodě na konstantní hodnotě.

Generátor obálky se používá mnoha způsoby, například při samplingu (zde lze využít automatické vytváření vzestupných a sestupných hran), syntéze řeči atd. Je také možné vytvářet tón pouze pomocí periodicky se opakující obálky a napodobovat tak generátor pilového nebo trojúhelníkového signálu.

Čip AY se samozřejmě musel nějakým způsobem připojit k adresové a datové sběrnici počítače. Předpokládalo se, že se použije osmibitová datová sběrnice multiplexovaná s dolními osmi bity sběrnice adresové. Na vstupy BDIR, BC1 a BC2 mohou být připojeny řídicí signály, na piny DA0 až DA7 se připojují multiplexované adresové a datové vodiče a vstupy A8 a !A9 slouží pro výběr čipu (to, zda jsou přímo zapojeny na adresovou sběrnici, či zda je před nimi předřazen dekodér, je již závislé na architektuře počítače).

Vstupně/výstupní osmibitové porty jsou vyvedeny na piny IOA0 až IOA7 (první port) a IOB0 až IOB7 (druhý port). Posledními digitálními vstupy jsou CLOCK (hodiny, od nichž jsou odvozeny frekvence generovaných tónů) a !SEL (zamknutí hodin). Na poslední tři piny označené ANALOG A, ANALOG B a ANALOG C jsou vyvedeny výstupy ze všech tří zvukových kanálů. Tyto výstupy buď mohou být přivedeny do jednoho zesilovače (mono zvuk) nebo do více zesilovačů (stereo zvuk, tři hlasy).

Již v úvodních odstavcích jsme si řekli, že pro AY-3–8910 jsou k dispozici dva osmibitové obousměrné porty a ve variantě AY-3–8912 jeden osmibitový obousměrný port (přesněji řečeno všechny tři varianty čipu AY-3–8910 oba paralelní porty interně obsahovaly, ale u variant s menším počtem kontaktů nebyl buď jeden nebo ani jeden port vyvedený na piny čipu, takže se celkový počet pinů mohl snížit z původních 40 na 28 popř. pouze 24 kontaktů).

Tyto osmibitové porty, které lze přepnout do vstupního či výstupního režimu, je možné využít například po připojení digitálních joysticků, tiskárny vybavené rozhraním Centronics atd. V některých osmibitových počítačích, jejichž mikroprocesory dokázaly adresovat většinou pouze 64 kB operační paměti (MOS 6502, Motorola M6809, Intel 8080, Z80), býval jeden z portů využíván pro přepínání aktivní paměťové banky – v portu byl uložen index zvolené paměťové banky, čímž bylo možné zvýšit celkovou kapacitu paměti z původních maximálně 64 kB až na několikanásobek této hodnoty, podle toho, kolik bank bylo skutečně obsazených paměťovými čipy.

Výstup z portu byl připojen na vstup CS – Chip Select paralelně zapojených paměťových pouzder – předpokladem správné funkce je, že se datové výstupy paměťových čipů přepnou do režimu vysoké impedance v případě, že čip není vybraný signálem CS.



# Slavný SID firmy MOS

