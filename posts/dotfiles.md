Dotfiles
2-12-2015


**[TL;DR](http://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn't_read)** -- Dotfiler er (næsten) uundværlige i opsætningen af Mac - eller Linux - hvis man vil lidt ud over hvad der lige rummes i Systemindstillinger. Det her er mine dotfiler.

![MacBook Pro](https://log.logiskhave.dk/static/20151202_macbook-pro.jpg)

### Om dotfiler generelt

Hvis man en gang i mellem reinstallerer sin computer eller har flere maskiner, som man veksler i mellem og godt kan lide at den opfører sig på (nogenlunde) samme måde uanset hvilken man sidder ved eller om man lige har reinstalleret, så er dotfiles smarte.

Kort beskrevet, så er dotfiles en måde at beskrive hvordan en computer skal sættes op på i et meget robust format[^1].

Filerne bliver læst på forskellige tidspunkter alt efter hvilken fil der er tale om, og jeg har endnu ikke fundet en bedre beskrivelse af det end denne på "[The Lumber Room](https://shreevatsa.wordpress.com/2008/03/30/zshbash-startup-files-loading-order-bashrc-zshrc-etc/)"[^2].

Problemet med at beskrive hvornår hvad læses er, at Bash trækker på forskellige filer alt efter hvilken slags shell den mener den kører i. Eks.: for en "interaktiv ikke-login-shell", læses .bashrc, men for en "interaktiv login-shell" læser den udelukkende fra den første af .bash_profile, .bash_login og .profile. Der er ingen fornuftig grund til, at det er sådan, sådan er det bare...

Bash læser dotfilerne således (læs nedad i den relevante kolonne. Først udføres A, så B, så C osv. B1, B2, B3 betyder at bash kun udfører den første af disse filer, den støder på):

	+----------------+-----------+-----------+-------+
	|                |Interactive|Interactive|Script*|
	|                |login      |non-login  |       |
	+----------------+-----------+-----------+-------+
	|/etc/profile    |   A       |           |       |
	+----------------+-----------+-----------+-------+
	|/etc/bash.bashrc|           |    A      |       |
	+----------------+-----------+-----------+-------+
	|~/.bashrc       |           |    B      |       |
	+----------------+-----------+-----------+-------+
	|~/.bash_profile |   B1      |           |       |
	+----------------+-----------+-----------+-------+
	|~/.bash_login   |   B2      |           |       |
	+----------------+-----------+-----------+-------+
	|~/.profile      |   B3      |           |       |
	+----------------+-----------+-----------+-------+
	|BASH_ENV        |           |           |  A    |
	+----------------+-----------+-----------+-------+
	|                |           |           |       |
	+----------------+-----------+-----------+-------+
	|                |           |           |       |
	+----------------+-----------+-----------+-------+
	|~/.bash_logout  |    C      |           |       |
	+----------------+-----------+-----------+-------+

	* Or non-interactive non-login.

På en Mac afvikles en ny terminal et interaktivt login; på en linux-boks som et interaktivt non-login. Hvorfor det er sådan må Apple kunne svare på[^3]. Det betyder også at på min Mac, bliver først ~/.bash_profile kørt og ved logud (altså, når Terminalen lukkes) bliver så ~/.bash_logout eksekveret af systemet, resten af filerne (.bash_aliases, .bash_prompt og .osx) bliver så sourcet fra disse eller kørt manuelt.

### Filerne

~/.bash_profile - køres af køres af operativsystemet

<script src="https://gist.github.com/krestenjacobsen/f388a5a23aa9c597d2a2.js"></script><br><br>

~/.bash_aliases - køres fra ~/.bash_profile

<script src="https://gist.github.com/krestenjacobsen/3a092c6f423930ba13f8.js"></script><br><br>

~/.bash_prompt - køres fra ~/.bash_profile

<script src="https://gist.github.com/krestenjacobsen/762b08bd1fa81be3ca70.js"></script><br><br>

~/.bash_logout - køres af køres af operativsystemet

<script src="https://gist.github.com/krestenjacobsen/f8a6a91eff83a9f3c22f.js"></script><br><br>

~/.osx - håndkøres ved opsætning af ny Mac

<script src="https://gist.github.com/krestenjacobsen/3342e6a8849db8fe6290.js"></script><br><br>

[^1]: Ren tekst, som kan læses på en hvilken som helst computer lavet siden 70'erne. I øvrigt samme format, som denne blog bliver skrevet i.
[^2]: Hvorfra nedenstående tabel da også er tyvstjålet.
[^3]: Da det - som sædvanen byder - er dem, der afviger fra standarden. *suk*
