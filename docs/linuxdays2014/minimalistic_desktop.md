# Minimalistický desktop

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz`
* Datum: 2014-10-06
* Prezentace:
    - [https://tisnik.github.io/presentations/linuxdays2014/minimalistic_desktop.html](https://tisnik.github.io/presentations/linuxdays2014/minimalistic_desktop.html)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/linuxdays2014/minimalistic_desktop/desktop.txt](https://github.com/tisnik/presentations/blob/master/linuxdays2014/minimalistic_desktop/desktop.txt)

Konfigurace desktopu pro méně výkonné počítače
----------------------------------------------
* Starší PC
    - Školy, neziskové organizace...
* Notebooky/netbooky na bázi Intel Atomu
* Počítače osazené SoC (Koomey's law)
    - Raspberry Pi
    - BeagleBoard
    - PandaBoard

Raspberry Pi ve funkci desktopu
-------------------------------
* Model B+
    - SoC BCM2835
        • CPU + GPU
    - 512 MB RAM
        • "nasazena" na SoC
    - 4xUSB konektor
    - Ethernet
    - HDMI + TV výstup
    - Audio výstup
    - MicroSD + Externí HDD (over USB)

Raspberry Pi: SoC
-------------------------------
* CPU
    - Rodina ARM11
    - Instrukční sada ARMv6
    - 700 MHz
    - Lze snadno přetaktovat až na 1 GHz
    - Poměrně slabý výkon pro desktopové aplikace
* GPU
    - HVS - Hardware Video Scaler
    - 24 GFLOPS
    - silný zejména v GPU výpočtech (x desktop)

Raspberry Pi: konfigurace pro desktop
-------------------------------------
* MicroSD (8GB)
    - Raspbian
    - požadavek: minimum zápisů
* Externí HDD
    - připojený přes konvertor USB
    - ext3 + swap
    - automount přes fstab
    - linky na /tmp /var a /home

Obsazení MicroSD (a samozřejmě i disku)
---------------------------------------
~ $ df -H
Filesystem      Size  Used Avail Use% Mounted on
rootfs          6.1G  2.4G  3.5G  41% /
/dev/root       6.1G  2.4G  3.5G  41% /
devtmpfs        226M     0  226M   0% /dev
tmpfs            46M  287k   46M   1% /run
tmpfs           5.3M     0  5.3M   0% /run/lock
tmpfs           401M     0  401M   0% /run/shm
/dev/mmcblk0p5   62M   11M   52M  17% /boot
/dev/sda1        78G  5.5G   68G   8% /mnt

Linky na nejčastěji modifikované adresáře
-----------------------------------------
drwxr-xr-x   2 root root  4096 Sep 11 21:17 bin
drwxr-xr-x   2 root root  1536 Jan  1  1970 boot
drwxr-xr-x  14 root root  3360 Sep 18 19:27 dev
drwxr-xr-x 105 root root  4096 Sep 18 00:01 etc
lrwxrwxrwx   1 root root     9 Sep 11 20:13 home -> /mnt/home
drwxr-xr-x   3 root root  4096 Jan  1  1970 home_
drwxr-xr-x  12 root root  4096 Jan  1  1970 lib
drwx------   2 root root 16384 Jun 20 07:34 lost+found
drwxr-xr-x   3 root root  4096 Sep 12 20:49 media
drwxr-xr-x  22 root root  4096 Sep 12 19:46 mnt
drwxr-xr-x   5 root root  4096 Jan  1  1970 opt
dr-xr-xr-x 109 root root     0 Jan  1  1970 proc
drwx------   6 root root  4096 Sep 12 20:13 root
drwxr-xr-x   9 root root   440 Sep 18 00:01 run
drwxr-xr-x   2 root root  4096 Jan  1  1970 sbin
drwxr-xr-x   2 root root  4096 Jun 20  2012 selinux
drwxr-xr-x   2 root root  4096 Jun 20 07:36 srv
dr-xr-xr-x  12 root root     0 Jan  1  1970 sys
lrwxrwxrwx   1 root root     8 Sep 11 20:00 tmp -> /mnt/tmp
drwxr-xr-x  10 root root  4096 Jan  1  1970 usr
lrwxrwxrwx   1 root root    11 Sep 12 19:53 var -> /mnt/var
drwxr-xr-x  11 root root  4096 Sep 11 19:56 var_

Reálné "vytížení" paměťových médií
-----------------------------------------
* Tři hodiny reálné činnosti počítače: web+psaní těchto slajdů :-)
.
pi@raspberrypi ~ $ uptime
 22:23:09 up  3:00,  5 users,  load average: 0.63, 0.57, 0.64
.
pi@raspberrypi ~ $ cat /proc/fs/jbd2/mmcblk0p6-8/info 
6 transactions (2 requested), each up to 8192 blocks
.
pi@raspberrypi ~ $ cat /proc/fs/jbd2/sda1-8/info 
1063 transactions (704 requested), each up to 8192 blocks

Minimalistický desktop
----------------------
* Desktop
    - LXDE
    - XFCE
    - Fluxbox
    - Tile window manažery
        • wmii
        • awesome
        • atd. atd.

Programové vybavení [1]
-----------------------
    - Správce souborů
    - Webové prohlížeče
    - Textové editory
    - Textové procesory
    - Tabulkové procesory
    - Prohlížeče obrázků
    - Editory obrázků
    - Komunikace

Programové vybavení [2]
-----------------------
* Správce souborů
    - PCmanFM
    - Thunar
    - Midnight Commander

* Textové procesory
    (jsou skutečně zapotřebí? :-)
    - Abiword

Programové vybavení [3]
-----------------------
* Textové editory
    - Leafpad/Mousepad/NE
    - (G)Vim
    - Emacs
    - a asi 50 dalších možností
.        ________ ++     ________
.       /VVVVVVVV\++++  /VVVVVVVV\
.       \VVVVVVVV/++++++\VVVVVVVV/
.        |VVVVVV|++++++++/VVVVV/'
.        |VVVVVV|++++++/VVVVV/'
.       +|VVVVVV|++++/VVVVV/'+
.     +++|VVVVVV|++/VVVVV/'+++++
.   +++++|VVVVVV|/VVVVV/'+++++++++
.     +++|VVVVVVVVVVV/'+++++++++
.       +|VVVVVVVVV/'+++++++++
.        |VVVVVVV/'+++++++++
.        |VVVVV/'+++++++++
.        |VVV/'+++++++++
.        'V/'   ++++++
.                 ++

Programové vybavení [4]
-----------------------
* Tabulkové procesory
    - Gnumeric
    - (sc)
* Prohlížeče obrázků
    - fbi
    - feh
    - gpicview
    - (xsetroot pro hardcore uživatele)
* Editory obrázků
    - MTpaint

Programové vybavení [5]
-----------------------
* Komunikace
    - BitlBee+WeeChat
.
 ___       __         ______________        _____
 __ |     / /___________  ____/__  /_______ __  /_
 __ | /| / /_  _ \  _ \  /    __  __ \  __ `/  __/
 __ |/ |/ / /  __/  __/ /___  _  / / / /_/ // /_
 ____/|__/  \___/\___/\____/  /_/ /_/\__,_/ \__/

Programové vybavení [6]
-----------------------
* Webové prohlížeče
    (zde se nejvíce projeví slabý výkon CPU)
    - NetSurf (bez JS, dobrý layout engine)
    - Firefox (kupodivu v praxi rychlejší než Midori)
    - Midory (problém - načítání v jiném tabu zdržuje)
    - Links2
    - Textové prohlížeče: lynx, links, elinks, w3m

 _____________________
< Děkuji za pozornost >
 ---------------------
. \
.  \   \_\_    _/_/
.   \      \__/
.          (oo)\_______
.          (__)\       )\/\
.              ||----w |
.              ||     ||

 _________
< Otázky? >
 ---------
   \
.   \
.   ____
   /# /_\_
  |  |/o\o\
  |  \\_/_/
 / |_   |
|  ||\_ ~|
|  ||| \/
|  |||_
 \//  |
  ||  |
  ||_  \
  \_|  o|
  /\___/
 /  ||||__
.   (___)_)
..............................................
