---
source_id: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv/2023-07-18-bijlage-10-doelarchitectuur-e-dienstverlening
publication_slug: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv
pdf_slug: 2023-07-18-bijlage-10-doelarchitectuur-e-dienstverlening
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv
pdf_url: https://www.uwv.nl/assets-kai/files/b3506137-1f21-4035-830f-501deb0a2b25/bijlage-10-doelarchitectuur-e-dienstverlening.pdf
publication_title: Besluit Woo-verzoek IT strategie UWV
publication_date: '2023-07-18T00:00:00Z'
publication_type: WOO publicatie
pdf_label: Bijlage 10 Doelarchitectuur E-Dienstverlening (PDF, 4 MB)
retrieved_at: '2026-06-30T13:18:36+00:00'
sha256: fd75d08288cbc7c6a4c353956ab319ae8995683ef031b7dad56835e763f955a4
page_count: 117
ocr_used: false
---

Doelarchitectuur Doelarchitectuur E-Dienstverlening E-Dienstverlening

April November 2017 2017

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

2 van 117

## Versiebeheer

Versie Datum Status Korte beschrijving

1.00 06-06-2017 Definitief Versie definitief vastgesteld in AB, juni 2017

1.10 01-08-2017 Definitief Review commentaar cat. A verwerkt

1.20 Concept Aanvulling App diensten werkversie

1.30 11-09-2017 Concept Review binnen team App diensten

1.40 06-10-2017 Concept Collegiale review K&S

1.45 23-10-2017 Concept Review versie t.b.v. AB+

1.50 22-11-2017 Definitief Aanvulling App diensten geaccordeerd

Versiebeheer:

5.1 lid 2 sub e

Opgesteld door: · (Bedrijfsarchitectuur),

5.1 lid 2 sub e

5.1 lid 2 sub e

(Applicatiearchitectuur),

(NFR’s en Infrastructuurarchitectuur),

5.1 lid 2 sub e

, (Overall redactie).

5.1 lid 2 sub e

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand

of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enig andere

manier zonder voorafgaande schriftelijke toestemming van de uitgever.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

3 van 117

Inhoud

1 Inleiding 5

1.1 Visie op E-Dienstverlening 5

1.2 Doelarchitectuur E-Dienstverlening 6

1.3 Doelgroep 7

1.4 Relatie met overige doelarchitecturen 8

1.5 Inhoud van deze doelarchitectuur 9

1.6 In volgende versies 10

2 Afbakening doelarchitectuur E-Dienstverlening 11

2.1 Doelstelling 11

2.2 Afbakening architectuuraspecten 11

3 Architectuurprincipes en requirements 13

3.1 Denklijn 13

3.2 Architectuur principes 13

3.3 Niet-functionele eisen 16

4 Bedrijfs- en informatiearchitectuur 18

4.1 De klantreis 18

4.2 Patronen binnen de klantreis 22

4.3 Relatie klantreis en dienstpatronen 23

4.4 Klantreis, klantprocessen en kanalen 23

4.5 Ondersteunende processen 28

4.6 Gegevensarchitectuur 30

4.7 Informatiebeveiliging en privacy 30

5 Applicatie Architectuur 33

5.1 KIA/KOA referentiemodel 33

5.2 Architectuur BouwBlokken (ABB) 53

5.3 Applicatiepatronen 68

5.4 Software Bouwblokken (SBB) 86

6 Infrastructuur Architectuur 89

6.2 Infrastructuur E-Dienstverlening 91

6.3 SBB’s en infrastructuurcomponenten 92

Bijlage A, Gebruikte bronnen 93

Bijlage B, Ontwikkelingen digitale dienstverlening 94

Bijlage C, Architectuurprincipes 101

Bijlage D, Niet-functionele eisen 103

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand

of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enig andere

manier zonder voorafgaande schriftelijke toestemming van de uitgever.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

4 van 117

Bijlage E, Basis procesmodel 112

Bijlage F, SOA en MSA 114

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand

of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enig andere

manier zonder voorafgaande schriftelijke toestemming van de uitgever.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

5 van 117

1 Inleiding

UWV is een zelfstandig bestuursorgaan (ZBO) en verzorgt in opdracht van het ministerie van Sociale

Zaken en Werkgelegenheid de uitvoering van werknemers- en volksverzekeringen, zoals WW, WIA (IVA

en WGA), Wajong, WAO, WAZ, Wazo en Ziektewet, arbeidsmarkt- en gegevensdienstverlening.

[1]1:

UWV verricht kerntaken op vier gebieden

• Werk: we stimuleren mensen om aan het werk te blijven of nieuw werk te vinden. We werken

hierbij samen met gemeenten en private partijen. Werkgevers ondersteunen we bij het vinden

van personeel.

Sociaal-Medische Zaken (Indicatiestelling): we beoordelen volgens vastgestelde criteria ziekte

•

en arbeidsongeschiktheid, als grondslag voor re-integratie en het benutten van

participatiemogelijkheden.

Uitkeren: we verzorgen tijdig en correct uitkeringen als werken niet of niet direct mogelijk is.

•

Gegevensbeheer: we zorgen ervoor dat mensen slechts 1 keer gegevens over werk en uitkering

•

aan de overheid hoeven te geven.

UWV wil excelleren als publieke dienstverlener door de klant centraal te stellen. Deze ambitie wordt

concreet gemaakt aan de hand van de volgende meetbare criteria: persoonlijke aandacht,

bereikbaarheid, toegankelijkheid, tijdigheid, duidelijkheid en maatwerk.

klantgroepen2:

De kerntaken worden uitgevoerd voor en in samenwerking met de volgende

• Burger: een klant van UWV waarmee een persoon bedoeld wordt;

Werkgever (Bedrijf): een klant van UWV die één of meer personen arbeid laat verrichten in

•

een arbeidsverhouding;

Zakelijke partner: een klant van UWV in de hoedanigheid van een ‘gegevensafnemer’,

•

‘gegevensleverancier’ of een ‘arbeidsmarktpartij’, en eventueel ook gemeenten, SVB, etc.;

Ketenpartner: een bedrijf waarmee UWV samen een stuk dienstverlening neerzet. Bijvoorbeeld

•

een gemeente, of een andere overheidsinstelling.

De dienstverlening van UWV loopt via meerdere kanalen: op de vestiging, telefonisch, per post en via

digitale kanalen. Een klant krijgt dan ook te maken met meerdere kanalen. Uitdaging is deze kanalen op

een voor de klant intuïtieve manier op elkaar te laten aansluiten zodat zij dit als een logisch geheel

ervaren.

1.1 Visie op E-Dienstverlening

De afgelopen jaren is de dienstverlening steeds verder gedigitaliseerd en worden diensten aangeboden

via portalen, social media en digipoort. De strategie die UWV voor ogen heeft bij de overgang naar het

1

Referenties naar bronnen zijn opgenomen tussen rechte haken [ . . .]

2

UWV levert haar diensten steeds vaker ook aan klanten en partners buiten Nederland. Deze versie van de

doelarchitectuur schenkt daar nog geen specifieke aandacht aan. Wel wordt er zo veel mogelijk rekening gehouden

met toekomstige aansluiting bij Europese richtlijnen. In volgende versies van deze doelarchitectuur wordt dit

onderwerp verder uitgewerkt.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

6 van 117

digitaal zaken doen, is beschreven in de beleidslijn “Passend digitaal” [2, 4] en door K&S aangevuld in

februari 2017 in de Digitale Strategie [7]. Die gaat uit van een tempo van digitalisering van

dienstverlening dat door de klant als logisch wordt ervaren. De niet-digivaardige klant verliezen we

hierbij niet uit het oog. UWV onderkent dat digitale dienstverlening niet voor ieder proces en niet in

iedere situatie effectief is [6].

Waar digitaliseren voor UWV nu vooral betekent dat diensten via websites/portalen worden aangeboden,

beschrijft deze versie van de doelarchitectuur ook de basis voor het kunnen leveren van diensten via

mobiele apps. Ontwikkelingen op het vlak van digitale dienstverlening worden door UWV gevolgd en waar

nuttig en zinvol worden nieuwe mogelijkheden opgenomen in deze doelarchitectuur.

Met E-Dienstverlening stelt UWV haar klanten voor steeds meer diensten in staat zelf verantwoording te

nemen en zelfstandig uit te voeren. UWV medewerkers blijven beschikbaar voor ondersteuning in die

situaties waar de klant er niet op eigen kracht uit komt.

In Bijlage B, is een overzicht van recente ontwikkelingen met betrekking tot digitale dienstverlening

buiten en binnen UWV opgenomen.

1.2 Doelarchitectuur E-Dienstverlening

Deze doelarchitectuur E-Dienstverlening beschrijft de gewenste situatie van voor het digitale kanaal van

UWV vanuit het perspectief van de klant. Het is een document dat met regelmaat aangevuld wordt met

onderwerpen waar vanuit de klant- zowel als vanuit de interne organisatie behoefte aan is. Voor de

voorliggende versie betekent dit concreet, dat de doelarchitectuur is uitgewerkt voor portalen. De

onderwerpen in deze doelarchitectuur kunnen naar verwachting in 3-5 jaar gerealiseerd worden. De

verwachting is UWV daarna nog enkele jaren kan doorontwikkelen met de, in deze doelarchitectuur,

ingezette richting.

De doelarchitectuur in totaliteit

stelt kaders voor de realisatie van het applicatielandschap en infrastructuur waarmee de digitale

•

ondersteund3;

dienstverlening van UWV wordt

gebruiken we om projecten de juiste stappen te laten zetten richting de doelsituatie;

•

• gebruiken we om bestuurders en IV-regisseurs binnen UWV zicht te bieden op de doelsituatie;

gebruiken we om de afstemming te borgen met de doelarchitecturen E-Werken en

•

Gegevenshuishouding;

wordt door de Architectuur Board (AB) gebruikt als een van de toetsingskaders voor PSA’s en

•

nader op te stellen architectuurdocumenten;

wordt door de design authorities gebruikt als richtinggevend document en toetsingskader bij te

•

nemen beslissingen;

wordt gebruikt door alle afdelingen van UWV die zich bezig houden met de inrichting en

•

uitvoering van digitale dienstverlening, en in het bijzonder door K&S Digitale Dienstverlening,

WERKbedrijf E-Dienstverlening WERK (EDW) en Ontwerp en Beheer Werkplein dienstverlening

(OBW) en de afdelingen Informatiemanagement van de divisies K&S en Werkbedrijf;

• wordt gebruikt binnen de Internet Organisatie UWV (IOU) als referentiekader voor de technische

diensten4;

inrichting van digitale

3

NB: de niet-digitale dienstverlening van UWV valt expliciet buiten de scope van E-Dienstverlening.

4

Met deze versie van de doelarchitectuur E-Dienstverlening is deze uitspraak alleen geldig voor dienstverlening via

portalen. In volgende versies wordt dit breder uitgewerkt.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

7 van 117

is een levend document dat regelmatig aangepast moet worden naar nieuwe inzichten en

•

beschikbare technologieën.

Deze doelarchitectuur is opgesteld in samenwerking tussen diverse architecten binnen UWV onder leiding

van het K&S architectuur team. De versie van voorjaar 2017 bouwt voort op eerdere documenten (zie

ook bijlage A.)

1.3 Doelgroep

Deze doelarchitectuur is bedoeld voor de volgende groepen functionarissen die vanuit hun expertise

betrokken zijn bij verandertrajecten die vallen binnen de scope van digitale dienstverlening:

• Vanuit inhoudelijke expertise in verandertrajecten: architecten, business consultants, business

analisten, procesontwerpers en functioneel ontwerpers, adviseurs IB&P etc.

• Vanuit plannings- en sturingsexpertise op verandertrajecten: IV regisseurs, portfoliomanagers,

programmamanagers, projectmanagers, projectleiders en releasemanagers, etc.

• Vanuit opdracht gevende expertise: divisiedirecteuren, programmadirecteuren en business managers.

Voor het management van de divisie K&S is de doelarchitectuur één van de hulpmiddelen waarmee de

ICT-aspecten van de visie gepland en uitgewerkt en uiteindelijk gerealiseerd kunnen worden.

Het Hoofd van het K&S IM is eigenaar van deze doelarchitectuur en het onderhoud ervan is belegd bij de

lead architect K&S waarbij nauwe samenwerking met de afdeling Digitale Dienstverlening plaatsvindt.

Voor de CIO-Office biedt de doelarchitectuur enerzijds een instrument waarmee de ontwikkeling van de

integrale architectuur voor UWV kan worden gevolgd, anderzijds stelt deze doelarchitectuur de CIO-Office

in staat de grenzen tussen verschillende doelarchitecturen – en daarmee de integraliteit van het geheel -

te bewaken

Voor architecten van andere onderdelen van UWV biedt deze doelarchitectuur inzicht in de ontwikkelingen

op het vlak van E-Dienstverlening. Daarnaast beschrijft deze doelarchitectuur de raakvlakken met

overige (doel)architecturen vanuit de optiek van E-Dienstverlening.

Voor de bij UWV betrokken ICT-leveranciers biedt deze doelarchitectuur inzicht in de door UWV gewenste

ontwikkelingen zodat zij daar hun dienstverlening op kunnen afstemmen. Daarnaast mag deze

doelarchitectuur worden gezien als een uitnodiging om voorstellen te doen die UWV in staat stellen

sneller haar doelen te bereiken.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

8 van 117

1.4 Relatie met overige doelarchitecturen

De doelarchitectuur E-Dienstverlening staat niet op zich zelf, maar heeft

een sterke samenhang met de doelarchitecturen E-Werken en

gegevenshuishouding (en overige nog te ontwikkelen doelarchitecturen).

Deze samenhang komt voort uit het realiseren van diensten in het

digitale kanaal en het delen van informatie met diensten in andere

kanalen. Deze diensten zijn altijd het resultaat van een klantinteractie

bij een bedrijfsproces dat UWV uitvoert. Hieruit komt de relatie met de

doelarchitectuur E-Werken naar voren. De diensten zijn ook afhankelijk

van correcte, volledige en betrouwbare informatie. De doelarchitectuur

gegevenshuishouding geeft richting aan dat aspect, voor zo ver sprake

is van gestructureerde informatie.

Ondersteunend aan deze doelarchitecturen beschrijft de infrastructuur

Figuur 1, samenhang

architectuurdomeinen

architectuur de toe te passen infrastructuurcomponenten.

1.4.1 E-Werken

Vanuit de efficiëntiedoelen die door E-Werken moeten worden gerealiseerd ontwikkelt het programma E-

Werken E-Diensten waarmee, via een bedrijfsregel gestuurde vraag-en-antwoord-dialoog, uitkeringen

kunnen worden aangevraagd, inkomsten kunnen worden doorgegeven en wijzigingen in de (persoonlijke)

situatie van een klant (burger, bedrijf, ketenpartner) kunnen worden doorgegeven. Tevens worden

werkzoekenden door middel van E-Diensten laagdrempelig ondersteund in het vinden van werk en

werkgevers in het vinden van personeel. E-Diensten zijn functionaliteiten binnen de UWV-portalen, in

apps en in A2A-koppelingen die een specifiek deel van de dienstverlening van UWV afhandelen, zoals het

indienen van aanvragen (bijvoorbeeld voor een uitkering) of het doorgeven van inkomsten of

sollicitatieactiviteiten. Deze E-Diensten stellen geen overbodige vragen aan de burger, de bij UWV

hij5

beschikbare gegevens worden getoond, aan de burger wordt gevraagd of het hier mee eens is en hij

kan bepaalde gegevens aanvullen. Binnen de E-Diensten worden vragen gesteld die tot doel hebben

dienstverlening op maat te bieden (bijvoorbeeld de werkverkenner) of om vraag en aanbod bij elkaar te

brengen (via CV- en vacature bank en kandidatenverkenner banenafspraak), maar ook vragen die

bijdragen aan het nemen van de beslissing. Na afloop van de vraag-en-antwoord-dialoog worden de

resultaten getoond in de vorm van een conceptbeslissing die de burger gaat krijgen als hij zijn klantvraag

daadwerkelijk indient bij UWV. Binnen de E-Diensten worden gegevens op een gestructureerde manier bij

de burger uitgevraagd, zodat op basis hiervan zoveel mogelijk klantvragen op een geautomatiseerde

wijze kunnen worden afgehandeld.

De samenhang tussen E-Dienstverlening en E-Werken komt tot uitdrukking in de geautomatiseerde

afhandeling van de klantvragen in de primaire processen. Hiervoor kan de klantinteractie worden

ingericht met behulp van de genoemde E-Diensten. De ambitie bestaat om een snelle realisatie en

implementatie van de klantinteractie en E-Diensten mogelijk te maken, waarmee de digitale interactie

tussen klanten en UWV wordt ondersteund ten behoeve van de uitvoering van de (klant)processen. De

E-Diensten zijn hiervoor:

zodanig opgezet dat ze passen binnen de klantreis;

•

5

Waar in dit document ‘hij’ wordt genoemd, kan ook ‘zij’ worden gelezen.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

9 van 117

zodanig flexibel zijn dat ze zich aanpassen aan de persoonlijke omstandigheden van de klant;

•

via meerdere kanalen en apparaten de klant kunnen bereiken.

•

De consistentie tussen de doelarchitectuur E-Werken en de doelarchitectuur E-Dienstverlening wordt

voortdurend bewaakt. Bij het opstellen van deze versie is er regelmatig contact geweest tussen de

leadarchitecten van de verschillende doelarchitecturen om de aansluiting te bewaken.

1.4.2 Gegevenshuishouding UWV

Het werken met gestructureerde gegevens binnen de primaire processen speelt een belangrijke rol bij het

waarmaken van de ambities van UWV. E-Dienstverlening speelt een belangrijke rol bij het ophalen van

deze gestructureerde gegevens. Het zijn immers de E-Diensten die de directe (digitale) communicatie

verzorgen met de klanten. Gegevenshuishouding UWV richt zich op de inwinning, opslag, het beheer en

de beschikbaarstelling van gegevens. Dit omvat tevens de kaderstelling en gegevens logistieke

administraties. UWV streeft hiermee naar een goedkopere gegevenshuishouding en gegevensbeheer, en

een stabielere gegevenshuishouding. Daarnaast wordt gestreefd naar het betrouwbaarder, consistenter,

flexibeler en efficiënter vastleggen en leveren van gegevens met een hoge kwaliteit aan interne en

externe afnemers. Hiervoor wordt ingezet op de standaardisatie en minimalisatie van

technologievarianten voor de ontsluiting van systemen, de inzet van een aantal gemeenschappelijke

voorzieningen om de efficiency in het gegevensgebruik te vergroten en de inzet van standaard breed

inzetbare gegevensleveringen.

Om E-Diensten optimaal te laten functioneren is beschikbaarheid van gegevens het sleutelwoord. Digitale

dienstverlening vraagt om een hoge beschikbaarheid van gegevens. Een ander belangrijk onderwerp is

wendbaarheid. Het gaat daarbij vooral om het snel kunnen ontwikkelen van nieuwe dienstverlening aan

de klant. Ontkoppeling van systemen voor (digitale) dienstverlening en registratieve systemen is de

manier waarop we invulling willen geven aan de benodigde beschikbaarheid en wendbaarheid. De

doelarchitectuur Gegevenshuishouding beschrijft op welke wijze welke gegevens beschikbaar gesteld

kunnen worden. In de applicatiearchitectuur van E-Dienstverlening wordt de concrete relatie tussen de

beide doelarchitecturen zichtbaar door bij de applicatiepatronen aan te geven welke patronen voor

gegevensontsluiting daarbij van toepassing zijn.

1.4.3 Overige architecturen

Hoewel er binnen UWV drie doelarchitecturen zijn benoemd, worden voor onderdelen (w.o. KCC en

outputmanagement, infrastructuur) ook architecturen opgesteld. De doelarchitectuur E-Dienstverlening

sluit waar nuttig en mogelijk aan bij deze ontwikkelingen.

1.5 Inhoud van deze doelarchitectuur

Na dit inleidende hoofdstuk volgt de afbakening en doelstelling in hoofdstuk 2. De uitgangspunten,

architectuurprincipes en niet-functionele eisen worden benoemd in hoofdstuk 3. De hoofdstukken 4, 5 en

6 bevatten vervolgens de uitwerking van de verschillende architectuuraspecten (business, applicatie,

infrastructuur).

De bijlagen bij dit document bevatten geraadpleegde bronnen, ontwikkelingen op het gebied van digitale

dienstverlening, afkortingen en definities.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

10 van 117

1.6 In volgende versies

Volgende versies van deze doelarchitectuur zullen voortbouwen op en uitbreiden wat in deze versie is

beschreven.

De stapsgewijze doorontwikkeling van deze doelarchitectuur sluit zo veel mogelijk aan bij de roadmap

zoals die binnen K&S Digitale Dienstverlening (DD) wordt gehanteerd. Deze roadmap is onder andere

gebaseerd op de wensen met betrekking tot ontwikkeling van E-Diensten vanuit de divisies. Daarnaast

zijn de roadmaps van E-Werken, van de individuele en de planning van groot onderhoud (GOH) en

reguliere wijzigingen van invloed op de volgorde waarin onderwerpen in deze doelarchitectuur worden

verwerkt.

Concrete onderwerpen die in volgende versies aan de orde komen zijn:

• A2A koppelingen;

Aansluiten bij K&S visieontwikkeling m.b.t. beveiliging van en toegang tot gegevens

•

o

Verdere uitwerking gevolgen WGDI producten

5.1 lid 2 sub i

Waar relevant vanuit de klantbeleving aansluiten bij (door)ontwikkeling van de UWV visie met

•

betrekking tot:

o

## CRM;

o

Document Management;

o

Kanaalvoorkeuren en hybride gebruik van kanalen;

• Verantwoording c.q. aansluiten bij richtlijnen vanuit DIV voor archivering;

Gegevensarchitectuur (voor zover relevant voor E-Dienstverlening);

•

Internationale dienstverlening;

•

Uitlijnen van KKO project met doelarchitectuur en binnen doelarchitectuur duidelijkheid geven over

•

een mogelijke klantgegevensservice;

Uitbreiden doelarchitectuur door het verbinden van de klantbehoefte met de abstracte

•

klantreis/dienstpatronen. Dit kan op basis van life-events en/of het model in bijlage E en customer

journeys. Tevens het in lijn brengen van de begrippen en definities uit de doelarchitectuur met

vraagsturing/agifall.

De uitwerking van deze onderwerpen kan deels binnen projecten plaatsvinden. In dat geval wordt de

nieuw toegevoegde inhoud van de PSA onderdeel van de volgende versie van deze doelarchitectuur. Dit

houdt ook in dat het opstellen van deze PSA’s plaatsvindt in nauw overleg met de architecten die bij de

totstandkoming en beheer van deze doelarchitectuur betrokken zijn.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

11 van 117

2 Afbakening doelarchitectuur E-Dienstverlening

2.1 Doelstelling

De doelarchitectuur voor E-Dienstverlening geeft richting aan de ontwikkeling van E-Dienstverlening voor

UWV en schetst een beeld van de digitale dienstverlening aan de hand van de eerder vastgestelde

conceptuele klantreis en daarin onderkende patronen. Van daaruit beschrijft de doelarchitectuur het

ondersteunende applicatie landschap met daarbij de eisen die aan de onderliggende infrastructuur

worden gesteld. Daarmee maakt de doelarchitectuur het mogelijk keuzes te maken voor in te zetten

producten.

Daarnaast beschrijft de doelarchitectuur de applicatie architectuur inclusief patronen die de kaders

vormen voor verdere inrichting van het landschap van E-Diensten.

2.2 Afbakening architectuuraspecten

De doelarchitectuur voor E-Dienstverlening wordt vanuit verschillende invalshoeken beschreven. De

bedrijfsarchitectuur beschrijft het ‘Wat’ van de digitale dienstverlening en is het startpunt voor de

applicatie architectuur. In die applicatiearchitectuur wordt beschreven welke (ICT-) middelen worden

ingezet om de business te ondersteunen en hoe die met elkaar samenhangen. Alleen die onderdelen

worden beschreven die betrekking hebben op de digitale dienstverlening van UWV.

In de beschrijving van de infrastructuurarchitectuur wordt aangegeven welke eisen E-Dienstverlening

stelt aan de infrastructuur en de wijze waarop de elementen in de infrastructuur samenwerken.

2.2.1 Context architectuur domeinen

De doelarchitectuur E-Dienstverlening staat niet op zichzelf, maar sluit aan op E-Werken en

Gegevenshuishouding (DA GEIN). De context waarbinnen deze doelarchitectuur wordt uitgewerkt is in

onderstaande figuur weergegeven.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

12 van 117

Figuur 2, context architectuurdomeinen

De doelarchitectuur E-Dienstverlening richt zich vooral op de volgende onderdelen van dit model:

Communicatiekanalen in relatie tot klantvragen voor zo ver digitaal (Digitale kanaal, Digipoort);

•

• De klantreis;

partner6,

Klanten (Burger, Werkgever, Zakelijke Ketenpartner);

•

De bedrijfsfunctie “Verzorgen klantmanagement” (verticaal geplaatst, nr. 12).

•

De overige onderdelen worden beschreven in andere doelarchitecturen. Een overkoepelend overzicht is in

ontwikkeling.

6

Niet zijnde leveranciers t.b.v. dienstverlening

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

13 van 117

3 Architectuurprincipes en requirements

Dit hoofdstuk geeft een overzicht van de architectuurprincipes die sturing geven aan keuzes die in deze

doelarchitectuur zijn gemaakt. Een architectuurprincipe is een richtinggevende uitspraak waarin een voor

E-Dienstverlening relevant deel van het UWV-beleid is verwoord. Deze uitspraken zijn afgeleid uit de

visie, missie, bedrijfsdoelen en strategie, maar kunnen ook uit andere bronnen voortkomen.

3.1 Denklijn

De denklijn die we hanteren met betrekking tot E-Dienstverlening is dat UWV de klant in staat stelt zelf

zijn zaken te regelen, zoals aanvragen doen, wijzingen doorgeven en opvragen van de status van de

dienstverlening. Daarmee stelt UWV de klant in staat vragen te beantwoorden en dienstverlening af te

nemen zonder tussenkomst van een UWV medewerker. Bovendien verwachten we dat daarmee de

klanttevredenheid wordt verhoogd. Deze denklijn kunnen we realiseren op basis van de onderstaande

architectuurprincipes.

3.2 Architectuur principes

De voor E-Dienstverlening geldende set van algemene architectuurprincipes van UWV is opgenomen in

Bijlage C, Naast deze breed geldende architectuurprincipes is hieronder specifiek voor E-Dienstverlening

een set principes geformuleerd. Naast algemene constructieprincipes zijn principes opgenomen die er

mede voor zorgen dat de prioriteiten zoals die in het UIP zijn vastgelegd kunnen worden gerealiseerd.

3.2.1 Algemene constructieprincipes

Deze doelarchitectuur wordt grotendeels geïmplementeerd in een applicatielandschap waarin diensten

van UWV tegelijkertijd via verschillende (digitale) kanalen worden aangeboden. Daar waar sprake is van

ontwikkeling of aanschaf van software en het koppelen van applicaties, gelden de volgende algemene

constructieprincipes:

Scheiding tussen presentatie met interactielogica en verwerking met bedrijfslogica;

•

Kanalen zijn ontkoppeld van verwerking in de bron-en materiesystemen;

•

Gedrag en presentatie van applicaties worden gestuurd door kanaal, autorisatie en

•

personalisatie;

‘Design for failure’ zodat fouten in een keten niet leiden tot onbeschikbaarheid van een geheel

•

kanaal en/of meerdere ketens;

Over kanalen getoonde gegevens zijn consistent voor wat betreft de inhoud van de gegevens;

•

• ‘Archive by Design’ zodat gevolgde processen op een later tijdstip kunnen worden

gereproduceerd;

Applicaties dragen bij aan een optimale klanttevredenheid in termen van beschikbaarheid en

•

performance;

Maak gebruik van standaard communicatieprotocollen.

•

3.2.2 Stabiliteit en continuïteit

De architectuur voor E-Dienstverlening moet een stabiele dienstverlening mogelijk maken zodat klanten

van UWV er op kunnen rekenen dat de digitale dienstverlening beschikbaar is wanneer dat gewenst is.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

14 van 117

Hierbij spelen zowel technische als organisatorische aspecten een rol. Concrete onderwerpen die hierin

een rol spelen zijn hieronder weergegeven. Een groot deel van deze onderwerpen speelt overigens ook

een rol in de andere doelarchitecturen.

• Ontwerp foutafhandeling mee zodat eventueel optredende fouten inzichtelijk worden en op de

juiste wijze afgehandeld kunnen worden, bijvoorbeeld door, indien mogelijk, terug te vallen op een

default waarde;

Privacy & Security by Design borgt dat gedurende het gehele proces van idee tot en met

•

technische realisatie aandacht bestaat voor aspecten van privacy en informatiebeveiliging;

Logging en monitoring zodat trends in gebruik en het beschikbaar zijn van systemen kunnen

•

worden bewaakt en opgevolgd;

• Duurzaam toegankelijk zodat informatie die door UWV is opgeslagen beschikbaar is en blijft het

## NORA7;

thema Duurzame Toegankelijkheid binnen de

Horizontaal schalen zodat het mogelijk is extra capaciteit beschikbaar te stellen op momenten dat

•

er een grote toeloop van gebruikers wordt verwacht. Daarbij hoort ook dat capaciteit wordt

teruggeschroefd op het moment dat een kleinere toeloop gemeten wordt.

Redundantie zorgt er voor dat onderdelen van de architectuur dubbel worden ingericht en zodanig

•

worden geconfigureerd dat bij uitval van een onderdeel, de dienstverlening wel door kan gaan;

Eenvoud in opzet en ontwerp helpt bij het begrijpelijk en onderhoudbaar houden van de totale

•

dienstverlening en draagt daarmee bij aan de continuïteit.

Ontkoppelen: Ontkoppeling is het isoleren van systeemonderdelen (waaronder proces en

•

informatie) voor wijziging van structuur of toestand van andere systeemonderdelen. Door

ontkoppeling wordt ervoor gezorgd dat kritieke processen binnen E-Dienstverlening beschikbaar zijn

ongeacht de toestand van andere systeemonderdelen zoals beschikbaarheid en performance van

bron- en materiesystemen.

3.2.3 Wendbaarheid

Veranderingen in ICT volgen elkaar steeds sneller op. Zeker daar waar sprake is van digitale

dienstverlening geldt dat heel sterk. De doelarchitectuur helpt UWV de digitale dienstverlening naar de

klant flexibel op te zetten zodat veranderingen snel kunnen worden gerealiseerd. Concrete onderwerpen

zijn:

Ontkoppelen: Ontkoppeling is het isoleren van systeemonderdelen voor wijziging van structuur of

•

toestand van andere systeemonderdelen. Isolatie is niet absoluut, maar het beperkt de impact van

wijzigingen in één systeemonderdeel op andere systeemonderdelen en draagt daarmee ook bij aan

een vergroting van de wendbaarheid in het IT-landschap van UWV. De ontkoppeling draagt bij aan

het ondersteunen van wendbaarheid van applicaties waarmee de klant direct werkt en welke flexibel

en snel aanpasbaar moeten zijn. Dit geldt overigens ook voor bron en materiesystemen. Deze

ontkoppeling leidt er toe dat aanpassingen in de frontoffice los kunnen staan van aanpassingen in de

backoffice, maar ook dat E-Diensten los van elkaar kunnen worden ontwikkeld;

7

Zie: http://wiki.nationaalarchief.nl/pagina/DUTO:Over

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

15 van 117

Service Oriëntatie helpt het realiseren van eenheden die niet alleen afzonderlijk en snel kunnen

•

worden aangepast, maar die ook zelfstandig functioneren, waardoor het geheel wendbaar wordt.in de

praktijk van UWV wordt dit vormgegeven door toepassing van aspecten van zowel Service Oriented

## (MSA)8,9;

Architecture (SOA) als Micro Services Architecture

Werken met bedrijfsregels helpt UWV met het efficiënter en effectiever omgaan met wijzigingen in

•

wet- en regelgeving of intern bedrijfsbeleid door de bedrijfsregels integraal te beheren. Bedrijfsregels

vormen een vertaling van wet- en regelgeving en intern bedrijfsbeleid naar operationele richtlijnen

om tot het resultaat (meestal beslissingsondersteuning) te komen. Binnen de toekomstige E-Diensten

wordt steeds meer gewerkt met bedrijfsregels. Waar nodig maakt E-Dienstverlening gebruik van de

regelservices10.

aangeboden De verantwoordelijkheid voor de inhoud van de regelservice ligt echter

bij de verschillende divisies;

Governance en voortbrenging moeten zo zijn ingericht, dat aanpassingen ook daadwerkelijk snel

•

gerealiseerd en geïmplementeerd kunnen worden. Dit geldt zowel voor de architectuur zelf als voor

de producten die worden gerealiseerd binnen de architectuur. Een Agile werkwijze met een duidelijke

Agifall11 SAFe12

rol voor Product Owner, architecten en beveiliging, conform Vraagsturing, en is

daarbij wenselijk en sluit aan op de ontwikkelingen binnen UWV.

Een belangrijk onderdeel hiervan is de relatie met leveranciers die vooral moet zijn gericht op

samenwerking tussen UWV en de betreffende leverancier.

3.2.4 Vereenvoudiging en modernisering

Vereenvoudiging en modernisering worden voor geheel UWV vormgegeven met als doel zowel wendbaar

als stabiel te zijn. Voor E-Dienstverlening worden op dit vlak de volgende uitgangspunten gehanteerd:

Modulaire opbouw: Functionaliteit wordt gegroepeerd op basis van het business domein

•

(bedrijfsfuncties, processen en bedrijfsobjecten conform de UWV standaards voor

BedrijfsObjectModel- BOM) en op een niveau waarop de functie van de componenten concreet te

herkennen is voor kenners van het business domein. Voeg geen componenten samen om generieke

componenten te realiseren.

Dit uitgangspunt draagt overigens ook bij aan het vergroten van de wendbaarheid.

Ontkoppelen: Ontkoppeling is het isoleren van systeemonderdelen voor wijziging van structuur of

•

toestand van andere systeemonderdelen. Ontkoppeling draagt bij aan wendbaarheid welke zich ook

uit in het feit dat divisies wijzigingen kunnen doorvoeren met slechts minimale afstemming met

overige divisies. Daarmee faciliteert ontkoppelen het geleidelijk moderniseren van het UWV

applicatielandschap.

8

De begrippen SOA en MSA worden in de Applicatie Architectuur verder uitgewerkt. Meer algemene informatie in de

bijlagen en op: https://www.opengroup.org/soa/source-book/soa/soa.htm en

http://microservices.io/patterns/microservices.html

9

De aspecten van SOA en MSA die worden gehanteerd zijn uitgewerkt in hoofdstuk 5. Daarmee is expliciet geen keuze

gemaakt voor toepassing van SOA en MSA buiten de scope van E-Dienstverlening.

10

Het daadwerkelijk gebruik van regelservices wordt mogelijk nadat UWV systemen hiervoor heeft geselecteerd en geï

mplementeerd. Tot dat moment zijn bedrijfsregels integraal onderdeel van afzonderlijke applicaties.

11

Agifall is de agile werkwijze die is toegespitst op de bestaande situatie rond leverancierscontracten bij UWV

12

Scaled Agile Framework, zie: http://www.scaledagileframework.com/

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

16 van 117

In de uitwerking van de applicatiearchitectuur zijn de hier boven beschreven principes verder uitgewerkt.

3.3 Niet-functionele eisen

Op basis van de bedrijfsdoelen kunnen voor deze doelarchitectuur de eisen en wensen (requirements)

van de gebruikers worden verzameld. Figuur 3 toont hoe

doelen, eisen en wensen samenhangen. Naast functionele

eisen die worden gesteld aan de bouwblokken van deze

doelarchitectuur, zijn er ook niet-functionele eisen (non-

functional requirements). De set niet functionele eisen is

opgesteld aan de hand van ISO25010 en omvat de

hieronder beschreven onderwerpen. De meer gedetailleerde

uitwerking is opgenomen in Bijlage D,

Deze eisen en wensen zijn verzameld in een aantal

workshops met vertegenwoordigers van zowel business als

Figuur 3, eisen en wensen hiërarchie

ICT. Deze kwaliteitseisen zijn van toepassing op alle

onderdelen van het systeem waar de gebruiker mee werkt,

dus niet alleen infrastructuur, maar ook voor de applicaties en de processen waarbinnen de applicaties

worden ingezet.

3.3.1 Onderwerpen binnen ISO 25010

Functionele geschiktheid (Functional Suitability)

•

beschrijft de mate waarin een systeem functies levert

die voldoen aan de uitgesproken (en veronderstelde)

behoeften.

Voor UWV geldt hier, dat de gebruiker de garantie

dient te krijgen dat door hem ingevoerde en door

UWV geaccepteerde gegevens ook daadwerkelijk

worden verwerkt.

Prestatie-efficiëntie (Performance efficiency)

•

beschrijft de prestaties in verhouding tot de

hoeveelheid middelen gebruikt onder genoemde

condities.

Belangrijke eisen binnen dit onderwerp zijn de

responstijd (ook bij piekbelasting) en het geven van

een melding in geval van overbelasting

Uitwisselbaarheid (Compatibility) is de mate waarin

•

een product, systeem of component informatie uit kan

wisselen met andere producten, systemen of

Figuur 4, grafische weergave ISO 25010

componenten, en/of het de gewenste functies kan

uitvoeren terwijl het dezelfde hard- of software-

omgeving deelt.

Het toepassen van standaardkoppelingen is een voorbeeld van de eisen op dit gebied.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

17 van 117

Bruikbaarheid (Usability) beschrijft de mate waarin een product of systeem gebruikt kan worden

•

door gebruikers om effectief, efficiënt en naar tevredenheid doelen te bereiken in een bepaalde

gebruikscontext.

Aspecten binnen dit aandachtsgebied zijn het gebruik van verschillende browsers en devices en de

mate waarin door UWV aangeboden applicaties gebruikersfouten voorkomen, bijvoorbeeld door

controles op invoervelden.

Betrouwbaarheid (Reliability) is de mate waarin een systeem, product of component de

•

gespecificeerde functies uitvoert onder bepaalde condities gedurende een gespecificeerde hoeveelheid

tijd.

Binnen deze categorie vallen de eisen met betrekking tot beschikbaarheid en hersteltijden in geval

van storing.

Beveiligbaarheid (Security) omvat de mate waarin een product of systeem informatie en gegevens

•

beschermt zodat personen, andere producten of systemen de juiste gegevenstoegang hebben,

passend bij hun soort en niveau van autorisatie.

Een belangrijk onderdeel van deze eisen is de mate waarin door UWV aangeboden diensten kunnen

aansluiten bij de eisen op het vlak van Informatiebeveiliging en Privacy (IB&P), zoals bij voorbeeld

onweerlegbaarheid van transacties.

Onderhoudbaarheid (Maintainability) is de mate waarin een product of systeem effectief en

•

efficiënt gewijzigd kan worden door beheerders.

Een onderdeel hiervan is de analyseerbaarheid van storingen in een systeem aan de hand van de

logging en de wijze waarop getest kan worden.

Overdraagbaarheid (Portability) beschrijft de mate waarin een systeem, product of component

•

overgezet kan worden van één hardware, software, of andere operationele omgeving naar een

andere.

Binnen deze categorie worden bijvoorbeeld eisen gesteld aan de snelheid waarmee een applicatie

geschikt gemaakt kan worden voor migratie naar een ander rekencentrum.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

18 van 117

4 Bedrijfs- en informatiearchitectuur

De bedrijfsarchitectuur beschrijft op hoofdlijnen de inhoud en functionele behoefte van het domein

E-Dienstverlening. Het belangrijkste doel van dit onderdeel is het kunnen beschrijven van een goede

applicatiearchitectuur. De basis daarvoor is de conceptuele klantreis zoals deze binnen K&S wordt

gehanteerd. Dit model omvat in principe alle contactmomenten tussen UWV en haar klanten voor alle

vormen van dienstverlening van UWV. Deze doelarchitectuur beperkt zich echter tot de digitale

verschijningsvormen van de klantreis en beschrijft niet de meer traditionele vormen van contact tussen

de klanten en UWV (werkplein, KCC, etc.). Specifieke diensten die binnen deze klantreis aan individuele

klanten worden aangeboden, zijn niet uitgewerkt in deze versie

In dit hoofdstuk worden na de klantreis de ondersteunende processen beschreven voor zo ver deze van

invloed zijn op de applicatie architectuur voor E-Dienstverlening.

4.1 De klantreis

Bezien vanuit de klant is het startpunt voor de bedrijfsarchitectuur de conceptuele klantreis zoals in

onderstaande figuur getoond. Dit model toont geen volgordelijkheid, maar beschrijft fasen die een klant

een of meerdere keren doorloopt gedurende de periode waarin hij contact heeft met UWV. De in dit

model onderkende fasen worden uitgelegd in de tabel onder de figuur.

Figuur 5, basismodel klantreis

Fase Beschrijving

Oriënteren Bij de start van deze fase van de klantreis is de burger of werkgever

nog anoniem voor UWV. De klant bevindt zich veelal op een publieke

omgeving om algemene zaken te achterhalen. Hij oriënteert zich op de

arbeidsmarkt door het zoeken naar geschikte vacatures of het zoeken

naar informatie over een uitkering of ontslagaanvraag.

Hoe dichter de klant bij een aanvraag komt, hoe persoonlijker de

dienstverlening wordt. In het geval van een uitkeringsaanvraag wordt

dit vaak getriggerd door een telefonisch consult. In de toekomst kan

een burger ook laagdrempelige, maar betrouwbare, persoonlijke

berekeningen maken op de Mijn-omgeving. In de oriëntatie hanteert

UWV een verleidingsstrategie. We proberen de klant zover te krijgen

dat hij zichzelf zo snel mogelijk kenbaar maakt door zich te identificeren

en in te loggen zodat we hem beter van dienst kunnen zijn. In de

volgende fasen is inloggen veelal verplicht.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

19 van 117

Fase Beschrijving

Aanvragen De klant gaat over tot het aanvragen van een dienst van UWV (WW

uitkering, WWB uitkeringsaanvraag, WAJONG uitkering,

ontslagaanvraag, etc.). Tijdens dit proces zijn drie aspecten van belang.

Ten eerste dienen er zo weinig mogelijk aspecten voor de klant aan het

licht te komen die nog niet waren meegedeeld in de oriëntatie fase

(voorspelbaarheid). Daarnaast is het belangrijk dat zoveel mogelijk

informatie vooraf wordt ingevuld in de aanvraag (laagdrempelig) en als

laatste is het van belang dat direct een passende response wordt

gegeven (verwachting management). Dit zal in eerste instantie een

status update zijn, maar zal langzaam groeien richting concrete

antwoorden en beslissingen. Werkgevers vragen in deze fase bijv.

toegang tot de CV- en vacaturebank zodat zij geschikte kandidaten

kunnen benaderen en vacatures kunnen plaatsen.

Dienst/uitkering ontvangen Deze fase omvat het ontvangen van een uitkering of andere dienst van

(continueren / wijzigen) UWV. Deze fase staat in het teken van het doorgeven van wijzigingen

en verantwoordingsgegevens vanuit de klant en het informeren en

betalen vanuit UWV. Wanneer deze fase is bereikt neemt de intensiteit

van het contact over de uitkering in veel gevallen af. In het geval van

de ondersteuning in de weg naar werk, intensiveert het contact met

UWV veelal. Om tijdig de aandacht van de klant te krijgen speelt het

versturen van de juiste notificaties hier een belangrijke rol.

Werk(-nemer) zoeken Deze fase wordt ingezet om werkzoekenden te ondersteunen in de weg

naar werk en het zoeken naar geschikte kandidaten door werkgevers,

waarbij er specifieke aandacht is voor bijzondere klantgroepen.

Belangrijke aspecten hierbij zijn diverse soorten van online

leermodules, het bij elkaar brengen van vraag en aanbod en het

transparant maken van de arbeidsmarkt. Ook de werkgever wordt

ondersteunt bij het vinden van een werknemer.

Deze fase loopt in de praktijk deels parallel met de andere fasen en zal

al vanaf de fase Oriëntatie een rol spelen.

Beëindigen De laatste fase van de klantreis is de beëindiging van de uitkering en/of

het niet langer gebruik willen maken van ondersteuning in de weg naar

werk. Dit kan vanuit de burger doordat er werk is gevonden, maar de

uitkering kan ook worden beëindigd vanuit UWV doordat de maximale

doorlooptijd is bereikt. Er dient te allen tijden duidelijke communicatie

over het eventuele vervolg plaats te vinden, en dienen de relevante

stukken te worden gearchiveerd, voor zo ver deze nog niet eerder in

het proces waren gearchiveerd. Hier valt ook het kunnen exporteren

van gegevens voor eigen archiefdoeleinden van de klant.

Voor een deel van de klantreis geldt dat alleen publieke informatie beschikbaar wordt gesteld. Een groot

deel bevat echter informatie die voor een specifieke klant bedoeld is zodat identificatie van de

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

20 van 117

(potentiële) klant door middel van inloggen noodzakelijk is. Voor verschillende type informatie kan een

verschillende niveau van inloggen noodzakelijk zijn. Dit is verder uitgewerkt in paragraaf 4.7

Bij diensten van UWV worden klantprocessen onderkend die aansluiten bij deze klantreis. Om dit

concreet te maken is de conceptuele klantreis een niveau verder uitgewerkt, zoals getoond in Figuur 6 en

beschreven in de daaropvolgende tabel.

Ook voor deze onderverdeling geldt dat hier geen sprake is van een strikte volgorde en enkele

onderdelen kunnen ook in andere fasen voorkomen, afhankelijk van de detailuitwerking van een specifiek

klantproces. Klantprocessen worden niet in detail uitgewerkt in deze doelarchitectuur.

Figuur 6, detailmodel klantreis

Fase Beschrijving

Informeren Het informeren van klanten door algemene informatie op de door UWV

beheerde mediakanalen, zoals de eigen portalen of content aangeboden aan

derden zoals overheid.nl/life-events of via samenwerkingsverbanden.

Informeren via Het informeren van (toekomstige) klantgroepen over het Merk UWV via niet

Social Media door UWV beheerde kanalen, waarbij het merk duidelijk wordt

gepositioneerd als autoriteit op het gebied van werk en inkomen.

Daarnaast faciliteert social media als Open Digitale Communicatie om niet

persoonsgebonden informatie te delen met klantgroepen.

Helpen bij zoeken Ondersteuning via beslisbomen, stappenplannen, rekenhulpen,

oriëntatiemenu's, carrousels, How To video's, etc. Bedoeld om klantgroepen

meer inzicht te bieden in wat er te wachten staat. Dit kan ook zijn het

ondersteunen naar het vinden van werk of het vergroten van de kans op

werk. Deze informatie wordt aangeboden in de open omgeving.

Identificeren De klant identificeert zich bij UWV om vervolgens toegang te kunnen krijgen

tot voor hem bedoelde diensten en informatie. Daarnaast geeft de klant

aanvullende informatie over zijn situatie die niet al op voorhand bij UWV

bekend is.

Het niveau waarop de klant wordt geauthentiseerd bepaald welke diensten

en gegevens toegankelijk zijn.

Dienst aanvragen De klant vraagt een specifieke dienst van UWV aan.

Status aanvraag opvragen De klant vraagt aan UWV de status van zijn eerder ingediende aanvraag.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

21 van 117

Fase Beschrijving

Toekenning / afwijzing De klant ontvangt de toekenning of afwijzing van zijn eerder ingediende

ontvangen aanvraag. Deze stap in de reis omvat ook Bezwaar en Beroep.

Profileren De klant ontvangt voor hem persoonlijk gerichte content en diensten gericht

op zijn moment in de klantreis en zijn relatie met UWV. De klant geeft zijn

contactvoorkeuren aan en heeft inzicht in wat UWV van hem/haar weet.

Service krijgen De klant( c.q. klantgroep) wordt proactief geholpen in de dienstverlening.

Op basis van beschikbare gegevens krijgt de klant diensten en/of informatie

te zien of attenderingen die hem tot actie aanzetten of herinneren dat er

iets van hem verwacht wordt of dat er iets voor hem klaar staat.

Overzicht ontvangen De klant krijgt een totaaloverzicht over de diensten die door hem (kunnen)

worden afgenomen.

Status inzien De klant kan de status inzien van zijn eigen gegevens en specifieke diensten

gericht op het moment van de klantreis en de relatie met UWV of met een

derde partij.

Wijzigen Klantgroepen kunnen wijzigingen doorgeven die gevolgen hebben op de

recht duur en hoogte van hun uitkeringsrelatie. Van ziek of herstel

meldingen tot gedeeltelijke werkhervattingen of meer/minder werken, etc.

Ook kunnen klanten hun eigen (CV- of vacature) gegevens wijzigen om beter

gevonden te worden op de arbeidsmarkt.

Doorgeven De klantgroepen geven zelf informatie of taken door aan UWV die al dan

niet gevolgen hebben voor hun recht duur of hoogte,

uitkeringsverplichtingen zoals inkomsten, vakanties, etc. Dit kan ook het

doorgeven van nieuwe skillsets zijn.

Contact zoeken De klant zoekt contact met UWV om een specifiek onderwerp te bespreken

(en vice versa) of neemt digitaal ondersteunend contact op met UWV (chat,

call me back, virtuele assistent, FAQ) ten behoeve van het voorkomen van

uitval uit het digitale kanaal.

Naast het digitale kanaal zijn de adviseurs op Werkplein of het Werkgevers-

servicepunt hierbij betrokken

Vacature of werknemer De klant zoekt naar vacatures of potentiele werknemers.

zoeken en vinden

CV of vacature plaatsen Klant plaatst zijn CV of vacature om gevonden te kunnen worden.

Kans op succes vergroten De klant neemt aanvullende diensten van UWV af om de kans op succes te

vergroten (E-Learning, training, etc.).

Afspraken en De klant maakt afspraken met UWV m.b.t. de te volgen stappen en

verantwoording verantwoord de voortgang daarin.

Afmelden Het beëindigen van een of meer diensten van UWV.

Exporteren, opslaan en De klant zowel als UWV en/of een ketenpartner exporteren relevante

evalueren gegevens m.b.t. de beëindigde diensten en evalueren de dienstverlening.

UWV geeft hiermee aanvulling aan verplichtingen die voortvloeien uit de

archiefwet.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

22 van 117

4.1.1 Toepassing van de conceptuele Klantreis

Voor specifieke diensten van UWV wordt de conceptuele klantreis op maat gemaakt door stappen vanuit

de conceptuele klantreis te concretiseren en in volgorde te plaatsen. Daarbij kunnen parallelle klantreizen

plaatsvinden omdat een klant in een bepaalde stap een uitstapje maakt en daarbij (deels) een andere

klantreis doorloopt.

4.2 Patronen binnen de klantreis

Vanuit de klant gezien zijn binnen de klantreis de onderstaande, ondersteunende, patronen te

onderkennen voor Digitale Dienstverlening. Patronen die buiten de digitale dienstverlening vallen zijn niet

beschreven in deze doelarchitectuur. De technische vertaling van de hier beschreven dienstpatronen is te

vinden in de applicatiepatronen binnen de Applicatie Architectuur.

4.2.1 Inzien publieke informatie

Bij dit patroon wordt algemene informatie vanuit UWV aan een (potentiele klant) gepresenteerd. Waar de

klant specifiek vragen heeft, kan worden gezocht binnen de door UWV beschikbaar gestelde informatie,

maar er is geen sprake van een inhoudelijke dialoog over aan een specifieke persoon gerelateerde

informatie.

Binnen dit patroon gepresenteerde informatie zal veelal opgesteld zijn door (web-)redacteuren en

inhoudelijk deskundigen van UWV.

4.2.2 Publiek toegankelijke interactie met UWV

In een aantal situaties heeft de potentiele klant de mogelijkheid interactie te zoeken met UWV. De door

UWV gegeven antwoorden zijn echter altijd algemeen van aard en bevatten geen gegevens van

persoonlijke aard.

4.2.3 Inzien persoonlijke informatie

Dit patroon omvat het tonen van informatie die is gekoppeld aan een klant maar geen deel uit maakt van

een interactie tussen klant en UWV. Het kan daarbij gaan om zowel procesinformatie als om inhoudelijke

informatie. Een voorbeeld van procesinformatie is het tonen van inzicht in de stappen van een proces die

al zijn doorlopen en nog te nemen stappen. Inhoudelijk informatie kan bijvoorbeeld zijn het tonen van de

hoogte van een uitkering of aantal en duur van ziekmeldingen in een bepaalde periode.

Binnen dit patroon is wijzigen van bestaande informatie niet mogelijk.

De bron van deze informatie zijn de materiesystemen zoals

5.1 lid 2 sub i

4.2.4 Persoonlijke interactie met UWV

In dit patroon ligt de nadruk op interactieve communicatie en het wijzigen (c.q. voor het eerst opgeven)

van gegevens die bij UWV zijn (of worden) opgeslagen. Het gaat daarbij altijd om klantspecifieke

gegevens, al dan niet in relatie tot door UWV aangeboden diensten.

Voorbeelden van dit patroon zijn het aanvragen van een uitkering, het wijzigen van adresgegevens, de

werkverkenner en het invoeren van een CV en het (daaraan gekoppelde) zoeken en vinden van CV’s en

vacatures.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

23 van 117

4.2.5 Persoonlijke interactie met derden

Dit patroon geldt voor diensten die UWV inkoopt ten behoeve van haar klanten. De feitelijke inhoud van

de aan een klant geleverde dienst is niet altijd bekend bij UWV, maar de status (dienst gestart, cursus

afgerond, enz.) wordt door de externe dienstverlener doorgegeven aan UWV of kan door UWV

medewerkers rechtstreeks worden ingezien in de systemen van de aanbieder.

E-Coaching en E-Learning zijn voorbeelden van dit patroon.

4.3 Relatie klantreis en dienstpatronen

Elke stap in de klantreis maakt gebruik van een of meer dienstpatronen, afhankelijk van de dienst die de

klant afneemt van UWV. In de onderstaande figuur zijn de belangrijkste patronen bij de verschillende

stappen in de dienstreis weergegeven.

Figuur 7, relatie klantreis en dienstpatronen

Deze dienstpatronen sluiten aan op de applicatiepatronen die in de applicatiearchitectuur verder worden

uitgewerkt.

4.3.1 Verschijningvormen van de patronen

De beschreven patronen kennen verschillende uiterlijke vormen. Naast de verschijningsvorm als een

directe uiting van UWV, gelden deze patronen ook voor de White Label diensten die UWV via gemeenten

(en op termijn mogelijk ander partners) aanbiedt. De door UWV geboden klantreis verandert inhoudelijk

niet, maar verloopt wel via een ander kanaal dan het UWV-eigen kanaal. Eventueel kan een partij die een

UWV white label dienst aanbiedt er voor kiezen een eigen klantreis te definiëren waarbinnen de UWV

dienst wordt ingezet. Ook in dat geval blijft het patroon, vanuit UWV gezien, geldig.

4.4 Klantreis, klantprocessen en kanalen

Aansluitend op de klantreis en de dienstpatronen, onderkent UWV klantprocessen die lopen van

klantvraag tot antwoord aan de klant. Een generiek basismodel voor de klantprocessen van UWV is

opgenomen in Bijlage E, Voor de klant begint het klantproces met de E-Dienst start die hij start vanuit

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

24 van 117

het webportaal of een app. De E-Dienst wordt vervolgens verwerkt in een (zo veel mogelijk

geautomatiseerd) bedrijfsproces.

Figuur 8, basismodel toegang, diensten en processen

In deze doelarchitectuur wordt niet dieper ingegaan op deze invulling per specifiek klantproces. Deze

invulling wordt, waar relevant, opgenomen in PSA’s.

Communicatie vanuit de dienstverlening (kanaalkeuze)

UWV heeft als uitgangspunt dat we correct, volledig en transparant communiceren over de uitvoering van

taken aan de klant via communicatie uitingen in verschillende zones. Dit zijn

Zelfredzaamheid “zone”

•

Doel van deze zone is dat de klant zelfstandig zijn dienstverlening kan afnemen. De vraag wordt

zelfstandig beantwoord al dan niet ondersteund voor een geautomatiseerd ondersteunde

oplossing;

Assisted “zone”:

•

Doel van deze zone is dat de klant die gedrag vertoont waaruit (o.b.v. beslisregels) blijkt dat hij

ondersteuning nodig heeft, geassisteerd wordt. Daarmee wordt de klant geholpen om de in de

zelfredzaam zone verder te gaan zodat uitval voorkomen wordt;

Live/f2f zone:

•

Doel van deze zone is dat de klant die gedrag vertoont waaruit (o.b.v. beslisregels) blijkt dat hij

hulp nodig heeft, deze hulp krijgt in de vorm van ‘live services’, hetzij via persoonlijk, hetzij via

een videoverbinding. Daarmee wordt dienstverlening effectiever en efficiënter kan worden

aangeboden;

Oplos zone:

•

Doel van deze zone is het (voorkomen en) afhandelen van klachten en meldingen.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

25 van 117

De middelen (kanaalvarianten) die in deze zones worden voorzien zijn in onderstaande figuur

aangegeven.

Figuur 9, kanalen zone model

De digitale communicatievarianten hebben hierbij de voorkeur heeft omdat daarmee de zelfredzame

klant optimaal wordt gefaciliteerd.

Indien de klant niet in staat is het digitale kanaal te gebruiken, biedt UWV de keuze aan de klant om door

middel van opt-out kan aan te geven dat hij, incidenteel dan wel structureel, gebruik wil maken van het

traditionele, niet-digitale kanaal.

Communicatie tussen klant en UWV wordt veelal door de klant geïnitieerd. Een groot deel daarvan is het

opvragen van status informatie. Om vragen in het niet-digitale kanaal te verminderen wil UWV steeds

vaker door middel van notificaties de klant informeren over wijzigingen in de status van een bepaalde

dienst, gemaakte afspraken, herinneringsberichten of wijzigingen in de informatie. Daarmee neemt de

zelfredzaamheid van de klant toe.

NB: deze doelarchitectuur beperkt zich tot de digitala kanalen in de Zelfredzaam Zone. De overige zones

zijn onderdeel van de doelarchitectuur E-Werken en de themaarchitectuur KCC.

4.4.1 Kanaalvarianten

Binnen het digitale kanaal onderkent UWV, conform de digitale strategie van april 2017, verschillende

varianten:

• Websites/portalen (Browser);

Apps voor mobiele devices (App);

•

Social Media;

•

Systeemkoppelingen (API/A2A).

•

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

26 van 117

Deze varianten spelen een rol in verschillende delen van de klantreis zoals weergegeven in onderstaande

figuur13.

Figuur 10, positionering digitale kanalen in de klantreis

In dit model is de klantreis enigszins aangepast ten opzichte van de voorgaande paragrafen:

Awareness is de fase waarin (potentiële) klanten algemene informatie over UWV krijgen.

•

zonder dat er sprake is van concrete vragen die bij de klant leven. Dit laatste is in de regel wel

het geval tijdens de oriëntatiefase.

Continueren omvat de fasen ‘Dienst/Uitkeringen ontvangen’ en ‘Werk(nemer) zoeken’ en is in

•

dit model samengevoegd omdat het type activiteiten binnen deze fasen sterke overeenkomsten

vertonen waar het de digitale communicatie betreft.

diensten14.

Het webportaal is het digitale kanaal met de meest uitgebreide set Apps, social media en A2A

kanalen zijn aanvullend en bevatten een subset van de diensten die op het portaal beschikbaar zijn.

Slechts bij hoge uitzondering worden in deze kanalen diensten aangeboden die niet via het portaal

beschikbaar zijn. Het webportaal is beschikbaar voor zowel PC’s als voor mobiele devices. Daardoor is het

noodzakelijk de portalen zo in te richten dat de diensten en informatie met verschillende schermformaten

optimaal over komen (responsive design). Daarmee kan het echter nog steeds zo zijn, dat een dienst,

afhankelijke van het type mobiele apparaat, voor de gebruiker niet prettig functioneert. Dit kan bij

voorbeeld bijvoorbeeld het geval zijn als er veel informatie moet worden ingevoerd en de gebruiker werkt

via een browser op een smartphone.

4.4.2 Diensten en websites/portalen

Binnen de websites en portalen wordt de breedste set aan informatie diensten aangeboden door UWV.

Daarbinnen is een aantal clusters functionaliteiten te onderkennen zoals getoond in Figuur 11. De

13

Deze figuur zoomt in op het burgerperspectief en laat werkgevers en zakelijke klanten buiten beschouwing.

14

In de doelarchitectuur E-Dienstverlening wordt alleen het digitale kanaal behandeld. Niet-digitale kanalen vallen

buiten beschouwing.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

27 van 117

portalen van UWV zijn bereikbaar via werk.nl respectievelijk uwv.nl. Beide portalen bieden standaard

portaalfuncties waarin algemene informatie wordt een geboden en zoekmogelijkheden. Daarnaast bieden

de beide omgevingen ook meer specifieke informatie en diensten, gericht op bepaalde doelgroepen. Voor

werk.nl zijn dat:

Ondersteuning klanten met gemeentelijke uitkeringen op zoek naar werk;

•

Algemene burger (werkzoekende/werkgever) op zoek naar werk of werknemer (zonder

•

uitkeringsrelatie);

Ondersteuning werkzoekende met uitkeringsrelatie UWV op zoek naar werk;

•

Arbeidsmarkt op zoek naar arbeidsmarktinformatie (naast CV’s zijn dit trends, doelgroepen, et

•

cetera).

Uwv.nl biedt informatie en functionaliteit aan werknemer, werkgevers, leveranciers en ketenpartners op

het vlak van de diverse uitkeringen en gegevensdiensten.

Het onderstaande overzicht geeft een globaal beeld van de functionaliteiten binnen deze beide portalen.

De blokken boven de stippellijn tonen de onderdelen in de open omgevingen en de blokken onder de

stippellijn tonen de functionaliteiten die beschikbaar zijn voor een ingelogde klant.

Naast uwv.nl en werk.nl bestaan er diverse portalen voor bijvoorbeeld een specifieke doelgroep of thema.

Ook deze kennen zowel een open omgevingen als klantgerelateerde functionaliteiten.

Figuur 11, overzicht portalen en aangeboden functionaliteiten

Apps

Diensten die in eerste instantie in aanmerking komen om naast het webportaal ook in een app te worden

aangeboden, voldoen aan de volgende criteria:

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

28 van 117

De dienst heeft een repeterend karakter;

•

De dienst is kort cyclisch van karakter;

•

Levering via de app verhoogt het gebruikersgemak;

•

• Levering via de app verhoogt de gebruikersbeleving;

Authenticatie van de gebruiker en autorisatie voor toegang tot de dienst kunnen in een app op

•

het juiste niveau worden gerealiseerd.

Voorbeelden van functies die hier aan voldoen zijn:

App als aanvullend authenticatie mechanisme zodat een gebruiker zijn app kan gebruiken als een

•

token om op een portaal in te loggen met een hoog vertrouwensniveau;

• Doorgeven van inkomsten en ziek/beter meldingen;

Inzien van huidige situatie, persoonlijke gegevens, status van een aanvraag

•

Notificeren van de klant over taken, verplichtingen en herinneringen;

•

Contact informatie beschikbaar stellen.

•

• Vacatures of kandidaten zoeken

1 app, tenzij

beleid15.

UWV voert een ‘1 app, tenzij’ Daarmee wordt voorkomen dat er wildgroei ontstaat en het app-

landschap onbeheersbaar wordt. De ontwikkeling van een of meerdere sluit aan bij de UWV strategie en

de positionering van de E-Dienstverlening van Digitale Dienstverlening.

Bij de ontwikkeling van apps voor UWV moet de gebruikersbeleving consistent zijn voor alle apps en

portalen.

Social Media

Zoals uit het overzicht in Figuur 10 blijkt, worden social media alleen ingezet voor het verspreiden van

algemene informatie in de fasen Awareness en Oriëntatie. Via dit kanaal wordt, om privacyreden, geen

vertrouwelijke informatie met (potentiele) klanten uitgewisseld.

Daar waar mogelijkheden ontstaan om op een veilige wijze (met een geïdentificeerde en

geauthentiseerde gebruiker) te communiceren, worden deze nader onderzocht op bruikbaarheid voor

UWV en de mogelijkheden voor archivering en reconstructie van processen. Een voorbeeld van deze

ontwikkeling is de zakelijke acccounts binnen WhatsApp.

4.5 Ondersteunende processen

Bij de invulling van de hiervoor beschreven patronen en diensten wordt ook duidelijk dat er

ondersteunende processen zijn die noodzakelijk zijn om de klantreis te faciliteren over de verschillende

kanalen heen. Daarbij bestaat de wens de ondersteunende processen voor de digitale kanalen zo veel

mogelijk te integreren met de ondersteunende processen in de niet-digitale kanalen zodat bijv. een

integraal klantbeeld ontstaat op basis van over de klant bekende informatie uit alle mogelijke kanalen.

De nu onderkende processen ondersteunen de volgende aspecten van E-Dienstverlening:

15

Vastgesteld als onderdeel van het project IKO-App binnen Ketenstabilisatie.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

29 van 117

Klantondersteuning is een onderdeel van het domein E-Werken, maar heeft raakvlakken met

•

E-Dienstverlening. Middelen die hierbij ingezet worden zijn:

o

Co-browsing wordt ingezet om de KCC-medewerker direct mee te laten kijken met wat de

klant doet op het UWV portaal. De medewerker geeft de klant instructies en kijkt mee

met de resultaten;

o

Inkijk KCC MijnUWV is functionaliteit op MIJNUWV die voor de KCC-medewerkers

beschikbaar is ter ondersteuning van de afhandeling van een call door een klant;

o

Telefonie is het primaire medium voor de communicatie tussen de klant en de KCC-

medewerkers;

o

Chat wordt ingezet als alternatief voor en aanvulling op telefonie;

o

Berichten functionaliteit stelt de klant in staat vragen te stellen aan UWV. Eerstelijns

vragen worden afgehandeld door KCC, tweedelijns door de divisies;

o

FAQ en bijbehorende zoekfunctionaliteit wordt ingezet om eerder beantwoorde

klantvragen inzichtelijk te maken zodat klanten makkelijker zelf hun weg kunnen vinden

en minder vaak contact hoeven op te nemen met UWV (i.c. KCC);

segmentering16

Klantprofilering- en met als doel klanten zo veel mogelijk, en op het juiste

•

beveiligingsniveau, te voorzien van op de specifieke situatie toegespitste informatie en diensten;

o

Personalisatie en persoonlijk relevant maken zijn feitelijke resultaten van dit proces

waardoor de klant de informatie zo veel mogelijke op maat aangeboden krijgt in zowel

het portaal als in een app. Om dat mogelijk te maken moet de klant worden herkend op

basis van inloggegevens en, bij gebruik van een app, het gebonden middel (en daarmee

het geldende beveilgingsniveau). In eerste instantie zal dat betekenen dat de klant alleen

die diensten te zien krijgt die hij op dat moment afneemt van UWV (=persoonlijk relevant

maken). Hierbij wordt de klantreis per dienst als uitgangspunt genomen, waarbij niet

relevante diensten niet beschikbaar zijn. Overige diensten waar de klant gebruik van mag

maken blijven uiteraard toegankelijk voor de klant, maar worden minder prominent op

het scherm getoond. Daar waar de klant voor een dienst op een hoger beveiligingsniveau

moet inloggen, wordt dit ook zichtbaar gemaakt in het persoonlijk relevant gemaakte

portaal.

In volgende stappen krijgt de klant ook binnen de dienst steeds meer diensten en

informatie op maat aangeboden, bijvoorbeeld aan de hand van uitkeringsduur, positie op

de arbeidsmarkt of laatst uitgevoerde actie. Op termijn voorziet UWV dat de klant zijn

profiel deels zelf beheert. De informatie voor personalisatie is afkomstig uit zowel

transacties die binnen UWV zijn vastgelegd, als uit basisregistratie en gegevens over het

UWV-gerelateerde internetgedrag van de klant (bijv. klikgedrag);

o

Beheren klantcontactvoorkeuren heeft als doel het vastleggen van de kanaalvoorkeur en

de voorkeuren van de klant ten aanzien van berichten en notificaties.

De klant geeft hierbij aan via welke kanalen hij benaderd wenst te worden door UWV.

Standaard is dat het digitale kanaal, maar de klant kan er voor kiezen informatie van

16

Dit onderwerp wordt op onderdelen verder uitgewerkt in samenwerking met het KKO-project. Relevante resultaten

daaruit worden opgenomen in een volgende versie van deze doelarchitectuur/

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

30 van 117

UWV in de vorm van een papieren brief te krijgen (opt-out regeling). Daarnaast kan de

klant aangeven waarover hij geïnformeerd wil worden en via welk kanaal. UWV bepaalt

hierin de mate van keuzevrijheid zodat zeker kan worden gesteld dat noodzakelijke

berichten17

altijd aan de klant worden verstuurd. Vooral bij het gebruik van Mobiele Apps

moet de klant in staat zijn aan te geven over welke diensten hij wel en over welke hij

geen persoonlijke push notificaties wil ontvangen op zijn mobiele device. Dit moet ook

instelbaar zijn via de App;

Analyse en optimalisatie klantcommunicatie en –gedrag met als doel om op basis van

•

analyses van klantcontacten en klikgedrag de communicatie te verbeteren en daarmee de

klantwaardering te vergroten. Hierbij worden, onder andere, de volgende middelen ingezet:

o

Webanalyse waarbij het gedrag van de klant op de portalen wordt geanalyseerd zodat

een optimaal pad kan worden bepaald;

o

Data analyses ondersteunen de webanalyses;

o

Directe feedback biedt de klant de mogelijkheid aan te geven hoe hij de website van UWV

ervaart;

o

A/B Testen is een mechanisme waarbij de gebruikerservaring van twee interfaces met

elkaar wordt vergeleken zodat een gefundeerde keuze kan worden gemaakt om een

bepaald systeem wel of niet in productie te nemen;

• Redactie- en distributie (web-)content met als doel het ontwikkelen en beschikbaar stellen

van (web-)content die door (aanstaande) klanten zelfstandig wordt benaderd;

Identificatie en autorisatie van klanten met als doel de identiteit en daaraan gekoppelde

•

gegevens te beschermen tegen misbruik;

Device binding van mobiele apparaten is een volledig geautomatiseerd ondersteunend proces

•

met als doel het gebruiksgemak van apps te vergroten en de mogelijkheid persoonlijke push

notificaties op een zo veilig mogelijk wijze te realiseren.

4.6 Gegevensarchitectuur

UWV maakt gebruik van het bedrijfsobjectmodel (BOM) en het Corporate Gegevensmodel (CGM) als

hulpmiddel voor het communiceren en afstemmen van veranderingen in de gegevensbehoefte. Het

voorkomt daarmee communicatiestoornis en onduidelijkheden. De gegevens die worden verwerkt binnen

E-Dienstverlening zijn primair de gegevens die worden verwerkt in de E-Diensten zoals die aan de

klanten worden aangeboden. Daarnaast zijn er nog de gegevens die gebruikt worden in de

ondersteunende processen zoals deze binnen de Internet Organisatie van UWV (IOU) en divisies worden

uitgevoerd.

Het domeinobjectmodel voor K&S en E-Dienstverlening is een verfijning van het bedrijfsobjectmodel en

nog in ontwikkeling. In een volgende versie wordt het E-Dienstverlening specifieke deel van dit model

worden opgenomen.

4.7 Informatiebeveiliging en privacy

Klanten van UWV moeten er op kunnen vertrouwen dat informatie die zij aan UWV geven zorgvuldig

wordt behandeld en dat informatie die zij opvragen tijdig en betrouwbaar beschikbaar is. Tegelijkertijd

17

Onder noodzakelijk berichten vallen bijv. berichten met een wettelijke grondslag.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

31 van 117

moet UWV kunnen vertrouwen op de authenticiteit van de klant en daarmee op de juistheid van de

aangeleverde gegevens. Om dit te borgen, sluit UWV zo veel mogelijk aan bij de overheidsrichtlijnen

## BIR18 AVG19

en zodra deze in werking treedt. Waar voldoen aan de richtlijnen (nog) niet mogelijk is,

wordt de afwijking gemotiveerd (comply or explain).

Conform de AVG is UWV verplicht aan haar klanten aan te geven welke gegevens voor welk doel zijn

geregistreerd. UWV-breed zijn twee werkgroepen actief om dit verder uit te werken. De voor deze

doelarchitectuur relevante resultaten van deze werkgroepen zullen worden uitgewerkt in een volgende

versie van deze Doelarchitectuur.

Verdere uitwerking van Identity en Access Management (I&AM) is opgenomen bij de beschrijving van het

Architectuur BouwBlok (ABB) I&AM in paragraaf 5.2.6. Hierin worden functies met betrekking tot

identificatie (is dit de persoon de hij aangeeft te zijn) en autorisatie (wat mag deze persoon in welke

systeem c.q. voor welke dienst) beschreven. Personalisatie (het toespitsen van informatie en diensten op

een specifieke persoon) maakt deels gebruik van identificerende gegevens, maar is een ondersteunend

proces en geen onderdeel van I&AM.

Het eerder genoemde proces “Device binding” is een middel om de identiteit van de houder van een

mobiel device vast te stellen. Het apparaat inclusief de daarop geïnstalleerde en gebonden app werkt

hierbij als een Multi Factor Authenticatie (MFA) device.

4.7.1 Vertrouwelijkheid

Klanten van UWV hebben toegang tot gegevens uit verschillende vertrouwelijkheidsklassen.

Conform binnen UWV geldende richtlijnen worden gegevens en diensten op het laagst mogelijke niveau

geclassificeerd. Klanten die zijn ingelogd hebben toegang tot gegevens van de klasse die past bij het

gekozen niveau van authenticatie en de lager geclassificeerde gegevens.

Een klant krijgt altijd de mogelijkheid op het hoogst mogelijke niveau in te loggen. Als hij er voor kiest op

een lager niveau in te loggen, betekent dit alsnog step-up authenticatie als een hoger niveau nodig blijkt.

De klant wordt hierover geïnformeerd zodra hij gegevens aanlevert en benadert in een klasse waarvoor

het laagste niveau van authenticatie niet meer volstaat. Als een klant tijdens een sessie opnieuw moet

inloggen, kan hij daarna direct verder gaan met activiteiten waar hij al mee bezig was.

Een voorbeeld hierbij is als volgt: Indien een klant is ingelogd op het niveau waarop hij een wijziging in

zijn arbeidssituatie mag doorgeven, kan hij niet zijn medische gegevens inzien zonder opnieuw – en op

een hoger beveiligingsniveau – in te loggen. Als hij direct inlogt op het niveau waarop hij zijn medische

gegevens mag inzien en eventueel aanvullen, kan hij ook wijzigingen in zijn arbeidssituatie doorgegeven.

Voor toegang vanaf mobiele apparaten geldt, dat de gebonden app de sterkte erft van het middel (DigiD,

IDIN, etc.) waarmee device binding is gerealiseerd. Een app die binnen DigiD alleen via gebruikersnaam

en wachtwoord is gekoppeld is daarmee niet geschikt voor het verwerken van medische gegevens. Pas

als aanvullende SMS verificatie is gebruikt bij het binding proces, wordt een hoger niveau vrijgegeven in

de app.

## (WGDI)20.

De toegangsbeveiliging sluit aan bij de Wet Generieke Digitale Infrastructuur

18

Baseline Informatiebeveiliging Rijksdienst

19

De Algemene Verordening Gegevensbescherming is op 26 mei 2016 in werking getreden. De lidstaten hebben tot 1

mei 2018 de tijd om hieraan te voldoen.

20

https://www.digitaleoverheid.nl/beleid/digitalisering-aanbod/inhoud/

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

32 van 117

Vertrouwelijkheid en kanalen

Bij vertrouwelijkheid gelden specifieke aandachtspunten voor de verschillende kanalen.

Websites/portalen

Iedereen die beschikt over een webbrowser en internettoegang kan de algemene informatie op de

websites van UWV benaderen. Voor zaken waarbij vertrouwelijke informatie wordt uitgewisseld

(aanvragen uitkering, betermelding, ontslagaanvraag, RDH-berekening, etc.) is het noodzakelijk in te

loggen.

Apps

Bij gebruik van apps voor het opvragen van vertrouwelijke informatie of persoonlijke interactie wil UWV

dat duidelijk is welke natuurlijk persoon eigenaar is van het device waarop de app draait.

Om dit te bereiken wordt het apparaat aan de gebruiker gekoppeld in een proces waarbij de gebruiker

gegevens invoert in zowel de app als in het portaal. Via inloggen op het portaal wordt de identiteit van de

vastgesteld21.

gebruiker

Na het voltooien van dit ‘binding proces’ is de combinatie van gebruiker, app en apparaat bekend bij UWV

en kan worden volstaan met het identificeren van de gebruiker via een wachtwoord, pincode of

vingerafdruk in de app. Daarbij moeten wachtwoord of pincode aan minimumeisen voldoen die aansluiten

bij het geldende beveiligingsbeleid van UWV. Hierbij hoort onder andere het aantal keren dat een

foutieve code mag worden ingevoerd voordat de app wordt geblokkeerd.

Social Media

Voor het kanaal ‘Social Media’ geldt altijd dat UWV dit kanaal uitsluitend gebruikt voor het delen van

algemene informatie.

## API/A2A

[ De aspecten specifiek voor de vertrouwelijkheid op dit kanaal moeten nog worden uitgewerkt. ]

4.7.2 Integriteit

UWV borgt dat aan haar toevertrouwde gegevens juist, tijdig beschikbaar en veilig zijn en dus niet

ongemerkt kunnen veranderen.

Daar waar gegevens worden aangepast, wordt de aanpassing vastgelegd in een audit trail zodat, indien

gewenst, achteraf kan worden vastgesteld of een wijziging rechtmatig heeft plaatsgevonden.

4.7.3 Beschikbaarheid

Klanten van UWV verwachten zo uitgebreid mogelijke toegang tot informatie over UWV en de voor hen

relevante gegevens. Voor de digitale dienstverlening betekent dit, dat informatie 7 dagen per week, 24

uur per dag beschikbaar moet zijn. Indien gegevens zijn aangepast, is dit zo snel mogelijk (uiterlijk

binnen 24 uur) zichtbaar voor de klant. Deze zichtbaarheid geldt voor alle kanalen en niet alleen voor het

kanaal waarlangs de wijziging is aangebracht.

21

Zie voor verdere uitleg paragraaf 5.3.9, Patroon voor

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

33 van 117

5 Applicatie Architectuur

De applicatie architectuur van E-Dienstverlening omvat het geheel van applicaties dat nodig is om de

diensten van UWV digitaal aan haar klanten aan te bieden. Deze applicatiearchitectuur sluit aan op de

applicatiearchitecturen van

Doelarchitectuur E-Werken;

•

Doelarchitectuur GEIN;

•

• Architectuur Klant Contact Center;

Architectuur Marketing Automatisering (K&S).

•

Daar waar sprake is van overlappende applicaties wordt de overlap benoemd in alle betrokken

architectuurbeschrijvingen.

Een belangrijke pijler in deze applicatiearchitectuur is het referentiemodel voor Klant Interactie en Kanaal

Ondersteuning lagen (KI/KO model) met daarbinnen de Klant-Interactie-Applicaties resp. de Kanaal-

Ondersteunende-Applicaties. Daarnaast zijn er diverse Architectuur BouwBlokken (ABB’s) die samen met

de KIA’s en KOA’s uit het KI/KO model de verschillende applicatiepatronen vormen. Voor de ABB’s wordt

aangegeven met welke Software BouwBlokken (SBB’s) deze worden gerealiseerd.

Deze onderdelen van de applicatiearchitectuur vormen een startpunt voor de PSA waarin voor elk project

wordt aangegeven welke patronen worden gebruikt en hoe de richtlijnen en eisen worden

geïmplementeerd.

5.1 KIA/KOA referentiemodel

Het KIA/KOA model is de basis van de Applicatie Architectuur binnen de doelarchitectuur E-Dienstver-

lening en is het referentiemodel voor Digitale Dienstverlening. Daarmee vormt het model de basis voor

applicatielandschap22.

de inrichting van het

Het startpunt voor het model is de klant van UWV. Deze moet in staat zijn diensten van UWV via

meerdere(digitale) kanalen af te nemen. De klantinteractie wordt zodanig vormgegeven, dat deze is

toegespitst op de specifieke eigenschappen van een kanaal. Deze interacties worden, vanuit de laag

kanaalondersteuning, ondersteund door applicatiecomponenten waarin informatie beschikbaar is die

binnen de verschillende kanaalinteracties wordt gebruikt. Deze ondersteuningslaag maakt het mogelijk

de dienstverlening aan de klant vanuit verschillende kanalen op elkaar aan te laten sluiten. De applicaties

in deze laag worden ‘gevoed’ vanuit de Bron- en Materiesystemen waarin de klantgegevens zijn

vastgelegd. Daar waar relevant wordt informatie via de Div Regie Laag (DRL) uitgewisseld zodat

gegevens en documenten automatisch worden gearchiveerd conform eisen van DIV. In al deze lagen

gelden diverse aspecten van IB&P. Daarmee ontstaat het in Figuur 12 getoonde model wat verder in dit

document Klant Interactie / Kanaal Ondersteuning (KI/KO) concept genoemd wordt.

22

Het KIA/KOA model wordt inmiddels ook besproken als een model voor medewerkersapplicaties. Hoewel het model

op zich daarvoor toepasbaar zou kunnen zijn, vallen medewerkers applicaties buiten de scope van deze

Doelarchitectuur. Deze toepassing van het KIA/KOA model valt daarme buiten de scope van E-Dienstverlening.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

34 van 117

Figuur 12, basislagen in KIA/KOA concept

Dit referentiemodel is ontstaan na werkbezoeken aan de Rabobank en SVB, die beiden een soortelijk

model gebruiken. Het is een beproefd concept dat aansluit bij structuren zoals de Nederlandse Overheid

## (NORA)23

Referentie Architectuur die voorstelt. Vergelijkbare modellen worden gebruikt bij organisaties

als Delta Lloyd, PostNL en DUO. Het KI/KO model geeft invulling aan de voor de applicatiearchitectuur

belangrijkste architectuurprincipes (zie hoofdstuk 3):

Stabiliteit en continuïteit,

•

Wendbaarheid,

•

Modulaire opbouw,

•

• Ontkoppelen.

5.1.1 Klant Interactie laag (Kanaal)

In het contact met de klant is de combinatie van het digitale kanaal met andere kanalen gewenst.

Belangrijk hierbij is dat kanalen op elkaar zijn afgestemd en dat gedrag van klanten gemonitord kan

worden in relatie tot de effectieve inzet van diensten. Dit effectief inzetten van de diensten gebeurt op

basis van klantprofielen. Ten behoeve van de navigatie binnen de online-kanalen, worden deze profielen

door de afdeling Klantexpertise binnen K&S gecreëerd. Binnen deze doelarchitectuur worden de

uitgewerkt24.

onderstaande digitale kanalen

Web: UWV is aanwezig in de digitale wereld voor burgers en bedrijven die een sociale

•

zekerheidsrelatie hebben. Deze aanwezigheid is te zien in meerdere digitale omgevingen zoals uwv.nl

waar informatie en ondersteuning beschikbaar is vanuit de kerntaken van UWV op het gebied van

Uitkeren, Werk, Sociaal Medische Beoordeling, Gegevensdiensten en ondersteunende diensten.

Daarnaast is er werk.nl waar de werkzoekende ondersteund wordt bij het vinden van werk en de

werkgever bij het vinden van personeel. De bestaande E-Diensten worden opnieuw gepositioneerd

binnen deze portalen, zodat de dienstverlening daar is waar de klant die verwacht. De komende jaren

neemt het aantal E-Diensten en het aantal gebruikers van de digitale diensten verder toe. Deze

volumegroei maakt het noodzakelijk de huidige problemen m.b.t. stabiliteit en continuïteit snel aan te

23

www.noraonline.nl

24

NB: in de applicatiearchitectuur van E-Dienstverlening wordt het kanaal Social Media niet verder uitgewerkt omdat

hierin geen diensten worden aangeboden die aansluiten op het primaire proces van UWV.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

35 van 117

pakken.

Naast de twee genoemde portalen zijn er nog enkele portalen voor kleinere doelgroepen.

App: Het gebruik van mobiele apparatuur voor communicatie neemt verder toe, ook bij de klanten

•

van UWV. Dit betekent dat de behoefte voor het gebruik van digitale diensten verschuift van de

portalen naar mobiele apparatuur (tablet/smartphone, al dan niet via apps).

A2A – Applicatie-naar-Applicatie: Voor het zakelijk gebruik zien wij een verschuiving van

•

werkgevers- en zakelijk portaal naar applicatie-naar-applicatie (A2A) koppelingen. Daarnaast worden

voornamelijk voor gemeenten de zogenaamde White Label diensten ontwikkeld.

5.1.2 Klant Interactie laag (applicaties)

De KI laag bevat de functionaliteit die de interactie tussen de klant en UWV ondersteunt. Deze laag is

georganiseerd per kanaal omdat kanalen specifieke kenmerken hebben. Functionaliteit in deze laag is

samengebracht in de Klant Interactie Applicaties (KIA’s).

De belangrijkste richtlijnen met betrekking tot functionele inrichting van KIA’s zijn:

1. KIA’s zijn ontworpen vanuit klantbehoefte;

Een KIA is gericht op de daadwerkelijke interactie zoals beschreven in de patronen binnen de

klantreis: ‘Publiek toegankelijke interactie met UWV’ en ‘Persoonlijke interactie met UWV’. Er is een

duidelijk verschil tussen portaalfuncties en KIA’s in termen van bijvoorbeeld belasting en maatregelen

die genomen dienen te worden om de non-functionals in te vullen voor een gehele keten. Een in het

oog springend verschil is bijvoorbeeld dat een KIA voor de response aan de klant afhankelijk is van

onderliggende lagen terwijl een portaalfunctie in veel gevallen eenmalig wordt opgehaald en getoond.

Ieder kanaal (internet, mobiele devices, A2A koppelingen) kent zijn eigen technologie en de

oplossingen om binnen een specifiek kanaal te communiceren zijn dusdanig verschillende van elkaar

dat de KIA’s specifiek voor een kanaal ontwikkeld worden.

2. De scope van een KIA wordt gebaseerd op een eenheid van tijd, plaats en handeling;

Hiermee wordt de granulariteit van een KIA bepaald. Het doel is hierbij de onderdelen van een

interactie die echt bij elkaar horen zoveel mogelijk te bundelen en tegelijkertijd onderdelen die niet

per se gekoppeld dienen te zijn ook los te koppelen. Hiermee krijgen de KIA’s een omvang die

aansluit bij de menselijke maat en daarmee wordt het principe van modulaire opbouw ondersteund.

3. KIA’s communiceren niet met andere KIA’s en zijn onafhankelijk van elkaar;

De scope van een KIA wordt op dusdanige wijze gekozen dat de KIA niet met andere KIA’s hoeft te

communiceren. Deze richtlijn zorgt ervoor dat KIA’s maximaal ontkoppeld zijn, wat invulling geeft

aan de principes van wendbaarheid en stabiliteit.

Daar waar een klantinteractie via meerdere kanalen kan verlopen en de klant –opeenvolgend-

verschillende kanalen kan gebruiken wordt relevante data opgeslagen in de betrokken KOA(‘s).

4. KIA’s slaan geen gegevens permanent op;

Hierdoor wordt ervoor gezorgd dat gegevens niet gerelateerd zijn aan één kanaal maar dat in de KIA

afgehandelde gegevens ook beschikbaar zijn binnen andere kanalen. Daarmee ervaart de klant een

uniforme klantreis over de kanalen heen en wordt het uiteindelijk mogelijk dat een klant een

interactie in één kanaal begint en in een ander kanaal afrondt.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

36 van 117

Tijdens een interactiesessie kan een KIA gegevens cachen. Na afloop van een sessie worden deze

gegevens verwijderd.

5. KIA’s bevatten presentatie- / interactielogica en geen bedrijfslogica;

Onder interactielogica wordt o.a. verstaan het aanbieden van juiste invoervelden en het verzorgen

van formattering en eenvoudige validaties van ingevoerde gegevens. Hiermee ontstaat een duidelijke

scheiding tussen een presentatie-laag en functie die alleen presentatie verzorgt en een laag/functie

die bedrijfslogica verzorgt. Deze modulaire opbouw ondersteunt ontkoppeling en komt ten goede aan

zowel wendbaarheid als stabiliteit en continuïteit.

De bedrijfslogica die nodig is binnen een klantinteractie wordt geleverd door een of meerdere KOA’s.

6. Een unieke gebruiker heeft tegelijkertijd toegang tot één KIA;

Een gebruiker kan in principe slechts één zinvolle interactie tegelijkertijd aan. Binnen de portalen kan

deze interactie wel ondersteund worden door portaalfuncties die samen met een KIA aangeboden

worden.

bedrijfsobject25

7. KIA’s muteren (via een KOA)slechts één (samengesteld) direct en hebben geen

orkestratie functie;

Deze richtlijn zorgt er voor dat er geen orkestratiefuncties hoeven te worden gedupliceerd over KIA’s

voor verschillende kanalen. Het gevolg hiervan is, dat de bedrijfslogica die nodig is binnen een

klantinteractie in de andere lagen (KOA en bron/materiesystemen) wordt gerealiseerd.

Een KIA kan weliswaar meerdere KOA’s raadplegen, maar een mutatie blijft beperkt tot één KOA. Die

KOA kan wel een samengesteld object bevatten waardoor op de achtergrond meerdere KOA’s

betrokken zijn bij die ene verwerking.

8. Het gedrag en de toestand van KIA’s kan door autorisatie en personalisatie beïnvloed worden;

De daarvoor benodigde informatie wordt geleverd vanuit generieke KOA’s of door portaalfuncties

vanuit het platform waarbinnen de KIA ‘leeft’. Hierdoor kan een KIA zich in zijn specifieke kanaal

anders tonen en gedragen dan een KIA in andere kanalen die onderdeel is van dezelfde dienst. Dit

geeft ook weer een modulaire opbouw omdat zaken als autorisatie en personalisatie als losse

herbruikbare bouwstenen worden gerealiseerd. Overigens kan het ook zo zijn dat afhankelijk van het

kanaal andere informatie voor personalisatie een rol speelt. Denk hierbij aan een mobiele app die de

locatie vanuit het mobiele device gebruikt terwijl een portaal alleen informatie vanuit KOA's geleverd

krijgt.

Eisen KIA

Een KIA bestaat uit twee onderdelen. Een component die fysiek op het apparaat van de klant actief is,

bijvoorbeeld JavaScript of een App. Dit noemen we KIA Client Side (KIAcs). De tweede component is

actief op de infrastructuur van UWV. Dit is typisch een webservice die onder andere verantwoordelijk is

voor de ‘fine-grained’ access control (autorisatie) en, indien nodig, het verzamelen van informatie vanuit

verschillende bedrijfsobjecten. Dit noemen de KIA Server Side (KIAss).

De KIAcs communiceert uitsluitend met de KIAss. Die communicatie vindt plaats via REST/JSON. KIAcs

25

De bedrijfsobjecten zijn gedefinieerd in het bedrijfs object model (BOM). Dit is een kernobjectmodel in combinatie

met een aantal domein object modellen (DOM).

Binnen een klantinteractie kunnen bedrijfsobjecten nodig zijn die een samenvoeging zijn van meerdere objecten uit

het DOM/BOM. Via De KOA wordt die combinatie als één samengesteld object aan de KIA aangeboden.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

37 van 117

en KIAss zijn ontkoppeld en beveiligd via een Secure Reverse Proxy in combinatie met I&AM. , zie

onderstaande figuur. De KIAss communiceert vervolgens met de achterliggende KOA(‘s).

Figuur 13, Samenhang KIAcs en KIAss

## KIA26

Een is ontworpen om bij het niet beschikbaar zijn van een KOA de dienstverlening met een correcte

foutmelding aan de gebruiker te beëindigen zonder dat dit andere dienstverlening in de weg zit

(bijvoorbeeld doordat er een zwaar beslag op resource wordt gedaan zoals het onnodig lang vasthouden

van IP connecties). Hiervoor wordt de KIA op basis van de volgende maatregelen van de KOA’s

ontkoppelt:

Bij het opvragen, dit vindt in principe altijd plaats op basis van synchrone communicatie, wordt

•

het circuit breaker pattern toegepast, zie (1) in onderstaande figuur. Dit principe is nader

uitgewerkt in de PSA FailSafe (2017);

• Bij muteren wordt rekening gehouden met het principe ‘Design for Failure’. Dit betekent dat een

mutatie bij uitval van de functie niet verloren gaat. Hiermee kan worden volstaan met een

ontvangstmelding aan de klant, waarbij UWV de verantwoordelijkheid voor de uitvoering kan

nemen.

Een mogelijke implementatie hiervan is het Store-And-Forward (SAF) patroon zoals geleverd door

MQ. Dit heet asynchrone koppelingen met persistentie. Zie (2) in onderstaande figuur;

Indien voor de klantinteractie noodzakelijk (bijvoorbeeld indien synchrone validatie door de KOA

•

uitgevoerd dient te worden) kan er gekozen worden om een mutatie synchroon uit te voeren. Bij

synchrone mutaties wordt eveneens het circuit breaker pattern toegepast;

KIA’s communiceren met KOA(‘s) via standaard protocollen;

•

Binnen E-Dienstverlening worden hoofdzakelijk de protocollen REST en SOAP gebruikt. Welk

protocol in een specifieke situatie wordt toegepast, wordt bepaald in overleg tussen de betrokken

26

Een KIA bestaat altijd uit de combinatie van een KIAcs en een KIAss. In het vervolg van dit document wordt dee

combinatie bedoeld als er gesproken wordt over een KIA. Slechts indien dat relevant is voor het begrip van de

doelarchitectuur, worden KIAcs en KIAss afzonderlijk benoemd.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

38 van 117

divisies.

Andere protocollen dan REST en SOAP zullen op termijn verdwijnen als gevolg van vernieuwing

en standaardisatie;

• Een KIA maakt gebruik van dezelfde beveiligingsartefacten als het portaal (bijvoorbeeld SAML-

tokens). Bij het aanroepen van de KOA geeft de KIA die informatie mee die de KOA in staat stelt

volgens de eigen regels de beveiliging handhaven, bijvoorbeeld door uitsluitend informatie van

één BSN en daaraan gekoppelde machtigingen terug te geven aan de KIA;

manager27.

Ontkoppeling wordt gerealiseerd met behulp van een interface

•

5.1 lid 2 sub i

5.1 lid 2 sub i

Figuur 14, ontkoppelmaatregelen tussen KIA en KOA

5.1.3 Kanaal Ondersteuning laag

De KO laag bevat de functionaliteit die gedeeld wordt door de verschillende kanalen, maar geen productie

functie van een bron- of materiesysteem is. Deze laag ontkoppelt de interactie met de klant functioneel

van de Bron- en Materiesystemen en is kanaalonafhankelijk.

De KO laag bevat Kanaal Ondersteuning Applicaties (KOA’s). Deze KOA’s worden aangeroepen door een

KIA op het moment dat een klant een bepaalde interactie start. Dit omvat zowel het opvragen als het

toevoegen en aanpassen van gegevens in het achterland van UWV. De KOA’s die gekoppeld zijn aan

bron- en materiesystemen, stellen gegevens uit deze systemen beschikbaar aan de KIA’s. Naast de KOA’s

die gekoppeld zijn aan de bron- en materiesystemen, zijn er ook KOA’s die functionaliteit bieden waar

geen bron- of materiesysteem aan gekoppeld is. Dit zijn vooral de KOA’s die de klantreis faciliteren (zoals

bijv. de status van een klant in zijn klantreis). Daarmee wordt bijvoorbeeld een functionele ontkoppeling

gerealiseerd zodat status informatie voor een klant 24 uur per dag beschikbaar kan zijn terwijl de

bronsystemen dat niet hoeven te zijn.

27

Naar verwachting vindt in 2017 een aanbesteding plaats voor deze interfacemanager (API Gateway).

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

39 van 117

Daarnaast zijn er nog generieke KOA’s voorzien die faciliteiten bieden die niet gerelateerd zijn aan een

specifieke stap in de klantreis of een specifieke interactie, maar op meerdere plaatsen nodig zijn.

KOA’s28

De belangrijkste richtlijnen voor zijn:

1. KOA’s hebben geen interactie met gebruikers en bevatten dus geen klantinteractielogica;

2. KOA’s kunnen meerdere kanalen ondersteunen en daarmee één of meer KIA(s) en faciliteren

daarmee een uniforme klantreis over kanalen heen;

Waar een KIA de presentatiefunctie voor de klantreis specifiek voor een kanaal invult levert de KOA

de ondersteunende bedrijfslogica als een separate functie. Deze functie werkt voor alle kanalen

hetzelfde. De functionaliteit en de klantreis wordt daarmee uniform over kanalen heen. Een

samengestelde set van specifieke en generieke KOA biedt ondersteuning aan een dienst, een fase

van een dienst of een dienstverlening als onderdeel van de klantreis. Een KOA wordt ontworpen voor

klantinteractie. Indien een KOA geen klantinteractie ondersteunt, heeft de KOA geen bestaansrecht.

3. KOA’s leveren één (samengesteld)bedrijfsobject aan een KIA;

Daarmee heeft een KOA kennis (bedrijfslogica) nodig voor het samenstellen van objecten. Een

enkelvoudig bedrijfsobject is een bedrijfsobject zoals gedefinieerd in Bedrijfs- en Domein Object

Model. Let op dat de bedrijfsobjecten ontstaan vanuit de gewenste klantinteractie en dienen

betekenis te hebben voor de klant. KOA’s worden hiermee modulaire bouwblokken die invulling geven

aan de eisen van wendbaarheid, stabiliteit en continuïteit.

4. KOA’s zijn ontworpen vanuit de generieke klant- / interactiebehoefte over kanalen heen;

Een KOA kent derhalve één KIA gerelateerd interfacecontract dat beschikbaar is voor alle kanalen. Dit

contract wordt gebaseerd op het kanaal met de meest uitgebreide klantinteractie, meestal het

portaal. De KIA is vervolgens verantwoordelijk om de gegevens en functionaliteit die de KOA levert

specifiek voor het kanaal te presenteren.

5. KOA’s controleren mutaties op compleetheid en correctheid van de aangeboden gegevens en

bevestigen de verdere verwerking door UWV aan de KIA.

6. KOA’s wisselen mogelijk gegevens uit met andere KOA’s (opvragingen zowel als mutaties); ·

Waar een KOA mutaties communiceert met een andere KOA betreft dit alleen de mutaties van

zichzelf (c.q. de aan deze KOA gerelateerde bronsystemen) en niet over mutaties die het via andere

KOA’s laat uitvoeren.

Bij uitwisseling van gegevens tussen KOA’s moet altijd worden gekeken in hoeverre die uitwisseling

via KOA’s moet of dat het via bron- en materiesystemen moet lopen.

7. KOA’s communiceren onderling asynchroon;

De communicatie vanuit het vorige punt gebeurt zoveel mogelijk asynchroon volgens de patronen

van “event driven architecture”. Meer over “event driven architecture” volgt bij de implementatie

instructies.

8. KOA’s communiceren met één of meerdere systemen uit het achterland en/of externe systemen;

Een KOA is verantwoordelijk voor het laten verwerken van wijzigingen in de bron- en

materiesystemen (en eventuele externe systemen). Een KOA kan (meerdere) bron- en

28

E-Dienstverlening is verantwoordelijk het aanroepen van de KOA-interface en de performance die in deze oproep

moet worden gerealiseerd. De wijze waarop dit wordt gerealiseerd in de KOA en de daarachterliggende systemen valt

buiten de verantwoordelijkheid van E-Dienstverlening.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

40 van 117

materiesystemen enscapsuleren en ontkoppelt hiermee een KIA functioneel van bron- en

materiesystemen. Hierdoor is het niet altijd nodig bij gewenste functionele wijzigingen ook de KIA’s

aan te passen wanneer een bron- of materiesysteem wijzigt. Dit is bijvoorbeeld wel het geval bij

wetswijzigingen waardoor nieuwe gegevens moeten worden aangeleverd door de klant.

Een KOA is bij verwerking van een mutatie die archiefwaardig is zelf verantwoordelijk voor de

aanbieding van de mutatie in het bijbehorende bron- en materiesysteem en het aanroepen van de

DivRegieLaag (DRL) voor het archiveren en indien nodig het aanmaken van een zaak in Zomer.

9. Een KOA omvat mogelijk eigen gegevensopslag;

In principe geldt dit alleen voor gegevens die alleen voor E-Dienstverlening van toepassing zijn zoals

een klantprofielservice die aangeeft welke diensten aan een klant getoond moeten worden. Het is bij

eigen gegevensopslag in een KOA belangrijk om onderscheid te maken in gegevens die alleen door

de klant vanuit E-Dienstverlening gewijzigd worden en gegevens welke vanuit bron- en

materiesystemen gewijzigd worden.

10. Een KOA is het startpunt voor archivering;

Waar sprake is van verwerking van archiefwaardige gegevens, is het de verantwoordelijkheid van de

KOA en/of bron- en materiesystemen om deze gegevens te archiveren, al dan niet door deze via de

DIV Regie Laag aan te bieden aan het Elektronisch Archief.

11. Een KOA communiceert via standaard protocollen;

De KOA’s ten behoeve van E-Dienstverlening communiceren met de KIA’s op basis van de

## UWV29

Berichtenstandaard en maken daarbij gebruik van REST/JSON of SOAP/XML. Waar nog andere

bestaande communicatieprotocollen in gebruik zijn, worden deze op termijn vervangen. Welke

protocollen worden gebruikt voor de communicatie met de bron- en materiesystemen, wordt door de

eigenaar bepaald;

12. KOA’s geven alleen gegevens door aan een KIA waarvoor zowel de KIA als de gebruiker

geautoriseerd zijn;

Vanuit het oogpunt van vertrouwelijkheid mogen burgers alleen die gegevens opvragen die horen bij

hun identificerend kenmerk, of bij de identificerende kenmerken waarvoor zij gemachtigd zijn.

Bedrijfsmatige gebruikers kunnen alleen die gegevens opvragen waarvoor het bedrijf en de gebruiker

geautoriseerd zijn. Verder wordt ondersteund dat KIA’s in bepaalde gevallen niet alle gegevens

behorende bij een gebruiker mogen doorgeven, dit is een autorisatie op basis van de KIA en dit kan

zijn30.

ook autorisatie op basis van kanaal Het niveau waarop de betreffende gebruiker is

geauthentiseerd bepaalt welke gegevensklassen toegankelijk zijn voor deze gebruiker tijdens deze

sessie.

13. KOA’s ondersteunen outside-in release cycle;

Dat houdt in dat KOA’s de snelheid van wijzigingen volgen zoals die gewenst is vanuit de

klantinteractie. Door de modulaire opbouw en de losse koppeling tussen KIA’s en KOA’s wordt de

wendbaarheid van de oplossing vergroot. Hierdoor wordt het mogelijk verschillende release-

snelheden te volgen. In principe geldt de stelregel dat hoe dichter bij de klant (KIA, dan KOA, dan

bron- en materiesystemen) hoe vaker gereleased moet kunnen worden.

29

Zie: http://uwvdigitaal.info.uwv.nl/Applicatie/UGD/GM/Producten%20en%20kaders/

Berichtstandaard%20UWV%20versie%203.1.pdf

30

Hier is feitelijk sprake van een aanvulling op I&AM die op dit moment nog niet beschikbaar is.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

41 van 117

Eisen KOA

Er worden eisen op de volgende onderwerpen aan een KOA gesteld:

Beschikbaarheid

Om stabiele digitale dienstverlening te ondersteunen dient een KOA 7 x 24 beschikbaar te zijn. De

beschikbaarheid dient ook gegarandeerd te zijn bij uitval of onderhoud van gekoppelde (bron- en

materie) systemen en bij onderhoud aan de KOA. Dit is m.u.v. diensten waarvoor een geplande niet

beschikbaarheid tijdens daluren geaccepteerd wordt, bijvoorbeeld Mijn Gegevensdiensten.

Met 7 x 24 beschikbaarheid sluit UWV aan bij wat in de markt gebruikelijk is voor Digitale

Dienstverlening. Daar waar de beschikbaarheid van bron- en materiesystemen dit niveau niet kan

garanderen, kan worden overwogen, als onderdeel van de KOA, aanvullende maatregelen te nemen,

zoals bijvoorbeeld een CDS.

Performance

De snelheid (performance) die een gebruiker ervaart bij interactie van digitale dienstverlening is één van

de meest bepalende aspecten voor de klanttevredenheid. Tevens kan een trage site tot veel uitval in het

digitale kanaal leiden.

Het portaal en de KIA’s zijn voor performance grotendeels afhankelijk van één of meerdere KOA’s. Een

KOA dient daarom altijd aan strikte performance eisen te voldoen. Hiervoor worden de volgende

stelregels gehanteerd. Bij deze stelregels wordt de initialisatie van een KOA of systeem buiten

beschouwing gelaten. We hanteren hierbij responsetijd welke gedefinieerd wordt als de tijd die verstrijkt

tussen het moment dat de KIA een vraag naar een KOA doet en de KIA een response van de KOA

ontvangen heeft. Richtwaarden voor de verschillende type responsetijden zijn hieronder gegeven. Deze

zijn gebaseerd op algemeen gebruikelijke waarden binnen digitale dienstverlening. Uiteindelijk is de

totale responsetijd zoals die door de gebruiker wordt ervaren leidend.

• Responsetijd voor een read: <200 ms;

Responsetijd voor een read van een lijst: <400 ms;

•

Responsetijd voor een synchrone mutatie(s): <400 ms;

•

Response tijd voor een asynchrone mutatie: <400 ms;

•

hiervoor heeft het begrip responsetijd geen concrete betekenis, maar wanneer met de mutatie(s)

in het digitale kanaal verder gewerkt wordt dienen de mutatie(s) binnen 1.5s uitgevoerd te

worden, gemeten vanaf het starten van de keten in de KIA. Dit geldt ook voor asynchrone

mutaties die plaatsvinden op bij van het event driven architecture mechanisme.

De belasting waarvoor de responsetijden gelden worden vanuit de KIA per KOA afgesproken met de

eigenaar van de KOA.

Toestandloos (stateless)

Het voordeel van toestandloos is, dat er minder resources nodige zijn dan bij een situatie waarin de

toestand voor iedere gebruiker gedurende het proces bewaard wordt. Tevens neemt de schaalbaarheid

toe zodat de performance gegarandeerd kan worden bij grote aantallen gebruikers.

Vertrouwelijkheid van gegevens

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

42 van 117

Een KOA is verantwoordelijk voor het garanderen van de vertrouwelijkheid van gegevens en doelbinding

van gegevens. Dit wordt geïmplementeerd op basis van een security token bijvoorbeeld het SAML token.

Voor burgers garandeert een KOA dat alleen de gegevens betreffende het specifieke BSN van de burger

worden geleverd. Verder garandeert een KOA dat alleen gegevens aan een KIA worden geleverd als de

KIA en/of het betreffende kanaal geautoriseerd is tot de gegevens.

Voor werkgevers en andere organisaties wordt dit nog wat uitgebreider want hierbij komt de toets bij of

een de gebruiker als medewerker van een organisatie toegang mag hebben tot de opgevraagde

gegevens. Hierbij spelen zaken als persoonsautorisatie, kanaalautorisatie maar ook doelbinding en rol.

Communicatie

Er worden geen eisen gesteld aan de technologie waarmee een KOA geïmplementeerd wordt. Wel dient

de KOA minimaal te kunnen communiceren via de standaard protocollen REST/JSON of SOAP/XML.

Servicecontract

Een KOA dient een eenduidige interface aan te bieden volgens een geldend servicecontract, dit is inclusief

performance afspraken. Bij het aanroepen van een KOA door de KIA hoeft de KIA geen informatie te

hebben van het inhoudelijk functioneren van de KOA. De interface dient het liefst speciaal voor digitale

dienstverlening aangeboden te worden. Dit betekent dat de KOA interface alleen hoeft te veranderen

indien dit voor de digitale dienstverlening (KIA, portaal, app, …) noodzakelijk is. Gevolg is dat de KOA

ook aangepast dient te worden bij veranderingen van de bron die impact op de klantinteractie hebben.

Granulariteit

Het uitgangspunt is dat een KOA bestaat uit een opvraagservice en/of een mutatieservice en/of een

beheerservice. Iedere service kan tot vier operaties bevatten. Het scheiden van opvraagservice en een

mutatieservice is een good practice binnen MSA architectuur waarmee performance eisen kunnen worden

gegarandeerd. Daarnaast kunnen voor UWV medewerkers speciale beheerservices noodzakelijk zijn die

gescheiden moeten blijven van voor klant beschikbare services.

De grootte van vier operaties is gebaseerd op de best practice gebaseerd op de ervaring met het

ontwikkelen van services binnen het UWV WERKbedrijf. Daarnaast sluit deze eis tot het realiseren van

een modulaire opbouw van het landschap. Bij meer dan vier operaties ontstaat de mogelijkheid dat de

KOA het verkeer voor een kanaal aan het optimaliseren is. Dit is niet de bedoeling want de KOA

ondersteunt generiek E-Dienstverlening en de KIA bevat de specifieke implementatie voor een kanaal.

Meer specifieke richtlijnen worden in overleg met E-Werken bepaalt en in een volgende versie van de

doelarchitecturen opgenomen.

Actualiteit van gegevens

Gegevens in het digitale kanaal kunnen afgeleid worden (of een kopie zijn) van de gegevens in de bron-

en materiesystemen. Gebruik van redundante gegevens wordt ingezet als een maatregel om

beschikbaarheid en performance te garanderen.

Voor elke KOA wordt bepaald wat de actualiteit van gegevens dient te zijn. Het is niet altijd noodzakelijk

de nieuwste actuele gegevens ook realtime te kunnen tonen. Een gebruiker had bijvoorbeeld 15 minuten

eerder kunnen inloggen en dan zouden bepaalde gegevens wellicht nog niet bij UWV binnen zijn geweest.

Als stelregel wordt aangehouden dat de actualiteit van gegevens die door een KOA geleverd worden

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

43 van 117

varieert tussen maximaal 15 min oud en maximaal 1 dag oud. Deze grenswaarde moet voor elk proces in

het digitale domein worden bepaald en aansluiten bij het beleid met betrekking tot gegevensredundantie.

Algemene richtlijnen

Een KOA voldoet in principe aan de NFR’s zoals die elders in dit document zijn beschreven. Daarnaast

dient de software van KOA’s zo te zijn gerealiseerd,

dat de toestand van een systeem na verwerking door de KOA niet veranderd bij het meermaals

•

verwerken van hetzelfde bericht (idempotent) binnen een service;

dat het optreden van een fout in de werking van de KOA, niet leidt tot het onverwacht en

•

ongemerkt stoppen van de betreffende interactie maar dat een voor de gebruiker herkenbare

melding verschijnt.

5.1.4 Bron- en Materiesystemen

UWV gebruikt meerdere materiesystemen waarmee de bedrijfsprocessen ondersteund worden. De

doelarchitectuur E-Dienstverlening sluit, daar waar mogelijk, aan bij deze materiesystemen voor de

ondersteuning van de processen die binnen E-Dienstverlening worden ondersteund.

Voor de ontsluiting van deze systemen wordt de beleidsrichtlijn synchrone bronontsluiting gevolgd.

In de onderstaande figuur is het KI/KO model nog eens grafisch weergegeven. Een voorbeeld van dit

concept is uitgewerkt in de volgende paragraaf.

Figuur 15, gedetailleerd KI/KO model

Uiteraard geldt, net als in Figuur 17, ook bij dit overzicht dat EA/DRL deels tussen KOA en Bronsysteem

is geplaats en dat I&AM over alle lagen beschikbaar moet zijn.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

44 van 117

5.1.5 Voorbeeld: KIA Onderhouden CV

Als eerste voorbeeld van een KIA is in het onderstaande figuur de KIA Onderhouden CV geschetst. Dit is

een KIA die onderdeel uitmaakt van de persoonlijke omgeving voor werkzoekenden op werk.nl. De KIA

wordt ook wel de CV-wizard genoemd. Het voorbeeld beschrijft de essentiële onderdelen voor het begrip

maar is geen volledige weergave.

Figuur 16, voorbeelduitwerking KI/KO model voor Onderhouden CV

Start

De KIA Onderhouden CV wordt opgestart door de desbetreffende tegel op het hoofdscherm te selecteren.

Op dat moment wordt er gekeken of er al een CV bestaat door bij de KOA CV het CV van de

werkzoekende op te vragen. Indien er al een bestaand CV is kan de werkzoekende verder met het

bestaande CV of een nieuwe CV aanmaken.

Invoer

Daarna volgen verschillende invoerblokken verdeeld over meerdere schermen. Voor de invoer zijn

referentielijsten nodig en o.a. informatie over Beroepen, Opleidingen en Competenties. Deze gegevens

worden opgehaald door de KOA Referenties en KOA BO&C te raadplegen. Tijdens het doorlopen van de

invoerblokken en –schermen wordt het CV tussentijds opgeslagen, dit gebeurt door KOA CV te muteren

met “opslaan CV”.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

45 van 117

Activeren

Zodra het CV volledig is ingevoerd, kan de werkzoekende het CV activeren zodat dit CV gebruikt kan

worden door werkgevers, werkcoaches, e.d. Het activeren CV gebeurt door het aanroepen van KOA CV

met “activeren CV”. Tevens wordt de taak afgemeld en worden er afhankelijk van bestaande

zoekopdrachten 0 tot 3 zoekopdrachten op basis van het geactiveerde CV aangemaakt. Deze mutaties

zijn volledig verborgen voor de KIA, Alleen de KOA CV weet dat er nog iets met het event CV activeren

moet gebeuren. De KOA CV stuurt het event in de vorm van een bericht met onderwerp CV activeren

naar een Queue. De KOA CV kan daarna weer de controle aan de KIA teruggeven.

De Queue wordt vervolgens gelezen door KOA Taken die het event “CV activeren” verwerkt door een taak

af te melden en de KOA Zoekopdrachten die het event verwerkt door zoekopdrachten aan te maken. Dit

gebeurt allemaal losgekoppeld van de KOA CV en losgekoppeld van de KIA. Dit kan omdat de KIA de

informatie niet direct nodig heeft. Het gebruik van een Queue is wat genoemd wordt “event gedreven

architectuur” en is een maatregel om ontkoppeling te bereiken voor stabiliteit en het verbeterd

tegelijkertijd de performance.

E-mailen CV

Na het activeren kan een gebruiker diverse acties met het CV doen zoals printen, downloaden en ook E-

mailen. Dit gebeurt door de KOA CV aan te roepen.

Tonen zoekopdrachten

Op het scherm wordt nu naast de KIA ook een portaalfunctie Zoekopdrachten getoond. Deze worden

vanuit de KOA Zoekopdrachten gestuurd zodra de KOA Zoekopdrachten het event activeren CV van de

Queue heeft verwerkt. Op deze manier zijn niet alleen de KOA’s CV en Zoekopdrachten losgekoppeld

maar is er ook geen directe koppeling van de KIA CV naar Zoekopdrachten.

5.1.6 Voorbeeld: KIA Aanvragen WW

Als tweede voorbeeld van een KIA is in het onderstaande figuur de KIA Aanvragen WW geschetst. Dit is

een KIA die onderdeel gaat uitmaken van de persoonlijke omgeving voor werknemers op uwv.nl. De

dialoog binnen deze KIA wordt gerealiseerd met onder andere de nieuw te verwerven Business Rule

Engine (BRE). Het voorbeeld (zie Figuur 17) beschrijft de essentiële onderdelen voor het begrip maar is

geen volledige weergave.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

46 van 117

Figuur 17, voorbeelduitwerking KI/KO model voor Aanvragen WW

Start

De KIA Aanvragen WW wordt opgestart door een navigatie item in het portaal. Op dat moment wordt er

gekeken of voor de gebruiker een nog niet ingediende WW-aanvraag bestaat door dit bij de KOA WW-

aanvraag op te vragen. Indien er nog een nog niet ingediende WW-aanvraag bestaat kan de gebruiker

hiermee verder gaan of een nieuwe aanvraag invullen.

Tonen klantgegevens

Daarna worden de gegevens van de gebruiker getoond welke gebruikt worden om de WW-aanvraag mee

in te vullen. Deze gegevens worden o.a. uit Polis opgehaald maar mogelijk ook uit andere bron- en

materiesystemen, dit wordt verzorgd door de KOA Persoonsgegevens en de KIA kan dit bij de KOA

opvragen.

Dynamische vraag/antwoord dialoog

Zodra de klantgegevens volledig ingevuld en bevestigd zijn, worden de gegevens doorgeven aan de KOA

Bedrijfsregels. Deze KOA interpreteert de gegevens op basis van de bedrijfsregels en geeft aan de KIA

terug welk vraagblok de KIA moet uitvragen. Hiermee is de presentatie van de vraag/antwoord dialoog

losgekoppeld van de KOA die de dialoog op basis van bedrijfsregels stuurt. De KIA kan op basis van

Angular de vraagblokken aan de gebruiker tonen en dit proces wordt dynamisch gestuurd door de KOA

bedrijfsregels. Tijdens het doorlopen van de dialoog wordt het resultaat tussentijds opgeslagen in de KOA

WW-aanvraag en wordt iedere keer door de KIA aan de KOA bedrijfsregels het volgende vraagblok

gevraagd.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

47 van 117

Tonen resultaat

Na het doorlopen va de dynamische vraag/antwoord dialoog wordt het resultaat zo mogelijk in de vorm

van de Recht-Duur-Hoogte (RDH) beschikking getoond.

Indienen aanvraag

De gebruiker kan dan overgaan tot het indienen van de aanvraag. Dit gebeurt door de KOA WW-

aanvraag aan te roepen. De KOA muteert de WW-aanvraag en dient de WW-aanvraag in door de WW-

aanvraag op een Queue naar de DIV Regie Laag door te zetten.

Eisen BRE

De KOA Bedrijfsregels maakt gebruik van de BRE. Om de werking van de KIA Aanvragen WW (en andere

digitale aanvraagprocessen) te garanderen, is het nodig dat de BRE voldoet aan de onderstaande eisen.

Deze eisen worden verder uitgewerkt in de implementatierichtlijnen.

7 x 24 beschikbaar,

•

• responsetijd < 200 ms,

stabiel servicecontract.

•

Verder is het van belang dat de KOA Bedrijfsregels geen invloed ondervindt van de inzet van de BRE in

andere applicaties en andersom. Volgens het principe van gescheiden rijbanen wordt de BRE voor E-

Dienstverlening dan ook als een aparte instance geïmplementeerd van de BRE voor UWV medewerkers.

Hiermee krijgt de BRE voor E-Dienstverlening een eigen interface en kunnen de eisen t.a.v.

beschikbaarheid en performance specifiek voor E-Dienstverlening in de infrastructuur opgelost worden.

Hierbij is het een voordeel als de BRE toestandloos is. Dit betekent namelijk dat de BRE minder resources

nodig heeft dan bij een situatie waarbij de toestand voor iedere gebruiker tijdens het proces bewaard

wordt. Tevens is de BRE makkelijker schaalbaar zodat de performance ook bij grote aantallen gebruikers

gehaald kan worden. Performance testen moeten aantonen welke inrichting/infrastructuur capaciteit voor

de BRE uiteindelijk voldoet.

5.1.7 Implementatierichtlijnen KI/KO model

Het KI/KO model is gebaseerd op SOA en MSA. Meer uitleg bij deze onderwerpen is te vinden in Bijlage

C, . Om aan de eisen van een KOA te voldoen kunnen verschillende maatregelen geïmplementeerd

worden. Het gaat hier om diverse soorten van ontkoppelingsmaatregelen om invulling te geven aan

beschikbaarheid, performance en stabiel servicecontract. Een aantal maatregelen komen overeen met de

integratiepatronen in de doelarchitectuur GEIN en worden hierna in het perspectief van E-Dienstverlening

geplaatst.

De onderstaande figuur toont de mogelijke ontkoppelmaatregelen. De ontkoppeling tussen KIA en KOA is

inhoudelijk beschreven bij de eisen aan KIA (nummers (1) en (2) in onderstaande figuur). De overige

maatregelen zijn hieronder beschreven. Deze sluiten aan bij de integratiepatronen zoals deze in GEIN zijn

beschreven.

Welk integratiepatroon wordt gevolgd, wordt bepaald door de eigenaar van de KOA in overleg met

## K&S/IOU.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

48 van 117

Figuur 18, ontkoppelmaatregelen KIA, KOA en bronsystemen

De maatregelen zijn voorbeelden hoe e.e.a. aan te pakken. De leverancier van een KOA dient aan digitale

dienstverlening aan te kunnen geven welke maatregelen getroffen zijn om de eisen van een KOA te

realiseren. Aangezien dit afhankelijk is van specifieke omstandigheden (zoals de inrichting van een

bronsysteem, proces en bedrijfseconomische omstandigheden) is er niet één implementatiestandaard.

Mogelijke keuzes zijn hieronder beschreven.

Beschikbaarheid & Performance: koppelen met systemen

Wanneer er ontsluiting plaatsvindt, bijvoorbeeld opvragen waarbij het antwoord direct nodig is, dan zijn

er verschillende mogelijkheden. De cijfers hieronder refereren aan Figuur 18.

3. Direct synchroon opvragen bij een bronsysteem waar bijvoorbeeld ook andere UWV processen of

medewerkers mee werken. Dit kan betekenen dat digitale dienstverlening direct negatieve impact

kan hebben op de andere UWV processen of medewerkers aangezien deze systemen meestal niet

berekend zijn op de volumes en karakteristieken van digitale dienstverlening, m.a.w. er is niet

voldaan aan het principe van gescheiden rijbanen. Dit betekent ook dat het systeem 7 x 24

beschikbaar moet zijn. Dit is vaak niet het geval bij bijvoorbeeld onderhoud. Daarom is dit

scenario in de meeste gevallen af te raden.

4. Direct asynchroon opvragen middels het Request/Reply mechanisme. De KOA stuurt berichten

naar alle betrokken bronsystemen zonder tussendoor te wachten op antwoord van een individueel

systeem. Als alle antwoorden binnen zijn (of een bepaalde wachttijd verstreken is), gaat de KOA

verder met de verwerking. Dit mechanisme draagt in hoge mate bij aan een goede performance

voor de gebruiker.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

49 van 117

## (CDS)31

5. Ontkoppelen van het systeem door een Compenserende Data Store bij het systeem te

zetten vermindert de afhankelijkheid met het systeem doordat de CDS bevraagd wordt en niet

het systeem zelf. Hiervoor geldt wel dat het CDS 7 x 24 beschikbaarheid moet hebben ook bij

onderhoud en vooral ook wanneer het systeem zelf niet beschikbaar is.

6. Muteren van informatie in het bronsysteem. Door de klant ingevoerde gegevens worden (middels

het SAF mechanisme) verstuurd naar het bronsysteem. Als het bronsysteem beschikbaar is,

worden de gegevens verwerkt. Zo niet, dan worden de gegevens vastgehouden tot het

bronsysteem weer beschikbaar is.

Beschikbaarheid & Performance: KOA voor E-Dienstverlening

Een KOA die volledig zelfvoorzienend is en geen afhankelijkheid met een ander systeem heeft, kan door

eenvoudige maatregelen goed voldoen aan 7 x 24 beschikbaarheid en tevens voldoen aan de

performance eisen. Er zijn hiervan drie soorten:

7. KOA met CDS.

Een CDS niet bij de bron maar een volledige kopie specifiek voor E-Dienstverlening, als onderdeel

van de KOA, biedt maximale ontkoppeling. De KOA met CDS is speciaal ingericht voor E-

Dienstverlening en bevat maatregelen voor 7 x 24 beschikbaarheid ongeacht onderhoud en de

KOA is ook beschikbaar als er problemen in het achterland zijn.

8. KOA met eigen (bron)data.

Het gaat hier om data die binnen E-Dienstverlening ontstaat en (tijdelijk) bewaard moet worden

maar niet direct volledig in een achterliggend systeem kan worden opgeslagen. Dit kan zijn

omdat de gegevens niet volledig zijn of omdat niet alle informatie door het achterliggende

systeem gebruikt wordt. Voorbeelden hiervan zijn, CV en WW-aanvraag, maar ook

inleenadministratie zou dit mechanisme kunnen volgen.

Daarnaast kunnen, binnen dit patroon bestaan, KOA bronsysteem samenvallen. Een voorbeeld

hiervan is de KOA KlantContactVoorkeuren.

9. KOA met aggregatie data (=redundante data uit meerdere bronnen).

Binnen het landschap van digitale dienstverlening is een aantal functies dermate cruciaal dat ze

altijd dienen te functioneren. Een voorbeeld hiervan is het opbouwen van het hoofdscherm in de

persoonlijke omgeving. Het hoofdscherm toont een aantal tegels met korte status informatie als

een soort menu. Om het hoofdscherm altijd te kunnen tonen - zonder afhankelijkheden - wordt

er een KOA met eigen data, afkomstig uit meerder (deel-)systemen geïmplementeerd. Dit is een

bijzondere maatregel die uitsluitend wordt toegepast indien

beknopte informatie van meerdere bedrijfsobjecten nodig is,

•

het een algemene functie ondersteunt en

•

• meerdere KIA’s gebruik maken van deze functie.

In vrijwel alle andere gevallen is een KOA met een CDS of een CDS bij het bronsysteem als

maatregel voldoende.

31

CDS en de daar aan gerelateerde passen ontkoppelmaatregelen zijn opgenomen in de doelarchitectuur GEIN.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

50 van 117

Beschikbaarheid & Performance: asynchroon muteren

De beschikbaarheid van een KOA die een ander systeem ontsluit wordt in veel gevallen bepaald door het

systeem dat ontsloten wordt. Uitzondering hierop is wanneer de communicatie met het andere systeem

asynchroon is en de KOA en/of digitale dienstverlening de uitkomsten van de communicatie niet direct

nodig heeft. Een goed voorbeeld is het uitvoeren van asynchrone mutaties op basis van SAF patroon.

Indien een KOA of het bronsysteem een CDS heeft, dan wordt in principe het CDS niet direct gemuteerd

door de KOA maar voert de KOA een asynchrone mutatie uit op het achterliggende systeem welke het

CDS muteert. Hierdoor worden de gegevens van het CDS altijd gemuteerd op basis van de volledige

correcte verwerking door het systeem.

Beschikbaarheid & Performance: event driven architecture

Een maatregel om beschikbaarheid en performance te garanderen is gebruik te maken van event driven

architecture. In de plaats van mutaties over verschillende bedrijfsobjecten en systemen synchroon vanuit

één KOA uit te voeren kan er gekozen worden om dit los te koppelen. De KOA voert dan alleen de

noodzakelijke mutatie (event) op het eigen bedrijfsobject (in het onderliggende bronsysteem) uit en

geeft het event daarna asynchroon door. Dit event wordt daarna door verschillende KOA’s opgepakt om

daarmee de noodzakelijke mutatie voor het eigen bedrijfsobject uit te laten voeren. Dit koppelt processen

los en draagt daarom bij aan de beschikbaarheid. De performance verbetert omdat de gebruiker alleen

wacht op die mutaties die direct noodzakelijk zijn voor de gebruiker, de rest wordt asynchroon

uitgevoerd.

Dit betekent wel dat de KOA’s geschikt moeten zijn om te passen binnen een event driven architecture en

dit is met name toepasbaar op events die invulling geven aan de klantinteractie en niet op events in en

tussen de achterland systemen.

Beschikbaarheid & Performance: ‘gescheiden rijbanen’

De KIA/KOA structuur maakt het mogelijk dat klanten via meerdere kanalen met UWV communiceren.

Om de UWV diensten zo hoog mogelijk beschikbaar te maken, mogen kanalen elkaar niet beïnvloeden.

Als er een kanaal niet functioneert, mag een ander kanaal daar geen last van ondervinden.

Dit houdt in dat de KIA’s voor de verschillende kanalen – op logisch niveau - los van elkaar beschikbaar

moeten worden gesteld en pas op het niveau van de KOA’s bij elkaar komen.

Hoewel de KIA/KOA structuur ten behoeve van E-Dienstverlening is opgezet, kan deze structuur ook

elders binnen UWV worden toegepast. In dat geval moeten ook hier ‘gescheiden rijbanen’ worden

gerealiseerd.

Indien, bijvoorbeeld, informatie ten behoeve van UWV medewerkers ook via KOA’s zou worden ontsloten,

is het raadzaam deze KOA’s onafhankelijk te laten zijn van de KOA’s voor de kanalen binnen E-

Dienstverlening.

Stabiel servicecontract: n-3 versies

Indien een leverancier een KOA aanbiedt maar de interface niet specifiek is voor digitale dienstverlening

dan kan gekozen worden om de KOA altijd de nieuwste en 3 oudere versies van de interface te laten

ondersteunen. Een nieuwe versie (n) betekent een contract-brekende wijziging (NB optionele velden

kunnen nog steeds toegevoegd worden, bijvoorbeeld in een parametriseerbare webservice). Tevens geldt

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

51 van 117

dat een n versie maximaal eens in de 3 maanden uitgebracht wordt zodat digitale dienstverlening dus

maximaal één maal per 9 maanden mee dient te veranderen. Hiermee wordt de wendbaarheid vergroot

doordat KOA interfaces kunnen worden aangepast zonder de KIA aan te moeten passen en omgekeerd.

Door te kiezen voor de ondersteuning van n-3 versies kunnen KIA, KOA en bronsysteem onafhankelijk

van elkaar worden aangepast en gereleased waardoor de wendbaarheid van het landschap als geheel

toeneemt.

Stabiel servicecontract: eigen servicecontract

Er kan ook gekozen worden om een specifieke KOA met een eigen servicecontract aan te bieden voor

digitale dienstverlening. De KOA kan de wijzigingen met het systeem waarmee de KOA koppelt opvangen

zodat niet alle portaalfuncties en KIA’s aangepast moeten worden zodra het systeem gewijzigd wordt. Dit

laatste komt ook de wendbaarheid ten goede omdat een gekoppeld systeem kan wijzigen zonder dat dit

veel wijzigingen bij digitale dienstverlening betekent.

KOA is één (samengesteld) bedrijfsobject

Een KOA is ook een manier om een bedrijfsobject te ontsluiten waarvoor koppelingen met meerdere

bron- en materiesystemen gemaakt dienen te worden. Dit is een maatregel om te kunnen voldoen aan

één van de KOA richtlijnen.

5.1.8 Technische inrichting

De globale technische inrichting van het KI/KO model is in onderstaande figuur vertaald naar onderdelen

in de informatievoorziening. De realisatie van KIA’s binnen de klantinteractielaag vindt plaats door

## (IOU).32

medewerkers (c.q. leveranciers) van de Internetorganisatie UWV De klantinteractielaag valt in

onderstaande figuur samen met de lagen boven de API Gateway. KOA’s zijn in dit overzicht onderdeel

van de laag API’s/webservices.

32

Zie notitie Verantwoordelijkheidsverdeling E-Diensten 20161017

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

52 van 117

Figuur 19, technische onderdelen i.r.t. KI/KO model

Interface manager – API Gateway

UWV heeft het voornemen een interface manager in de vorm van een API Gateway (API-Gw) te

verwerven. De API-Gw kan worden ingezet als technische ontkoppeling tussen systemen van UWV. Het

kan bijvoorbeeld toegepast worden tussen KIA’s en KOA’s en ook tussen KOA’s en bron- en

materiesystemen. Ten behoeve van E-Dienstverlening worden van een API-Gw de volgende functies

verwacht:

Routing en versionering: de API-Gw verbindt de KOA’s en de achterliggende systemen waarbij

•

het niet nodig is, dat KOA’s of de achterliggende van elkaar weten welke versie van welke service

waar te vinden is. Interfaces ouder dan n-3 worden niet meer aangesproken en versies nieuwer

dan n worden alleen benaderd voor testdoeleinden;

Service governance; vooral ‘design time’ ondersteunt de API-Gw ontwikkeling en testen van

•

nieuwe versie van services door aan te geven of het een nieuwe hoofdversie is of een special.

Verder kan tijdens ontwikkeling de API-Gw ook interfaces stubben zodat de API-Gw bijdraagt aan

een agile ontwikkelstraat

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

53 van 117

Throttling; de API-Gw limiteert het volume van het verkeer dat op een KOA of een bron- en

•

materiesysteem afkomt. Voorbeeld: indien mobiel en portaal van dezelfde KOA gebruik maakt

dan kan er een maximale belasting voor het kanaal worden afgesproken. Indien het kanaal over

het maximum heengaat wordt de belasting gemaximaliseerd zodat er geen impact op het andere

kanaal is.

Throttling kan ook gebruikt worden als capaciteitsbeveiliging voor het synchroon aanroepen van

bron- en materiesystemen waar meerdere afnemers gebruik van maken. Indien het volledig

implementeren van gescheiden rijbanen niet haalbaar is, kan throttling een alternatief zijn. In dat

geval worden overigens niet alle gevaren opgelost. Zo kan het nog steeds voorkomen dat

verschillende gebruikersgroepen elkaars performance beïnvloeden waar dit niet zou kunnen bij

gescheiden rijbanen.

Circuit breaking; Indien de API-Gw constateert dat een bronsysteem niet beschikbaar is, wordt

•

hiervan een melding gegeven aan de KOA zodat deze niet onnodig berichten blijft sturen en

wacht op antwoord. De KOA dient zo te zijn ingericht, dat deze adequaat kan reageren op

dergelijke meldingen.

Beveiliging; de API-Gw geeft toegang tot een KOA op basis van de KIA en de omgeving

•

waarbinnen deze KIA zich bevindt. Binnen de KOA moet worden bepaald welke operaties wel en

niet uitgevoerd mogen worden door een specifieke gebruiker of transactie.

• Logging en monitoring; de API-Gw kan logging en monitoring verzorgen zodat hiervoor geen

separaat middel ingezet hoeft te worden. De vastgelegde log-informatie kan worden gedeeld

zodat ook de keten als geheel gemonitord kan worden.

5.2 Architectuur BouwBlokken (ABB)

De digitale contactmomenten in de klantreis worden ondersteund met een aantal

architectuurbouwblokken. ABB’s omvatten een cluster van functionaliteiten met als doel het

ondersteunen van een of meer onderdelen van diensten aan klanten. De individuele bouwblokken kunnen

bestaan uit meerdere onderdelen die specifiek zijn voor dat bouwblok. Combinaties van bouwblokken

vormen de applicatiepatronen en een bouwblok kan in meerdere patronen voorkomen. Door bouwblokken

te identificeren kan voor de patronen worden volstaan met de beschrijving van de rol van het patroon en

het benoemen van de bouwblokken zonder de bouwblokken telkens opnieuw te moeten beschrijven.

Een totaaloverzicht van de binnen E-Dienstverlening onderkende ABB’s is opgenomen in Figuur 20.

Daarop aansluitend volgt een algemene beschrijving, bezien vanuit de klant. Detailuitwerking van deze

ABB’s vindt plaats in de volgende subparagrafen.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

54 van 117

Figuur 20, totaaloverzicht architectuur bouwblokken Klantinteractie

Als eerste komt de klant het Portaal tegen. Binnen dit Portaal vindt de klant diverse portaalfuncties zoals

‘mijn vestiging’ en ‘loginsessie’. De algemene informatie die de klant hier vindt, wordt geleverd door de

ABB Content Distributie. Het beheer, inclusief redactie, van die informatie wordt ondersteund met

Content Management. Als de klant inlogt, wordt gebruik gemaakt van Identity en Access Management

(I&AM). Na inloggen komt aanvullende informatie beschikbaar voor de opbouw van het portaalscherm.

tegels33

Zo worden de meer of minder prominent getoond afhankelijk van het klantprofiel, opgebouwd in

het ABB ‘Profileren en segmenteren’. Door op een van de tegels te klikken, kiest de klant voor het starten

Applicatie34

van een specifieke Klant Interactie (KIA) die een bepaalde E-Dienst vertegenwoordigd.

Afhankelijk van het doel van de KIA, communiceert deze met Kanaal Ondersteunende Applicatie(s)

(KOA’s), Bestand Management, Externe Service of Externe Interactie.

De KOA realiseert de ontkoppeling tussen de voorkant en de bron- en materiesystemen binnen UWV of

een externe service buiten UWV. KOA’s worden bij voorkeur zo ingericht dat deze het niveau van

beschikbaarheid en performance garanderen dat UWV haar klanten wil bieden, ook als de betrokken

bron- en materiesystemen dat (nog) niet in voldoende maten kunnen garanderen. Daar waar sprake is

het uitwisselen van bestanden/documenten worden deze bestanden uitgewisseld met behulp van het ABB

Bestand Management.

Een klant kan vanuit een KIA ook naar een Externe Interactie worden doorgeleid. Een voorbeeld hiervan

is het volgen van een eLearning module die de klant helpt de kans op het vinden van werk te vergroten.

33

Een tegel vormt het startpunt voor een interactie en toont beperkte informatie m.b.t. de te starten interactie.

34

De begrippen KIA en KOA en de afbakening wordt uitgewerkt in paragraaf 5.1.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

55 van 117

De klant wordt op de website de mogelijkheid geboden om, via de app-stores, een app op zijn mobiele

device te installeren. Om binnen de app de functies te gebruiken waarmee de klant persoonlijke

gegevens kan benaderen, acht UWV het noodzakelijk de app eerst te ‘binden’. Dit proces start met de

KIA Bind. Van daaruit wordt de klant door het proces begeleid om zijn device uiteindelijk geregistreerd te

krijgen in de KOA Binded_dev(ices). Deze wordt bij elk volgend contact via de app geraadpleegd om te

controleren of de combinatie van app en apparaat bekend is. Als dit het geval is, wordt de bijbehorende

gebruiker geïdentificeerd en wordt de betreffende interactie verder afgehandeld tussen KIA en de

‘root-toegang’35

desbetreffende KOA’s. Voorwaarde voor gebruik van de app is, dat op de gebruiker geen

tot het device heeft.

Naast de ABB’s die een directe rol spelen in de klantreis, zijn er ook ABB’s voor ondersteunende functies

onderkend. Zo kan de klant binnen de ABB klantondersteuning een chat sessie initiëren met het KCC of

kan de klant vanuit het KCC worden ondersteund met behulp van co-browsing.

De ABB Analytics & Optimaliseren omvat het verzamelen en analyseren van het gedrag van de klanten in

het digitale kanaal. Vanuit de analyse kunnen portalen en E-Diensten worden geoptimaliseerd om een zo

goed mogelijke klantbeleving ter realiseren.

De stippellijn in deze figuur (en volgende figuren) geeft aan waar de grens ligt tussen klantinteractie en

kanaalondersteuning. Impliciet is dit ook een onderscheid in verantwoordelijkheid. Dit onderscheid wordt

verder beschreven bij de uitwerking van het KIA/KOA model.

5.2.1 ABB Portaal

Het eerste punt waar de klant via het web met UWV interacteert is het portaal. Daarmee biedt het portaal

een standaard interface voor algemene (web-)content en voor E-Diensten die een specifieke dienst van

UWV aanbieden in het digitale kanaal. In de bedrijfsarchitectuur zijn de patronen binnen de klantreis

geïntroduceerd. Hierbij gaat het over patronen die betrekking hebben op publieke omgevingen en

patronen die betrekking hebben op persoonlijke omgevingen. Binnen de portaalarchitectuur maken we

onderscheid in:

Publieke omgeving waar algemeen beschikbare informatie ingezien kan worden. Dit is

•

voornamelijk informatie in de vorm van webcontent. Daarnaast is gelimiteerde (publiek

toegankelijke) interactie met UWV mogelijk;

Persoonlijke omgeving waar klantgerelateerde informatie ingezien kan worden. Hierbij gaat

•

het vooral om informatie in de vorm van gegevens en in mindere mate in de vorm van content.

Verder is de persoonlijke omgeving met name gericht op klantgerelateerde interactie met UWV;

Beheer omgeving waarin functionaliteit en informatie zijn opgenomen ten behoeve van

•

beheerders zodat de portalen onderhouden kunnen worden.

Omdat de publieke omgeving voornamelijk content gericht is, wordt deze getoond vanuit een content-

distributiefunctie. Binnen deze functie is het mogelijk om de persoonlijke interactie met UWV aan te

gaan. De content die in deze omgeving wordt aangeboden, wordt voorbereid in een content management

omgeving waarin de informatie wordt opgesteld door (web-)redacteuren en inhoudelijk deskundigen van

35

Root-toegang zorgt er voor dat een gebruiker directe toegang heeft tot alle technische functies van het betreffende

mobiele device. Daarmee kan elke beveiliging worden omzeild. Dit betekent het voor een gebruiker van een ‘ge-root’

device niet mogelijk mag zijn, via een app, toegang te krijgen tot informatie binnen UWV.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

56 van 117

UWV. Daarmee ontstaat een situatie waarin de medewerkers zoveel mogelijk zelf de inhoud van de

portalen kunnen onderhouden.

De persoonlijke omgeving is een selfservice omgeving waarin de klantinteractie plaatsvindt nadat een

klant is ingelogd. Deze omgeving wordt geleverd vanuit een portaalapplicatie. Met deze inrichting is het

portaal onafhankelijk en maximaal ontkoppeld van de content distributie functie voor wat betreft de

stabiliteit en (product)leverancier van deze functie.

De onderstaande figuur toont de home pagina van een persoonlijke omgeving waarin de gebruiker is

ingelogd en ziet welke informatie hij kan ophalen en wat hij nu kan doen in relatie tot diensten van UWV.

Deze home pagina toont persoonlijke informatie en is een startpunt voor het patroon “Inzien persoonlijke

informatie”. Deze informatie is binnen de portaalapplicatie opgebouwd uit een aantal portaalfuncties, die

informatie (gegevens en/of content) tonen en het mogelijk maken naar een volgend portaalonderdeel te

navigeren. Voorbeelden van portaalfuncties zijn: ‘Login’, menu, ‘Mijn vestiging’, relevante content en de

tegeltjes op de home pagina.

5.1 lid 2 sub e

5.1 lid

2 sub

e

5.1 lid 2 sub e

5.1 lid 2 sub

e

Figuur 21, voorbeeld ‘inzien persoonlijke informatie’

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

57 van 117

Het volgende scherm toont een pagina waarop naar vacatures gezocht kan worden. Het blok waarbinnen

naar vacatures gezocht kan worden is een voorbeeld van het patroon “Persoonlijke interactie met UWV”.

## (KIA)36

Dit blok wordt ingevuld met een zelfstandige applicatie welke Klant Interactie Applicatie genoemd

wordt.

5.1 lid 2 sub e

5.1 lid

2 sub

e

Figuur 22, voorbeeld 'Persoonlijke interactie met UWV '

Structuur ABB Portaal

De hiervoor beschreven portaalarchitectuur leidt tot twee ABB schema’s die marginaal van elkaar

verschillen. In de publieke omgeving is primair sprake van contentdistributie terwijl de persoonlijke

omgeving vooral het feitelijke interactie-portaal omvat. De beide ABB’s zijn hieronder weergegeven.

36

Zie uitleg bij KI/KO model

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

58 van 117

Figuur 23, ABB’s publiek en persoonlijk portaal

Software bouwblokken

De publieke omgeving bestaat voornamelijk uit contentpagina’s welke geleverd worden door een Content

Management Systeem (CMS), zie ABB Content Management. Daarnaast kent de publieke omgeving een

aantal Publieke toegankelijke interacties welke door een KIA ingevuld worden. Net als in de persoonlijke

omgeving wordt een KIA gerealiseerd .

5.1 lid 2 sub i

portaal38

De persoonlijke omgeving is een op de klant van UWV gericht dat gerealiseerd wordt als

maatwerksoftware met het ASP.Net framework. Deze omgeving wordt opgebouwd nadat een gebruiker is

ingelogd39.

De opbouw is getoond in Figuur 24.

1. Het portaal draait in de browser in de vorm van HTML;

2. De HTML van het portaal wordt geleverd door de portaalapplicatie gebaseerd op het

5.1 lid 2 sub i

framework. De portaalfuncties vormen losse onderdelen maar worden binnen dezelfde omgeving

opgebouwd wat voordelen biedt in termen van performance.

3. De Klant Interactie Applicatie (KIA) staat los van het portaal en wordt gerealiseerd op basis van

KIA-View40.

Net framework met voor de

5.1 lid 2 sub i 5.1 lid 2 sub

i

4. De en de bijbehorende HTML views worden geleverd in de vorm van resource files vanaf

5.1 lid 2 sub i

een webserver.

5. De Angular modules halen gegevens op bij een API die geïmplementeerd is o.b.v. het

5.1 lid 2 sub i

.Net framework.

5.1 lid

2 sub i

N.B.: De onderdelen 3, 4 en 5 vormen gezamenlijk de KIA. Het portaal in de browser en de KIA in de

browser bestaan alleen tijdens run-time.

37

De keuze voor voor de portalen van UWV is in januari 2017 bekrachtigd door de raad van

5.1 lid 2 sub i

Bestuur.

38

Binnen UWV wordt ook nagedacht over het toepassen van de hier beschreven structuren in systemen ten behoeve

van interne medewerkers. Keuzes voor dit concept zowel als voor de eventuele inrichting en technologie vallen buiten

de scope van E-Dienstverlening. De in deze doelarchitectuur gemaakte keuzes zijn dus niet zonder meer van

toepassing buiten dit domein.

39

Zie ook patroon ‘Opbouwen Persoonlijke Omgeving’ in paragraaf 5.3.1

40

Deze keuze is in januari 2017 vastgesteld op basis van een voorafgaand onderzoek en PoC

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

59 van 117

5.1 lid 2 sub i

5.1 lid 2 sub i

5.1 lid 2 sub i

5.1 lid 2 sub

i

Figuur 24, opbouw persoonlijk portaal

Deze opzet maakt het mogelijk dat de KIA’s volledig los van de portaalapplicatie ontwikkeld en

opgebouwd worden. Iets wat de stabiliteit en wendbaarheid ten goede komt. Hiermee wordt de

persoonlijke omgeving opgebouwd uit een aantal los te ontwikkelen componenten (in tegenstelling tot

een monolithische applicatie) waarmee invulling wordt gegeven aan het principe van modulaire opbouw.

Daarmee vereenvoudigt de realisatie van de gehele omgeving.

De keuze voor de combinatie van sluit aan bij keuzes die door veel

5.1 lid 2 sub i

partijen buiten UWV worden gemaakt voor de realisatie van hun portalen.

5.2.2 ABB App

De ABB App voor mobiele devices is vergelijkbaar met de ABB Portaal: er zijn algemene app functies en

er zijn functies voor persoonlijk interacties die met een KIA worden ingevuld.

Een algemene functie is het persoonlijk en persoonlijk relevant maken van de app op het mobile device.

De app (portaal) functie gebruikt hiervoor informatie verkregen vanuit de KOA ‘Klant Profiel Service’. Een

andere algemene functie is de ‘Remote Kill’ functie die gebruikt wordt indien de veiligheid van de app

ondermijnd wordt (apparaat geroot, security leak in app, app versie wordt niet langer ondersteund etc.).

Een voorbeeld van een KIA is het zoeken naar vacatures. Deze KIA (binnen de app) maakt gebruik van

de KOA die ook door de portaal-KIA voor het zoeken naar CV’s’ wordt aangeroepen.

Een voorbeeld van schermen die een UWV app zou kunnen bieden is gegeven in Figuur 25.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

60 van 117

Figuur 25, voorbeeld aanzet schermen en functies in een app

Structuur

5.1 lid 2 sub i

5.1 lid 2 sub i 5.1 lid 2 sub i

Figuur Figuur 27, 26, structuur structuur ABB ABB App App

Bind heeft als enige functie om de app te binden aan het device en de persoon. Dit is in eerste

5.1 lid 2

sub i

instantie de enige KIA die voor de gebruiker toegankelijk is. Nadat dit binding-proces (zie paragraaf

5.3.9) heeft plaatsgevonden, kan de gebruiker zich bij de app identificeren door middel van een pincode

gebruiker41

of wachtwoord. Daarna blijft de KIA-Bind verborgen voor de en zijn de overige KIA’s binnen

de app toegankelijk voor de gebruiker.

Software bouwblokken ABB App

De software bouwblokken voor de App zijn in de onderstaande figuur weergegeven. Daarbij valt op, dat

de beide KIA blokken verdeeld zijn in een deel in de App (KIAcs) en een deel op de systemen binnen het

UWV domein (KIAss).

Onderdelen in de app zijn gebouwd in de taal die aansluit bij het gekozen platform ).

5.1 lid 2 sub i

Doel van de inzet van dit platform is om maximaal hergebruik te kunnen maken van code over de

verschillende besturingssystemen heen (iOS, Android, etc.). Het platform genereert een app per

besturingssysteem.

41

Onderdelen van deze KIA zouden nog wel gebruikt kunnen worden, bijvoorbeeld bij het opvragen van de signature

van het apparaat tijdens het opstarten van de app.

42

is het voorkeursplatform omdat dit platform goed aansluit bij zowel de nu bekende behoefte al bij de

5.1 lid 2 sub

i

tooling die wordt gebruikt in de ontwikkelomgeving voor portalen. Daarnaast is dit platform reeds in gebruik bij

5.1 lid

2 sub

de primaire leverancier van software voor E-Dienstverlening

5.1 lid 2 sub i

i

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

61 van 117

De onderdelen die binnen het UWV domein draaien (KIA-App Bind-srvr en KIA-App-srvr) worden

gebouwd in .Net. Ontkoppeling tussen de componenten in de App en de componenten op de server vindt

plaats in de infra component Reverse Proxy

5.1 lid 2 sub i

Figuur 28, software bouwblokken ABB App

5.2.3 ABB Content Management

Content Management in het kader van de doelarchitectuur E-Dienstverlening beperkt zich tot het deel

van de content dat wordt aangeboden via de digitale kanalen (waarvan portalen vooralsnog het meest

gebruikt zijn).

In het geval van apps zal de content management distributie nog enkele specifieke functies vervullen:

• Remote management van ‘Kritische meldingen’ zonder release of update van de app;

Update van lokaal (in het device) opgeslagen content. Deze wordt getoond als geen contact met

•

de UWV omgeving mogelijk is;

Failsafe melding;

•

• Aankondiging nieuwe versie;

Update advies bij nieuwe versie.

•

De gewenste situatie kent één proces voor webcontentmanagement voor geheel UWV. Het

ondersteunende systeem (c.q. combinatie van systemen) kent naast functies voor beheer en publicatie

ook functies voor de bewaking van de consistentie en integraliteit van content. Ook is het systeem in

staat analyses op het gebruik van content uit te voeren. Contentelementen dienen zo opgeslagen te

worden, dat deze in het redactieproces hergebruikt kunnen worden, ook over meerdere portalen heen.

Metadatering van deze content wordt dan nog belangrijker. In de verdere, bredere uitwerking van

contentmanagement zal hieraan expliciet aandacht worden besteed, evenals aan de eisen met betrekking

tot archivering. Hierbij wordt ook aandacht gegeven aan de momenten waarop content wordt

vrijgegeven.

Functies van webcontentmanagement

Systemen ter ondersteuning van webcontentmanagement dienen de volgende functionaliteit te bieden:

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

62 van 117

Redactie: Informatie vanuit verschillende bronnen en redacties moet met elkaar geïntegreerd

•

kunnen worden tot een geheel. Daarbij zijn meerdere rollen betrokken bij het produceren van inhoud

en het goedkeuren van teksten voor publicatie.

• Responsiveness/adaptiveness: Inhoud moet geschikt zijn voor meerdere devices. Dat wil zeggen

dat de inhoud op een mobiel apparaat of tablet even goed leesbaar moet zijn als op een PC. Het

ondersteunende systeem moet hiervoor de faciliteiten bieden.

(Proef-)publicatie: Redacteuren moeten getoond kunnen krijgen wat ook de klant na publicatie te

•

zien krijgt, conform het principe van Wysiwyg (What you see is what you get). Het systeem moet

hierin kunnen tonen hoe pagina’s er zullen uitzien op kleinere schermen.

Veelgestelde vragen: Een specifiek onderdeel van contentmanagement is de sectie veelgestelde

•

vragen. Hierin moet de klant in staat zijn het antwoorde op een bestaande vraag te vinden of een

nieuwe vraag te stellen. Reeds bestaande vragen en antwoorden worden onderhouden en beschikbar

gesteld als onderdeel van dit ABB.

Crisispublicatie: Gedurende een crisis (bijv. het niet beschikbaar zijn van verwerkende systemen)

•

moet een klant direct kunnen worden geïnformeerd over wat er aan de hand i sen wat de

verwachtingen zijn. Voor de klant moet helder zijn wat er ook van hem verwacht wordt. Bijvoorbeeld

de aangepaste termijn voor een taakafhandeling als gevolg van deze storing.

Pagina’s waarin deze informatie wordt gegeven moeten op afroep door een beheerder ‘aangezet’

kunnen worden.

Structuur van webcontentmanagement

De structuur van dit ABB omvat twee onderdelen, te weten de distributie- en de

contentmanagementfunctie. Deze laatste functie omvat zowel opslag van content voor

verdere bewerking als de ondersteuning van het redactieproces.

Contentdistributie omvat de opslag en het beschikbaar stellen van beschikbaar gestelde

content.

Software bouwblok webcontentmanagement

Voor webcontentmanagement geldt dat er gebruik gemaakt zal worden van standaard

applicaties die vervangbaar zijn en invulling geven aan de behoefte van UWV. Er wordt nadrukkelijk niet

gekozen voor producten die onderdeel zijn van een suite en binnen de suite afhankelijk zijn van andere

producten. Zolang het bestaande contract geldt, wordt gebruik gemaakt van Tridion voor content

management.

5.2.4 ABB Document Management

Document management wordt binnen de digitale dienstverlening gebruikt als middel om de klant te

ondersteunen tijdens een aantal interacties. Een voorbeeld hiervan is het tijdelijk opslaan van document

voor een klant. Zolang het document nog niet definitief is en niet officieel aan UWV verstuurt, blijft het

binnen het DMS van het domein van E-Dienstverlening. Zodra het document ‘definitief’ is en/of wordt

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

63 van 117

verstuurd aan UWV, wordt het opgeslagen conform de regels van bewaren, verwijderen en archiveren

documenten43.

van

De huidige werkwijze is zichtbaar in onderstaande figuur.

Figuur 29, documentstromen en DMS

Software bouwblok DMS

Voor het portaal werk.nl wordt de bestaande situatie rond Document Management in het domein E-

Dienstverlening gecontinueerd. Dat houdt in dat het DMS dat is gekoppeld aan werk.nl het Oracle product

Web Center Content (WCC) blijft.

5.2.5 ABB Externe service

In een aantal situaties maakt UWV gebruik van externe services om diensten aan haar klanten aan te

bieden. Deze services worden veelal als SaaS service afgenomen. De klant wordt vanuit het UWV portaal

doorgeleid naar de betreffende aanbieder.

43

In de huidige situatie is de opslag in het EA nog niet gerealiseerd. In het UIP is de realisatie van dit voornemen

gekoppeld aan UWV brede onderzoek naar ontsluiting van gegevens en het verbeteren van CRM-functionaliteit. De

resultaten van dit onderzoek zullen in een volgende versie van deze doelarchitectuur worden verwerkt.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

64 van 117

5.2.6 ABB Identity en Access Management (I&AM)

Identity en Access Management richt zich op klanten en het op een veilige wijze verlenen van toegang tot

gegevens en functionaliteit binnen UWV. Daarbij wordt gebruik gemaakt van faciliteiten conform de

## (WGDI)44

(aanstaande) Wet Generieke Digitale Infrastructuur en de europese ‘electronic IDentification,

Authentication and trust Services’ (eIDAS), zoals die in ontwikkeling zijn. Voorbeelden daarvan zijn DigiD,

e-Herkenning en Digipoort, maar ook het door de banken aangeboden iDIN.

Klanten kunnen toegang krijgen op verschillende beveiligingsniveaus. Welk niveau nodig is, wordt

bepaald door het type informatie waartoe de klant toegang vraagt. Zo vereist toegang tot medische

gegevens een hoger beveiligingsniveau dan toegang tot basale persoonlijke gegevens (zie ook paragraaf

4.7.1).

I&AM binnen E-Dienstverlening richt zich uitsluiten op toegang voor klanten en niet op het verlenen van

toegang tot informatie en systemen voor medewerkers van UWV of voor medewerkers van partners die

werkzaamheden verrichten in de backoffice.

Binnen K&S wordt gewerkt aan een roadmap voor de aansluiting op nieuwe diensten conform de WGDI.

E-Dienstverlening sluit zo veel mogelijk aan bij deze roadmap.

Functies in Identity en Access Management

figuur45.

De belangrijkste functies binnen I&AM zijn getoond in de onderstaande

Figuur 30, functies binnen I&AM

Identity Governance: is de functie waarbinnen beleid met betrekking tot identiteiten van

•

gebruikers(groepen) wordt vastgesteld. Voor dit onderdeel wordt nauwe samenwerking met de

44

Voor meer informatie zie: https://www.digitaleoverheid.nl/beleid/digitalisering-aanbod/inhoud/

45

In deze versie van de figuur ontbreekt machtigingen, gebruikers die namens een organisatie of persoon toegang

moeten krijgen tot gegevens of systemen binnen UWV. Deze worden in een volgende versie toegevoegd.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

65 van 117

CISO gezocht. Als onderdeel van deze governance wordt onder andere bepaald welke

mechanismen voor identificatie gebruikt kunnen worden voor toegang door klanten van UWV.

Access Management: het verlenen van toegang tot systemen en gegevens (autorisatie) op

•

basis van rechten die zijn gekoppeld aan het profiel van een individuele gebruiker.

Identity Management: het beheren van de digitale identiteiten van individuele gebruikers voor

•

zover UWV geen gebruik maakt van faciliteiten die elders binnen de overheid worden

aangeboden. Onder Identity Management valt ook het beheer van Machtigingen en de toepassing

van DigiD-Machtigen.

Authenticatie Diensten: beschrijft de verschillende mechanismen die worden ingezet voor de

•

verschillende toegangsniveaus. Hieronder valt bijvoorbeeld de noodzaak voor authenticatie via

DigiD in combinatie met SMS voor toegang tot gevoelige persoonlijke gegevens.

Identity Store: bevat de gegevens van de identiteiten van klanten van UWV ten behoeve van

•

toegang tot voor de betreffende klant specifiek beschikbare informatie. Daar waar gebruik

gemaakt wordt van voorzieningen elders binnen de overheid zullen deze gegevens niet (volledig)

in een Identity Store van UWV worden opgenomen.

Eisen aan I&AM

De eisen die vanuit E-Dienstverlening worden gesteld aan I&AM zijn:

Aansluiting op (inter-)nationale voorzieningen zoals DigiD;

•

Gescheiden van applicatie logica;

•

• Voldoet aan open standaarden;

Gecentraliseerd beheer en decentrale uitvoering;

•

Externe toegang is strikt gescheiden van interne toegang;

•

• Ondersteuning van verschillende STORK niveaus zodat ook medische gegevens veilig benaderd

kunnen worden;

Ontkoppelbaar;

•

Stabiel en 7*24 beschikbaar

•

• Niet belemmerend voor de klant.

Software bouwblok I&AM

Uiteindelijk wil UWV één digitaal platform met een ontkoppelbare I&AM oplossing die Single Sign On

(SSO) voor alle digitale dienstverlening van UWV realiseert. Daarbij wordt gestandaardiseerd op

protocollen (w.o. SAML) die aansluiten bij de richtlijnen conform de WGDI.

I&AM biedt dan ook oplossingen voor toegang vanaf mobiele devices (via apps).

In eerste instantie kan worden volstaan met gebruik van voor I&AM. Voor de

5.1 lid 2 sub i

langere termijn moet een alternatief worden gezocht voor de huidige versie omdat deze versie in de

komende jaren alleen nog ‘Sustaining Support’ heeft. UWV heeft het voornemen eind 2017 te starten met

het onderzoek naar alternatieven.

5.2.7 ABB Formulierengenerator

Voor eenvoudige formulieren waarin geen of beperkte controles op de invoer nodig zijn, kan een

formulierengenerator ingezet worden. Daar waar bij het invullen gegevens direct gecontroleerd worden in

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

66 van 117

relatie tot reeds aanwezig gegevens, wordt de interactie uitgewerkt in een KIA.

Met behulp van de formulierengenerator gerealiseerde documenten worden, al dan niet in EA,

gearchiveerd conform de eisen die DIV daaraan stelt.

Software bouwblok formulieren

Binnen UWV is gekozen voor als doeltechnologie voor het genereren van formulieren. Met het

5.1 lid 2 sub i

aanroepen van een formulier vanuit het portaal wordt de gebruiker (tijdelijk) naar de server

5.1 lid 2 sub i

geleid. Na het invullen en versturen van het formulier, keert de gebruiker weer terug naar het portaal.

5.2.8 ABB Monitoring, Logging en Analytics

Het uitgangspunt van monitoring binnen E-Dienstverlening is de klantreis en het kunnen verbeteren

ervan aan de hand van de ervaringen van de klant gedurende die reis. De klantreis omvat de gehele

keten, dus ook onderliggende klant- en bedrijfsprocessen. Daarmee overstijgt dit onderwerp uiteindelijk

ook de grenzen van de doelarchitectuur E-Dienstverlening. Conform het APM Conceptual Model van

Gartner bestaat monitoring uit vijf gebieden:

Ervaring van de eindgebruiker;

•

Performance van de applicaties;

•

Performance van transacties (end-to-end);

•

• Detailmonitoring van (applicatie)componenten;

Analyse en rapportage.

•

Daar waar sprake is van monitoring is ook direct sprake van logging omdat de verzamelde gegevens

vastgelegd moeten worden voor analyse.

In 2017 zal deze visie verder worden uitgewerkt en vertaald naar concrete patronen voor monitoring en

de analyse van gegevens. Daarbij wordt de samenwerking gezocht met doelarchitectuur gegevens en

afdelingen binnen UWV die al bezig zijn met bijvoorbeeld ketenmonitoring en de analyse van klikpaden.

5.2.9 Ondersteunend ABB Klantondersteuning

Co-browsing en chat

Dit bouwblok omvat een aantal functies. Ten eerste kan met dit bouwblok kan de klant door

medewerkers Klant Contact Center ondersteund worden in zijn digitale klantreis. Daarnaast kan de klant

via een chat-sessie contact opnemen met het KCC. Belangrijke aspecten van dit ABB zijn:

• Zeker stellen dat de sessie met de juiste klant wordt geopend;

Vastleggen metagegevens van de sessie (wanneer, betrokken klant, betrokken medewerker,

•

duur);

• Vastleggen chatsessie in relevant systeem;

Voorkomen dat door de klant ingevoerde gegevens bewaard blijven op de PC van de

•

medewerker.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

67 van 117

Software bouwblok Co-browsing en chat

Om dit ABB te realiseren wordt het product iAdvize ingezet voor Co-browsing en chat.

E-mailnieuwsbrief

Algemene communicatie over diensten van UWV verloopt onder andere via een E-mailnieuwsbrief. Deze

nieuwsbrief bevat nooit persoonlijke gegevens maar berichten die voor verschillende klantgroepen van

UWV interessant kunnen zijn. Deze berichten worden in één batch uitgestuurd met behulp van een

speciaal daarvoor ingericht systeem. Dit systeem staat geheel los van VDC en het KA-mail systeem dat

voor interne medewerkers beschikbaar is.

Software bouwblok E-mailnieuwsbrief

De ABB E-mailnieuwsbrief wordt voor UWV ingevuld met

5.1 lid 2 sub i

5.2.10 Ondersteunend ABB Analytics en Optimaliseren

Webanalyse

Webanalyse verzameld gegevens met betrekking tot het gebruik van de portalen. Deze gegevens zijn via

gebruiker46.

een -hash gekoppeld aan een Op grond van de verzamelde gegevens kan het klikgedrag

5.1 lid

2 sub i

van gebruikers worden onderzocht en van daaruit geoptimaliseerd.

Software bouwblok Webanalyse

De ABB Webanalyse wordt ingevuld met Webtrekk

Data analyse

Met betrekking tot het gebruik van de (digitale) dienstverlening van UWV wordt veel data verzameld. Het

doel van die dataverzameling is, onder andere, inzichtelijk te maken hoe het gebruik van diensten en

kanalen zich ontwikkeld. Daartoe wordt de data verzameld, geanalyseerd en grafisch weergegeven. Op

grond van deze informatie kan de klantervaring worden verbeterd en kan een nieuw door UWV te leveren

dienst optimaal worden ingericht.

Software bouwblok Data analyse

Dit ABB wordt – naar verwachting op termijn – gerealiseerd met het product Tableau.

Directe feedback

De ABB directe feedback wordt ingezet om te meten hoe tevreden klanten zijn met betrekking tot de

digitale dienstverlening van UWV. Aan bepaalde interacties wordt een beoordelingsvraag gekoppeld. Het

antwoord van de klant wordt, anoniem, vastgelegd voor verdere analyse en optimalisatie van de

interacties.

46

Deze hash is voor een beperkte groep medewerkers en alleen aan de hand van aanvullende gegevens te herleiden

tot het oorspronkelijke BSN zodat hier mee verdere, specifieke analyses kunnen worden uitgevoerd. Deze werkwijze is

besproken met beoordeeld en goedgekeurd door de specialisten van IB&P.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

68 van 117

Software bouwblok directe feedback

Het product waarmee dit ABB wordt ingevuld met Usabilla.

A/B Testen

A/B testen faciliteert het parallel gebruik van verschillende gebruikersinterfaces voor dezelfde interactie.

Door het gedrag van de gebruiker te meten en te analyseren met de daarvoor beschikbare ABB’s kan

vervolgende worden bepaald of een nieuwe interface beter voldoet.

Software bouwblok A/B testen

Optimizely wordt ingezet om de ABB te realiseren.

5.2.11 Ondersteunend ABB Profileren en segmenteren

UWV wil haar klanten zo veel mogelijk op informatie op maat aanbieden. Daartoe wordt informatie

verzameld vanuit de bron- en materiesystemen zowel als vanuit het online gedrag van de klant.

Als onderdeel van de ABB Personalisatie wordt een klantprofiel opgebouwd vanuit in de bronsystemen

bekende gegevens. Op grond van deze gegevens wordt bepaald welke ‘tegels’ vooraan in het portaal

worden geplaatst. In applicatiepatroon 1 (‘Opbouwen persoonlijke omgeving’) wordt dit element verder

uitgewerkt in de context van het portaal.

Software bouwblok profileren en segmenteren

Dit ABB wordt voor de publieke omgevingen voor het aanbieden van persoonlijke content ingevuld met

Blueconic. Voor de persoonlijke omgevingen is een Klant Profiel Service in ontwikkeling. Deze laatste

bevat de gegevens die bepalen welke ‘tegels’ in het portaal beschikbaar komen voor de gebruiker.

5.3 Applicatiepatronen

Binnen de onderdelen van de klantreis is een aantal dienstpatronen onderkend (zie bedrijfsarchitectuur).

In de applicatiearchitectuur vertalen deze dienstpatronen zich naar de hier beschreven

applicatiepatronen. De volgende patronen zijn hier onderkend:

Opbouwen persoonlijke omgeving is het patroon op basis waarvan middels een login het

•

hoofdscherm van de persoonlijke omgeving opgebouwd wordt;

Tonen content is het patroon waarin (web-)content – kanaalonafhankelijk - wordt opgehaald en

•

getoond;

Aanvragen dienst is het basispatroon voor het aanvragen van een UWV-dienst waarbij de klant

•

zo veel mogelijk zelfstandig kan afhandelen;

Tonen status is het patroon voor het, op initiatief van de klant, weergegeven van de status van

•

een aanvraag of een reeds afgenomen dienst;

Opvragen informatie is het patroon waarmee klanten informatie op kunnen halen bij UWV;

•

Uitvoeren verwerking is het patroon waarin door een klant in een interactie aangepaste

•

informatie wordt verwerkt in de bron- en materiesystemen;

Notificatie is het patroon waarbij een melding vanuit UWV actief naar een klant wordt gestuurd;

•

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

69 van 117

Ontsluiten externe interactie / service is het patroon dat wordt gehanteerd bij het aanbieden

•

van diensten van derden aan klanten van UWV;

App binding is het patroon voor het registreren van de combinatie gebruiker/app/apparaat

•

zodat:

o

de gebruiker via de app op eenvoudige wijze kan krijgt tot informatie binnen UWV;

o

gegevens via de app veilig kunnen worden uitgewisseld tussen gebruiker en UWV;

o

het device geschikt wordt gemaakt als onderdeel van Multi Factor Authenticatie.

De relatie tussen de dienstpatronen en de applicatiepatronen is als volgt:

t

e

Dienstpatronen

e e

m

k k k

e e

j j j

e e e

li li li

i i

t t

e e

i i i

n n n

a a

t t t

k k

c c c

n

o o o

m m

e e

a a a

e

o o o

i i

r r r r r

d

s s s

l l

e e e

o o

b b

r r r

r

Applicatiepatronen

t t t

f f

u u

e e e

e

n n n n n

## P P P P P

d

i i i i i

Opbouwen persoonlijke omgeving X

Tonen content X X

Aanvragen dienst X

Tonen status X

Opvragen informatie X X X

Uitvoeren verwerking X X

Notificatie X X X

Ontsluiten externe interactie X

Ontsluiten externe service X X

Bij de beschrijving van deze patronen wordt ook de aangegeven welke patronen voor gegevensintegratie

er bij aansluiten. De integratiepatronen zijn beschreven in de doelarchitectuur Gegevensintegratie (GEIN)

en worden daarom niet verder uitgewerkt in de doelarchitectuur E-Dienstverlening.

Deze patronen gelden als basis voor specifieke implementaties van E-Diensten. Daar waar bijvoorbeeld

sprake is van een KIA/KOA combinatie voor een aanvraag, worden deze specifiek gemaakt voor de

implementatie van een bepaald type aanvraag (Aanvraag WW, Aanvraag bestandslevering, Aanvraag

WAJONG uitkering, etc.).

5.3.1 Patroon ‘Opbouwen persoonlijke omgeving’

Dit patroon omvat het persoonlijk en persoonlijk relevant maken van de gebruikersinterface. Persoonlijk

maken houdt in het tonen van een persoonlijk gerichte welkomstboodschap en het tonen van naam en

andere identificerende informatie . Persoonlijk relevant maken is het met hoge prioriteit tonen van

5.1 lid 2

sub i

relevante diensten en het minder prominent tonen van niet-relevante diensten. De identiteit en

authenticiteit van de individu vaststellen, weten welke rechten deze persoon heeft, en vaststellen welke

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

70 van 117

diensten en/of gegevens daarbij horen is het belangrijkste aspect van dit patroon. Tevens wordt de

persoonlijke omgeving zoveel mogelijk gepersonaliseerd door middel van klantspecifieke profielen.

Structuur van het patroon

De belangrijkste onderdelen in dit patroon zijn:

1. Vaststellen identiteit, authenticiteit en rechten (autorisatie)

2. Ophalen bij KOA Klant Profiel Service welke diensten bij persoon horen

3. Ophalen bij Content Distributie welke content bij persoonlijke pagina horen

4. Tonen specifieke portaalfunctie(s) “Tegels”

5. Opstarten specifieke dienst (KIA, een voorbeeld kan bijvoorbeeld zijn Onderhouden CV)

Figuur 31, opbouwen persoonlijke omgeving

Bijzonderheden

Alle toegangsrechten worden verkregen vanuit één systeem (I&AM);

•

I&AM kan – op termijn – koppelen met diverse securityproviders zoals DigiD, iDIN, et cetera;

•

Personalisatie van het portaal vindt plaats op basis van de KOA klantprofielservice.

•

Technische realisatie

Authenticatie wordt losgetrokken van het portaal, zie ook de software bouwblokken later in dit hoofdstuk.

Dit betekent dat I&AM geïmplementeerd middels OAM de authenticatie (en ook autorisatie) van

gebruikers verzorgt. Het gebruik van OAM kan gezien worden als een gedelegeerde securityprovider

welke voor burgers nu alleen DigiD ontsluit maar op termijn ook iDIN en andere aanbieders op een voor

het portaal transparante manier kan ontsluiten. Pas wanneer een gebruiker geauthentiseerd is wordt (het

bericht van) de gebruiker doorgezet naar het portaal (of een KIA).

47.

Het portaal wordt gerealiseerd met technologie op basis van Het opbouwen van een

5.1 lid

5.1 lid 2 sub i

2 sub i

persoonlijke omgeving is, na authenticatie, feitelijk het tonen van het hoofdscherm van een portaal. Dit

47

staat voor . Dit is een patroon voor software ontwikkeling.

5.1 lid 5.1 lid 2 sub i

2 sub i

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

71 van 117

hoofdscherm toont op basis van een persoonlijk profiel tegels als een soort navigatie-elementen met

daarin (of o.b.v.) enkele persoonlijke gegevens. De verschillende tegels tonen gegevens van

verschillende bedrijfsobjecten die uit een veelvoud van systemen geleverd worden.

Om dit patroon altijd beschikbaar te maken en te voldoen aan performance-eisen wordt gebruik gemaakt

van een KOA Klantprofielservice. Deze KOA heeft een eigen data opslag voor alles wat nodig is om de

tegels op het hoofdscherm te tonen. Dit is een bijzondere vorm van ‘CDS bij consument’ aangezien het

gegevens voor meerdere bedrijfsobjecten en vanuit meerdere bronsystemen bevat en dus eigenlijk

meerdere CDS-en in zich heeft. Er wordt gekozen voor deze implementatievorm omdat het hoofdscherm

zo cruciaal is voor de persoonlijke omgeving dat deze altijd performant beschikbaar dient te zijn.

Er dient per portaal een keuze gemaakt te worden of het opbouwen van het hoofdscherm dermate

complex is en veel gebruikers kent, dat voor de hier beschreven KOA Klantprofielservice gekozen wordt.

Het is de voorkeursoplossing voor een werkzoekende- of werknemersportaal maar minder noodzakelijk in

bijvoorbeeld het Gegevensportaal waarbij de gegevens uit minder systemen komen en er sprake is van

een kleiner aantal gebruikers.

Ook het ontvangstscherm van een app zal met deze functie persoonlijke en persoonlijk relevant worden

gemaakt.

Relatie met integratiepatronen

Bij de realisatie van dit patroon kunnen de volgende integratiepatronen, zoals beschreven in de

doelarchitectuur GEIN, worden toegepast. Bij elk van de mogelijke patronen is aangegeven of dit een

voorkeurspatroon is, dan wel een optioneel patroon. Niet genoemde patronen komen niet in aanmerking.

Patroon 4 is optioneel maar het kan in bijzondere gevallen zoals hierboven beschreven wel het

voorkeurspatroon zijn.

Patroon Omschrijving V/O Opmerking

1 Bron direct (synchroon) V

3 CDS bij bron V

4 CDS bij consument O Het beheer van de CDS valt in dit geval onder

E-Dienstverlening. De gegevens binnen het CDS zijn

een kopie van de bron. De juistheid van de door de

bron aangeleverde gegevens blijft de

verantwoordelijkheid van deze bron.

5.3.2 Patroon ‘Tonen content’

Alle webcontent wordt van het portaal bij één content distributie dienst gehaald. De publieke omgeving

wordt opgebouwd vanuit de content distributie dienst. In de persoonlijke omgeving heeft de content

distributie dienst zelf geen slimheid in zich om te bepalen welke content waar getoond moet worden. De

vragende pagina’s en/of E-Diensten bepalen welke content blok getoond moet worden en vraagt deze uit

bij de content distributie service.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

72 van 117

Structuur van het patroon

Dit patroon bestaat uit een patroon voor het tonen van content in de persoonlijke omgeving (zie Figuur

32) en een patroon voor het tonen van content in de publieke omgeving (zie Figuur 33). In de

persoonlijke omgeving wordt de content in het portaal getoond binnen portaalfuncties zoals bijvoorbeeld

de portaalfunctie ‘content’ die alleen inhoud vanuit ‘content distributie’ toont (1). Daarnaast wordt

content uit de content distributie (1) binnen een KIA getoond

Figuur 32, tonen persoonlijke omgeving

Figuur 33, tonen publieke omgeving

De publieke omgeving wordt getoond vanuit een content distributie functie (1). Binnen de content

distributie worden portaalfuncties en KIA’s getoond welke gelijk aan de persoonlijke omgeving content uit

de content distributie tonen (2).

Bijzonderheden

1. De content distributie kent geen intelligentie om te bepalen welke content getoond moet worden;

2. Alle E-Diensten, op alle communicatiekanalen, o.b.v. dezelfde content distributie functie;

3. Er is één redactieproces (content management) waarin meerdere disciplines van UWV

verschillende divisies betrokken zijn.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

73 van 117

Technische realisatie

De portaalarchitectuur van de persoonlijke omgeving is gebaseerd op een portaalapplicatie welke wordt

gerealiseerd op basis van ASP.Net technologie. De content wordt vanuit de content distributie omgeving

van Tridion klaargezet als zogenaamde resources om, op het moment dat dat nodig is, binnen het portaal

en de portaalfuncties opgenomen te worden. Wanneer binnen de KIA’s content getoond dient te worden,

gebruiken de KIA’s de resources uit het content distributie omgeving op vergelijkbare wijze.

Het portaal van de publieke omgeving wordt getoond vanuit de content distributie functie welke

geïmplementeerd wordt door het Content Management Systeem (CMS) . De publieke omgeving

5.1 lid 2

sub i

kent een aantal Publieke toegankelijke interacties welke door een KIA ingevuld worden op basis van

ASP.Net en Angular gelijk aan de persoonlijke omgeving.

Relatie met integratiepatronen

Bij de realisatie van dit patroon kunnen de volgende integratiepatronen, zoals beschreven in de

doelarchitectuur GEIN, worden toegepast. Bij elk van de mogelijke patronen is aangegeven of dit een

voorkeurspatroon (V) is, dan wel een optioneel patroon (O). Niet genoemde patronen komen niet in

aanmerking.

Patroon Omschrijving V/O Opmerking

4 CDS bij consument V Deze dienst ligt geheel binnen de divisie K&S. De

inhoud wordt altijd direct vanuit de bron aan het kanaal

aangeboden, dus zonder gebruik te maken van de

integratielaag.

5.3.3 Patroon voor ‘Dienst aanvragen of wijzigen’

Het aanvraagpatroon geldt voor E-Diensten waarmee (aanstaande) klanten van UWV, via een

bedrijfsregel gestuurde vraag-en-antwoord-dialoog, aanvragen kunnen doen, inkomsten en wijzigingen

kunnen doorgeven en klachten kunnen indi0enen.

Voorbeelden van aanvragen zijn: indienen van een aanvraag WW-uitkering bij ontslag, WIA- en

beoordeling arbeidsvermogen, het aanvragen van een voorziening, het indienen van een bezwaarschrift

of een ontslagaanvraag. Voorbeelden van wijzigingen zijn: doorgeven van wijzigingen in de persoonlijke

situatie van een burger met een uitkering WW, WIA en/of Wajong.

Structuur van het patroon

1. Bij het opstarten van de KIA Aanvragen wordt o.b.v. de KOA Aanvraag (bijvoorbeeld WW

Aanvraag) bepaalt of er een niet ingediende aanvraag beschikbaar (opgeslagen) is;

2. Bij een nieuwe aanvraag is het nodig om de relevante gegevens op te halen, bijvoorbeeld de

persoonsgegevens in geval van Aanvragen WW. Ook in geval van een bestaande aanvraag kan

het nodig zijn om voorafgaand aan en tijdens de dynamische dialoog additionele gegevens op te

halen (dit wordt niet in aparte stappen in het patroon aangegeven);

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

74 van 117

3. Gebruiker controleert de getoonde persoonsgegevens en vult persoonsgegevens aan en dit wordt

bij de Aanvraag opgeslagen in de KOA Aanvraag zodat de ingevoerde gegevens niet verloren

gaan als het aanvraagproces afgebroken wordt;

4. Raadplegen KOA Bedrijfsregels om te bepalen welk vraagblok door de KIA uitgevraagd dient te

worden. Tussentijds worden de ingevoerde gegevens opgeslagen in de KOA Aanvraag (3) en

eventueel additionele gegevens opgehaald bij een KOA, zoals bijvoorbeeld KOA

Persoonsgegevens (2);

5. Na het tonen van het resultaat wordt de aanvraag ingediend.

Figuur 34, dienst aanvragen

Belangrijke kenmerken

De belangrijkste kenmerken van het aanvraag patroon is:

Aanvragen zijn altijd persoonsgebonden en vereisen daarmee dat de gebruiker is ingelogd;

•

• Aanvragen zijn altijd specifiek voor een bepaalde dienst;

Aanvragen doorlopen een vooraf ingestelde vragenlijst. Deze kan dynamisch zijn en bloksgewijs

•

gestuurd worden door de KOA Bedrijfsregels;

Aanvragen worden verstuurd naar de backofficesystemen zodra de gebruiker de aanvraag

•

indient;

Door een klant ingevoerde gegevens gaan niet verloren bij vroegtijdig afbreken van een

•

aanvraag. De klant heeft de mogelijk op een later moment zijn aanvraag af te ronden, tenzij dit

strijdig is met eisen van privacy. Dit laatste kan voorkomen bij het uitwisselen van bepaalde

medische informatie;

Alle aanvragen worden geregistreerd als zaak en voorzien van een zaaknummer;

•

Alle aanvragen worden, conform de door DIV geformuleerde eisen, opgeslagen in het archief;

•

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

75 van 117

Door een klant ingevulde en verstuurde aanvraag wordt gegarandeerd geregistreerd binnen de

•

systemen van UWV.

Technische implementatie

De KIA aanvragen wordt, net als andere KIA’s, ontwikkeld op basis van De KOA

5.1 lid 2 sub i

Aanvraag haalt een eventueel bestaande aanvraag op. Alle opvraag connecties met de KOA’s worden

synchroon geïmplementeerd en worden ontkoppeld d.m.v. het Circuit Breaker patroon (1, 2, 4). Het

vastleggen van gegevens en het indienen van de aanvraag bij de KOA Aanvraag wordt asynchroon

geïmplementeerd en wordt ontkoppeld op basis van een SAF patroon.

Als de klant de aanvraag daadwerkelijk indient bij UWV, dan worden de documenten (inclusief de

gegevens) in het elektronisch archief verwerkt, wordt een nieuwe zaak gestart en krijgt de betreffende

divisie een signaal toegestuurd voor het verder (al dan niet automatisch) afhandelen van deze aanvraag.

Geïnitieerd door de KOA Bedrijfsregels wordt de klant automatisch een bevestigingsbericht verstuurd

waarin staat dat de aanvraag is ontvangen.

De KOA Bedrijfsregels raadpleegt de BRE en heeft daarmee een directe relatie met de doelarchitectuur E-

Werken. Meer over de eisen hieraan en dit patroon is te vinden in het voorbeeld van de KIA Aanvragen

WW in het KIKO model.

Relatie met integratiepatronen

Bij de realisatie van dit patroon kunnen de volgende integratiepatronen, zoals beschreven in de

doelarchitectuur GEIN, worden toegepast. Bij elk van de mogelijke patronen is aangegeven of dit een

voorkeurspatroon is, dan wel een optioneel patroon. Niet genoemde patronen komen niet in aanmerking.

Patroon Omschrijving V/O Opmerking

1 Bron direct (synchroon) V Ophalen gegevens vanuit KOA

2 Bron direct (asynchroon) V Voorkeur voor mutaties vanuit KOA

3 CDS bij bron V

4 CDS bij consument O

5.3.4 Patroon voor ‘Tonen status’

Bij het patroon van een statusdienst wordt de klant geïnformeerd over de actuele status van een of meer

lopende zaken binnen UWV. Dit kan bijvoorbeeld een het tonen van een nieuwe taak of een document

ten behoeve van een uitkering, aanvraag, wijziging, of beëindiging zijn. In alle gevallen is informatie

vanuit de backoffice noodzakelijk.

Structuur van het patroon

1. Statusdetail informatie van een lopende zaak in de persoonlijke omgeving wordt getoond door

een portaalfunctie;

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

76 van 117

2. Hiervoor benadert de portaalfunctie een KOA (bijvoorbeeld KOA WW Aanvraag) om op basis van

een identificatie (zoals BSN) van de gebruiker de statusdetailgegevens op te vragen, al dan niet

vanuit achterliggende (zaakmanagement)systemen;

3. Indien nodig wordt de bijbehorende content opgehaald uit de content distributie.

Figuur 35, tonen status

Belangrijke kenmerken

Statusinformatie is altijd persoonsgebonden en vereist daarmee dat de gebruiker is ingelogd;

•

Het leveren van statusinformatie wordt niet opgeslagen in het archief.

•

Technische implementatie

Het tonen van statusdetail informatie wordt niet gezien als interactie de gegevens worden namelijk

getoond op basis van navigatie naar de betreffende statuspagina en op basis van de identificatie van de

gebruiker. Dit wordt dan ook geïmplementeerd door middel van een portaalfunctie (strikt gesproken

kunnen het een aantal technische componenten of een aantal portaalfuncties zijn die de pagina

opbouwen).

Des te hoger het gebruik van de statusdetail informatie des te belangrijker zijn de eisen die aan de

aanleverende KOA gesteld worden. Het gebruik van integratie patroon 1 wordt dan minder waarschijnlijk,

patroon 3 of zelf patroon 4 wordt dan relevanter en is beter in staat om de beschikbaarheid en

performance eisen voldoende te ondersteunen.

Relatie met integratiepatronen

Bij de realisatie van dit patroon kunnen de volgende integratiepatronen, zoals beschreven in de

doelarchitectuur GEIN, worden toegepast. Bij elk van de mogelijke patronen is aangegeven of dit een

voorkeurspatroon is, dan wel een optioneel patroon. Niet genoemde patronen komen niet in aanmerking.

Patroon Omschrijving V/O Opmerking

1 Bron direct (synchroon) V

3 CDS bij bron V

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

77 van 117

Patroon Omschrijving V/O Opmerking

4 CDS bij consument O De behoefte aan actualiteit van statusinformatie kan

verschillen per proces. In veel gevallen zal een

actualiteit van een half uur voldoende zijn en in slechts

enkele situaties is realtime statusinformatie

noodzakelijk.

5.3.5 Patroon voor ‘Opvragen informatie’

Het patroon voor informatievragen dient als basis voor alle diensten waarbij een klant algemene (of

specifieke) informatie vraagt bij UWV.

Structuur van het patroon

1. Informatie kan opgevraagd worden als onderdeel van een portaalfunctie of een KIA;

2. Vanuit de portaalfunctie of KIA worden gegevens opgevraagd bij een KOA;

3. Indien content nodig is, haalt de portaalfunctie of KIA deze op bij de contentdistributiefunctie en

toont gegevens en content.

Figuur 36, opvragen informatie

Een uitbreiding van het basis patroon voor opvragen informatie is opvragen van informatie met een

bestand. Dit bestand kan een document (bijvoorbeeld een PDF bestand dat uit EA opgehaald wordt) zijn

maar ook een Bulklevering. Bij een Bulklevering worden gegevens met betrekking tot meerdere klanten

in een bestand aangeboden. Deze verlopen standaard via het portaal MijnGegevensdiensten op uwv.nl.

Het volgende diagram geeft de structuur voor het uitgebreide patroon van het opvragen van informatie

met een bestand.

Structuur van het uitgebreide patroon

1. Informatie kan opgevraagd worden als onderdeel van een portaalfunctie of een KIA;

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

78 van 117

2. Vanuit de portaalfunctie of KIA worden gegevens opgevraagd bij een KOA. Hierbij wordt tevens

de referentie van een bestand in het bestand management gegeven aan de KIA;

3. Indien content nodig is, haalt de portaalfunctie of KIA content op bij content distributie en toont

gegevens en content;

4. De gebruiker kan in de portaalfunctie of KIA de download link selecteren om het bestand te

downloaden. Het bestand kan een document of Bulklevering zijn.

Figuur 37, opvragen informatie incl. bestand

Een voorbeeld van informatie opvragen als onderdeel van een Portaalfunctie is het “Ophalen van een

Bewijs van inschrijving”. Dit is een functionaliteit in de persoonlijke omgeving van werk.nl waarbij een

werkzoekende een link selecteert een het Bewijs van inschrijving gedownload wordt. Een document kan

ook gedownload worden in een KIA zoals bijvoorbeeld een document bij een bericht in werk.nl of een

leveringsbestand in het Gegevensportaal op uwv.nl.

Bijzonderheden

De informatie die opgevraagd wordt is persoonsgebonden of gebonden aan de organisatie van de

•

gebruiker (o.a. in het geval van Bulklevering).

Technische implementatie

De portaalfunctie en de KIA wordt op de standaard wijze geïmplementeerd. Het benaderen van de KOA

gebeurt in principe synchroon omdat er informatie opgehaald wordt waarop de gebruiker wacht.

Ontkoppeling vindt plaats door middel van het Circuit Breaker patroon. In hoeverre de KOA of een

bronsysteem van een CDS gebruikt maakt is afhankelijk van de specifieke use case en de betrokken

applicaties. Het bestandmanagement kan een DMS voor E-Dienstverlening zijn

5.1 lid 2 sub i

, een leverend systeem voor Bulkleveringen op Mijngegevens portaal, maar kan

5.1 lid 2 sub i

bijvoorbeeld ook het EA of Polis zijn.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

79 van 117

Van belang bij het downloaden van gegevens is goed te bepalen welke route het download bestand aflegt

naar de gebruiker. Het is bijvoorbeeld niet zonder meer mogelijk om bij grote gebruikersaantallen een

groot bestand via een OSB of een API-Gw te routeren.

Relatie met integratiepatronen

Bij de realisatie van dit patroon kunnen de volgende integratiepatronen, zoals beschreven in de

doelarchitectuur GEIN, worden toegepast. Bij elk van de mogelijke patronen is aangegeven of dit een

voorkeurspatroon is, dan wel een optioneel patroon. Niet genoemde patronen komen niet in aanmerking.

Patroon Omschrijving V/O Opmerking

1 Bron direct (synchroon) V Indien bron hoog-performant en –beschikbaar is.

2 Bron direct (asynchroon) O Bij Bulklevering. Dit is een uitzonderingssituatie.

3 CDS bij bron V V bij Bulklevering-synchroon

4 CDS bij consument O Alleen bij ‘niet-bulk’ levering

5 CDS in integratiedomein O Alleen bij Bulklevering. Wordt de komende jaren nog

niet gerealiseerd.

6 CDS + DVS O Alleen bij Bulklevering. Wordt de komende jaren nog

niet gerealiseerd.

8 (Bulk-)leveringen V Dit is het standaard patroon voor de Informatiedienst

voor bulkleveringen, waarbij het EPM als CDS fungeert,

maar ook de KOA functionaliteit levert. De feitelijke

leveringen komen verschillende systemen.

5.3.6 Patroon voor ‘Uitvoeren verwerking’

Het patroon ‘uitvoeren verwerking’ wordt toegepast wanneer, als onderdeel van de interactie in een KIA,

gegevens (en eventuele documenten) verwerkt moeten worden in bron- en materiesystemen. Dit patroon

werkt zonder een bedrijfsregel gestuurde vraag-en-antwoord-dialoog.

Structuur van het patroon

1. Tijdens de interactie geeft de KIA (bijvoorbeeld KIA Onderhouden CV) een bericht met de te

muteren gegevens door aan een KOA (bijvoorbeeld KOA CV bij het event activeren CV).

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

80 van 117

Figuur 38, uitvoeren verwerking

Een alternatief op dit basispatroon is het verwerken van gegevens waarbij tijdens de interactie een

bestand door een gebruiker wordt toegevoegd.

1. Het bestand wordt binnen de KIA geüpload naar een veilige omgeving;

2. De KIA stuurt bestandreferentie naar de KOA voor inchecken;

3. De KOA slaat bestandreferentie op een initieert Bestand Management voor inchecken;

4. Bestand management checkt het bestand op virussen en andere malware;

5. Bestand management geeft aan KOA door dat bestand is ingecheckt en dit wordt bij de KOA

geregistreerd. De KOA verwerkt vervolgens het bestand.

Figuur 39, uitvoeren verwerking met bestand

Een voorbeeld is het uploaden van een aanvraag voor een gegevenslevering waarbij bijvoorbeeld eerst

een lijst van BSN’s door een gebruiker aangeleverd wordt.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

81 van 117

Technische implementatie

De upload van het bestand vindt altijd plaats op een veilige, geïsoleerde, omgeving waarbij een

virusscanner het bestand valideert voor verdere verwerking.

Relatie met integratiepatronen

Transacties volgens dit patroon zorgen voor verwerking van gegevens inde bron- en materiesystemen.

Daarmee kan geen gebruik gemaakt worden van een CDS zodat hier geen relatie met integratiepatronen

conform GEIN.

5.3.7 Patroon voor Notificatie

Het patroon voor Notificatie wordt toegepast indien UWV de klant actief informeert. Het kan dan

bijvoorbeeld gaan over een wijziging in een status (naar toegekend/afwijzen) of een bestand dat

beschikbaar is. Notificaties kunnen per email, SMS en naar de mobiele app worden gestuurd. Een klant

kanaal48.

kan aangeven in zijn profiel waarover de klant genotificeerd wilt worden en via welk Het gaat in

notificaties vooral om operationele instructies en niet om officiële uitingen. Om die reden wordt een

notificatie niet in het EA opgeslagen.

Structuur van het patroon

1. Het patroon wordt gestart: a.) o.b.v. een trigger uit een KOA aangestuurd als onderdeel van een

interactie op één van de digitale kanalen of een event uit het achterland of b.) o.b.v. een trigger

direct uit een applicatie in het achterland. In alle gevallen start de KOA Notificatie met het

notificatieberichttype en inhoudelijke berichtgegevens.

Bij het ontwerp van de individuele notificaties moet er voor worden gezorgd dat een klant niet

meerdere notificaties voor hetzelfde event krijgt;

2. De KOA Notificatie bepaalt op basis van informatie in de KOA KlantContactVoorkeur of en via welk

kanaal de notificatie verstuurt dient te worden;

3. De KOA Notificatie stuurt de notificatie door aan de KOA voor het desbetreffende

communicatiekanaal;

4. De KOA voor het desbetreffende communicatiekanaal (email, SMS, mobiele applicatie) maakt de

notificatie op overeenkomstig het kanaal en verstuurt het bericht.

48

Zie ook ‘Beheren klantcontactvoorkeuren’ in paragraaf 4.5.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

82 van 117

Figuur 40, notificatie

Bijzonderheden

• Opmaak van het notificatiebericht vindt plaats in de KOA die de daadwerkelijke communicatie

verzorgt;

Technische implementatie

De implementatie van het notificatiepatroon gebeurt op basis van het eventmechanisme. Hierdoor wordt

de notificatie losgekoppeld van de rest van de transactie. De KOA’s SMS, Mobiel Notificatie en E-mail

roepen de kanaal specifieke technische communicatieservices aan zoals een SMTP server voor E-mail.

Relatie met integratiepatronen

Geen directe ontsluiting van bronsystemen anders dan dat bronsystemen de notificatie via een

eventmechanisme kunnen aansturen.

5.3.8 Patroon voor ‘Ontsluiten externe dienst’

Binnen het digitale landschap van UWV worden steeds vaker diensten van ketenpartners ingezet. Dit

patroon bevat een patroon voor het ontsluiten van externe interactie en een patroon voor het ontsluiten

van een externe service.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

83 van 117

Structuur van dit patroon

Het patroon voor het ontsluiten van externe interactie is als volgt.

1. Vanuit het portaal, een portaalfunctie of een KIA wordt de externe interactie in de vorm van een

externe site opgestart.

Figuur 41, ontsluiten externe interactie

Een voorbeeld voor een externe interactie is bijvoorbeeld de externe E-Learning site waarnaar vanuit

werk.nl genavigeerd kan worden.

Het patroon voor het ontsluiten van een externe service is als volgt.

1. Vanuit een portaalfunctie of een KIA is informatie nodig van een externe service. Deze informatie

wordt opgevraagd bij een KOA.

2. De KOA reguleert de toegang tot de externe service.

Figuur 42, ontsluiten externe service

Bijzonderheden

Patroon Externe interactie: de externe interactie is zelf verantwoordelijk voor het authentiseren

•

en autoriseren van gebruikers;

Patroon Externe service: Bij gebruik van een externe service bewaakt de KOA dat de gebruiker de

•

juiste rechten heeft voor deze service;

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

84 van 117

Technische implementatie

Patroon Externe interactie

Tussen het portaal en de externe interactie zit geen koppeling in de vorm van Single Sign On (SSO). De

gebruiker dient, indien nodig, opnieuw in te loggen op de externe interactie.

Patroon Externe service

De externe service wordt altijd via een KOA aangeroepen. De KOA verzorgt het aanbieden van een stabiel

servicecontract aan de KIA ongeacht een verandering van het servicecontract van de externe service. Bij

de KOA die een externe service aanroept gelden dezelfde implementatie richtlijnen als bij KOA’s die

interne systemen aanroepen. Het is bij een externe service nog belangrijker dat de eisen (bijvoorbeeld

betreffende beschikbaarheid en performance) helder worden afgesproken met de externe leverancier. Dit

betreft vaak formele contracten welke niet zomaar gewijzigd kunnen worden. Ook is nog belangrijker om

te ontwerpen voor de foutsituatie, d.w.z. hoe reageert de KIA en de KOA als de externe service niet of

slecht beschikbaar is.

Relatie met integratiepatronen

De integratie patronen worden alleen toegepast bij externe service. Bij de realisatie van dit patroon

kunnen de volgende integratiepatronen, zoals beschreven in de doelarchitectuur GEIN, worden toegepast.

Bij elk van de mogelijke patronen is aangegeven of dit een voorkeurspatroon is, dan wel een optioneel

patroon. Niet genoemde patronen komen niet in aanmerking.

Patroon Omschrijving V/O Opmerking

1 Bron direct (synchroon) V Externe dienst wordt altijd rechtstreeks benaderd en

maakt geen gebruik van opslag van voor die specifieke

gegevens binnen UWV. Een voorbeeld is Suwinet Inkijk.

8 (Bulk)leveringen V Externe dienst verloopt via tussenschakels, het EPM en

wellicht ook overheidsbrede voorzieningen. Digilevering

kan in de toekomst een mogelijkheid zijn.

5.3.9 Patroon voor Aanmelden herkenningsmiddel

Het patroon voor het aanmelden van een herkenningsmiddel is een patroon dat wordt gebruikt om een

middel voor persoonsherkenning (authenticatie) bij UWV aan te melden. Na deze eenmalige aanmelding

kan de klant zichzelf, met dit specifieke middel, identificeren tijdens het afnemen van UWV diensten.

Voorbeelden hiervan zijn het aanmelden van een mobiel device door middel van device/app binding of

IDIN (aanmelden via bankherkenning).

Bij aanmelden van een herkenningsmiddel geeft de klant zelf aan via welk middel hij/zij wil worden

herkend en bewijst vervolgens dit middel inderdaad in bezit te hebben door de aanmelding elektronisch

te bekrachtigen (“signen”)

Een bijzondere vorm hiervan is “App binding”, waarbij naast aanmelden van het middel ook de activering

van dat middel wordt gedaan.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

85 van 117

Tijdens aanmelden gaat de gebruiker akkoord met de gebruikers voorwaarden en het feit dat de eIDAS

sterkte van het middel wordt geadopteerd. Daarmee wordt de gebruiker ook op de hoogte gesteld van

het niveau waarop hij zich kan authentiseren en welke groepen diensten daarmee beschikbaar zijn.

Het patroon voor Device/app binding is een patroon dat in principe eenmalig wordt gevolgd indien de

klant een UWV app (opnieuw) installeert op zijn device. Indien UWV een nieuwe versie van een

bestaande app aanbiedt, blijft de binding geldig.

Structuur van dit patroon

Dit patroon zijn zowel de App als een portaal-KIA en I&AM betrokken zoals getoond in Figuur 43, App

binding.

Figuur 43, App binding

Het gevolgde patroon is hierbij als volgt:

1. De gebruiker bereidt het aan te melden device voor om te activeren (optioneel indien device nog

niet is geactiveerd);

2. De gebruiker maakt zichzelf bekend en start het aanmeldproces (KIA);

3. De gebruiker kiest het aan te melden middel (soort en id.);

4. Gebruiker gaat akkoord met de gebruiksvoorwaarden van het middel in combinatie met de UWV

diensten;

5. Gebruiker accordeert de aanmelding door het bezit van het device aan te tonen (signen) (in het

geval van een nog niet geactiveerd middel wordt dit voorbereid middels een activeringscode);

6. Met de activeringscode wordt het middel geactiveerd en het middel definitief aangemeld

(optioneel).

Elk volgende keer dat de gebruiker zijn App gebruikt en opent met zijn pincode, wordt de binding

gecontroleerd in de KOA Binded_dev voordat de gebruiker informatie krijgt vanuit de relevante KOA’s.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

86 van 117

Bijzonderheden

Bij dit patroon zijn zowel de app als het portaal betrokken.

•

Technische implementatie

Het binding proces moet altijd volledig worden afgerond binnen een beperkte tijd. Dit vereist een volledig

synchroon proces met daarin synchrone communicatie.

Relatie met integratiepatronen

Voor dit patroon zijn geen integratiepatronen voorzien.

5.4 Software Bouwblokken (SBB)

Onderstaand diagram toont een overzicht van de software bouwblokken op basis van de architectuur

bouwblokken zoals eerder in dit hoofdstuk beschreven.

5.1 lid 2 sub i

5.1 lid 2

5.1 lid 2 sub

sub i

i

5.1 lid 2 sub i

5.1 lid 2

5.1 lid 2 sub i

5.1 lid 2 sub

5.1 lid 2 sub i

5.1 lid 2 sub i

sub i

i

5.1 lid 2 sub

5.1 lid 2 sub i

i

5.1 lid 2 sub i

5.1 lid 2

5.1 lid 2

sub i

sub i

Figuur 44, totaaloverzicht van bouwblokken

5.1 lid 2 sub i

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

87 van 117

5.1 lid 2 sub i

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

88 van 117

Bouwblok Omschrijving

KOA’s Uitkeren, SMZ, … De KOA’s welke, via de bedrijfsobjecten, diensten van de verschillende

divisies ontsluiten voor de digitale kanalen.

KOA’s K&S De KOA’s welke, via de bedrijfsobjecten, diensten van de K&S divisies

ontsluiten en KOA’s die de klantreis ondersteunen (zoals de

Klantprofielservice). Deze KOA’s worden geïmplementeerd op basis van

ASP.Net.

KOA’s Werkbedrijf De KOA’s welke, via de bedrijfsobjecten, diensten van het Werkbedrijf

ondersteunen. Deze KOA’s zijn op dit moment geïmplementeerd op

basis van producten zoals de

5.1 lid 2 sub i 5.1 lid 2 sub i

DMS Bijzondere KOA welke in gebruik is onder werk.nl om, nog niet definitief

gemaakte of nog niet verstuurde documenten van gebruikers online

altijd beschikbaar te hebben en niet afhankelijk te zijn van applicaties in

het achterland.

Vooralsnog is hier gekozen voor de omdat

5.1 lid 2 sub i

dit goed functioneert binnen werk.nl. Een breder onderzoek zal duidelijk

maken welk product hier voor de langere termijn wordt gekozen.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

89 van 117

6 Infrastructuur Architectuur

Het fenomeen ‘always connected’ maakt dat ook de klanten van UWV 24 uur per dag toegang willen

hebben tot diensten van UWV. In combinatie met het streven van UWV om een stabiele, kwalitatief

goede en veilige dienstverlening te bieden stelt dat hoge eisen aan de infrastructuur voor E-Dienst-

verlening.

Op het moment van schrijven van deze doelarchitectuur, is de infrastructuur ondergebracht bij één

hosting provider, Keuzes moeten echter zo veel mogelijk onafhankelijk zijn van een specifieke

5.1 lid

2 sub i

leverancier. Dit wordt nog een versterkt door de ontwikkelingen van een nieuwe datacenter strategie in

verband met een nieuwe aanbesteding voor hosting, na afloop van het huidige contract met IBM.

De doelarchitectuur E-Dienstverlening zal zo veel mogelijk aansluiten bij de datacenter strategie, maar

zal ook haar invloed hebben op deze strategie. Juist in het domein waarin E-Dienstverlening opereert, is

meer en meer sprake van clouddiensten. Het is dan ook te verwachten dat traditionele infrastructuur op

termijn geïntegreerd moet worden met clouddiensten, in welke vorm (Iaas, PaaS, SaaS, XaaS) dan ook.

Daarmee ontstaat een hybride infrastructuur, inclusief de daarbij behorende nieuwe coördinatie

mechanismen.

Het gebruik van cloudtechnologie stelt ook eisen aan de wijze waarop applicaties worden ontwikkeld.

Deze moeten zogenaamd cloud ready zijn en cloud native ontwikkeld worden, ook als ze (in eerste

instantie) in een traditionele hosting omgeving draaien.

6.1.1 Functies binnen de infrastructuur

Functies in relatie tot infrastructuur zijn in drie lagen in te delen:

Technische infrastructuur diensten: hieronder vallen de rekenkracht (CPU) en opslag van data,

•

zowel on-premise als in de cloud. In de situatie van UWV worden deze diensten zonder uitzondering

geleverd door partijen buiten UWV. De inrichting van deze infrastructuur moet aansluiten bij o.a. de

bi-modal gedachte zodat verschillende divisies hun eigen tempo kunnen volgen bij het realiseren van

aanpassingen.

• Platformdiensten: omvat diensten om de onderliggende technische infrastructuur beschikbaar te

stellen en te beheren. Deze platformdiensten worden geleverd door partijen buiten UWV.

Regie: besturing van ontwikkeling en realisatie van de onderliggende lagen. Deze activiteiten worden

•

deels binnen UWV en deels door externe partijen uitgevoerd. Welke activiteiten bij welke partij (c.q.

afdeling van UWV) worden belegd is onderdeel van de datacenter strategie en aanbesteding en de

contractering ter zake.

Grafisch kunnen deze lagen als volgt worden weergegeven:

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

90 van 117

Figuur 45, lagen in de infrastructuur

6.1.2 Eisen aan de infrastructuur

Om de gewenste mate van veranderbaarheid in de digitale dienstverlening te borgen is gekozen voor

ontkoppeling van de klantinteractie en de verwerking in de bron- en materiesystemen. Daarmee ontstaat

ook de eis om flexibel gebruik te kunnen maken van infrastructurele componenten, bijvoorbeeld bij het

verwerken van piekbelastingen.

De concrete (niet functionele) eisen aan de infrastructuur zijn opgesteld aan de hand van ISO25010 en

opgenomen in hoofdstuk 3.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

91 van 117

Voortbrenging

In de voortbrengingsketen wil UWV gebruik maken van Cloud gebaseerde principes. Snelle uitrol van

virtuele machines voor ontwikkelaars en functionele testers middels selfservice. Een on-demand

ontwikkel- en testomgeving is een belangrijke randvoorwaarde voor succesvolle agile

voortbrengingsprocessen. Het regime op de acceptatie en productieomgeving is veel meer rigide. Hier

voeren stabiliteit en beheersbaarheid de boventoon in de requirements.

6.2 Infrastructuur E-Dienstverlening

De infrastructuur voor E-Dienstverlening omvat infrastructuur voor alle kanalen. De onderstaande plaat

toont hoe de samenhang is tussen de Bouwblokken en de Infracomponenten. Daarbij is te zien, dat

componenten die in de applicatie architectuur met elkaar overeenkomen, ook op gelijke

infrastructuurcomponenten landen. Conform de noodzaak voor ‘gescheiden rijbanen’ blijven componenten

behorende bij verschillende kanalen logisch van elkaar gescheiden. Dit betekent niet dat ook de fysieke

infrastructuur gescheiden moet blijven. Het al dan niet scheiden in de fysieke infrastructuur wordt

bepaald vanuit de capaciteitsbehoefte van de verschillende componenten.

5.1 lid 2 sub i

5.1 lid 2 sub i

5.1 lid 2 sub i

5.1 lid 2 sub i

De bouwblokken zijn verdeeld over verschillende infrastructuur zones. De app draait op het specifieke

device van de klant en valt daarmee in de niet-vertrouwde (untrusted) zone.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

92 van 117

Berichten tussen de app en UWV worden versleuteld met behulp van SSL. In de half-vertrouwde (semi-

trusted) zone worden de berichten ontsleuteld en wordt gecontroleerd of de gebruiker en zijn apparaat

bekend zijn binnen UWV. Als dat zo is, wordt de verbinding tussen app en UWV systemen in de

vertrouwde (trusted) zone tot stand gebracht.

Bij de keuze voor infracomponenten wordt gebruik gemaakt van componenten die binnen UWV als

standaard zijn gekozen.

6.3 SBB’s en infrastructuurcomponenten

De Software BouwBlokken zoals die binnen de applicatiearchitectuur zijn benoemd vereisen bepaalde

infrastructuurcomponenten. Deze relaties zijn als volgt:

•

5.1 lid 2 sub i

5.1 lid 2 sub i

Portaalfunctie + KIA’s

•

o

Webserver, Applicatieserver RDBMS Server;

o

IIS en SQL server op X86 Virtueel Winserver 2016 platform

•

5.1 lid 2 sub i

•

5.1 lid 2 sub i

Interfacemanager / API Gateway

•

o

nog te verwerven product. Na verwerving kan onderliggende infrastructuur worden

vastgesteld.

• KOA’s K&S

o

5.1 lid 2 sub i

KOA’s

•

o

ter beoordeling van leverende divisies

App

•

o

iOS en Android voor zowel mobile devices als tablets

6.3.1 Gescheiden rijbanen

De KIA/KOA structuur beschrijft op applicatieniveau het principe van gescheiden rijbanen (zie paragraaf

5.1.7.). Op welke wijze dit in de infrastructuur kan worden gerealiseerd vereist nadere uitwerking.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

93 van 117

## Bijlage A, Gebruikte bronnen

Bij de verder ontwikkeling van de doelarchitectuur worden diverse bronnen gebruikt, waaronder:

Doelarchitectuur E–Dienstverlening van januari 2016;

•

• UWV Informatie Plan 2016 - 2020;

NORA (Nederlandse Overheid Referentie Architectuur) 2.0;

•

• [API GW documenten]

Portaalarchitectuur juli 2016

•

Presentaties over E-Dvl in AB van 1, 8 en 15 december 2016

•

Verantwoordelijkheidsverdeling E-Diensten 20161017

•

Presentaties over Basisplatform App Diensten in AB van juli t/m september 2017

•

PSA Failsafe (2017)

•

1. Corporate factsheet UWV juli 2016. “Ned_Corporate_factsheet_tcm5-215250.pdf” .

2. Passend digitaal 18 juni 2015. “01.2 definitieve notitie passend digitaal 19-6.docx;

3. Doelarchitectuur E-Dienstverlening 26 november 2015 v0.95. doelarchitectuur E-Dienstverlening

20151126.pdf.

4. UWV Informatieplan 2016 – 2020 Puzzelen met prioriteiten.

5. Digitale Dienstverlening Werkgevers Roadmap. 20160930 Verandervrijdag - Roadmap Werkgevers

1.0.pdf.

6. https://www.rijksoverheid.nl/documenten/rapporten/2016/12/07/rapport-digitale-contacten-met-de-

overheid

7. Digitale Strategie v1.0, februari 2017

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

94 van 117

## Bijlage B, Ontwikkelingen digitale dienstverlening

Deze bijlage schetst de verschillende externe en UWV ontwikkelingen die van invloed zijn op inrichting van digitale

dienstverlening.

B.1 Externe ontwikkelingen

De externe ontwikkelingen worden, onderverdeeld naar klantbehoefte, technologie en wet- en regelgeving, hierna

beschreven.

B.1.1 Klantbehoefte

De verschillende klantgroepen: burgers, werkgevers, keten- en zakelijke partners kennen ieder hun eigen behoeften.

Burgers

De digitalisering van de maatschappij betekent dat de burger van bedrijven en organisaties verwacht dat steeds meer

zaken digitaal afgehandeld kunnen worden waar en wanneer de klant dit wil. De burger verwacht vergelijkbare

dienstverlening als met andere publieke maar ook zeker met private organisaties.

Het mobiele gebruik neemt in de komende jaren verder toe. Dit betekent dat de behoefte voor het gebruik van digitale

media4.

diensten verschuift van de portalen naar apps (tablet/smartphone) en een uitbreiding op social

Grootschalige digitalisering geeft naast nieuwe kansen ook nieuwe bedreigingen. Een digitale informatiemaatschappij

is alleen mogelijk als het vertrouwen van de burger daarin niet kan worden beschadigd door grootschalig misbruik of

(identiteit)fraude3.

Het goed functioneren van de dienstverlening van UWV staat of valt met de wil van de burger om informatie te delen.

Voor de meeste wetgevende taken geldt hiervoor de plicht om informatie te delen.

Vanuit het perspectief van de burger is het van belang dat de digitale dienstverlening in goede samenhang verloopt

met de “niet” digitale dienstverlening. Hier liggen twee verschillende behoeften achter: enerzijds vanuit het niet

digivaardig zijn en anderzijds vanuit het samenhangend gebruik van de verschillende kanalen. UWV zal altijd niet

digivaardige klanten ondersteunen. Hiertoe zijn we vanuit de maatschappelijke positie van UWV toe verplicht.

Daarnaast beweegt de klant in zijn klantreis door verschillende kanalen heen. Hierbij is het voor de klant van belang

deze verschillende interactiemomenten in samenhang te kunnen zien. Deze behoefte geldt daarbij ook voor de UWV

medewerker die de klant helpt bij het beantwoorden van zijn vraag of ondersteuning geeft in de weg naar werk.

Werkgevers

De behoefte van werkgevers vertoont veel overeenkomsten met de burgers. Meer specifiek ervaren werkgevers de

## UWV5:

volgende knelpunten bij de dienstverlening van

• Werkgevers willen digitaal zaken doen met UWV en verwachten hier een basisniveau zoals ze gewend zijn

bij andere organisaties.

Werkgevers willen een goeie ervaring hebben in de performance en betrouwbaarheid van het platform.

•

• Diensten moeten voldoen aan het vereiste beveiligingsniveau.

Werkgevers willen status informatie over o.a. opgestuurde stukken, aanvragen en tijdstip waar men wat

•

kan verwachten

Werkgevers missen digitale diensten in klantprocessen waardoor ze niet zelfredzaam en efficiënt zaken

•

kunnen doen met UWV.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

95 van 117

Werkgevers willen de dienstverlening over verschillende kanalen heen in samenhang kunnen gebruiken.

•

De werkgever heeft de volgende behoeften:

Als werkgever wil ik mijn basis administratieve taken digitaal kunnen doen; aanvragen, muteren,

•

correspondentie inzien;

• Als werkgever wil ik genotificeerd worden wanneer er wat voor mij klaar staan of, wanneer ik wat kan

verwachten of wanneer ik wat moet doen;

• Als werkgever wil ik worden geholpen in een persoonlijke omgeving die overzicht bied;

• Als werkgever wil ik kunnen aangeven hoe ik wil dat UWV digitaal met mij in contact treedt en hoe ik digitaal

met UWV in contact wil zijn;

Als werkgever wil ik mobiel goed en snel mijn diensten kunnen afnemen, zodat ik aan mijn verplichtingen

•

voldoe;

• Als werkgever wil ik alle diensten digitaal afnemen, zodat ik zelfredzaam kan zijn.

Als werkgever wil ik gegevensuitwisseling digitaal zodat deze direct verwerkt kunnen worden in mijn

•

administratieve systemen.

Werkgevers worden onderverdeeld naar grootte: kleine, middelgrote en grote werkgevers. Op dit moment vindt de

dienstverlening plaats via de werkgevers portalen op uwv.nl en werk.nl. Daarnaast kan verzuim via Digipoort gemeld

worden.

Ketenpartners

UWV heeft een wettelijk plicht tot samenwerken op het gebied van processen en delen van diensten. Het UWV voert

voor de gemeente de inschrijving Werk uit en de digitale aanvraag WWB. Hiervoor delen we als UWV de hulpmiddelen

die we zelf gebruiken, zoals portaalomgevingen, met onze ketenpartners. Door vraag en aanbod in Nederland en in

Europa transparant te maken op werk.nl stimuleren we de arbeidsmarkt. Binnen de beleidsruimte wordt deze

samenwerking nog verder versterkt door onderlinge afspraken te maken.

Zakelijke partners

UWV levert aan verschillende partners gegevens ter ondersteuning van het primaire proces van deze partner. Hier kan

gedacht worden aan pensioenfondsen voor het gebruik van inkomstengegevens uit de polisadministratie voor het

vaststellen van pensioenrechten; het CBS voor het gebruik van uitkeringsgegevens voor het samenstellen van

statistieken of arbeidsmarktinformatie voor beleidsmakers.

Het zakelijk portaal stelt interne UWV-partijen in staat gegevensbestanden te delen met externe partijen, zoals

gemeenten of pensioenuitvoeringsorganisaties. Deze externe partijen kunnen op het portaal inloggen en – afhankelijk

van de contracten die zij hebben – toegang krijgen tot de verschillende leveringen (gegevensproducten). De interne

UWV-partijen die leveringen aan willen bieden, kunnen snel, eenvoudig, goedkoop, veilig en volautomatisch gebruik

maken van deze functionaliteit. De voorzieningen die dit mogelijk maken zijn zowel in te zetten voor periodieke

leveringen als voor ad hoc opdrachten.

B.1.2. Technologie

Technologie ontwikkelingen welke impact hebben op digitale dienstverlening groeperen zich in een aantal thema’s.

Infrastructuur

De infrastructuur wordt door de leverancier overwegend ‘bare metal’ geleverd (voor elke applicatie een nieuwe

computer in het rekencentrum) waar de marktstandaard virtualisatie is (meerdere applicaties maken slim gebruik van

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

96 van 117

rekencentrum)4.

meerdere computers in het Op het vlak van infrastructuur zijn diverse ontwikkelingen gaande zoals:

(Hybrid) Cloud computing en Software Defined Datacenter (SDDC), Software Defined Networking (SDN) en

verregaande automatisering van het beheer.

Software Ontwikkeling en Implementatie

De laatste jaren zijn nieuwe manieren voor software ontwikkeling en implementatie geïntroduceerd:

Scrum / Agile en het Scaled Agile Framework (SAFe);

•

• DevOps teams;

• Automatiseren van software testen en implementatie (deploy);

Microservices: een specialisatie van en implementatie aanpak voor service-oriented architectures (SOA)

•

gebruikt om flexibel, zelfstandig inzetbare software systemen te bouwen;

• Software containers zoals bijvoorbeeld Docker. Docker containers verpakken een stukje software in een

bestandssysteem dat alles bevat wat nodig is om te draaien: code, runtime, systeemtools,

systeembibliotheken - iets dat op een server kan worden geïnstalleerd. Dit garandeert dat de software zich

altijd op dezelfde wijze gedraagt, ongeacht de omgeving.

Bigdata / A.I. / Machine learning – Personalisatie en Virtueel assisteren

Begrippen als bigdata, kunstmatige intelligentie en machine learning worden steeds krachtiger ingezet voor

kennismanagement en semantische systemen. Voor digitale dienstverlening hebben we het hier bijvoorbeeld over

systemen die het gedrag en transacties van klanten vertalen in een klantprofiel op basis waarvan de dienstverlening

persoonlijk en in context geplaatst wordt. Hiervoor zijn inmiddels diverse ondersteunende technologieën en producten

beschikbaar. Verregaande ondersteunen van de klant bijvoorbeeld door virtueel assisteren gaat in toenemende mate

een rol spelen. Er zijn al diverse digitale assistenten op de markt.

Identificatie en autorisatie

De drempel tot inloggen daalt en vervaagt. Daarnaast worden mogelijkheden om tot vertrouwelijke informatie te

komen uitgebreid. Voorbeelden hiervan zijn biometrisch, social logins. Randvoorwaarde hierbij zijn de B&P eisen die

gesteld worden aan het authenticatieniveau van de specifieke dienstverlening.

Internet of Things

Het introduceren van landelijke Internet of Things (IoT) toepassingen in Nederland wordt steeds reëler gezien het

recentelijke nieuws over de implementatie van twee nieuwe landelijke netwerken gebaseerd op NarrowBand

technologie naast het bestaande landelijke KPN netwerk gebaseerd op LoRa (Long Range Wide Area) technologie.

Hierdoor kan IoT mogelijk in de toekomst de dienstverlening van UWV ondersteunen.

De toepasbaarheid van IoT is nog onderwerp van discussie binnen UWV. Belangrijk onderwerp in deze discussie in de

veiligheid van het IoT.

B.1.3 Wet- en regelgeving

De volgende ontwikkelingen op het gebied van wet- en regelgeving zijn relevant voor digitale dienstverlening.

Een belangrijke ontwikkeling is de decentralisatie van taken van de centrale overheid naar gemeenten in het kader van

de Participatiewet. Dit betekent een andere rol voor UWV. Verder wil de overheid kostenbesparing bereiken door

overheidspartijen3.

betere samenwerking tussen

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

97 van 117

Daarnaast wordt een verdere verschuiving verwacht van de publieke naar private sector. Voor de WGA en ZW kunnen

meer werkgevers zich privaat gaan verzekeren. Bij deze verschuivingen en ontwikkelingen wordt van organisaties als

systemen3.

UWV verwacht dat zij beschikken over flexibiliteit, wendbare processen en

Via de Wet Generieke Digitale Infrastructuur (WGDI) en de aanpassingen van de Algemene Wet Bestuursrecht (AWB)

zet de overheid herbruikbare centrale voorzieningen neer zoals DigiD en e-Herkenning en stelt het de overheid

verplicht om het voor klanten mogelijk te maken om volledig digitaal met de overheid te communiceren. Meest recente

ontwikkeling binnen wetgeving op dit gebied is de Wet Open Beleid (WOO).

Naast wetgeving binnen Nederland is Europese wet- regelgeving ook een belangrijke drijfveer in ontwikkeling en

verandering van digitale dienstverlening. Deze regelingen geven inrichting aan Europese samenwerking en

uitwisseling.

B.2 UWV Ontwikkelingen

B.2.1. Strategie digitale dienstverlening

De digitale dienstverlening richt zich op het digitaliseren van de klantcontacten en klantinteractie waarbij uitstekende

dienstverlening en klanteigen kanaalkeuzes aan de kernbegrippen zijn. Digitale Dienstverlening brengt de

dienstverlening naar de klant toe. De visie laat zich verwoorden in het onderstaande motto:

“Bij UWV kan ik zelfstandig digitaal, mijn relevante zaken regelen waar en wanneer mij dat uitkomt. UWV laat mij

proactief weten wanneer er iets van mij wordt verwacht. Hierdoor word ik op weg naar werk of aan inkomen geholpen

of wat ik voor mijn personeel moet doen.”

Uitstekende digitale dienstverlening gaat UWV in een aantal logische stappen bereiken. Hierbij zetten we elke keer een

stap verder in het volwassenheidsniveau van digitale dienstverlening. Het volwassenheidsniveau wordt hierbij in grote

mate bepaald door het beschikbaar en veilig zijn van de dienstverlening.

De volgende drie stappen/business doelstellingen worden daarbij voorzien:

• Bereikbaar: “Als klant wil ik UWV op logische digitale plekken bereiken zodat ik mijn zaken kan uitvoeren.”.

Betrouwbaar: “Als klant kan ik actuele en betrouwbare informatie vinden zodat ik zeker weet dat ik

•

juist geïnformeerd ben”.

Behulpzaam: “Als klant word ik op weg geholpen zodat ik zelfstandig mijn zaken kan regelen. Waar

•

nodig staat UWV mij altijd proactief bij”.

De stappen beschrijven de weg naar een volwassen klantreis. In deze reis gaat elke stap gepaard met specifieke

klantbehoeften. Wat beweegt de klant in welke stap van de klantreis. Hiervoor wil UWV de klant begrijpen om hierop

te kunnen acteren. De verwachtingen van de klant zijn hoog in tijden van deze servicegerichte economie. De klant

verwacht een bereikbare, betrouwbare en behulpzaam UWV.

B.2.2. IV-strategie

Het UIP verwoordt de IV strategie als volgt: “Door middel van stapsgewijs en meerjarig robuust en veilig maken,

vereenvoudigen en moderniseren zal UWV zijn ICT-landschap de komende jaren toekomstbestendig maken.”

Om een uniforme aanpak op het ICT landschap te realiseren, hebben we onze belangrijkste keuzes ondergebracht in

de volgende richtinggevende IV-principes. Deze IV-principes worden toegepast bij de trajecten in dit Informatieplan.

1. UWV stelt Stabiliteit en continuïteit en informatiebeveiliging voorop

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

98 van 117

2. UWV kiest voor besturing van de informatievoorziening in IV-ketens en binnen centrale kaders

3. UWV kiest voor tijdig en geleidelijk vernieuwen

4. UWV zet gepaste outsourcing in voor applicatieontwikkeling en –beheer en volledige outsourcing voor

exploitatie van infrastructurele voorzieningen

5. UWV voert zijn klant- en bedrijfsprocessen geautomatiseerd uit

6. UWV kiest voor het persoonlijk maken van zijn digitale dienstverlening

7. UWV kiest voor het gebruik van gemeenschappelijke en generieke voorzieningen

8. UWV kiest voor een inrichting van het ICT-landschap met gestandaardiseerde en vervangbare bouwblokken,

zowel in de infrastructuur als in de software

9. UWV kiest bij de selectie van een IV-oplossing voor hergebruik boven standaardoplossing; standaardoplossing

boven maatwerk

10. UWV kiest uitwisselingsstandaarden op basis van overheids-, open- en marktstandaarden

11. UWV kiest ervoor om het eigenaarschap van applicaties eenduidig te beleggen

B2.3. Verwachtingen divisies

Digitale Dienstverlening kan niet als zelfstandig worden gezien en staat ten dienste van de primaire processen. Het

vertaalt echter de primaire processen naar de klanten. Hierin wordt de verbinding gevonden tussen E-Dienstverlening

en e-werken door zelfredzaamheid bij de klant te beleggen waar mogelijk. Dit om uitval zoveel mogelijk te reduceren

en daarmee de STP voor de primaire divisies te kunnen realiseren. Enerzijds door verantwoordelijkheid bij de klant

neer te leggen (zelf digitaal zaken met UWV te doen en waarvoor de dialoog wordt opgezocht) anderzijds door de

menselijke maat in de dienstverlening terug te brengen en gebruik te maken van de kennis die we al van onze klanten

hebben in onze dienstverlening. Eenvoud aan de voor de klant zichtbare kant, complexiteit bevindt zich vooral aan de

UWV kant. Hiermee beogen we tevens de effectiviteit van de dienstverlening te vergroten.

B.2.4 Ontwikkeling portalen en kanalen

De ambitie is aanwezig te zijn in de digitale wereld voor burgers en bedrijven die een sociale zekerheidsrelatie hebben.

We geven deze ambitie vorm met twee verschillende digitale omgevingen. De eerste is uwv.nl en gaat informatie en

ondersteuning bieden vanuit de kerntaken van UWV op het gebied van Uitkeren, Werk, Sociaal Medische Beoordeling,

Gegevensdiensten en ondersteunende diensten. De andere is werk.nl en gaat de werkzoekende in Nederland

ondersteunen bij het vinden van werk en de werkgever bij het vinden van personeel. De bestaande E-Diensten gaan

we herpositioneren over deze portalen, zodat de dienstverlening daar is waar de klant die verwacht.

De komende jaren neemt het aantal E-Diensten en het aantal gebruikers verder toe. Deze volumegroei maakt het

noodzakelijk de huidige problemen m.b.t. stabiliteit en continuïteit snel aan te pakken.

Het mobiele gebruik neemt verder toe. Dit betekent dat de behoefte voor het gebruik van digitale diensten verschuift

van de portalen naar apps (tablet/smartphone) en een uitbreiding op social media. Voor het zakelijk gebruik zien wij

een verschuiving van werkgevers- en zakelijkportaal naar applicatie-to-applicatie (A2A) koppelingen.

De verschillende vormen van dienstverlening in het digitale kanaal moeten integraal met elkaar en met alle andere

UWV kanalen samenwerken zodat de klant een consistente klantreis beleeft. Ook willen we het klantgedrag over alle

kanalen meten zodat we een consistente gepersonaliseerde dienstverlening over alle kanalen heen kunnen bieden. Een

integraal klantbeeld is hiervoor één van de belangrijkste middelen om in te richten.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

99 van 117

B.2.5. Gepersonaliseerde dienstverlening

De dienstverlening wordt persoonlijker, persoonlijk relevant en aanwezig op de plek waar de burgers en bedrijven de

dienstverlening verwacht te vinden zodat zij zelfstandig de diensten kunnen afnemen. Door gebruik te maken van wat

UWV weet van de klant (kanaalgedrag, klantvoorkeuren, profielkenmerken) kan UWV de klant proactief ondersteunen

in het afnemen van diensten. De digitale dienstverlening sluit ook naadloos aan op de dienstverlening via de

vestigingen en geautomatiseerde verwerking binnen de werkprocessen van UWV. Medewerkers en klanten krijgen

meer regelruimte voor dienstverlening op maat.

B.2.6. Gemeentelijke samenwerking

UWV is, via de wet SUWI, ketenpartner van Gemeentelijke Sociale Diensten en de SVB. Door aanpassing van

wetgeving zijn er taken en klanten van UWV verschoven naar deze ketenpartners. UWV biedt een uitgestoken hand bij

de overdacht naar deze ketenpartners door onze kennis en kunde en landelijke infrastructuur ter beschikking te

stellen. Doelstelling is de UWV centrale uitvoerder in veld van Werk en Inkomen blijft ook als de

beleidsverantwoordelijkheid decentraal ligt.

De bijbehorende (digitale) dienstverlening wordt via white label services aan de ketenpartners aangeboden. Portalen

van de ketenpartners (derden) kunnen hierop aangesloten worden.

B.2.7. Inzet gemeenschappelijke voorzieningen

De inzet van gemeenschappelijke voorzieningen is één van de elf richtinggevende IV-principes van UWV. Deze

voorzieningen zijn in hoge mate gestandaardiseerd en kennen meerdere gebruikers. Dit zorgt voor het vergroten van

de robuustheid van de informatievoorziening en een versnelling van de doorlooptijd van het veranderproces.

UWV sluit aan op gemeenschappelijke overheidsvoorzieningen. Voorwaarde hiervoor is wel een bewezen werken. Het

gebruik van overheidsvoorzieningen vergroot het gemak voor de burgers en werkgevers omdat zij dan niet te maken

krijgen met voorzieningen per overheidsorganisatie. Voorbeeld hiervan is DigiD.

Naast overheidsvoorzieningen kent UWV zelf ook gemeenschappelijke voorzieningen. Voorbeeld hiervan zijn:

inputmanagement en outputmanagement. Deze voorzieningen willen we gebruiken binnen de uitvoering van alle

primaire processen en ook bij de kantcontacten via E-Diensten. Hiermee bereiken we dat de integraliteit van

communicatie in primaire processen en digitale dienstverlening voor de klant zijn geborgd.

B.2.8. End-of-life en compliancy

De informatievoorziening van UWV bestaat uit een groot aantal systemen en diensten die we ingekocht hebben bij

leveranciers. Hiervoor moeten we meestal een aanbesteding uitvoeren omdat de kosten van verwerving (inclusief

licenties en ondersteuning) snel de aanbesteding grens overschrijden. Het bewaken van de contractduur en het

rechtmatig verwerven zijn een continue zorg. Daarnaast zorgt een aanbesteding ook voor lange doorlooptijden in het

veranderproces.

B.3 Visie op (digitale) dienstverlening vanuit K&S

Een grafische weergave van de visie van K&S op de dienstverlening van UWV is hieronder weergegeven.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

100 van 117

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

101 van 117

## Bijlage C, Architectuurprincipes

De algemene architectuur principes waarop de inrichting van de Doelarchitectuur van E-Dienstverlening is gebaseerd,

zijn een subset van de algemeen geldende architectuurprincipes die binnen UWV zijn vastgesteld. Voor E-

Dienstverlening gelden de volgende sturende principes:

Principe Omschrijving en uitwerking

Samenwerking UWV biedt, samen met publieke en private partijen, vanuit een heldere rol, een

samenhangend pakket van diensten aan burgers, werkgevers en organisaties.

De uitwerking van dit principe is terug te vinden in de specifieke diensten die UWV

aanbiedt via de digitale kanalen, al dan niet via interacties met externe partijen.

Effectiviteit wetgeving De wet en de bedoeling van de wetgever bepalen welke diensten UWV levert en op

welke wijze.

Onder andere op grond van dit principe biedt UWV haar diensten via internet aan.

Daarmee voldoet UWV aan de richtlijnen van de digitale overheid, waaronder de

## WGDI

Zelfredzaamheid klanten UWV gaat uit van zelfredzaamheid van klanten. Werkgevers en burgers hebben

een eigen verantwoordelijkheid en krijgen de regierol.

Door klanten de mogelijkheid te bieden algemene zowel als specifieke informatie

te vinden en persoonlijke interacties via digitale kanalen af te handelen, bevordert

UWV de bedelde zelfredzaamheid.

Duidelijke en respectvol UWV behandelt klanten respectvol en empathisch en geeft helder en duidelijk aan

wat ze van UWV kunnen en mogen verwachten, en wat UWV van hen verwacht.

. . .

Betrouwbare dienstverlening UWV houdt zich aan afspraken en levert een betrouwbare kwaliteit.

Uniformiteit dienstverlening UWV zorgt dat klanten uniformiteit in de dienstverlening ervaren.

Kanaal is passend digitaal UWV combineert (verplichte) online dienstverlening met een meer persoonlijke

benadering. Het karakter van de dienst en de betrokken klantgroep bepalen wat

het meest effectieve en passende kanaal is.

Persoonlijk digitale UWV kiest voor het persoonlijk maken van de digitale dienstverlening. De

dienstverlening dienstverlening wordt persoonlijker, persoonlijk relevant en aanwezig op de plek

waar de burgers en bedrijven het verwachten te vinden.

Alleen noodzakelijke UWV vraagt bij klanten alleen die gegevens uit die nodig zijn voor de uitvoering

uitvraag van de taken en die nog niet bij UWV, bij SUWI-partners of in de basisregistraties

beschikbaar zijn.

Vertrouwelijkheid Afnemers kunnen erop vertrouwen dat informatie niet wordt misbruikt.

Werk bij de klant UWV legt het werk waar mogelijk neer bij de klant.

Stabiliteit, continuïteit, De beschikbaarheid van de informatievoorziening wordt gewaarborgd door het

beschikbaarheid voorop stellen van stabiliteit, continuïteit en informatiebeveiliging.

Gemeenschappelijk en Bij het implementeren van nieuwe oplossingen moet waar mogelijk gebruik

generiek gemaakt worden van gemeenschappelijke en generieke voorzieningen.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

102 van 117

Principe Omschrijving en uitwerking

Gestandaardiseerde UWV kiest voor een inrichting van het ICT-landschap met gestandaardiseerde en

bouwblokken vervangbare bouwblokken, zowel in de infrastructuur als in de software.

Hergebruik, standaard, UWV kiest bij de selectie van een IV-oplossing voor hergebruik boven

maatwerk standaardoplossing, en standaardoplossing boven maatwerk.

Controleerbaarheid De mate van beschikbaarheid, integriteit en vertrouwelijkheid van de

informatievoorziening moet objectief vastgesteld kunnen worden.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.50

Pagina

103 van 117

## Bijlage D, Niet-functionele eisen

Op basis van de bedrijfsdoelen kunnen voor deze doelarchitectuur de eisen en wensen (requirements) van de

gebruikers worden verzameld. Figuur 46 toont hoe doelen, eisen en

wensen samenhangen. Naast functionele eisen die worden gesteld

aan de bouwblokken van deze doelarchitectuur, zijn er ook niet-

functionele eisen (non-functional requirements). De set niet

functionele eisen is opgesteld aan de hand van ISO25010 en omvat

de hieronder beschreven onderwerpen.

Deze eisen en wensen zijn verzameld in een aantal workshops met

vertegenwoordigers van zowel business als ICT. Deze

kwaliteitseisen zijn van toepassing op alle onderdelen van het

systeem waar de gebruiker mee werkt, dus niet alleen

Figuur 46, eisen en wensen hiërarchie

infrastructuur, maar ook applicaties. Naast de infrastructuur gelden

deze eisen daarmee ook voor de applicaties en zelfs voor de

processen waarbinnen de applicaties worden ingezet.

6.3.2 Onderwerpen binnen ISO 25010

• Functionele geschiktheid (Functional Suitability) beschrijft

de mate waarin een systeem functies levert die voldoen aan

de uitgesproken (en veronderstelde) behoeften;

• Prestatie-efficiëntie (Performance efficiency) beschrijft de

prestaties in verhouding tot de hoeveelheid middelen

gebruikt onder genoemde condities;

Uitwisselbaarheid (Compatibility) is de mate waarin een

•

product, systeem of component informatie uit kan wisselen

met andere producten, systemen of componenten, en/of het

de gewenste functies kan uitvoeren terwijl het dezelfde hard-

of software-omgeving deelt.

• Bruikbaarheid (Usability) beschrijft de mate waarin een

product of systeem gebruikt kan worden door gebruikers om

effectief, efficiënt en naar tevredenheid doelen te bereiken in

een bepaalde gebruikscontext.

• Betrouwbaarheid (Reliability) is de mate waarin een

systeem, product of component de gespecificeerde functies

uitvoert onder bepaalde condities gedurende een

Figuur 47, grafische weergave ISO 25010

gespecificeerde hoeveelheid tijd.

Beveiligbaarheid (Security) omvat de mate waarin een

•

product of systeem informatie en gegevens beschermt zodat personen, andere producten of systemen de juiste

gegevenstoegang hebben, passend bij hun soort en niveau van autorisatie.

• Onderhoudbaarheid (Maintainability) is de mate waarin een product of systeem effectief en efficiënt gewijzigd

kan worden door beheerders.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

104 van 117

Overdraagbaarheid (Portability) beschrijft de mate waarin een systeem, product of component overgezet kan

•

worden van één hardware, software, of andere operationele omgeving naar een andere.

Deze onderwerpen en de relevante subonderwerpen daarbinnen zijn in de hierna volgende paragrafen uitgewerkt.

Indien niet expliciet als ‘Wens’ vermeld kunnen de onderstaande punten gezien worden als ‘Eis’

6.3.3 Functionele geschiktheid

Functionele correctheid omvat de eisen met betrekking tot de mate waarin een softwareproducten of systeem de

juiste resultaten met de benodigde nauwkeurigheid beschikbaar stelt.

Code Omschrijving Rationale

NFR-01-01 Transactieverwerking is persistent en wordt De gebruiker dient de garantie te krijgen dat

uitgevoerd. door hem ingevoerde en door UWV

5.1 lid 2 sub i

geaccepteerde gegevens ook daadwerkelijk door

UWV worden verwerkt.

Het feitelijk opslaan van de gegevens in de

achterliggende systemen hoeft niet ‘realtime’ te

gebeuren.

Indien UWV gegevens niet kan accepteren, krijgt

de klant daarvan een melding.

6.3.4 Prestatie-efficiëntie

Middelenbeslag omvat de eisen die gelden met betrekking tot de mate waarin de hoeveelheid en type middelen die

gebruikt worden door een product of systeem, tijdens de uitvoer van zijn functies, voldoet aan de wensen.

Code Omschrijving Rationale

NFR-02-01 Het systeem moet bij overbelasting een melding UWV wil zo veel mogelijk voor de gebruiker

geven. zinvolle informatie geven bij zijn digitale reis

binnen UWV, ook als een systeem tijdelijk niet

beschikbaar is.

Snelheid bevat eisen met betrekking de mate waarin antwoord- en verwerkingstijden en doorvoersnelheid van een

product of systeem, tijdens de uitvoer van zijn functies, voldoet aan de wensen van de gebruiker van het systeem.

Code Omschrijving Rationale

NFR-02-02 De reactietijd van het systeem (opvragen/laden De gebruikerservaringen zoals die in 2016 en

van gegevens/schermen /rapporten) valt binnen 2017 maandelijks gerapporteerd worden zijn

laadtijden49.

de door UWV toegestane hierin bepalend

NFR-02-03 Responsetijd bij piekbelasting valt in 95% van UWV wil dat de dienstverlening aan de klant

de gevallen binnen de gewenste responstijd voldoende schaalbaar is en voor de gebruiker

waarbij het systeem 2x de geprognosticeerde acceptabel responsetijden kent, ook bij

piekbelasting aan kan. piekbelasting.

49

Deze responsetijd geldt voor een "reguliere" kantooromgeving met een LAN+WAN-koppeling naar de server

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

105 van 117

Code Omschrijving Rationale

NFR-02-04 Geprognosticeerde belasting: · Op basis van de maandelijks gegenereerde

Aantal inlogs per jaar: n.t.b. statistische gegevens en economische en

Gem. # schermen per inlog 20 bedrijfs- verwachtingen worden prognoses

Gem. # schermen per jaar 20*n.t.b. opgesteld voor het aantal inlogs

NFR-02-05 De transactieverwerking dient voor de Voor de asynchrone verwerking van de

gebruikerservaring binnen 3 seconden terug te gegevens kan de daadwerkelijke afhandeltijd

keren met een (zinvolle) melding. oplopen. De gebruiker dient hier evenwel geen

last van te hebben

6.3.5 Uitwisselbaarheid

Koppelbaarheid gaat over de mate waarin systemen gegevens kunnen uitwisselen en de uitgewisselde gegeven

kunnen gebruiken (c.q. verwerken).

Code Omschrijving Rationale

NFR-03-01 De verschillen in beschikbaarheid van de De digitale dienstverlening aan de klant van

systemen binnen E-Dienstverlening en de UWV dient 7*24 uur beschikbaar te zijn.

achterliggende bronsystemen vormen geen

belemmering voor het functioneren van deze

systemen.

NFR-03-02 Koppelingen voldoen aan standaarden Conform de inrichting van binnen UWV in te

zetten faciliteiten voor systeemintegratie

NFR-03-03 Informatieverzoeken handelt het systeem Daar waar klanten binnen UWV beschikbare

realtime af informatie opvragen moet deze in alle gevallen

direct worden geleverd.

6.3.6 Bruikbaarheid

Herkenbaarheid van geschiktheid beschrijft de mate waarin gebruikers kunnen herkennen of een product of

systeem geschikt is voor hun behoeften.

Code Omschrijving Rationale

NFR-04-01 De applicatie moet kunnen draaien in de Klanten moeten vanaf hun eigen apparatuur

browsers die genoemd worden in de lijst met gegevens kunnen uitwisselen met UWV. Uit

browsers50

gangbare en ondersteunde oogpunt van beschikbare functionaliteit en

beveiliging kunnen beperkingen worden gesteld

aan ouderdom en type apparatuur en software.

50

De lijst met ondersteunde browsers wordt aan het begin van een release gedeeld met alle betrokkenen. Gezien de

snelle mutaties hierin, bevat deze doelarchitectuur geen opsomming van te ondersteunen browsers.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

106 van 117

Code Omschrijving Rationale

NFR-04-02 Vooraf gedefinieerde diensten moeten op Door toenemend gebruik van en snelle groei van

verschillende devices bruikbaar zijn verscheidenheid aan apparaten is er behoefte

(responsiveness) om onze diensten aan te kunnen passen aan het

medium waarmee de klant communiceert

NFR-04-03 Gepersonaliseerde, specifieke, diensten worden UWV wil haar klanten toeleiden naar relevante

aangeboden op basis van vooraf gedefinieerde diensten

gebruikersprofielen

Voorkomen gebruikersfouten gaat over de mate waarin het systeem de gebruikers beschermt tegen het maken

van fouten.

Code Omschrijving Rationale

NFR-04-04 Ingevoerde gegevens worden gevalideerd tegen UWV borgt dat ingevoerde gegevens

bij UWV bekende gegevens en syntactische daadwerkelijk betekenis hebben.

regels alvorens te worden verwerkt

Toegankelijkheid De mate waarin een product of systeem gebruikt kan worden door mensen met de meest

uiteenlopende eigenschappen en mogelijkheden om een gespecificeerd doel te bereiken in een gespecificeerde

gebruikscontext

Code Omschrijving Rationale

NFR-04-05 Gebruikers van onze dienstverlening ( burgers, Gescheiden identity & acces voorzieningen voor

werknemers, werkgevers en zakelijke partners) klanten en medewerkers voorkomt dat in een

hebben een eigen voorziening waarin het geval van calamiteit niemand meer toegang

systeem hun identiteit en toegang vaststelt heeft tot de dienstverlening.

tegenover de voorziening waar de medewerkers

gebruik van maken

NFR-04-06 Het systeem voldoet aan de richtlijnen die de UWV is een overheidsorganisatie en dient

Nederlandse overheid stelt aan het web. daarmee te voldoen aan geldende wet- en

regelgeving op dit gebied.

NFR-04-07 De gebruiker doet een éénmalige inlog Uit het oogpunt van gebruikersgemak is

afhankelijk van het hoogste beveiligingsniveau eenmalige inlog binnen een dienst voor de

dat van toepassing is. gebruiker te prefereren boven ‘step-up

authenticatie’. Dat vraagt om een ontwerp

waarbij we van tevoren vaststellen wat het

vereiste beveiligingsniveau is van de gebruiker.

Begrijpelijkheid is de mate waarin een klant toegang krijgt zonder specifieke kennis of uitleg buiten het aangeboden

systeem.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

107 van 117

Code Omschrijving Rationale

NFR-04-08 De website is zelfverklarend UWV streeft naar een zo goed mogelijke

gebruikerservaring en systemen die voor zo veel

mogelijk klanten toegankelijk zijn, zonder

aanvullende kennis of uitleg buiten het

betreffende systeem.

Leerbaarheid bevat eisen met betrekking tot de mate waarin een product of systeem gebruikt kan worden door

gebruikers om bepaalde doelen te bereiken met betrekking tot het gebruik van het product of systeem.

Code Omschrijving Rationale

NFR-04-09 Het systeem genereert suggesties voor de klant UWV streeft naar een zo goed mogelijke

in de context van zijn/haar bezoek gebruikerservaring en biedt daarbij waar

mogelijk ondersteuning zonder tussenkomst van

UWV medewerkers

Gebruiksgemak is de mate waarin een gebruikersinterface het de gebruiker mogelijk maakt om een plezierige en

voldoening gevende interactie te hebben.

Code Omschrijving Rationale

NFR-04-10 Het systeem moet laten zien dat het bezig is als UWV streeft naar een zo goed mogelijke

het meer dan 3 seconden nodig heeft om gebruikerservaring en wil de klant optimaal

zichtbaar op een actie van de gebruiker te ondersteunen.

reageren.

6.3.7 Betrouwbaarheid

Beschikbaarheid beschrijft de mate waarin een systeem, product of component operationeel en toegankelijk is

wanneer men het wil gebruiken.

Code Omschrijving Rationale

NFR-05-01 De verwerkingsinfrastructuur is 24 x 7 x 365 Hardware is niet langer het obstakel of de

virtualisatie51

beschikbaar kostenbepaler. Door kan een

oneindige pool van resources worden

aangeboord.

NFR-05-02 De functionaliteit van het E-Dienstenplatform is UWV wil haar klanten de mogelijkheid bieden

24/7/365 beschikbaar met een informatie uit te wisselen met UWV op het

beschikbaarheidspercentage van 99,8% met moment dat de klant het beste uit komt.

uitzondering van vooraf overeengekomen

perioden van onbeschikbaarheid.

51

Binnen bestaande contractafspraken is deze eis beperkt realiseerbaar. Vanuit (onder andere) E-Dienstverlening is dit

onderwerp ingebracht in de aanbesteding voor de een nieuwe datacenterleverancier.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

108 van 117

Code Omschrijving Rationale

NFR-05-03 Beschikbaarheid: Belasting Deze eis is gebaseerd op beschikbare

Geprognotiseerd cijfermatige gegevens. Het niveau van

Aantal inlogs/pageviews per jaar, per dag, per dienstverlening mag niet lager worden dan wat

uur tot op heden gebruikelijk was.

Foutbestendigheid - De mate waarin een systeem, product of component werkt zoals bedoeld ondanks de

aanwezigheid van hard- of softwarefouten.

Code Omschrijving Rationale

NFR-05-04 Alle ingevoerde gegevens moeten op juistheid, Informatie die door een klant in UWV systemen

tijdigheid en volledigheid worden gecontroleerd wordt ingevoerd, moet voldoen aan (technische)

voordat verdere verwerking plaatsvindt om eisen die een juiste opslag en verwerking door

fouten en verstoringen in de verwerking te UWV mogelijk maken. Controles daarop moeten

voorkomen. zo dicht mogelijk bij de gebruiker plaatsvinden.

NFR-05-05 Tussentijdse opslag van data dient te UWV streeft naar een zo goed mogelijke

voorkomen dat gebruikers al hun gegevens kwijt gebruikerservaring en wil de klant optimaal

zijn bij het afbreken van een sessie. Wanneer de ondersteunen. Wanneer onverhoopt een sessie

sessie dan toch wordt afgebroken, bewaart het onverwacht eindigt, moet het gegevensverlies zo

systeem alleen de opgeslagen gegevens veel mogelijk beperkt blijven.

Herstelbaarheid - De mate waarin het product of systeem, in geval van een onderbreking of bij een fout, de direct

betrokken gegevens kan herstellen en het systeem in de gewenste staat kan terug brengen.

Code Omschrijving Rationale

NFR-05-06 Er zijn maatregelen getroffen om bij UWV wil een zo hoog mogelijk niveau van

verstoringen binnen de gestelde termijn dienstverlening aan haar klanten garanderen.

(automatisch) terug te keren op het afgesproken

niveau van dienstverlening

6.3.8 Beveiligbaarheid

Vertrouwelijkheid is de mate waarin een product of systeem ervoor zorgt dat gegevens alleen toegankelijk zijn voor

diegenen die geautoriseerd zijn.

Code Omschrijving Rationale

NFR-06-01 Het informatiesysteem beschermt UWV wil dat klanten zich veilig voelt in de

privacygevoelige informatie tegen ongewenste contacten met UWV. Om die reden neemt UWV

inzage of oneigenlijk gebruik door derden maatregelen om dat gevoel van veiligheid te

(afluisteren, hacking, inbraak, identiteitsfraude, borgen.

etc.) conform het UWV security &

beveiligingsbeleid, risicoklasse hoog.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

109 van 117

Code Omschrijving Rationale

NFR-06-02 UWV stelt vast van de gebruiker wie hij/zij zegt De klant van UWV heeft alleen toegang tot

te zijn en welke bevoegdheid tot toegang tot gegevens waartoe hij gemachtigd is.

informatie van toepassing is in de context van

de vraag

NFR-06-03 Beveiligingsniveau van de diensten wordt UWV wil dat haar klanten altijd op het passende

bepaald door privacygevoeligheid van de veiligheidsniveau werken.

gegevens die hierbij betrokken zijn

NFR-06-04 Het systeem dwingt het beveiligingsniveau af op UWV wil het gebruik van diensten beperken tot

basis van identiteit, dienst en locatie de geautoriseerde gebruiker en de locatie van

waaraf de dienst wordt benaderd.

Voor authenticatie en autorisatie zijn de drie

genoemde elementen bepalend.

Onweerlegbaarheid - De mate waarin kan worden bewezen dat acties of gebeurtenissen plaats hebben gevonden,

zodat later deze acties of gebeurtenissen niet ontkend kunnen worden.

Code Omschrijving Rationale

NFR-06-05 De gebruikers verwerking wordt vastgelegd in Bij meningsverschillen tussen klanten en UWV

een ‘audit trail’ en deze informatie wordt dient UWV aan te tonen wat de klant heeft

bewaard52

minstens 1 maand gedaan op de UWV omgeving. Daarnaast is

i.h.k.v. klantexpertise het nodig het gedrag van

de klant vast te leggen om daar later op te

kunnen analyseren (zie ook

onderhoudbaarheid).

Verantwoording bevat eisen met betrekking tot de mate waarin acties getraceerd kunnen worden naar die specifieke

gebruiker.

Code Omschrijving Rationale

NFR-06-06 De verwerking van de gebruiker wordt gelogd in Bij meningsverschillen tussen klanten en UWV

het kader van wettelijke verplichting en de dient UWV aan te tonen wat de klant heeft

business noodzaak om inzicht in het klantgedrag gedaan op de UWV omgeving. Daarnaast is

te hebben i.h.k.v. klantexpertise het nodig het gedrag van

de klant vast te leggen om daar later op te

kunnen analyseren (zie ook onderhoudbaarheid)

52

De termijn van 1 maand is genoemd, maar nog niet definitief vastgesteld per 1 maart 2017. Het aantal maanden

kan dus nog veranderen.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

110 van 117

6.3.9 Onderhoudbaarheid

Analyseerbaarheid - De mate waarin het mogelijk is om effectief en efficiënt de impact, van een geplande

verandering van één of meer onderdelen, op een product of systeem te beoordelen, om afwijkingen en/of

foutoorzaken van een product vast te stellen of om onderdelen te identificeren die gewijzigd moeten worden.

Code Omschrijving Rationale

NFR07-01 Het systeem stelt realtime informatie UWV haar klanten wil een zo hoog mogelijke

beschikbaar welke inzicht geeft in de beschikbaarheid bieden. Daarom is het

operationele condities van het systeem t.b.v. noodzakelijk inzicht te hebben in de actuele

technisch beheer van status van systemen en te signaleren wanneer

infrastructuurcomponenten. een (deel van een) systeem niet beschikbaar is.

NFR07-02 De audittrail dient vanuit wettelijk en business UWV wil transparant zijn en zorgt er voor dat zij

oogpunt te zijn geborgd verantwoording kan afleggen

NFR07-03 Foutmeldingen zijn altijd voorzien van een “Time Om (achteraf) een goede analyse van een

Stamp” storing te kunnen maken, moet duidelijk zijn

welk event zich wanneer heeft voorgedaan in

welk systeem.

NFR07-04 Het systeem dient aan de standaard logging UWV wil haar klanten een hoge beschikbaarheid

richtlijn te voldoen bieden en zorgt ervoor dat eventuele

verstoringen geanalyseerd kunnen worden

NFR07-05 Transacties dienen uniek identificeerbaar te zijn UWV wil haar klanten een hoge beschikbaarheid

en te volgen door het systeem bieden en zorgt ervoor dat eventuele

verstoringen geanalyseerd kunnen worden

Beheerbaarheid bevat de eisen waaraan de beheerbaarheid van het applicatielandschap binnen het domein E-

Dienstverlening moet voldoen.

Code Omschrijving Rationale

NFR07-06 De technische, applicatieve en functionele UWV organiseert zichzelf zo dat al haar

beheertaken en bijbehorende systemen adequaat beheerd worden.

verantwoordelijkheden en bevoegdheden zijn

belegd.

Testbaarheid bevat de eisten voor de mate waarin effectief en efficiënt testcriteria vastgesteld kunnen worden voor

een systeem, product of component en waarin tests uitgevoerd kunnen worden om vast te stellen of aan die criteria is

voldaan.

Code Omschrijving Rationale

NFR07-07 Het is mogelijk om automatisch te UWV wil flexibel zowel als betrouwbaar zijn in de

(Wens) regressietesten van front-end en middleware wijze waarop diensten digitaal aan de klant

binnen 1 dagdeel. worden aangeboden. Nieuwe c.q. aangepaste

functionaliteit moet in korte periode beschikbaar

gesteld worden.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

111 van 117

6.3.10 Overdraagbaarheid

Aanpasbaarheid gaat over de eisen waaraan een product of systeem moet voldoen om effectief en efficiënt

aangepast kan worden voor andere of zich ontwikkelende hardware, software of andere operationele of

gebruiksomgevingen.

Code Omschrijving Rationale

NFR-08-01 De software moet binnen een week overgezet UWV wil zo veel mogelijk standaardiseren. In

kunnen worden naar een nieuw rekencentrum het kader van de te verwachten aanbesteding

voor het rekencentrum is deze waarde gesteld

op basis van good practices.

Instaleerbaarheid - De mate waarin het product of het systeem effectief en efficiënt geïnstalleerd of verwijderd kan

worden in een gespecificeerde omgeving.

Code Omschrijving Rationale

NFR-08-02 Bij behoefte aan additionele capaciteit of bij Om een zo hoog mogelijke beschikbaarheid te

herstel van het systeem, is het systeem in staat garanderen is het gewenst dat altijd voldoende

is53.

om automatisch zichzelf te configureren (c.q. verwerkingscapaciteit beschikbaar

zichzelf automatische te deployen) conform

vooraf bepaalde eigenschappen.

Inpasbaarheid - De mate waarin een product een ander specifiek softwareproduct, met hetzelfde doel in dezelfde

omgeving, kan vervangen.

Code Omschrijving Rationale

NFR-08-03 Waar nieuwe diensten de oude diensten UWV biedt haar klanten continuïteit en zorgt er

vervangen en bij geconstateerde fouten kan er voor dat het niveau van dienstverlening niet

worden teruggevallen op de oude diensten verminderd als gevolg vaan aanpassingen.

NFR-08-04 Vooraf gedefinieerde diensten moeten ontsloten Bepaalde diensten wil UWV beschikbaar stellen

kunnen worden op eigen platformen en die van aan haar ketenpartners voor gebruik op eigen

(keten)partners systemen

NFR-08-05 Nieuwe functionaliteit wordt middels een UWV wil nieuwe functionaliteit gecontroleerd

geleidelijke uitrol aan gebruikers beschikbaar beschikbaar stellen

gesteld

NFR-08-06 Het opschalen van nieuwe functionaliteit vindt Nieuwe functionaliteit moet geleidelijk aan in

plaats met behulp van “graceful shutdown” van gebruik worden genomen op zodanige wijze dat

de oude functionaliteit oude en nieuwe systemen tijdelijk naast elkaar

functioneren.

53

Dit is feitelijk Auto Deployment

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

112 van 117

## Bijlage E, Basis procesmodel

Het kennen van de klant en vervolgens het inzetten van passende (digitale) dienstverlening binnen de klantreis

betekent dat klantinformatie over feiten, gedrag en communicatie integraal beschikbaar moet zijn, zodat betrokken

medewerkers en/of IV-systemen vervolgens kwalitatief goede en klantgerichte diensten kunnen inzetten. Daarbij is

van belang dat er een integraal klantdossier ontstaat en bestaat zodat daaruit afgeleide klantbeelden de

dienstverlening kunnen ondersteunen. Daarnaast wil UWV, in geval van onduidelijkheid of geschil, zich ook kunnen

verantwoorden over haar handelen. Vanuit de archieffunctie van de divisie DIV worden er eisen gesteld aan de

vastlegging van gegevens met deze verantwoording als doel.

model54

Om te kunnen voldoen aan deze eisen hanteert E-Dienstverlening een waarmee diensten en dienstverlening

op een eenduidige wijze kunnen worden ingericht. Het model geeft handvatten voor het structureren van diensten en

processen en vervolgens de vertaling ervan via patronen en klantbeelden naar IV middelen en specifieke

communicatiekanalen.

Basismodel

De dienstverlening van UWV is in de basis aanbodgericht ingericht en de klant kan op basis van zijn behoefte (event)

een keus maken voor de dienst die hij dat moment nodig heeft.

Als de klant een keus maakt voor het afnemen van een dienst, begint dat met een event en op basis van het event

start een (bedrijfs-)proces binnen UWV. Het bedrijfsproces wordt doorlopen en levert uiteindelijk een product op aan

de klant. Error! Reference source not found.

Bedrijfsproces, werkproces en zaak

Een bedrijfsproces is een aaneengesloten set van activiteiten

event product

met een gemeenschappelijk doel. Om die activiteiten te

onderscheiden bestaat een bedrijfsproces uit 1 of meer

Klantproces, vraaggericht

werkprocessen. Elk werkproces is vervolgens weer opgebouwd

uit 1 of meer processtappen. Op deze manier ontstaat een

zaak

gestructureerd en samenhangend bedrijfsproces.

UWV kiest voor zaakgericht werken, een zaak is daarbij een

## PROCES

administratief item dat als een paperclip de diverse betrokken

Ontvang Verstuur

administraties en (deel)producten bijeen houdt. Op deze manier

processtap

is UWV in staat een integraal dossier te vormen met decentrale

werkproces

administraties.

Verzamel Besluit

Elke dienst heeft een eigen zaaktype en is daardoor als zodanig

Beoordeel

te herkennen. Via de primaire systemen is door de medewerker

Bedrijfsproces, aanbodgericht

en via de mijn-omgeving door de klant, deze dienst op te roepen

waarbij het zaaknummer als paperclip toegang geeft tot het

Figuur 48, uitgewerkt model procesverloop

integrale dossier waarin het verloop van de dienstverlening is

vastgelegd.

54

Dit model is initieel opgesteld binnen DIV met een sterke focus op het kunnen vastleggen en reconstrueren van het

procesverloop in relatie tot de archieffunctie.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

113 van 117

Tijdens de uitvoering van een dienst kan het nodig zijn om een uitstapje te maken naar een andere dienst.

Bijvoorbeeld als blijkt dat er een medische beoordeling nodig is om tot besluitvorming te komen. Het model voorziet

daarin door een relatie tussen zaken (zaakrelatie) te onderscheiden. Op deze manier wordt een integraal dossier

gewaarborgd. In de onderstaande figuur wordt dit grafisch weergegeven.

Uitgangspunt is dat bij aanvang van de dienstverlening de opbouw van het klantdossier in de verschillende

administraties integraal benaderbaar is. De informatie wordt daarbij volgens een bepaalde orde geregistreerd en

geclassificeerd zodat de informatie in het klantdossier, onafhankelijk van het kanaal, voldoet aan de volgende eisen:

• toegankelijkheid (het zoeken en terugvinden van de informatie) is en blijft geborgd;

doelbinding is geborgd zodat informatie alleen beschikbaar is voor personen die daar vanuit hun rol toegang

•

toe moeten hebben;

• contextinformatie wordt geregistreerd zodat informatie eenduidig geïnterpreteerd kan worden;

• transparantie is geborgd zodat UWV haar handelen kan verantwoorden (reconstrueren).

Communiceren vanuit de dienstverlening (kanaalkeuze)

UWV heeft als uitgangspunt dat we correct, volledig en transparant communiceren over de uitvoering van taken aan

de klant via communicatie uitingen. Uitgangspunt is dat het digitale communicatiekanaal de voorkeur heeft. UWV biedt

de mogelijkheid andere kanalen te gebruiken, indien de klant niet in staat is gebruik van te maken, of en specifieke

situatie daarom vraagt. De keuze is daarbij aan de klant die door middel van opt-out kan aangeven gebruik te willen

maken van het traditionele, niet-digitale kanaal.

Het web-portaal is het meest uitgebreide kanaal met de meest uitgebreide dienstenset. Apps, social media en

eventuele andere kanalen zijn aanvullend.

Hoewel web en mobiele devices beiden digitale dienstverlening ondersteunen, zijn de kanaaleigenschappen niet gelijk.

Een gekozen communicatieuiting via web is daardoor mogelijk niet effectief op een mobiel device en vraagt om een

andere vorm. De boodschap die met een communicatie uiting via web of mobile wordt gecommuniceerd moet echter

wel eenduidig en (juridisch) kloppend zijn.

Communicatie tussen klant en UWV wordt veelal door de klant geïnitieerd. Een groot deel daarvan is het opvragen van

status informatie. Om uitval in het digitale kanaal te verminderen wil UWV steeds vaker door middel van notificaties de

klant informeren over wijzigingen in de status van een bepaalde dienst, gemaakte afspraken, herinneringsberichten of

wijzigingen in de informatie.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

114 van 117

## Bijlage F, SOA en MSA

Een KOA is een service en ten behoeve van de specifieke implementatie maatregelen voor een KOA behandelen

worden hier een aantal generieke aspecten uit de service georiënteerde architectuur (SOA) en micro-services

architectuur (MSA).

SOA bestaat al vele jaren maar het is moeilijk gebleken om SOA op een goede manier te implementeren en

daadwerkelijk de voordelen te behalen. MSA is een recentere ontwikkeling van de laatste paar jaar en is meer bottom-

up ontstaan en wordt succesvol toegepast door internetbedrijven als Spotify en Amazon. UWV is een organisatie met

een grote bestaande ICT footprint. Het is niet realistische en niet zinvol om het gehele landschap nu conform MSA te

herontwikkelen. De denkbeelden uit SOA en MSA zijn echter ook voor UWV zeer waardevol en staan aan de basis van

het KI/KO concept en de implementatiemaatregelen.

De volgende aspecten van SOA zijn relevant.

• Expliciete grenzen. Alles wat een service nodig heeft om functionaliteiten te leveren wordt via een bericht

doorgegeven. De service heeft zelf kennis van onderliggende functionaliteiten en gegevens om functioneel

volledig te zijn.

Voor UWV: Een KIA hoeft niet te weten hoe een KOA functioneert. En KOA’s communiceren op basis van

UWVml formaat.

Gedeeld contract en schema. Een service deelt met de buiten wereld het servicecontract met daarin een

•

gedeeld gegevens model of te wel schema. Technische implementatie details worden verborgen en

communicatie gebeurt op basis van standaard protocollen bijvoorbeeld SOAP/XML.

Voor UWV: gebruik canoniek gegevens model (CGM) afgeleid van FUGEM. Spreek servicelevels af voor KOA’s

en ontwikkel pas als het contract (interface ontwerp) bepaald is.

Beleid gestuurd. Naast functionele aspecten van een service worden ook niet-functionele aspecten zoals

•

beveiliging, protocollen, performance, e.d. afgesproken. Deze beleidsrichtlijnen op technisch vlak dienen

bekend te zijn.

Voor UWV: alle verkeer intern en extern via HTTPS en gebruik security artefacten (zoals SAML tokens) voor

autorisatie van berichten.

• Autonoom. Alleen de interface van een service is bekend. Deployment en versionering zijn ingericht.

Voor UWV: elke service heeft een versie en deze is vindbaar via een API Gateway. Elke service heeft een

middel (zie maatregelen KOA) om het niet beschikbaar zijn van andere resources ordelijk af te handelen.

Standaard protocollen. Er wordt gecommuniceerd via standaard protocollen die niet afhankelijk zijn van een

•

programmeertaal of specifiek framework.

Voor UWV: services (KOA’s) zijn te benaderen zonder kennis van specifieke implementatie en alleen open

standaarden zijn toegestaan.

5.1 lid 2 sub i

Document georiënteerd. Communicatie met de service verloopt via een bericht bestaande uit een document.

•

Verzender en ontvanger van documenten kunnen onafhankelijk van elkaar worden ontwikkeld.

Voor UWV: alle berichten moeten voorzien kunnen worden van een XSLT om deze voor mens of systeem

leesbaar te maken. Berichten zijn complement: geen opgedeelde berichten. BLOB in payload.

• Los verbonden. De kern van SOA is ontkoppeling over tijd, plaats, soort, versie, … Service zijn dan ook

relatief kleine componenten die onafhankelijk van elkaar zijn.

Voor UWV: de bouw van software moet gericht zijn op services. Monolieten en pakketten moeten hier ook aan

voldoen en dienen te communiceren volgens de hier genoemde uitgangspunten.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

115 van 117

Voldoen aan standaarden. Zie boven.

•

• Leverancier onafhankelijk. Er mag geen gebruik worden gemaakt van specifieke protocollen en

implementaties van leveranciers van software, hardware, telecommunicatie, ed.

Meta-data gestuurd.

•

Principes van SOA:

• Gestandaardiseerd contract.

Services bieden zich aan via een “service contract”. Services hanteren een eenduidige definitie, opbouw en

technische invulling van de samenwerkingafspraak tussen aanbieder en gebruiker. Service contracten dienen

consistent, betrouwbaar en reguleerbaar te zijn.

Losse service koppeling.

•

Services zijn zo opgebouwd dat afhankelijkheid van anderen zo laag mogelijk is. Er is een continue drang om

de afhankelijkheid van de service implementatie een interne aangelegenheid van de service aanbieder te

laten zijn. Zo zijn service gebruikers wel gekoppeld aan het service contract van een service, maar niet aan

de implementatie van die service of aan de koppelingen met andere services.

Service abstractie.

•

Service contracten bevatten alleen de absoluut noodzakelijke (en dus de essentiële) informatie over de

diensten (functies) die de service biedt. De gebruiker zal alleen deze informatie tot zijn beschikking hebben

en hoeven te hebben om gebruik te kunnen maken van de service.

Service hergebruik.

•

Een service moet herbruikbaar zijn zodat andere services er keer op keer gebruik van kunnen maken. Het

ontwerp van de service dient aandachtig bekeken te worden en getoetst te worden op herbruikbaarheid

binnen de context van de architectuur.

Service autonomie.

•

Services dienen op de juiste wijze te kunnen beschikken over de resources en de omgeving waarin deze

services draaien. Services waarvan andere services (in een keten) afhankelijk zijn dienen een groter niveau

van autonomie te hebben.

Service toestandloos.

•

Services trachten de resources die ze gebruiken te minimaliseren door ofwel de informatie over de huidige

status van de service niet zelf bij te houden, maar dit over te laten aan andere systemen, of de

statusinformatie die door de service zelf wordt bijgehouden in ieder geval zo minimaal mogelijk te laten zijn.

Service vindbaarheid.

•

Indien een service gezien wil worden als een herbruikbare asset binnen het ecosysteem dient deze makkelijk

te kunnen worden herkend en begrepen. Het gaat hier om de kwaliteit van de metadata die het service

contract biedt. Het service contract dient kenbaar te maken welke functies en welk doel de service dient. Zo

kan bij het zoeken naar herbruikbare services binnen de architectuur de service gemakkelijk worden

gevonden.

Service combineerbaarheid.

•

Een service moet gemakkelijk gebruikt kunnen worden binnen een groter geheel van services, een keten. De

eisen die aan het ontwerp van een service worden gesteld zijn gericht op het voorkomen dat een service

binnen een bredere oplossing moet worden “gelepeld”. Van een service wordt verwacht dat ze gemakkelijk

een rol kan vervullen binnen een keten, zonder dat daar bij het ontwerp van de keten expliciet rekening mee

wordt gehouden. Het draait hier dus om “separation of concerns”.

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

116 van 117

Service optimalisatie.

•

Wanneer meerdere services beschikbaar zijn die dezelfde functionaliteit bieden, gaat een service met een

hogere kwaliteit boven de service met een lagere kwaliteit.

Service relevantie.

•

Een service dient die functies aan te bieden die door een gebruiker ook als zinvolle functies worden gezien.

Indien de functies te klein of juist te groot worden ontworpen dan daalt daarmee de waarde die de functies

hebben voor de gebruikers van de service.

• Service inkapseling.

Een service kan andere services inkapselen die niet in eerste instantie opgezet waren om te functioneren

binnen een SOA. Denk daarbij aan legacy systemen en databases waarbij een SOA service de

functionaliteiten van die systemen kan publiceren om zo deze functionaliteit te kunnen laten meedraaien in

een SOA.

• Service omgeving transparant.

Een service zou overal moeten kunnen werken ongeacht waar de service zich fysiek bevindt. Hierdoor is het

uitwisselen van services over geografische, technische en organisatorische grenzen heen mogelijk.

De volgende MSA aspecten zijn relevant.

Service contracten.

•

SOA en MSA zijn afhankelijk van protocollen (REST, SOAP, AMQP, JMS, MSMQ, RMI etc.) en daarmee van

contracten. Contracten zijn de manier om eenduidige communicatie vast te leggen en versionering te

bereiken.

Service beschikbaarheid en responsiviteit.

•

Voor service availability is het noodzakelijk data an het contract wordt voldaan. Hiervoor is het zaak om

programming en design guidelines af te spreken en deze te toetsen bij oplevering van de service (meenemen

in DoD). Daarnaast wordt aan de kant van de consumer compesatable data stores en caches gebruikt. Voor

service responsiveness wordt het circuit breaker pattern gebruikt.

Beveiliging.

•

Authenticatie en autorisatie wordt door middel van SAML tokens afgehandeld <<verder uitzoeken, auth

delegeren autorisatie intern, Oauth gebruiken>>

Transacties.

•

SOA service handelen ACID (atomair, consistent, isolated, durable) transacties af. MSA handelen dit als BASE

transacties af.

Servicetypes.

•

In MSA bestaan functionele services en infrastructuur services. Elke functionele service roept een

infrastructuur service aan om bijvoorbeeld events te posten of te ontvangen.

Eigenaarschap berust bij (DevOps) scrum teams verantwoordelijk voor een bepaalde microservice (functional

en infrastructure) zoals het spotify model, of het Amazon model voor kleine teams (two pizza team). Soa

heeft een meer gelaagde taxonomy met business services, messaging services, enterprise services,

application services en infrastructure services

Services.

•

Idempotent, kleine granulariteit, bieden standaard services en operaties (CRUD).

Services bieden (minstens) de volgende functionaliteit aan: lees service met als operaties lees item, lees lijst

Doelarchitectuur E-

Dienstverlening

Datum

23 november 2017

Auteur

Architectuur team E-

Status

Dienstverlening

Goedgekeurd

5.1 lid 2 sub e

Versie

@uwv.nl

1.50

Pagina

117 van 117

en lees met parameters en een mutatieservice met als operaties maak nieuw item, werk item bij en verwijder

item.

Event queues.

•

Werking van een event queue is als volgt: 1 Leverancier stuurt bericht naar queue, 2. Queue bevestigd

ontvangst, 3. Afnemer raadpleegt queue en haalt bericht op, 4. Afnemer bevestigt bericht ontvangen. Bij een

event queue weet alleen de leverancier het onderwerp van een bericht, de ontvanger abonneert zich op een

onderwerp en haalt overeenkomstig berichten op.

---

Bron: [Besluit Woo-verzoek IT strategie UWV](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv) · [Bijlage 10 Doelarchitectuur E-Dienstverlening (PDF, 4 MB)](https://www.uwv.nl/assets-kai/files/b3506137-1f21-4035-830f-501deb0a2b25/bijlage-10-doelarchitectuur-e-dienstverlening.pdf)
