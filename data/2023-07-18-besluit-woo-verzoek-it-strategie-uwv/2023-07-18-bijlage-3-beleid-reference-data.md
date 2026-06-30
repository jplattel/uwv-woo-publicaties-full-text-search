---
source_id: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv/2023-07-18-bijlage-3-beleid-reference-data
publication_slug: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv
pdf_slug: 2023-07-18-bijlage-3-beleid-reference-data
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv
pdf_url: https://www.uwv.nl/assets-kai/files/963606f0-324a-4366-9277-97aca9ab0637/bijlage-3-beleid-reference-data.pdf
publication_title: Besluit Woo-verzoek IT strategie UWV
publication_date: '2023-07-18T00:00:00Z'
publication_type: WOO publicatie
pdf_label: Bijlage 3 Beleid Reference Data v3.0 (PDF, 727 kB)
retrieved_at: '2026-06-30T13:18:09+00:00'
sha256: d69b7902660748616816f5283aacae3500a3c1749e9bdfe5a30ef5a43a7ef31f
page_count: 17
ocr_used: false
---

Beleid

Reference Data UWV

voor het beheren en beschikbaar stellen van reference data

Beleid

Reference Data UWV

Datum

28 december 2022

Status Auteur

Definitief Data Office UWV

Versie Pagina

3.0 2 van 17

Versiehistorie

Versie Datum Wijzigingen t.o.v. vorige versie

2.1 30 -01-2016 Herformulering beleid Reference Data na consultatie met Data-Office

en Lokaal Gegevensmanagement

2.2 14-02-2016 Herformulering beleid Reference data na consultatie met Data-Office

en Lokaal Gegevensmanagement

2.3 15-02-2016 Commentaren verwerkt van DO

2.4 26-02-2016 Invoeging TVB rond beheerplatform reference data n.a.v. bespreking

in LGM

2.5 01-03-2016 Finale review Data Office verwerkt

2.6 21-03-2016 Review commentaar LGM verwerkt: 3.2.2 betreft naast nieuwe

applicaties ook nieuwe reference data in een applicatie

2.7 24-03-2016 Vastgesteld in LGM 24-03-2016, met de aanpassing, dat in 3.3.1.

“Ook bewaakt de gegevenseigenaar of de wijzigingen adequaat zijn

doorgevoerd” moet worden gelezen als: gegevenseigenaar vraagt

bevestiging van afnemer dat deze de gegevens correct heeft

overgenomen. Geen controle op daadwerkelijk doorvoeren

Daarnaast verzoekt het LGM om een vervolg in de vorm van

stappenplan voor implementatie (niet in dit beleidsdocument).

2.8 13-04-2016 Vastgesteld in KOG 13-04-2016

Gecontroleerd op werking hyperlinks en terminologie

## 3.0 D 28-12-2022

C = Concept; D = Definitief

Status besluitvorming

Versie Datum Besluitvorming

2.0 22 januari Vastgesteld in Kaderstellend Overleg d.d. 22-1-2015

2015

3.0 D 18 april Vastgesteld in Coalitie Gegevensmanagement d.d. 18 april 2016

2016

C = Concept; D = Definitief

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in

een geautomatiseerd gegevensbestand of openbaar gemaakt, in enige vorm of op enige wijze,

hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enig andere manier zonder

voorafgaande schriftelijke toestemming van de uitgever.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

3 van 17

Inhoud

1 Inleiding 4

1.1 Aanleiding 4

1.2 Historie 4

1.3 Doel 4

1.4 Reikwijdte 4

1.5 Relatie met andere producten van

gegevensmanagement 5

2 Reference data 6

2.1 Wat is het belang van reference data? 6

2.2 Kwaliteitseisen aan reference data 8

2.2.1 Meervoudig gebruik 8

2.2.2 Vast waardebereik (gedurende een periode) 8

2.2.3 Geldigheidstermijn (waardebereik) 8

3 Beleidsuitgangspunten Reference Data Management 9

3.1 Procesmodel Reference Data Management 9

3.2 Modellering en beheer 10

3.2.1 TVB voortbrengingsproces reference data 11

3.2.2 TVB beheer CGM reference data 11

3.3 Distributie 12

3.3.1 TVB distributie van gewijzigde waardebereiken 13

3.4 Afnemen 14

3.4.1 TVB Afname van gewijzigde waardebereiken 15

4 Afkortingenlijst 16

Bijlage A Issues met de landcodetabel binnen UWV 17

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

4 van 17

## 1

Inleiding

1.1 Aanleiding

reference1

Eenduidig gebruik van data binnen UWV moet goed zijn geregeld. Het bestaande

beleid, zoals beschreven in “Beleid Tabellen UGR” dekt slechts een deel van de materie af en

dient vernieuwd te worden.

1.2 Historie

In 2005 is het beleid “Beleid Tabellen UGR” opgesteld. Hierop zijn in januari 2015 de

“Beleidsuitgangspunten reference Data UWV” gebaseerd. Dit is vooral gericht op de inpassing

in het Canonieke Gegevensmodel UWV (CGM), het belang voor de UWV

FUGEMs2.

gegevenshuishouding en het project UWV Daarnaast is een voorstel gedaan om

een “Centraal tabellenregister voor UWV” in te richten binnen Gegevensdiensten. Deze

aanbeveling is niet overgenomen in de organisatie. Er is aangegeven dat centraal beheer niet

past in de organisatie.

Door de beschrijving van reference data in dit document, vervalt paragraaf 4.1.1 Wat is een

Codegegeven? in het gepubliceerde Beleid Tabellen UGR, versie 1.0 van 9 mei 2005.

De overige inhoud van “Beleid Tabellen UGR” zal worden herijkt en vervolgens worden

verwerkt in de FUGEM-standaard en het metamodel van het Canoniek Gegevensmodel UWV.

Daarmee zal het Beleid Tabellen UGR in zijn geheel komen te vervallen.

1.3 Doel

Het doel is duidelijk te maken wat het belang van reference data voor de bedrijfsvoering is

en hoe reference data binnen UWV moet worden beheerd. Het moet voor iedereen mogelijk

zijn om gebruik te maken van eenduidige en consistente reference data: “Reference data die

volledig, juist en actueel zijn”. Het beleid richt zich op een federatief model, niet meer op een

centraal register.

1.4 Reikwijdte

Dit document stelt de definities vast van reference data en reference data management. Het

geeft richting aan de wijze van modelleren, beheren en beschikbaar stellen van reference

data binnen UWV. Reference data zijn een speciale categorie van Master Data. Waarbij het

gaat om het vaststellen en beheren van de “enkelvoudige waarheid over de belangrijkste

bedrijfsgegevens van UWV”.

Dit document is bestemd voor gegevenseigenaren, lokaal gegevensmanagers,

bedrijfsarchitecten, gegevensarchitecten, systeemeigenaren, functioneel beheerders,

functioneel ontwerpers en gegevensspecialisten. Voor wat betreft de beschikbaarstelling

middels services, is er een impact te verwachten op de berichtontwikkeling en –uitwisseling.

Daarnaast speelt het beheerplatform GM een rol bij wijzigingen.

1 Er wordt bewust voor het engelse begrip “reference data” gekozen in plaats van “referentie data”, dit in lijn met de

term Master data. Twee begrippen die nauw verwant zijn.

2

Het project UWV FUGEMs speelt zich af in de periode van begin 2014 tot medio 2016

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

5 van 17

1.5 Relatie met andere producten van gegevensmanagement

Reference data zijn een bepaald soort bedrijfsgegevens. Vanuit dit specifieke perspectief

heeft dit document een relatie met diverse producten van gegevensmanagement

(gegevensstandaarden, -beleid en –architectuur).

De hieronder en verder in dit document genoemde beleids- en/of architectuurdocumenten

van de Data Office UWV zijn beschikbaar op de Digitale Werkplek onder Data Office UWV,

Producten en Kaders.

Titel Relatie

Standaards voor Geeft aan hoe een gegeven moet worden gedefinieerd en

Functioneel ontworpen. Hoe je reference data modelleert staat hierin

Gegevensmodel beschreven.

Canoniek Toont hoe gegevens in bijbehorende context zijn gemodelleerd.

Gegevensmodel UWV Reference data is zichtbaar gemaakt in diagrammen en

(CGM) bijbehorende metadata is vastgelegd.

Beleid Elk gegeven kent een gegevenseigenaar, dus ook reference data.

gegevenseigenaarschap

Beleid Met het beleid reference data wordt gestreefd naar het principe van

gegevensredundantie eenmalige uitvraag (en onderhouden) en meervoudig gebruik

binnen UWV. Geen onnodige opslag van kopieën.

Beleid tijdsdimensies Voor goed beheer van reference data is het noodzakelijk te werken

met de geldigheidsdimensie en transactiedimensie.

Gegevensprincipes Dit document raakt aan gegevensprincipes 1, 2, 3, 4, 6, 7, 8 en 9.

Berichtstandaard Geeft aan hoe beschikbaarstelling van reference data, door middel

van UwvML, wordt vormgegeven.

Beleid Normenhiërarchie Dit document geeft richting aan de te kiezen reference data

wanneer er sprake is van meerdere varianten afkomstig van

verschillende bronnen/instanties (bijv. landcodetabel).

Onderzoek Master Data Het onderzoek naar nut en noodzaak van master data management

Management raakt ook aan reference data, aangezien deze een soort Master

Data zijn.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

6 van 17

## 2

Reference data

Dit hoofdstuk beschrijft wat reference data zijn en hoe deze eruit zien.

2.1 Wat is het belang van reference data?

Reference data (UWV definitie):



Gegevens die worden gebruikt om bedrijfsgegevens te classificeren.



Reference data hebben altijd een vast waardebereik gedurende een bepaalde periode

in de tijd.

Reference data bieden de context voor de uitvoering: de bedrijfssector indeling,

opleidingsniveau’s, opleidingen, rekenregels. De gegevens aan de hand waarvan wordt

geclassificeerd om later vergelijkingen en uitspraken te kunnen doen. B.v stuurinformatie

verkrijgen over WIA uitkeringsduur per opleidingsniveau en WW uitkeringsduur per

opleidingsniveau. Dit maakt het belang duidelijk van een vast waardebereik voor een

bepaalde periode in de tijd en van eenduidigheid over de betekenis van de gebruikte

3

waarden.

Het kan van belang zijn om gedurende een zekere tijd een vaste set aan waarden te hebben,

b.v. premiepercentages hebben een geldigheid van een jaar.

Voorbeelden van reference data zijn:

 Postcodetabel

Landentabel



Nationaliteitentabel



Tabel SZ-wet



 Minimumloontabel

Premiepercentages



Indexeringscijfers



Kostenplaatsindeling



 Opleidingsniveau

Opleidingen



Bedrijfssectoren



 Regio-indeling

Uit bovenstaand overzicht mag duidelijk zijn dat het een breed palet aan soorten gegevens is

waarop geclassificeerd wordt:

Extern gedefinieerde gegevens, waarvoor verschillende lijsten met een waardebereik



bestaan (landen, nationaliteiten),

Extern gedefinieerde gegevens waarvan één waardenlijst van toepassing is



(Postcodetabel),

Extern gedefinieerde gegevens, gebaseerd op wet en regelgeving uit het sociale



domein (SZ-wet, Minimumloontabel, Indexeringscijfers),

3

In de analyses van de FUGEM en het CGM wordt duidelijk welke bedrijfsgegevens gebruik maken van reference data

t.b.v. classificatie. Ook is duidelijk dat in de huidige implementatie van deze reference data niet altijd een eenduidige

definitie/ uitvoering van het begrip wordt gehanteerd (vrije velden om b.v. land van geboorte aan te geven; hergebruik

van oude codes, omdat het aantal mogelijk waarden beperkt was (codes van 1 numeriek, waar in de tijd meer dan 10

waarden nodig zijn)).

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

7 van 17

Intern gedefinieerde gegevens als Kostenplaatsindeling en Regio-indeling.



De eenvoudigste vorm waarin de reference data voorkomen is: een lijst met waarden. Zoals

die in een app voor de smartphone als keuzelijst beschikbaar is voor het kiezen van het land

van geboorte. Soms wordt aan een waarde nog een korte toelichting toegevoegd, of een

aanvullend kenmerk.

Aan het beschikbaar stellen van eenduidige reference data kleven verschillende aspecten:

Omgaan met wijzigingen in omschrijvingen, terwijl de kern van het begrip blijft



bestaan

Omgaan met verschillende synoniemen voor een zelfde begrip (meertaligheid)



Hier is een aanpak nodig die de continuïteit van het object garandeert terwijl de beschrijving

in de loop der tijd of per taal mag wisselen. Er wordt gekozen om een betekenisloze code te

koppelen aan het begrip. Dus code 1 voor “Man”, code 2 voor “Vrouw” in plaats van code “M”

voor “Man” en code “V” voor vrouw. Zo kun je taalonafhankelijk met elkaar communiceren.

In het Frans zou immers gekozen worden voor “H(omme)” en “F(emme)” etc. Het maakt het

gelijk lastig als je persoonsgegevens wilt lezen zonder de uitleg bij code 1 en 2. In de

communicatie zal altijd de werkelijke waarde van het begrip meegeleverd moeten worden.

De praktijk is echter weerbarstig, in bestaande normenlijsten en gegevenssets komen

betekenisdragende codes voor. Deze uitbannen is niet mogelijk. Het beleid is daarom te

streven naar het gebruik van betekenisloze codes.

Omgaan en vaststellen van een goede lijst aan reference data is tweeledig:

1. Vanuit het informatieperspectief: Reference data moet alle voor de gebruiker

relevante waarden bevatten, compleet en actueel, welke synoniemen worden

gehanteerd, hoe verschillende normstelsels zich tot elkaar verhouden.

2. Vanuit beschikbaarheidsperspectief: De reference data moet voor alle afnemers tijdig,

compleet en juist beschikbaar zijn op het moment waarop het nodig is.

Een voorbeeld ad 1: Bij de registratie van werkzoekenden en het matchen van

werkzoekenden op aanvragen is men gediend bij het beschikbaar hebben van een correcte,

complete en actuele keuzelijst voor werkzoekenden om zijn opleidingen op te geven.

N.B. Wat compleet betekent, is afhankelijk van wat we als informatiebehoefte hanteren en

accepteren: de DUO goedgekeurde opleidingen, of een lijst, waarin ook buitenlandse

opleidingen en opleidingen, die voor de werkzoekende relevant waren, maar geen officiële

status hebben, zijn opgenomen.

Een voorbeeld ad 2: Als er nieuwe opleidingen beschikbaar komen, moeten deze aan zowel

de werkzoekenden registratie systemen, als de matching systemen worden opgevoerd, zodat

beide actueel zijn.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

8 van 17

2.2 Kwaliteitseisen aan reference data

Het meervoudig gebruik van een vast waardebereik op enig moment in de tijd stelt hoge

eisen aan de kwaliteit van de reference data en hoe er mee moet worden omgegaan.

2.2.1 Meervoudig gebruik

Uit de aard van reference data volgt het meervoudig gebruik in verschillende processen en

systemen. In deze processen kunnen de reference data in verschillende rollen voorkomen

(geboorteland, nationaliteit, land van overlijden, woonadres land). Het beleid rond

meervoudig gebruik van gegevens en meerdere keren voorkomen van dezelfde gegevens in

verschillende systemen wordt behandeld in “Beleid gegevensredundantie”. Dit beleid laat

zien dat het de voorkeur binnen UWV heeft om van een gegeven slechts één exemplaar als

origineel (Master) in een (centrale) applicatie te hebben waarvan eventuele kopieën (Slaves)

in een één op één relatie hiermee in een aantal aanpalende omgevingen staan.

2.2.2 Vast waardebereik (gedurende een periode)

Het vaststellen wat het waardebereik op enig moment is, is een gezamenlijke keuze van de

afnemers4

en de gegevenseigenaar, de partij die de opdracht heeft dit waardebereik voor

UWV te onderhouden. Uiteraard wordt de keuzevrijheid beperkt door de bedrijfsvoering waar

men mee te maken heeft. In geval van buiten UWV geformuleerde waardenlijsten kan men

niet afwijken van de gehanteerde standaards. Voor uitsluitend binnen UWV gehanteerde

begrippen is de vrijheid groter. Echter één partij binnen UWV vervult de rol van

gegevenseigenaar, de anderen van afnemer. De taken en verantwoordelijkheden die hierbij

in het geding zijn, zijn verwoord in het “Beleid gegevenseigenaarschap”.

Het vaste karakter van het waardebereik heeft meerdere aspecten:

 Een bepaald reference data voorkomen heeft een betekenis en die geldt voor allen

die het gebruiken: voorkom homoniemen en synoniemen, dit geldt gedurende het

hele bestaan van dit gegeven.

Voor bepaalde reference data zijn externe bronnen beschikbaar, UWV streeft ernaar



aan te sluiten op één van deze bronnen, zie het “Beleid Normenhiërarchie”. Gezien

de historie binnen, maar ook buiten UWV, zal het voorkomen dat meerdere bronnen

als uitgangspunt zijn genomen. Voor adequate classificatie is beleid geformuleerd in

de normenhiërarchie over hoe om te gaan met deze samenloop.

 De mate waarin het waardebereik kan groeien, krimpen door de tijd heen bepaalt de

bruikbaarheid voor het maken van analyses op basis van de gegevens. Hoe stabieler

hoe makkelijker. Het is een eigenschap, die bekend moet zijn bij afnemers om

eenduidigheid in gebruik te bevorderen.

2.2.3 Geldigheidstermijn (waardebereik)

De geldigheidstermijn van het waardebereik is van essentieel belang om te weten, zodat

vergelijkingen van waarden eenduidig kunnen worden gemaakt. Het “Beleid tijdsdimensies”

geeft de richtlijn hoe om te gaan met de geldigheidsduur van een voorkomen en de

administratieve kant van het beheer van een voorkomen, denk aan terugwerkende kracht

mutaties. D.w.z. elke referentie waarde heeft een begin en einddatum waarop deze geldig is

en een mutatiedatum, die aangeeft per wanneer het gegeven beschikbaar is gekomen.

4

We kiezen expliciet voor de term “Afnemer” in plaats van “gebruiker”, om de afhankelijkheid van de eigenaar aan te

geven. De term “gebruiker” wordt vaak ook gehanteerd voor de functionaris die de registratie verzorgt van de

gegevens in een applicatie. Afnemer versus Eigenaar is daarom duidelijker in deze context.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

9 van 17

## 3

Beleidsuitgangspunten Reference Data Management

Een goed beheer (management) van reference data is noodzakelijk om issues zoals

bijvoorbeeld m.b.t. de integratie en kwaliteit van data op te lossen en in de toekomst te

voorkomen. Dit hoofdstuk beschrijft daarom de beleidsuitgangspunten om tot die goede

beheersing te komen. Onder het “managen” van reference data wordt het volgende

verstaan:

Reference data management (UWV definitie):

Het geheel van richtlijnen, processen en applicaties om reference data te beheren en ter

beschikking te stellen voor een bedrijfsbreed gebruik.

In het vorige hoofdstuk is toegelicht vanuit welke gegevensbeleid naar reference data kan

worden gekeken. Dat heeft zijn consequenties voor het beheer van de reference data.

Wijzigingen in de reference data hebben grote impact op de mogelijkheid tot classificatie en

vervolgens analyse van bedrijfsgegevens. De invoering van nieuwe waarden vraagt daarom

om zorgvuldig management: afstemmen met de bron wanneer de data geldig wordt,

informeren van en afstemmen met de afnemers (partijen die de reference data gebruiken

voor gegevens invoer en gegevens uitvoer (rapportages, leveringen, analyses etc.)). Deze

rol ligt bij de gegevenseigenaar, of zijn vertegenwoordiger, zie beleid

gegevenseigenaarschap.

Zodra de nieuwe lijst met waarden is vastgesteld zal de ingangsdatum gesteld worden en de

lijst worden vrijgegeven voor gebruik in productie.

Het is in deze raadzaam om à la de OTAP-straat voor systeemontwikkeling een acceptatie en

release traject in te richten voor de wijziging van waardebereiken.

3.1

Procesmodel Reference Data Management

Onderstaand model geeft de verschillende aspecten weer van Reference Data management:

1. Modellering en beheer van de reference data

2. Distributie van reference data

3. Afnemen van reference data

In de paragrafen hierna worden de verschillende onderdelen toegelicht.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

10 van 17

3.2

Modellering en beheer

De modellering van reference data volgt het standaard pad van de gegevensanalyse en

vastlegging in de repositories. De reference data kennen een UWV-breed gebruik. In

verschillende omgevingen kunnen ze verschillend worden gebruikt. Het is daarom zaak de

afspraak in het CGM vast te leggen over wat de “enkelvoudige bron van de waarheid” is en

hoe er met de afgeleiden wordt omgegaan. In het CGM wordt aangegeven welke waarden

geldig zijn. Dit kan door expliciet een lijst met waarden op te nemen of aan te geven in welk

systeem, of welke documentatie deze waarden als “enkelvoudige waarheid” worden beheerd.

In de FUGEM’s worden de verschijningsvormen van de reference data in de

bedrijfsapplicaties gedocumenteerd.

Met het aangeven van wat de bron van de referentiedata is, wordt ook de eigenaar van deze

gegevens aangemerkt: die eigenaar bepaalt dat er een wijziging op de lijst met waarden

aanstaande is. Namens de bron-eigenaar kan een bron-houder worden aangemerkt. Deze

treedt binnen UWV namens de bron-eigenaar op in de besturing en beheer van de reference

data.

De eigenaar van de reference data maakt met de afnemers afspraken over het beheer.

De afnemers worden aan de hand van de CGM/FUGEM-documentatie bepaald. Deze

afspraken worden vastgelegd in een Service Niveau Overeenkomst (SNO).

Hierin staan de rechten en plichten van beide partijen. Op hoofdlijn:



Wat verwachten de afnemers van de kwaliteit van de reference data,

o

kwaliteitsdimensies (beschikbaarheid, vertrouwelijkheid, compleetheid,

consistentie, juistheid en tijdigheid )

o

inhoudelijk (welke waarden willen we als reference data zien).



Wat verwachten de houders van de wijzigingsverwerking door de afnemers

o

Verwerking wijzigingen binnen afgesproken tijdsvenster

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

11 van 17

o

Signalering issues bij gebruik van reference data

Op basis van deze afspraken voeren alle afnemers samen met de eigenaar het reference

data change management in het Beheer platform. Hierin wordt minimaal het volgende

besproken.



Overleg over kwaliteitsniveau service verlening reference data



Wijzigingenbeheer (wanneer welke wijzigingen doornemen)



Maatregelen treffen t.b.v. tijdige verwerking wijzigingen

Van Beheer platform overleg wordt verslag gedaan, waarbij ook de lokaal gegevensmanager

wordt geconsulteerd/ geïnformeerd om eventuele wijzigingen in de reference data in het

CGM/ FUGEM te (laten) doorvoeren.

3.2.1 TVB voortbrengingsproces reference data

Bij de ontwikkeling van nieuwe reference data moet de lokaal gegevensmanager

geconsulteerd worden, opdat deze i.s.m. Data Office toetst of de reference data al elders

beschikbaar is en ingezet kan worden. Indien een en ander geheel nieuw is, kan de lokaal

gegevensmanager adviseren over de beste aanpak, opdat het CGM goed gevuld zal worden

met nieuwe waardebereiken.

3.2.2 TVB beheer CGM reference data

De ontwikkelaar van nieuwe reference data heeft de verantwoordelijkheid (R) om deze

adequaat te (laten) documenteren in het FUGEM en te delen met Data Office om een en

ander op te nemen in het CGM.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

12 van 17

3.3

Distributie

Periodiek zullen de wijzigingen in de reference data worden klaargezet voor distributie naar

de afnemers, dan gaat het om die reference data waar in het beheer platform

overeenstemming over is bereikt.

Dit klaarzetten kent twee verschijningsvormen: a-synchroon en synchroon.



Synchroon

o

Real-time, 24*7 services op de repositories, waarin de referentie worden

beheerd, leveren de geldige gevraagde waarden voor een bepaalde reference

data. Geldig in termen van goedgekeurd en actueel voor het moment dat de

vastlegging moet plaats vinden.



A-Synchroon

o

Daar waar de reference data niet in een database worden beheerd, het te

verwerken volume aan wijzigingen groot is en/of de beherende systemen en

het afnemende systeem verschillende productiekarakteristieken hebben (hoge

versus lage verwerkingssnelheid); systeembeschikbaarheid (24*7 versus 8-

gehanteerd5

18:00) wordt de a-synchrone verwerking

o

De wijzigingen in de reference data worden in files of in niet-geautomatiseerd

verwerkbare berichten ter beschikking gesteld aan de afnemende systemen.

5

Het gegevensredundantie beleid geeft een aantal aspecten van systemen, waardoor gegevens

redundant worden opgeslagen. Dus ook reference data.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

13 van 17

3.3.1 TVB distributie van gewijzigde waardebereiken

Het beheerplatform van de gegevenseigenaar zorgt voor het tijdig informeren van zijn

afnemers van reference data, opdat deze voldoende tijd hebben om wijzigingen door te

voeren. Ook bewaakt de gegevenseigenaar passend of de wijzigingen zijn doorgevoerd.

Passend is situationeel. In de meeste gevallen is een bevestiging van de afnemer dat de

gegevens zijn doorgevoerd voldoende. Daar waar het belang van UWV dit vraagt kan het in

gevallen nodig zijn dat er meer zekerheid over het doorvoeren nodig is. De

gegevenseigenaar en de afnemers maken hier expliciet afspraken over in de Service Niveau

Overeenkomst.

Hierbij gesteund door de LGM’er, die een consulted rol heeft in het toetsen van het correct

houden van de diverse gedistribueerde sets aan reference data.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

14 van 17

3.4

Afnemen

De afnemer verwerkt conform de afspraak in de SNO. Dit is cruciaal om te zorgen dat iedere

gebruiker van de reference data dezelfde set aan data op dezelfde tijd ter beschikking heeft.

Dit om analyses en werkzaamheden over heel UWV in lijn te houden.

De verwerking van de wijzigingen worden getoetst door het Beheerplatform voor de

reference data.

Met de nieuwe waarden voor de reference data heeft de gebruiker de UWV gevalideerde set

aan waarden. Hiermee kan in het eigen werkproces conform de richtlijnen van UWV gewerkt

worden. Een bepaalde referentie waarde zal door heel het bedrijf met de zelfde betekenis

gehanteerd moeten worden.

Elke gebruiker zal speciale regels hebben bovenop de richtlijnen voor het gebruik van de

reference data die UWV breed gelden.



Een bepaald werkproces zal bijvoorbeeld niet alle waarden uit een waardenlijst willen

gebruiken. Daarvoor zal intern een masker moeten worden ontwikkeld dat de niet te

gebruiken waarden afschermt.



Voor rapportages en analyses zullen meer “gebruikersvriendelijke” omschrijvingen van

de referentie waarden gewenst zijn. Ook deze kunnen als aanvulling binnen de eigen

omgeving op de referentie gegevens worden opgenomen.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

15 van 17

3.4.1 TVB Afname van gewijzigde waardebereiken

De afnemers van reference data zorgen voor tijdig doorvoeren van wijzigingen in de

reference data. Zij rapporteren hierover aan de gegevenseigenaar. Hierbij gesteund door de

LGM’er, die een consulted rol heeft in het toetsen van het correct houden van de diverse

gedistribueerde sets aan reference data. Daar waar het waardebereik van de reference data

ook in het CGM is opgenomen, zullen de gegevensspecialisten van DO de aangepaste lijst

verwerken in het CGM.

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

16 van 17

## 4

Afkortingenlijst

BRP Basisregistratie Personen

CGM Canoniek Gegevensmodel UWV

DIV Documentaire Informatievoorziening

FUGEM Functioneel Gegevensmodel

GBA Gemeentelijke Basisadministratie Persoonsgegevens

ISO International Organization for Standardization

LGM Lokaal Gegevensmanagement

NEN Nederlandse Norm

ODS Operational Datastore

SNO Service Niveau Overeenkomst

TVB Taken Verantwoordelijkheden Bevoegdheden

WW Werkloosheidswet

Beleid

Reference Data UWV

Datum

28 december 2022

Versie

3.0

Pagina

17 van 17

## Bijlage A

Issues met de landcodetabel binnen UWV

(20141017), (20160229)

5.1 lid 2 sub e 5.1 lid 2 sub e

BRP-adressen en loonaangifteadressen in Polis:

Landcode wordt geregistreerd zowel bij adressen afkomstig uit Basisregistratie personen

(BRP) als bij adressen afkomstig uit de loonaangifte. UWV past beschikbare normen toe

volgens het beleid normenhiërarchie. Dat beleid leidt ertoe dat:

Adressen afkomstig uit de Basisregistratie Personen (BRP) een landcode hebben



overeenkomstig de tabel landcode GBA.

Adressen afkomstig uit de loonaangifte een landcode hebben overeenkomstig de



tabel landcode ISO.

Resa/Fasa maakt gebruik van de z.g.n. GAK-BRP landcode, niet te verwarren met de



Basisregistratie Personen (BRP) landencode. Dit gebeurt naast het gebruik van de

ISO 2 lettercode voor landen.

In de gegevensketen blijkt dat ODS zich beperkt tot Landcode ISO. Waarom dit zo is, is niet

duidelijk. Vertalen van de landcode GBA naar de landcode ISO leidt tot informatieverlies,

omdat de landcodetabel GBA gedetailleerder gegevens bevat dan de landcodetabel ISO. Een

eventueel noodzakelijke vertaling van landcode GBA naar landcode ISO mag in ieder geval

niet leiden tot verlies van de landcode GBA.

Andere buitenlandse adressen waarbij verzekerde de bron is:

Als de verzekerde de bron is van adresgegevens en als daarbij een landcode geregistreerd

wordt, dan wordt dat conform beleid normenhiërarchie de landcode ISO.

Uit de beschrijving “T2301 Muteren adresgegevens” blijkt dat voor “Verblijfadres” en

“Postadres” (volgens adressenbeleid “Verblijfadres bij ziekte”, “Verblijfadres bij afwijkend

woonland” en “Correspondentieadres”) een landcode overeenkomstig de tabel landcode ISO

geregistreerd wordt. Omdat Resa/Fasa uitgaat van landcode GAK-BRP naast de ISO Alpha-2

(letter) code, wordt bij uitwisseling met Resa/Fasa de landcode ISO vertaald naar landcode

GBA. Ook hier leidt dat in bepaalde gevallen tot informatieverlies.

Conclusie:

Er wordt in de praktijk kennelijk vanuit gegaan dat er een 1:1-vertaling mogelijk is van

landcode ISO naar landcode GBA. Zoals hierboven gezegd is dat een onjuiste aanname. Uit

de praktijk komen dan ook bij herhaling signalen dat er foutsituaties optreden bij het

uitwisselen van landcodes. Op grond van het bovenstaande is dat goed verklaarbaar.

Om deze foutsituaties te vermijden moet men zodanige maatregelen nemen dat in

alle gevallen waarin sprake is van vertaling van de code uit het ene codestelsel

naar een code uit het andere stelsel, in ieder geval de oorspronkelijke code

behouden blijft.

---

Bron: [Besluit Woo-verzoek IT strategie UWV](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv) · [Bijlage 3 Beleid Reference Data v3.0 (PDF, 727 kB)](https://www.uwv.nl/assets-kai/files/963606f0-324a-4366-9277-97aca9ab0637/bijlage-3-beleid-reference-data.pdf)
