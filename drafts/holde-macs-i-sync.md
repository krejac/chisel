At holde flere Macs i sync
19-02-2015

[TL;DR](http://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn't_read) -- Det evige problem med hvad der er p� hvilken Mac l�ses - til en hvis udstr�kning - med BitTorrent Sync og automatiseret app-lukning.

Efter vi fik en Mac mini til kontoret har det evigt v�ret et problem for mig at holde data nogenlunde i sync og jeg har l�nge g�et og grublet over hvordan jeg kunne l�se det problem uden at fylde min Dropbox med iTunes biblioteker, film og lignende. Nu tror jeg jeg har fundet l�sningen.

Med [BitTorrent Sync](http://www.getsync.com/) kan man synkronisere hvad som helst - og af en hvilken som helst st�rrelse - p� tv�rs af maskiner. Det der kr�ves, for der er ingen server involdveret er at begge de maskiner der skal synkroniseres er t�ndte og forbundede til nettet samtigt.

## Hvilke mapper synkroniseres ##

{Find tips til hvilke mapper der kan / ikke kan synkroniseres - http://luo.ma/geek/how-i-use-bittorrent-sync}

## Forholdsregler ##

Fordi en begr�nsning ved BitTorrent Sync er at den ikke vil synkroniserer filer, som systemet eller - m�ske mere aktuelt -  dine apps arbejder aktivt p�, har jeg valgt automatisk at slukke mit iTunes hver nat kl. 01:00 og starte det igen om morgenen kl. 06:00. Hvis ikke man g�r det, rissikerer man at de filer, som holder styr p� hvad der ligger i iTunes kommer ud af sync. Samtidigt vil jeg dog ikke rissikere at miste data, hvis mit iTuns st�r og tygger p� en st�rre opgave (importerer film eller lign.), s� derfor er det n�dvendigt at simulere at man lukker det "normalt" (som man g�r via menuen eller CMD + Q). Men for at kunne schedulere det var jeg n�dt til at kunne scripte mig ud af det og heldigvis har OS X en fin funktion til netop det ([ref.](http://osxdaily.com/2014/09/05/gracefully-quit-application-command-line/)):

    osascript -e 'quit app "iTunes"'
	
	osascript -e 'open app "iTunes"'
	
Eller 

	tell application "iTunes"
		if it is running then
		pause
		end if
	end tell


- Luk apps der bruger data; BitTorrent Sync vil ikke synkronisere �bne filer.

- Konflikter??? {Find ud af hvordan BitTorrent Sync h�ndterer konflikter}

## Konklusion ##

- Virker det eller virker det ikke? 
- Kan det anbefales?

[^1]: Setuppet begr�nser sig egentligt ikke til Macs, men de Windows og Linux maskiner jeg har, tjener andre funktioner og der skal mine personlige data ikke (n�dvendigvis) over.