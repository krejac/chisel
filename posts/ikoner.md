Favicon og apple-touch-icon
08-10-2013


Så kom der også favicon og apple-touch-icon på siden. Favicon'et kan typisk ses ud for URL'en, hvis browseren understøtter det. Apple-touch-icon'et bliver vist, hvis man tilføjer siden til sin hjemmeskærm på sin iPxx-enhed.

![Billede af log.logiskhave.dk-ikon på hjemmeskærmen](/static/20131008_apple-icon.png)

Så jeg kan huske det til en anden god gang, så brugte jeg [Favicon Generator](http://favicon-generator.org) til at lave en .ico-fil ud af et billede, uploadede det og indsatte nedenstående i headeren i min index.html.

     <link rel="icon" href="/static/favicon.ico">

Apple-touch-icon'et er her en jpg-fil med dimentionerne 200x200 - selvom det højeste nogen iPxx kan bruge, uden at nedskalere, vist er 144x144. Denne fil uploades og refereres så til med denne linie (indsat lige under ovenstående i headeren):

     <link rel="apple-touch-icon" href="/static/apple-touch-icon.jpg"/>
