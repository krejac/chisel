Rundt i manegen med tele-scammeren
03-10-2017


**[TL;DR](http://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn't_read)** - Tele-scammere ringer jævnligt rundt til uforvarende for at fra-narre dem penge eller lignende. Jeg prøvede i dag at tage med på turen for at se hvad de ville.

![tele-scammeren](https://log.logiskhave.dk/static/20171003_scam.jpg)

I dag havde jeg _endelig_ tid til at lytte til den venlige indiske "Microsoft" support-dame, der med jævne mellemrum ringer og fortæller mig den er gal med min Windows-maskine[^1] - og den var tilsyneladende _helt_ gal for de kunne nemt påvise mange fejl...

<img class="screen" src="https://log.logiskhave.dk/static/20171003_run-command-box.png" alt="cmd">

Først vil tele-scammeren have een til at åbne en kommandoprompt ([win]+r efterfulgt af "cmd" og et tryk på ok). Her blev jeg så bedt om at taste "assoc" og de læste min maskines "unikke identifikator" op.

<img class="screen" src="https://log.logiskhave.dk/static/20171003_assoc-output.png" alt="assoc">

    .ZFSendToTarget=CLSID\{888DCA60-FC0A-11CF-8F0F-00C04FD7D062}

Jeps, den passede[^2]. Så jeg blev sendt videre til 2. level support - meget professionelt.

2. level-supporteren, som var en mand, som bad mig åbne "event viewer" ([win]+r efterfulgt af "eventvwr" og et tryk på ok) og navigere frem til en laang list med "fejl"[^3].

<img class="screen" src="https://log.logiskhave.dk/static/20171003_event-log.jpg" alt="event log">

Når det så er konstateret overfor mig som bruger, at der er en masse fejl på min maskine, bad 2. level-supporteren mig om at navigere til www[.]support[.]me og logge ind. Men den side er et link til et [fjernskrivebordsværktøj](https://en.wikipedia.org/wiki/LogMeIn), som man bliver bedt om at downloade og installere, hvorefter man giver dem fuld adgang til maskinen - _så her skal man altså stå af_.

Det var så også her jeg bekendte kulør og sagde at jeg desværre måtte indrømme, at jeg arbejdede med it til dagligt og blot havde trukket dem en tur rundt i manegen for at finde ud af hvordan det foregik og havde spildt deres tid.

Og jeg skal da SÅ ellers lige love for at jeg fik en sviner på et ellers meget sødt engelsk med indisk accent. :)

[^1]: Hvilket er spøjst fordi jeg bruger macOS.
[^2]: Fordi det naturligvis [_ikke_ er en "unik identifikator" for en given maskine](https://msdn.microsoft.com/en-us/library/windows/desktop/ms691424(v=vs.85).aspx).
[^3]: Som en alindelig bruger ikke bør bekymre sig om - de logs er primært til udviklere og / eller systemadministratorer.
