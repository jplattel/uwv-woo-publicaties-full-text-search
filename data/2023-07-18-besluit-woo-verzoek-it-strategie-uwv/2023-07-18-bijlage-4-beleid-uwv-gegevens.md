---
source_id: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv/2023-07-18-bijlage-4-beleid-uwv-gegevens
publication_slug: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv
pdf_slug: 2023-07-18-bijlage-4-beleid-uwv-gegevens
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv
pdf_url: https://www.uwv.nl/assets-kai/files/388a1548-a936-416b-a116-fcd296fe27a5/bijlage-4-beleid-uwv-gegevens.pdf
publication_title: Besluit Woo-verzoek IT strategie UWV
publication_date: '2023-07-18T00:00:00Z'
publication_type: WOO publicatie
pdf_label: Bijlage 4 Beleid UWV Gegevens versie 1.1 (PDF, 562 kB)
retrieved_at: '2026-06-30T13:18:11+00:00'
sha256: 73fa1cfed54069ba0d4ab0a26587effc8cd70633f1468e1c310ad9ecfaed656e
page_count: 22
ocr_used: false
---

Beleid UWV Gegevens

Standaardiseren, modelleren, beschrijven en beheren van

bedrijfsgegevens UWV conform vastgestelde methodieken

Beleid UWV Gegevens

Datum

8 september 2015

Status

Auteur

Definitief

5.1 lid 2 sub e

5.1 lid 2 sub e

Versie

@uwv.nl

5.1 lid 2 sub e

1.1

Ons kenmerk

-

Pagina

2 van 22

Versiehistorie

Versie Datum Wijzigingen t.o.v. vorige versie Verspreid aan

## 0.1 27-05-05 - GM

0.2 17-06-05 Opmerkingen uit collegiale toetsing verwerkt

0.3 (C) Voorjaar 2011 Integrale actualisering van het document Gegevensarchitecten

‘UGR-Beleid 0.2’ van , d.d. 23 Centraal

5.1 lid 2 sub e

juni 2005. Gegevensmanagement

0.5 (C) 11-08-2011 Omgezet in nieuw sjabloon Gegevensarchitecten Data

beleidsdocumenten. Reviewcommentaar Office

verwerkt (incl. diverse aanvullingen). Nieuwe

ontwikkelingen toegevoegd.

0.6 (C) 03-12-2012 Opzet en inhoud aangepast naar aanleiding Data Office

van bijeenkomst Lokaal Gegevensmanagers

19112012

0.61 (C) 07-12-2012 Gewijzigd na beperkte review door Data Lokaal

Office. Gegevensmanagement

Versie in ontwikkeling voor bespreking met

Lokaal Gegevensmanagement

0.7 (C) 24-01-2013 Versie ter review door Lokaal Lokaal

Gegevensmanagement. Gegevensmanagement

0.9 (C) 19-02-2013 Versie ter vaststelling door het KOG Leden KOG

0.91 (C) 03-04-2013 Versie na verwerking opmerkingen nav Gegevensarchitecten

aanhouding KOG d.d. 28-02-2013

0.92 (C) 11-04-2013 Versie na verwerking aanvullingen Lokaal Gegevensmanagers

gegevensarchitecten

0.93 (C) 17-04-2013 Versie na verwerking opmerkingen Lokaal Kaderstellend Overleg

Gegevensmanagers Gegevensmanagement

1.1 (D) 08-09-2015 Geactualiseerd, geen inhoudelijke wijzigingen

C = Concept; D = Definitief

Status besluitvorming

Versie Datum Besluitvorming

1.0 (C) nvt

1.0 (D) 23-04-2013 Vastgesteld in het Kaderstellend Overleg Gegevensmanagement d.d. 23-04-

2013

C = Concept; D = Definitief

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in

een geautomatiseerd gegevensbestand of openbaar gemaakt, in enige vorm of op enige wijze,

hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enig andere manier zonder

voorafgaande schriftelijke toestemming van de uitgever.

Beleid UWV Gegevens

Status

Definitief

Versie

1.1

## Inhoud

Managementsamenvatting 4

1 Inleiding 5

1.1 Aanleiding 5

1.2 Doel Beleid 6

1.3 Aard en Reikwijdte beleid 6

1.4 Relatie met andere Gegevensmanagement producten 6

1.5 Samenhang met UWV missie en visie 8

Deel I Beleidsuitgangspunten UWV Gegevens 9

2 Beleidsuitgangspunten 9

Deel II Beschrijving beleid UWV Gegevens 10

3 Het beleid UWV Gegevens 10

3.1 Doel en gebruik beleid UWV Gegevens 10

3.2 Onderdelen beleid UWV Gegevens 11

3.3 Doorontwikkeling en Beheer 13

4 Normen, Richtlijnen en Standaarden 13

4.1 Interne normen, richtlijnen en standaarden 13

4.2 Externe normen, richtlijnen en standaarden 14

5 Begrippenlijst UWV 15

6 Bedrijfsobjectmodel UWV 15

## 7 CGM/UGR 16

7.1 Canoniek gegevensmodel UWV 16

7.2 UWV Gegevensregister 16

8 Doelmodellen 17

8.1 Functionele gegevensmodellen 17

8.2 Berichtmodellen 18

8.3 Overige modellen 19

8.3.1 Datawarehouse (DWH) 19

8.3.2 Modellen standaard softwarepakketten 19

Bijlage I: Begrippen- en afkortingenlijst 20

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand

of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enig andere

manier zonder voorafgaande schriftelijke toestemming van de uitgever.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

4 van 22

Managementsamenvatting

semantische1

Dit document beschrijft de beleidsuitgangspunten voor de basis van de UWV

gegevenshuishouding, dit laatste ook aangeduid als het beleid UWV Gegevens.

Het kennen van de betekenis van gegevens is cruciaal bij hergebruik en uitwisseling van gegevens.

Daarnaast is het kennen van de betekenis, maar ook van andere eigenschappen van gegevens (zoals

bron, formaat, opslagwijze), randvoorwaardelijk voor het geautomatiseerd laten verlopen van processen

(straight through processing).

Het beleid UWV Gegevens geeft invulling aan het gegevensprincipe “De UWV-gegevenshuishouding is

gestandaardiseerd” en daarmee aan de voorwaarden voor een goed ingerichte gegevenshuishouding,

namelijk:

Gegevens zijn gestandaardiseerd zodat de uitwisselbaarheid en het hergebruik van gegevens



mogelijk wordt gemaakt.

Er is inzicht in de betekenis van de UWV bedrijfsgegevens en het gebruik ervan in



informatiesystemen en uitwisselingen.

Dit beleid heeft twee belangrijke kenmerken of karaktereigenschappen. Het is een streefbeeld/norm: zo

willen we het doen. Dit betekent dat de huidige situatie nog niet volledig conform dit streefbeeld is, maar

anderzijds wel dat elke verandering ten aanzien van gegevens aan dit beleid moet voldoen.

Het andere kenmerk is dat dit beleid een ‘paraplubeleid’ is waaronder bij de onderdelen van dit beleid

behorend (deel-) beleid, standaarden en richtlijnen gepositioneerd kunnen worden.

Dit document heeft dus niet tot doel elk onderdeel van het beleid UWV Gegevens tot in detail te

beschrijven. De onderdelen worden in een of meer aparte documenten beschreven.

De inhoud bestaat uit twee delen. Deel I geeft op globaal niveau de beleidsuitgangspunten weer. In deel

II geeft dit document inzicht in het doel, de inhoud, het gebruik en de reikwijdte van het beleid UWV

Gegevens. Tot slot is een beschrijving gegeven van de onderdelen van het beleid met daarbij de

samenhang tussen relevante onderdelen van het beleid.

1

Semantiek betreft de betekenis van gegevens en begrippen.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

5 van 22

1 Inleiding

Dit document beschrijft het beleid voor de semantische basis van de UWV Gegevenshuishouding.

Semantiek betreft de betekenis van gegevens en begrippen. Het kennen van de betekenis van gegevens

is cruciaal bij hergebruik en uitwisseling van gegevens. Zoals het forum standaardisatie stelt in het

stelselschaal’2:

rapport ‘semantiek op

“Verantwoord hergebruik vergt zekerheid over betekenis van informatie”.

Waar het gaat over betekenissen spreken we over semantiek en de mogelijkheid tot onderlinge

uitwisseling op dit terrein heet semantische interoperabiliteit.

Daarnaast is het kennen van de betekenis, maar ook van andere eigenschappen van gegevens (zoals

bron, formaat, opslagwijze) randvoorwaardelijk voor het geautomatiseerd laten verlopen van processen

(straight through processing).

Aanleiding3

1.1

De vorige versie van dit document stamt uit 2005. Niet alleen zijn delen van de tekst verouderd , ook een

aantal lopende of afgeronde ontwikkelingen nopen tot actualisering. De belangrijkste zijn:

de programma’s e-Werken en e-Dienstverlening,



de Visie UWV Gegevenshuishouding,



de inrichting van Lokaal Gegevensmanagement,



ontwikkelingen rond datakwaliteit zoals aangestuurd door de Coalitie Gegevensmanagement,



 en de standaard ISO 17113 voor berichtontwikkeling.

Binnen al deze onderwerpen gaat het om het uitwisselen, hergebruiken en beheren van gegevens, een

goed beschreven en onderhouden domein UWV Gegevens is hiervoor randvoorwaardelijk.

Een andere aanleiding tot herziening is de gewijzigde kijk op een aantal onderdelen van het beleid UWV

Gegevens. Een tweetal voorbeelden: het Bedrijfsobjectmodel (BOM) bestaat nu uit meer delen, een

kernmodel en een aantal domeinmodellen. In de vorige versie spraken we over Standaard FUGEM UWV,

nu noemen we dat het Canoniek Gegevensmodel.

De vorige versie van dit document droeg de naam ‘UGR-beleid’. Nu heet het ‘Beleid UWV Gegevens’. Dit

suggereert een uitbreiding van de scope, maar dat is niet het geval. In de praktijk is de benaming UGR

meer en meer vereenzelvigd met het gegevenswoordenboek van UWV, zoals dat sinds jaar en dag op het

intranet wordt gepubliceerd. Het gebruik van dezelfde naam voor twee begrippen schept verwarring,

daarom is ervoor gekozen het grote geheel ‘UWV Gegevens´ te noemen, en de naam UGR te blijven

gebruiken voor het gegevenswoordenboek.

2

http://www.forumstandaardisatie.nl/fileadmin/os/documenten/FS20-06-

08%20Semantiek%20op%20stelselschaal.pdf (geraadpleegd: 21-07-2015)

3

Juli 2015: Bij de actualisatie van dit document (geen inhoudelijke wijzigingen ) is een aantal beschreven aanleidingen

niet meer juist of actueel. Echter het geeft weer waarom in 2013 het document is opgesteld. Het doel van het

document is nog steeds onverminderd geldig.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

6 van 22

1.2 Doel Beleid

Het beleid UWV Gegevens heeft als doel de kwaliteit en de efficiency van de UWV Gegevenshuishouding

te verhogen en te garanderen door middel van het standaardiseren, modelleren, beschrijven en beheren

van de bedrijfsgegevens van UWV op metaniveau.

Het beleid UWV Gegevens geeft hiermee invulling aan het gegevensprincipe

“De UWV Gegevenshuishouding is gestandaardiseerd”

en daarmee aan de voorwaarden voor een goed ingerichte gegevenshuishouding, namelijk:

Gegevens zijn gestandaardiseerd zodat de uitwisselbaarheid en het hergebruik van gegevens



mogelijk wordt gemaakt.

Er is inzicht in de betekenis van de UWV bedrijfsgegevens en het gebruik ervan in



informatiesystemen en uitwisselingen.

1.3 Aard en Reikwijdte beleid

Dit beleid is een streefbeeld/norm: zo willen we het doen. Dit betekent dat de huidige situatie nog niet

volledig conform dit streefbeeld is maar aan de andere kant wel dat elke verandering ten aanzien van

gegevens aan dit beleid moet voldoen.

Tot de doelgroep gebruikers behoren: beleidsadviseurs, architecten, lokaal gegevensmanagers, business

consultants, informatieanalisten, functioneel ontwerpers, functioneel beheerders, berichtontwikkelaars,

procesontwerpers, projectleiders/-managers en alle anderen die zich met de UWV Gegevenshuishouding

bezig houden.

1.4 Relatie met andere Gegevensmanagement producten

Voor specifieke onderdelen van het beleid UWV Gegevens (voor een beschrijving zie deel II) zijn

beleidsdocumenten opgesteld. De in dit document genoemde (gerelateerde) beleids- en/of

architectuurdocumenten van de Data Office UWV zijn beschikbaar op de Digitale Werkplek onder Data

Office UWV, Producten en Kaders.

Gegevensmanagement product Relatie met beleid UWV Gegevens

Gegevensprincipes Beleid UWV Gegevens levert bijdrage aan nadere

invulling van de gegevensprincipes.

Beleid Normenhiërarchie Behoort tot de Standaarden en Richtlijnen van het

beleid UWV Gegevens.

Beleid Tabellen UGR Onderdeel van het blok Standaarden en Richtlijnen

van het beleid UWV Gegevens.

[herziene versie in ontwikkeling]

Beleid omgaan met gegevensredundantie Beleid heeft indirecte relatie met beleid UWV

Gegevens en betreft hoe moet worden omgegaan met

opslag van gegevens.

Versiebeheer UGR en UwvML Onderdeel van het blok Standaarden en Richtlijnen

van het beleid UWV Gegevens.

Dit document beschrijft hoe er moet worden

omgegaan met versies van het UGR en het UwvML

Basisschema en biedt inzicht in de onderlinge relatie

tussen versies.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

7 van 22

Gegevensmanagement product Relatie met beleid UWV Gegevens

Gegevenseigenaarschap Onderdeel van het blok Standaarden en Richtlijnen

van het beleid UWV Gegevens.

Beschrijft hoe de eigenaar van een gegeven wordt

bepaald. En wat de TVB’n van die eigenaar zijn op het

gebied van gebruik, kwaliteit en definiëring van dat

gegeven.

[herziene versie in ontwikkeling]

Beheerproces UGR en CGM Geeft aan hoe het beheerproces van de onderdelen

UWV Gegevensregister en Canoniek Gegevensmodel

is ingericht. [document in ontwikkeling]

Beleidsontwikkelingsproces Geeft aan hoe het beleidsontwikkelingsproces is

ingericht; onderdeel Standaarden en richtlijnen.

[document in ontwikkeling]

Samenwerkingsafspraken Centraal en Lokaal Betreft de samenwerking met betrekking tot de

Gegevensmanagement toepassing binnen de divisie/staf door Lokaal

Gegevensmanagement van alle onderdelen uit het

beleid UWV Gegevens [wordt deels vervangen door

het in ontwikkeling zijnde beheerproces UGR en CGM]

Wijzigingsprocedure SGR voor UWV Maakt gebruik van het beleid UWV Gegevens

UWV standaards voor BedrijfsObjectModel Onderdeel van het blok Standaarden en Richtlijnen

(BOM) van het beleid UWV Gegevens. Geeft aan hoe een

BOM eruitziet en de wijze van vormgeving.

UWV standaards voor Functioneel Onderdeel van het blok Standaarden en Richtlijnen

Gegevensmodel (FUGEM) van het beleid UWV Gegevens. Geeft aan hoe een

functioneel gegevensmodel eruit ziet en de wijze van

vormgeving.

[herziene versie in ontwikkeling]

Berichtstandaard UWV Onderdeel van het blok Standaarden en Richtlijnen

van het beleid UWV Gegevens. Geeft functionele

aanwijzingen voor het opstellen

gegevensuitwisselingen (berichten).

UwvML Servicestandaard Onderdeel van het blok Standaarden en Richtlijnen

van het beleid UWV Gegevens. Geeft technische

aanwijzingen voor het opstellen van UwvML

gegevensuitwisselingen (berichten).

Beschrijving Metamodel CGM en UGR Beschrijft in detail hoe het UGR en het CGM zijn

opgebouwd, en welke informatie hier in is

opgenomen.

[document in ontwikkeling]

UwvML Basisschema Onderdeel van het beleid UWV Gegevens. ‘Uitwerking

van de richtlijnen en standaarden in UwvML (XML).

Begrippenlijst UWV Gegevensmanagement Maakt deel uit van het onderdeel Begrippenlijst UWV.

UWV Bedrijfsobjectmodel (BOM) Onderdeel van het beleid UWV Gegevens

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

8 van 22

1.5 Samenhang met UWV missie en visie

Een goed ingerichte gegevenshuishouding is een huishouding waarbinnen gemeenschappelijk gebruik van

gegevens gestimuleerd wordt en waarin op een effectieve en efficiënte wijze gegevens worden

verzameld, vastgelegd en uitgewisseld, zodat de juiste gegevens met de juiste kwaliteit op het juiste

moment tegen een redelijke prijs aan zowel interne als externe partijen beschikbaar gesteld kunnen

worden.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

9 van 22

Deel I Beleidsuitgangspunten UWV Gegevens

2 Beleidsuitgangspunten

Gegevens4.

In dit hoofdstuk staan de belangrijkste beleidsuitgangspunten voor het beleid UWV Deze

vormen de uitwerking van het gegevensprincipe:

gestandaardiseerd”5.

“De UWV-gegevenshuishouding is

Alle UWV gegevens vallen onder het beleid UWV Gegevens.



Het Bedrijfsobjectmodel (BOM) in combinatie met het Canoniek gegevensmodel (CGM) is de basis



voor de ontwikkeling van het gegevensdeel bij veranderingen in de informatievoorziening.

Alle gegevens en gegevensmodellen, op functioneel niveau, worden opgesteld, vastgelegd en



toegepast volgens de richtlijnen/standaarden van het beleid UWV Gegevens

- Alle UWV gegevens zijn beschreven in het UWV Gegevensregister (UGR)

- Alle kernbegrippen van UWV zijn opgenomen in het bedrijfswoordenboek van UWV, de

begrippenlijst UWV. Deze lijst vormt onder meer de basis voor het opstellen van

gegevensdefinities, business rules en procesbeschrijvingen

Uitwisseling van gegevens binnen en buiten UWV gebeurt volgens de richtlijnen/standaarden van het



beleid UWV Gegevens.

Toevoegingen en wijzigingen van onderdelen van het beleid UWV Gegevens worden verplicht



afgestemd met belanghebbende binnen de organisatie.

 Na afstemming van wijzigingen en toevoegingen met belanghebbenden bepaalt de Data Office de

inhoud en vormgeving van de onderdelen van het beleid UWV Gegevens.

4

Conform het karakter van het voorliggende beleid (paraplubeleid) zijn voor verschillende onderdelen van en

onderwerpen dit beleid nadere beleidsuitgangspunten neergelegd in separate documenten, zie hiervoor paragraaf 1.4

5

Bron: Gegevensprincipes

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

10 van 22

Deel II Beschrijving beleid UWV Gegevens

In dit deel is het beleid UWV Gegevens, de onderdelen daarvan en de samenhang daartussen

beschreven. Hoofdstuk 3 gaat in op het beleid UWV Gegevens als geheel, met een (korte) beschrijving

van de onderdelen en de samenhang. De daarna volgende hoofdstukken behandelen de afzonderlijke

onderdelen in meer detail.

3 Het beleid UWV Gegevens

Dit hoofdstuk beschrijft het beleid UWV Gegevens op hoofdlijnen. Deze is geschetst in figuur 1. Deze

onderdelen zijn in meer detail beschreven in hoofdstuk 4 tot en met hoofdstuk 8. Er volgt een

beschrijving van het doel en gebruik van het beleid UWV Gegevens, de samenhang tussen de onderdelen

en tot slot hoe we omgaan met ontwikkeling en beheer.

Figuur 1 Onderdelen beleid UWV Gegevens

3.1 Doel en gebruik beleid UWV Gegevens

Het beleid UWV Gegevens levert de semantische basis voor de UWV gegevenshuishouding. Het heeft als

doel de kwaliteit en de efficiency van de UWV Gegevenshuishouding te verhogen en te garanderen door

middel van het standaardiseren, modelleren, beschrijven en beheren van de bedrijfsgegevens van UWV

op metaniveau. Het inzicht in de bedrijfsgegevens dat hiermee ontstaat, geldt als een kritieke

succesfactor voor de bedrijfsvoering van UWV.

Ook ondersteunt het beleid UWV Gegevens de gestandaardiseerde uitwisseling van gegevens

(semantische interoperabiliteit). De aanwezigheid van gestandaardiseerde gegevens zijn noodzakelijk

voor het kunnen toepassen van binnen UWV geldende standaarden voor

gegevensuitwisselingsarchitectuur (zie Berichtstandaard UWV).

Het biedt daarmee het volgende:

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

11 van 22

Inzicht in de gegevens van UWV



Weten wat de gegevens die we binnen UWV gebruiken betekenen, en hoe ze er uit zien. Waar ze

worden gebruikt, hoe ze worden uitgewisseld, en in welke berichten ze staan.

Inzicht in knelpunten



Dit beleid biedt een streefbeeld/norm: zo willen we het doen. Dit betekent dat de huidige situatie nog

niet volledig conform dit streefbeeld is. Het 'streefbeeld' kan gebruikt worden om het pad van IST

naar SOLL inzichtelijk te maken inclusief de knelpunten. We kunnen zien waar er binnen de

gegevenshuishouding knelpunten zijn, of dreigen te ontstaan. Bijvoorbeeld: waar zijn gegevens

moeilijk koppelbaar? Waar is er redundantie, waar zijn er inconsistenties of witte vlekken? Waar

liggen er kansen en mogelijkheden tot verbeteringen of sanering in het systeemlandschap?

Leidraad voor ontwikkeling en verandering van informatiesystemen



Ontwikkeling en aanpassing (beheer) van informatiesystemen en processen omvat veelal ook het

ontwerp en de implementatie van nieuwe of gewijzigde gegevens, gegevenskoppelingen, en/of opslag

van gegevens in databases. Het beleid UWV Gegevens biedt hiervoor standaarden, richtlijnen,

modellen en gegevensdefinities.

Faciliteren van interoperabiliteit in ketens



Interoperabiliteit of uitwisselbaarheid is het vermogen van organisaties (en hun functies, processen

en systemen) om effectief en efficiënt diensten (waaronder informatie) te delen met de omgeving.

Het beleid UWV Gegevens is gericht op semantische interoperabiliteit, dat wil zeggen het vermogen

van systemen of organisaties om aan de kant van zender en ontvanger gegevens op dezelfde manier

te interpreteren. Dit is een belangrijke kwaliteitseis binnen ketens.

De in het beleid opgenomen modellen (BOM- CGM/UGR-doelmodellen), zoals weergegeven in figuur 1,

hebben ieder hun eigen context in functie en gebruik. Op hoofdlijnen betekent dit dat met name het

gebruik van de afzonderlijke modellen afhankelijk is van het niveau waarop je in gesprek bent. De

verschillende niveaus waarover over ‘gegevens’ wordt gesproken zijn bijvoorbeeld, management,

architectuur en of ontwerp van de gegevens. Daarnaast is er van samenhang tussen de onderdelen. In

paragraaf 3.2 wordt de samenhang hiervan weergegeven. Dit beleid geeft geen invulling aan de wijze

waarop de gegevens feitelijk zijn opgeslagen in het logische informatiesysteem (feitelijke

gegevensmodel) of hoe het functioneel gegevensmodel technisch vertaald is in de database (technische

gegevensmodel).

3.2 Onderdelen beleid UWV Gegevens

Deze paragraaf geeft een korte beschrijving van de onderdelen van het beleid UWV Gegevens. In bijlage

2 is een weergave van de relatie tussen het BOM, CGM/UGR en FUGEM weergegeven.

De Begrippenlijst UWV definieert de begrippen die binnen UWV worden gehanteerd. De begrippen

worden gehanteerd in alle andere blokken, bijvoorbeeld in definities van bedrijfsobjecten en van

gegevens, behalve in het ‘normenblok’. De begrippenlijst wordt uiteraard ook buiten de grenzen van het

beleid UWV Gegevens zelf gebruikt zoals in business rules en procesbeschrijvingen.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

12 van 22

Het Bedrijfsobjectmodel (BOM) is de beschrijving van die ‘dingen in de werkelijkheid’ waarover

mogelijk gegevens moeten worden vastgelegd ten behoeve van de taakuitvoering van UWV. Het BOM

bestaat uit een kernmodel met daarnaast een aantal domeinmodellen.

Samen geven de Begrippenlijst UWV en het Bedrijfsobjectmodel inzicht in de onderwerpen die belangrijk

zijn voor UWV en de taal waarin daarover gesproken wordt. Dit wordt ook wel aangeduid als ‘universe of

discourse’.

Welke gegevens vastgelegd worden, en hoe deze onderling gerelateerd zijn, staat in het Canoniek

Gegevensmodel (CGM). Er is dus een nauwe relatie tussen BOM en CGM: alle gegevens (entiteiten,

attributen, relaties) in het CGM zijn terug te voeren op elementen van het BOM (bedrijfsobjecten,

eigenschappen, relaties). Vanuit het oogpunt van het BOM gekeken kun je zien welke gegevens in het

CGM er op BOM elementen betrekking hebben. Dit is van belang bij impactanalyses en afbakening van

veranderingen.

Het CGM is modelmatig een compleet gegevensmodel, dat bestaat uit een visuele representatie in de

diagrammen6,

vorm van met daaraan gekoppeld de beschrijvingen van entiteiten, relaties tussen

entiteiten en van de gegevenselementen die op de diagrammen zijn afgebeeld.

Het UWV Gegevensregister (UGR) is te beschouwen als een gegevenswoordenboek. Alle beschrijvingen

van de attributen in het CGM zijn als gegevenselement opgenomen in het gegevenswoordenboek.

UGR is een deelverzameling van het CGM. De ingang van het UGR is primair op elementniveau, in

tegenstelling tot het CGM waarin de context en samenhang de primaire ingang is.

De Doelmodellen bevatten de functionele gegevensmodellen van informatiesystemen (de FUGEMs),

datawarehouses, berichten enzovoort. Dit zijn de niet gestandaardiseerde FUGEMs, maar ook de

gestandaardiseerde FUGEMs die zijn opgenomen in (lees: conform zijn met) het CGM.

Het CGM is uiteraard niet statisch, het wordt steeds in afstemming met de gebruikersorganisatie

aangepast aan wijzigingen in de informatiebehoefte. Dat betekent ook dat wijzigingen op een doelmodel,

na afstemming, worden opgenomen in het CGM. Er is dus twee-richtingenverkeer tussen CGM en

doelmodellen.

Het deel Normen, Richtlijnen en Standaarden biedt een kaderstellende basis voor de andere blokken:

voor alle onderdelen gelden de door het beleid bepaalde richtlijnen voor onder andere vormgeving en

ontwikkeling.

6

Deze diagrammen vertonen relevante ‘views’ op het totale model, bijvoorbeeld ‘persoonsgegevens’ of ‘loonaangifte’.

worden.

Het totale model is wel beschikbaar in de tooling, maar zal vanwege de omvang niet gepubliceerd

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

13 van 22

3.3 Doorontwikkeling en Beheer

Het beleid UWV Gegevens in werking is geen statisch geheel. Omdat UWV en zijn omgeving verandert,

verandert ook het begrippenkader en zijn er wijzigingen in de gegevenhuishouding. Ook technologische

ontwikkelingen hebben invloed: klanten kunnen in nabije toekomst zelf een deel van hun gegevens

beheren via internet, goedkope en snelle opslagmedia maken het mogelijk om allerlei metagegevens

(bijvoorbeeld kwaliteitsaspecten) bij de materiegegevens vast te leggen. Het beleid UWV Gegevens is in

zijn dus steeds geheel aan verandering onderhevig.

Na deze beschrijving van het beleid UWV Gegevens als geheel, gaan de volgende hoofdstukken meer in

detail in op de afzonderlijk onderdelen van het beleid.

4 Normen, Richtlijnen en Standaarden

Dit blok omvat alle kaders en voorschriften waaraan de inhoud van de andere blokken dient te voldoen.

Deze kaders en voorschriften zijn zeer divers, omdat zij op verschillende producten en op verschillende

aspecten betrekking hebben. Normen, richtlijnen en standaarden van het beleid UWV Gegevens zijn een

deelverzameling van de totale verzameling gegevensbeleid, -richtlijnen, -standaarden en –architectuur.

4.1 Interne normen, richtlijnen en standaarden

Voor een aantal onderwerpen zijn er al toepassingsrichtlijnen opgesteld die binnen UWV gelden. Dit zijn

onder meer:

UWV standaard voor Bedrijfsobjectmodel (BOM-standaard)

De BOM-standaard bevat de voorschriften en richtlijnen voor ontwikkeling van het Bedrijfsobjectmodel

van UWV.

UWV standaard voor Functioneel Gegevensmodel (FUGEM-standaard)

De FUGEM-standaard (FUGEM = Functioneel Gegevensmodel) bevat de voorschriften en richtlijnen voor

ontwikkeling van functionele gegevensmodellen binnen UWV.

Beleidsuitgangspunten Reference Data (uitbreiding en vervanging van Beleid Tabellen)

Dit document stelt de definitie vast van reference data en reference data management. Het geeft richting

aan de wijze van modelleren, beheren en beschikbaar stellen van reference data binnen UWV.

Berichtstandaard en UwvML Servicestandaard

UWV heeft strategisch gekozen voor een ‘service georiënteerde architectuur’ op basis van services. De

berichtstandaard bevat de richtlijnen voor het opstellen van de berichtdefinities waarmee de services

aangesproken worden.

Beleid normenhiërarchie

Richtlijnen voor de volgorde van toepassing van diverse interne en externe normen, richtlijnen en

standaarden.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

14 van 22

Versiebeheer UGR en UwvML

Richtlijnen voor het omgaan met versies van het UGR en het UwvML basisschema.

Wijzigingsprocedure SUWI Gegevensregister (SGR) voor UWV

Dit document beschrijft de procedure als wijzigingen van het SGR nodig zijn.

4.2 Externe normen, richtlijnen en standaarden

UWV heeft als uitgangspunt gekozen zoveel mogelijk bij nationale en internationale standaarden aan te

sluiten. Dit betekent dat het beleid UWV Gegevens naast interne ook een groep externe normen,

richtlijnen en standaarden kent.

De gegevens in de normen fungeren als ‘template’ of ‘sjabloon’ voor overeenkomstige gegevens in het

UGR. Bijvoorbeeld als UWV een landcode wil opnemen in een informatiesysteem dan fungeert ‘landcode

ISO’ als sjabloon voor de gegevensbeschrijving die dan in het UGR wordt opgenomen.

Ook zijn er overheidsstandaarden waarvan conform het ‘pas toe, of leg uit’-principe gebruik moet worden

gemaakt. Deze standaarden worden vastgesteld door het Forum Standaardisatie.7 Het gebruik van deze

standaarden door UWV (of de uitleg waarom niet) dient beschreven te zijn.

UWV neemt deel aan overleg met externe standaardiseringsorganisaties, bijvoorbeeld de gremia van het

Stelsel Basisregistraties en de SUWIketen.

Voorbeelden van deze standaarden zijn NEN en ISO-normen, de gegevensdefinities van de

Basisregistraties (o.a. GBA, NHR) en sectormodellen zoals het SUWI Gegevensregister.

NEN- en ISO-normen

Voor gegevens die veel voorkomen in gegevensuitwisselingen zijn nationale en internationale

standaarden of normen gemaakt. Conform het Beleid Normenhiërarchie moet bij het beschrijven van

nieuwe gegevens, veelal in de fase van informatieanalyse, eerst bekeken worden of een van deze normen

een adequate beschrijving geeft voor het nieuwe gegeven. Als dit het geval is, nemen we deze

beschrijving over in het CGM/UGR.

Basisregistraties

In de UWV gegevenshuishouding komen gegevens voor die overgenomen zijn van externe

basisregistraties, bijvoorbeeld de GBA. Indien van toepassing wordt in het UGR de gegevensbeschrijving

van de basisregistratie overgenomen.

Normregisters

Een normregister is een gegevensregister waarin afspraken zijn vastgelegd over de in een bepaalde

sector te gebruiken gegevensbeschrijvingen, bijvoorbeeld het SUWI Gegevensregister (SGR).

Gegevensbeschrijvingen uit deze bronnen voor gegevens die ook binnen UWV gebruikt worden, worden in

principe overgenomen.

7

Zie http://lijsten.forumstandaardisatie.nl/lijsten/open-standaarden (geraadpleegd 21-7-2015)

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

15 van 22

De gegevensstandaarden van UWV omvatten de modellen die het gegevensaspect beschrijven van de

wereld van business (Begrippenlijst UWV en bedrijfsobjectmodel) en van de wereld van de

informatievoorziening (UGR en canoniek gegevensmodel). Deze worden hieronder kort beschreven.

5 Begrippenlijst UWV

Door de verschillende bedrijfsonderdelen worden ‘eigen’ begrippen en definities gehanteerd en

vastgelegd in begrippenlijsten. Hierdoor ontstaat al gauw een soort Babylonische spraakverwarring. Uit

oogpunt van communicatie en standaardisatie is het wenselijk deze verschillende ‘begrippenlijsten’

samen te voegen in één UWV bedrijfswoordenboek onder de noemer Begrippenlijst UWV.

De voor de organisatie belangrijke begrippen of termen worden bedrijfsbreed gedefinieerd in dit

woordenboek en waar nodig verbijzonderd naar specifieke context. Ze zijn vervolgens te gebruiken bij

het opstellen van bijvoorbeeld gegevensdefinities, bedrijfsregels en beschrijvingen van processen.

Door gemeenschappelijke begrippen en definities vast te stellen wordt de spraakverwarring opgelost.

Bovendien levert een eenduidige en actuele definiëring een grote bijdrage aan de kwaliteit van de

gegevens en gegevensuitwisseling. Je moet immers goed weten wat je in handen hebt.

## UWV8

6 Bedrijfsobjectmodel

objecten9

Een bedrijfsobjectmodel is de gestructureerde beschrijving van de belangrijkste en de relaties

tussen deze objecten. Een object is een weergave van iets (persoon of zaak) dat in de werkelijkheid van

UWV belangrijk is.

Het bedrijfsobjectmodel UWV bevat:

1. de beschrijving van objecten

2. een diagram dat relaties/verbanden tussen objecten schematisch weergeeft, vooral de relaties die

nodig zijn voor een goed begrip van de objecten

3. ontwerpbeslissingen.

Het bedrijfsobjectmodel kent een kernmodel en meerdere domeinmodellen:

1. het kernmodel met objecten die op hoog abstractieniveau de ‘onderwerpen van gesprek’ binnen de

primaire bedrijfsfuncties van UWV weergeven

2. de domeinmodellen die het kernmodel aanvullen of nader definiëren.

Het kernobjectmodel en de domeinobjectmodellen vormen samen het bedrijfsbrede objectmodel van

UWV en bieden in die samenhang een basis voor de meer gedetailleerde gegevensmodellen waarin alle

worden.10

mogelijk te onderkennen gegevenselementen met hun kenmerken tot in detail beschreven

8

Zie hiervoor in detail de documenten die BOM en BOM-standaard beschrijven.

9

Volgens de theorie moeten we hier eigenlijk spreken over ‘objecttype’ in plaats van over ‘object’. Een object is het

ding zelf, wat door het type beschreven wordt. Om aan te sluiten op het normale spraakgebruik gebruiken we in

document de term ‘object’.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

16 van 22

## 7 CGM/UGR

In deze paragraaf wordt de combinatie van CGM en UGR, die in paragraaf 3 al geschetst is, inhoudelijk

nader beschreven.

7.1 Canoniek gegevensmodel UWV

Het canoniek gegevensmodel (CGM) is een beschrijving van de gegevens van UWV en van de samenhang

tussen gegevens door middel van groeperingen en de relaties daartussen. Het is daarmee een

bedrijfsbreed gegevensmodel. De toevoeging ‘canoniek’ betekent hier: overeengekomen en daarmee tot

richtsnoer dienend.

Het CGM is dus het standaard gegevensmodel van de belangrijkste gegevens van UWV.

Het CGM sluit aan op het Bedrijfsobjectmodel: bedrijfsobjecten en hun eigenschappen vinden we in het

CGM terug als entiteiten met attributen, de relaties tussen objecten vinden we terug als relaties tussen

entiteiten.

Alle attributen zijn beschreven in het UWV Gegevensregister, dat met het CGM één geheel vormt.

Het CGM is vormgegeven overeenkomstig de standaard voor functionele gegevensmodellen (FUGEM-

standaard).

De gegevens in lokale bronsystemen kunnen aan de gegevens in dit model worden gerelateerd zodat

zichtbaar wordt waar welke gegevens in de UWV Gegevenshuishouding aanwezig zijn.

Het canoniek gegevensmodel vormt de basis voor ontwikkeling en beheer van diverse typen

gegevensmodellen van UWV: van datamodellen van informatiesystemen, berichtmodellen,

datawarehousemodellen enzovoort. Deze modellen hebben allemaal een eigen functie binnen de UWV

Gegevenshuishouding. In een volgende paragraaf gaan we verder op die functies in.

Wat al die modellen gemeen hebben is dat ze op het gebied van de semantiek in overeenstemming

moeten zijn met het CGM. In het overzicht (zie de afbeelding in paragraaf 3) zijn ze daarom

‘doelmodellen’ genoemd.

Waar er wellicht geen directe overeenstemming is te bereiken (legacy-systemen) en waar dat op het

eerste gezicht problematisch is (ERP-systemen), wordt de verbinding gelegd met de corresponderende

gegevens in het CGM, en wordt de afwijking gedocumenteerd. Het moet hierdoor altijd mogelijk zijn een

vertaling te maken van het ‘eigen’ gegeven naar het CGM.

Zodoende is geborgd dat de uitwisseling van gegevens via services en berichten conform de standaard

kan zijn.

7.2 UWV Gegevensregister

Het UWV Gegevensregister (UGR) is het gegevenswoordenboek (ook: data dictionary) van UWV. Dit

woordenboek bevat de gegevenselementen van UWV, de bouwstenen voor de overige gegevensmodellen.

10

Zie het architectuurdocument UWV Bedrijfsobjectmodel waarin doel en inhoud van het BOM is beschreven .

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

17 van 22

Het UGR bevat metagegevens 11, hiermee geven we onder meer de betekenis van en aanwijzingen over

het gebruik van gegevens weer. Als we het hebben over de semantische basis van de

gegevenshuishouding dan zijn metagegevens het onderdeel dat hieraan veel bijdraagt.

Hierna volgt de beschrijving van de hoofdonderdelen waaruit het UGR bestaat.

Standaard gegevenselementen

Dit zijn gegevens die we UWV-breed gebruiken en bestaan veelal uit gegevens die meervoudig gebruikt

worden of die overgenomen zijn uit externe normen. De UWV standaardgegevens hebben een

voorschrijvend karakter bij de ontwikkeling van nieuwe informatiesystemen. Anderzijds leveren

(veranderingen in of nieuwe) informatiesystemen nieuwe beschrijvingen aan voor zover deze nog niet in

UGR voorkomen. De gegevens zijn in context en samenhang gemodelleerd in het CGM.

Standaardtabellen

Een Tabel is bijzondere vorm van een gegevensgroep. Is een ‘normale’ gegevensgroep een groepering

van bij elkaar horende eigenschappen van iets in de werkelijkheid (gegevens), een tabel is een

verzameling gegevens (minimaal code, omschrijving) die betrekking heeft op de mogelijke waarden van

één eigenschap. Om te voorkomen dat er voor veel gebruikte tabellen meer varianten bestaan, kent het

UGR standaardtabellen. Bijvoorbeeld: Tabel code CAO, Tabel Landen ISO, Postcodetabel.

UwvML-basisschema

Het UwvML Basisschema is onderdeel van de UwvML-standaard en is een vertaling van het CGM/UGR

naar de internet standaard XML (Extensible Markup Language). UwvML is een XML-dialect. Het is de

gemeenschappelijke taal voor elektronische gegevensuitwisseling binnen UWV en tussen UWV en

bepaalde partijen buiten UWV.12

8 Doelmodellen

Doelmodellen zijn de gegevensmodellen die binnen UWV aanwezig zijn of moeten worden vervaardigd op

basis van de standaardmodellen BOM en CGM, daarbij gebruikmakend van de begrippenlijst UWV en het

UGR. De belangrijkste daarvan worden in de volgende paragrafen kort behandeld: Functionele

gegevensmodellen (FUGEMs), Berichtmodellen en Overige modellen.

8.1 Functionele gegevensmodellen

FUGEM staat voor Functioneel Gegevensmodel. Dat is een model van de gegevens die in een

informatiesysteem worden gebruikt, beheerd en/of gecreëerd. Het model geeft de structuur van de

gegevensverzameling weer door middel van groepering van gegevenselementen op basis van functionele

afhankelijkheid en door middel van verbanden tussen de groepen. Het is inrichtingsafhankelijk, want

alleen die gegevens worden gemodelleerd die daadwerkelijk (zullen) worden gebruikt. Het is wel

technologieonafhankelijk, en dus nadrukkelijk geen ontwerp van een database.

Deze metagegevens van CGM/UGR zullen in een apart document worden beschreven.

11

12

Zie hiervoor de documenten ‘Berichtstandaard UWV’ en ‘UwvML Servicestandaard’.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

18 van 22

De vorm is die van een gestructureerde beschrijving van entiteittypen, attribuuttypen en relatietypen die

een rol spelen in het betreffende informatiesysteem, met bijbehorend diagram.

Anders dan de naam doet vermoeden ontstaat dit model niet geheel in de fase van functioneel ontwerp,

maar geeft het al in de analysefase een overzicht van de informatiebehoefte die het systeem (zowel de

afdekken.13

geautomatiseerde als de handmatige delen) moet

In het kort dient een FUGEM de volgende doelen:

Volledig overzicht van de relevante genormaliseerde gegevensstructuur van een logisch



informatiesysteem. Het FUGEM is een afspiegeling van de volledige gegevensbehoefte van dat logisch

informatiesysteem.

Inzicht in de onderlinge afhankelijkheden van gegevenselementen.



Input voor technisch ontwerp, in het bijzonder databaseontwerp, voor die onderdelen van het logisch



informatiesysteem die geautomatiseerd moeten worden ondersteund.

Vaststelling van het begrippenkader van het informatiesysteem middels eenduidige entiteittype



definities (gebaseerd op BOM en CGM).

In zijn ideale vorm is een FUGEM van een informatiesysteem niets anders dan een view op het CGM,

aangevuld met functionele gegevens die alleen voor de werking van het informatiesysteem zelf van

belang zijn, zoals tussenresultaten of gegevens om mutaties net terugwerkende kracht uit te kunnen

voeren . In de praktijk zien we dat veel FUGEMs al elementen van databaseontwerp of andere

inrichtingsaspecten in zich dragen.

Er zijn binnen UWV nog gegevensbeschrijvingen aanwezig die nog niet in het CGM gestandaardiseerd zijn

of ook niet meer gestandaardiseerd zullen worden in verband met bijvoorbeeld uitfaseren. Dit betreft

functionele gegevensmodellen (FUGEMs) van bijvoorbeeld legacy-systemen. Deze niet

gestandaardiseerde modellen zijn van zeer heterogene aard op het gebied van modelleringswijze,

volledigheid, gebruikte tooling, kwaliteit van beschrijving, toegankelijkheid etc. Tot de tijd dat dat ze op

standaard zijn gebracht worden de beschikbare modellen ‘as is’ in de afdeling Doelmodellen opgenomen.

8.2 Berichtmodellen

Standaardberichten bevatten gegevens die worden uitgewisseld met partijen of informatiesystemen zowel

binnen als buiten UWV. Net zoals een standaardgegeven wordt een standaardbericht beschreven conform

een vast metamodel.

13

Over het begrip ‘functioneel’ in dit verband:

Functioneel ontwerp: functioneel heeft hierin de betekenis van "geschikt voor een doel, taak of functie". Het gaat er in

een functioneel ontwerp om doel, taken en functie van het systeem te beschrijven en de wijze waarop het systeem die

realiseert.

Functioneel gegevensmodel: functioneel heeft hierin de betekenis van: in functie van elkaar, functioneel van elkaar

afhankelijk, met elkaar veranderend, meeveranderend met de bovenliggende grootheid. Het gaat er in een functioneel

gegevensmodel om dat de onderlinge afhankelijkheid van gegevens in het model verbeeld wordt.

Als een functioneel ontwerp verwijst naar gegevens en naar gegevensstructuren, dan gebeurt dat wel in de termen en

eenheden van het functionele gegevensmodel. Dat is immers als product van de gegevensanalyse beschikbaar.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

19 van 22

8.3 Overige modellen

Overal waar het gaat om eenduidige begrippen en gegevensdefinities binnen UWV, en in de

communicatie van UWV met partners dient gebruik gemaakt te worden van het beleid UWV Gegevens.

Dit geldt dus niet alleen voor de huidige situatie, maar ook voor toekomstige ontwikkelingen die binnen

UWV hun weerslag gaan vinden. Echter het is mogelijk dat er gegevensmodellen voorkomen of ontstaan

die niet volledig aan de eisen van het beleid UWV Gegevens voldoen (NB hierover moet altijd afstemming

plaatsvinden met de Data Office en Lokaal Gegevensmanagement). Deze situatie komt voor bij een

afwijkend gebruiksdoel en bijbehorende modellering (bijvoorbeeld Datawarehouse) of bij het gebruik van

een standaard softwarepakket. In alle gevallen dient wel gegevensuitwisseling met de omgeving te

gebeuren conform de eisen van het beleid UWV Gegevens.

Deze paragraaf beschrijft een aantal voorbeelden uit deze categorie.

8.3.1 Datawarehouse (DWH)

Ook de datawarehouses van UWV maken voor hun gegevensintegratie gebruik van het CGM.

DWH en/of Datamarts gebruiken een afwijkende modellering, veelal sterdiagrammen waar het UGR-

domein ERD-modellering voorschrijft.

8.3.2 Modellen standaard softwarepakketten

Het applicatiebeleid van UWV gaat uit van standaard softwarepakketten of suites. Deze pakketten hebben

soms een standaard gegevensmodel dat beperkt aangepast kan worden. In principe moet

standaardsoftware voldoen aan de eisen en richtlijnen van het beleid UWV Gegevens en vindt vastlegging

van het FUGEM plaats conform de standaarden. Waar deze software niet aan de genoemde eisen en

richtlijnen kan voldoen worden afwijkingen gedocumenteerd in de Projectstartarchitectuur en/of overige

projectdocumentatie en ook in de modelbeschrijving dat onderdeel is van het beleid UWV Gegevens.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

20 van 22

Bijlage I: Begrippen- en afkortingenlijst

Hieronder volgt een lijst met in dit document gebruikte begrippen en afkortingen waarvan de betekenis in

die context wellicht niet meteen duidelijk is.

Begrip Omschrijving Bron

Business Zie Gebruikersorganisatie

Bedrijfsobject Zie Objecttype

Canoniek Standaard gegevensmodel van de belangrijkste

gegevensmodel (CGM) gegevens van UWV. Bevat de beschrijving van de

gegevens van UWV en van de samenhang tussen

gegevens door middel van groeperingen en de

relaties daartussen.

De toevoeging ‘canoniek’ betekent hier:

overeengekomen en daarmee tot richtsnoer

dienend.

Doelmodel De gegevensmodellen die binnen UWV moeten

worden vervaardigd op basis van de

standaardmodellen BOM en CGM, daarbij gebruik

makend van de begrippenlijst UWV en het UGR.

We onderscheiden drie typen doelmodellen:

Functionele gegevensmodellen (FUGEMs),

berichtmodellen en overige modellen

FUGEM – Functioneel Een gestructureerde beschrijving van Begrippenlijst UWV

GegevensModel entiteittypen, attributen en relatietypen die een Gegevensmanagement

rol spelen in een logisch systeem of in een

logische applicatie, incl. een schematische

voorstelling.

Gebruikersorganisatie Het geheel van mensen en middelen dat zich

bezighoudt met de bedrijfsprocessen`.

Gegevenshuishouding Het geheel aan bedrijfsgegevens, inclusief de

bijbehorende taken zoals verwerven, vastleggen,

toegankelijk maken, beheren en verstrekken of

uitwisselen.

Interoperabiliteit Uitwisselbaarheid, het vermogen van organisaties http://www.noraonline.nl/

(en hun functies, processen en systemen) om wiki/Interoperabiliteit

effectief en efficiënt diensten (waaronder (geraadpleegd 28072015)

informatie) te delen met de omgeving

Interoperabiliteit kent drie deelaspecten:

semantische, technische en organisatorische

interoperabiliteit.

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

21 van 22

Begrip Omschrijving Bron

Metagegeven Feit dat een onderdeel is van de beschrijving van Begrippenlijst UWV

een gegeven of gegevensgroep of van een Gegevensmanagement

gegevenselement.

Metamodel A metamodel is a precise definition of the

constructs and rules needed for creating models

A model that describes how and with what the TOGAF 9 definitions

architecture will be described in a structured way.

Norm Een norm is een vrijwillige afspraak tussen NEN website 28-2-2011

belanghebbende partijen over een product, dienst

of proces.

Objecttype Soort van iets uit de werkelijkheid waarvan Begrippenlijst UWV

eigenschappen in de vorm van gegevens worden Gegevensmanagement

vastgelegd.

Een individueel voorkomend iets uit de

werkelijkheid dat beantwoordt aan deze

soortbeschrijving noemen we een object.

UWV onderkent:

1. kernobjecten die op hoog abstractieniveau de

‘onderwerpen van gesprek’ binnen de primaire

bedrijfsfuncties van UWV weergeven en deel

uitmaken van het kernobjectmodel.

2. domeinobjecten die de ‘onderwerpen van

gesprek’ weergeven binnen een afgebakend

domein van bedrijfsfuncties en deel uitmaken van

een domeinobjectmodel.

Kernobjectmodel en domeinobjectmodellen samen

vormen het UWV-brede “bedrijfsobjectmodel”

## (BOM).

Reference Data Gegevens die worden gebruikt om andere Beleidsuitgangspunten

gegevens te classificeren of te categoriseren. Reference Data

Reference data hebben altijd een vast

waardebereik op een bepaald moment in de tijd.

Semantiek Betekenissenleer.

(semantisch) In deze context betreft het de betekenis van

gegevens en begrippen die door UWV gebruikt en

uitgewisseld worden.

Semantische Het vermogen van systemen of organisaties om

interoperabiliteit aan de kant van zender en ontvanger gegevens

op dezelfde manier te interpreteren

SUWI Gegevensregister Het gegevenswoordenboek voor de SUWIketen

## (SGR)

Beleid UWV Gegevens

Datum

8 september 2015

Versie

1.1

Pagina

22 van 22

Begrip Omschrijving Bron

SuwiML XML variant gebruikt binnen de SUWIketen,

‘XML-vertaling’ van het SGR

Richtlijn Aanwijzing van een te volgen gedrag of Van Dale

handelwijze; voorschrift

Standaard Vaststaand erkend voorbeeld of model Van Dale

UGR UWV Gegevensregister

UwvML XML variant gebruikt door UWV

‘XML-vertaling’ van het CGM/UGR

XML Extensible Markup Language (XML) is een Gebaseerd op

standaard van het World Wide Web Consortium http://nl.wikipedia.org/wik

voor de syntaxis van formele opmaaktalen i/XML

waarmee men gestructureerde gegevens kan (geraadpleegd 21-07-

weergeven in de vorm van platte tekst. 2015)

---

Bron: [Besluit Woo-verzoek IT strategie UWV](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv) · [Bijlage 4 Beleid UWV Gegevens versie 1.1 (PDF, 562 kB)](https://www.uwv.nl/assets-kai/files/388a1548-a936-416b-a116-fcd296fe27a5/bijlage-4-beleid-uwv-gegevens.pdf)
