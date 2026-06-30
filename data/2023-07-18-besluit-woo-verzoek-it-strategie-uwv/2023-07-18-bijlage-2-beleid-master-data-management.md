---
source_id: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv/2023-07-18-bijlage-2-beleid-master-data-management
publication_slug: 2023-07-18-besluit-woo-verzoek-it-strategie-uwv
pdf_slug: 2023-07-18-bijlage-2-beleid-master-data-management
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv
pdf_url: https://www.uwv.nl/assets-kai/files/fbafb48e-590a-4e4e-8bc1-c0780b9c0ac1/bijlage-2-beleid-master-data-management.pdf
publication_title: Besluit Woo-verzoek IT strategie UWV
publication_date: '2023-07-18T00:00:00Z'
publication_type: WOO publicatie
pdf_label: Bijlage 2 Beleid Master Data Management versie 1.1.1 (PDF, 600 kB)
retrieved_at: '2026-06-30T13:18:07+00:00'
sha256: 7704a2b35953706d710fdd3fe4af77815ea1c0d10438610e01749cc4457e8586
page_count: 14
ocr_used: false
---

Beleid Master Data Management

Doorgaan op de ingeslagen weg

Beleid Master Data

Management

Datum

28 december 2022

Auteur

Status

Data Office UWV

Vastgesteld door KOG

Ons kenmerk

Versie

-

1.1.1

Pagina

2 van 14

Versiehistorie

Ver- Datum Status Wijziging Auteur

sie

0.1 29 november 2015 Concept Eerste versie

5.1 lid 2 sub e

0.2 30 december 2016 Concept Reviewversie voor LGM en DO

5.1 lid 2 sub e

0.3 10 februari 2017 Concept Aanpassingen op basis eerste re-

5.1 lid 2 sub e

view

0.6 6 maart 2017 Concept Aanpassingen op basis review Ge-

5.1 lid 2 sub e

gevensmanagers

0.7 10 maart 2017 Akkoord Enkele aanvullingen vanuit GM-

5.1 lid 2 sub e

GM overleg

1.0 15 maart 2017 Vastge- Geen wijzigingen.

5.1 lid 2 sub e

steld door

## KOG

1.1 9 mei 2018 Wijzigin- Herzien in het kader van AVG.

gen vast-

gesteld

door KOG

1.1.1 19 februari 2019 Geen wijzi- Onbruikbare URL’s verwijderd.

5.1 lid 2 sub e

ging Geen inhoudelijke wijzigingen.

1.1.1 28 december 2022 Geen wijzi- Gecontroleerd op werking hyper-

5.1 lid 2 sub e

ging links en terminologie

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand

of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door fotokopieën, opnamen of op enig andere

manier zonder voorafgaande schriftelijke toestemming van UWV.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

3 van 14

Inhoud

1 Inleiding 4

2 Wat is Master Data en Master Data Management? 4

2.1 Data types 4

2.2 Definitie van Master Data 5

2.3 Definitie van Master Data Management 5

3 Doelen Master Data Management 6

4 Beleid 9

4.1 Invullen randvoorwaarden 9

4.1.1 De gegevenshuishouding is in kaart gebracht 9

4.1.2 De gegevens zijn bekend en gedefinieerd 9

4.1.3 De gegevensuitwisseling is gestandaardiseerd 9

4.1.4 Governance van de gegevenshuishouding is ingericht 9

4.2 Vaststellen van de UWV Master Data 10

4.2.1 Over welke objecten worden Master Data verzameld? 10

4.2.2 Welke gegevens worden aangemerkt als Master Data? 10

4.2.3 Voorbeelden van Master Data Registraties 10

4.3 Het gewenste ambitieniveau 11

5 Samenhang met ontwikkelingen binnen UWV 12

5.1 UWV Informatieplan en MDM 12

5.2 Het programma DEC/DF 13

5.3 Project BRP, tenzij 13

5.4 Reference data management 13

6 Tenslotte 13

7 Gerelateerde documenten 14

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

4 van 14

1 Inleiding

Dit beleid is het vervolg op het onderzoek naar Master Data Management dat in 2014 is uitgevoerd [1].

Het bouwt voort op de conclusie dat er door UWV al veel gedaan wordt aan Master Data Management, dat er

geen grootschalig programma nodig is, en dat er aangesloten moet worden bij lopende trajecten en ontwik-

kelingen.

Het neemt enkele delen uit dat onderzoek over, waaronder de beschrijvingen van definities en de toege-

voegde waarde, en het geeft een nadere uitwerking van de toepassing van master data en master data ma-

nagement binnen UWV. Het onderzoek wordt hiermee integraal een bijlage bij dit beleid.

In hoofdstuk 2 worden de definities van Master Data en Master Data Management (MDM) gegeven, afkom-

stig uit het voorgaande onderzoek.

Hoofdstuk 3 beschrijft de businessdoelen van MDM, en de relatie met de gegevensprincipes van UWV.

Hoofdstuk 4 bevat beleidsuitspraken ten aanzien van MDM. Paragraaf 4.3 gaat met name op de verdere ont-

wikkelingen in.

Hoofdstuk 5 beschrijft beknopt een aantal ontwikkelingen binnen UWV waarbij MDM aan de orde is.

Hoofdstuk 6 tenslotte geeft een korte samenvatting.

2 Wat is Master Data en Master Data Management?

Het begrip Master Data Management is rond 2005 opgekomen en er zijn verschillende definities van in om-

loop. Het is belangrijk om voor UWV een definitie te kiezen die gericht is op de context van UWV. In de lite-

ratuur wordt het begrip Master Data vaak gekoppeld aan het begrip Reference Data. We kiezen ervoor om

binnen UWV deze twee begrippen duidelijk te onderscheiden en twee definities te hanteren [2]. Master en

Reference Data sluiten elkaar uiteraard niet uit. Een belangrijke reden hiervoor is dat UWV sinds jaar en dag

onderscheid maakt in ‘gewone’ en ‘tabelgegevens’; de tabelgegevens zijn het onderwerp van het vastge-

stelde Beleid Reference Data.

2.1 Data types

Het is mogelijk om gegevens te categoriseren; de literatuur beschrijft Master Data, Transactional Data, Re-

ference Data, Metadata, Historical Data en Temporary Data. Master Data wordt in dit document verder gede-

finieerd, de overige typen worden hieronder kort omschreven.

Transactional Data. Beschrijft een gebeurtenis of transactie die plaatsvindt binnen een organisatie.



Denk hierbij aan Excasso, de betaalomgeving van UWV.

Reference Data. In het beleid Reference data is de volgende definitie vastgesteld: Gegevens die wor-



den gebruikt om andere gegevens te classificeren of te categoriseren. Reference data hebben altijd

een vast waardebereik op een bepaald moment in de tijd. Voorbeelden van Reference data zijn: Na-

tionaliteitentabel, Tabel SZ-wet, Minimumloontabel.

 Metadata. Letterlijk: data over data. Dit type gegevens beschrijft de kenmerken van gegevens. Denk

hierbij aan de naam van een gegeven, het aantal tekens etc. Binnen UWV is het Canoniek Gege-

vensmodel (CGM) een goed voorbeeld. In het CGM worden onder meer definities en waardebereiken

van gegevens vastgelegd. Hiernaast zijn er ook technische metadata, zoals de datum-tijd laatste

wijziging van een gegeven.

Historical Data. Dit zijn gegevens die belangrijke feiten vastleggen op een bepaald punt in de tijd.



Binnen UWV kennen we de Historische Gegevens Opslag (HGO). Zo worden WW-gegevens in het

Kwaliteit Registratie Systeem (KRS) gearchiveerd in HGO, en dus niet in de applicatie KRS zelf.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

5 van 14

Temporary Data. Deze gegevens worden tijdelijk in het geheugen van een computer bewaard om



processen sneller te laten verlopen. Na het afronden van het proces wordt deze data direct weer

vernietigd.

2.2 Definitie van Master Data

Binnen UWV hanteren we onderstaande definitie voor Master Data. Deze is vastgesteld in het kader van het

Onderzoek Master Data Management.

Master Data

Gegevens over voor UWV belangrijke objecten die in processen worden gebruikt. Het zijn bedrijfsbreed ge-

bruikte gegevens waarvan de organisatie het vertrouwen heeft dat deze gegevens het dichtst de werkelijk-

heid benaderen binnen de context van de bedrijfsvoering van de organisatie.

Bij de genoemde gegevens gaat het om de voorkomens van gegevens in informatiesystemen. Een voorbeeld

van Master Data betreft de naamgegevens van een natuurlijk persoon, die zijn opgeslagen in UPA. UPA is de

master. Andere applicaties die deze gegevens verwerken moeten daarom gebruik maken van de gegevens

uit UPA.

De mastergegevens kunnen binnen UWV gecreëerd zijn, maar ook afkomstig van een externe bron.

In dat geval fungeert het UWV-systeem als master voor UWV, en is de externe registratie de master voor

het betreffende UWV-systeem.

Voorbeelden van Master Data zijn gegevens over:

• Personen en organisaties, inclusief hun verschillende rollen;

• Producten en diensten;

• Inkomens.

2.3 Definitie van Master Data Management

Binnen UWV hanteren we onderstaande definitie voor Master Data Management. Ook deze is vastgesteld in

het kader van het Onderzoek Master Data Management.

Master Data Management

Het geheel van richtlijnen, processen en applicaties om Master Data te beheren en ter beschikking te stellen

voor bedrijfsbreed gebruik van accurate, tijdige en actuele waardes van de Master Data.

Naast Master Data Management onderscheiden we ook Reference Data Management. Dit onderscheid heeft

vooral te maken met de behoefte aan UWV-breed management van Reference data. In andere organisaties

wordt dit onderscheid niet gemaakt.

Het onderscheiden van deze twee ‘concepten’ zegt overigens niets over technologie, software(suite) of im-

plementatie. Beide concepten zijn apart of binnen één omgeving te implementeren.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

6 van 14

3 Doelen Master Data Management

In het Onderzoek Master Data Management is uitgebreid aandacht besteed aan de doelen en voordelen van

MDM. De belangrijkste worden verderop in deze paragraaf aangehaald, en in verband gebracht met de

speerpunten uit de Strategische Focus Gegevensmanagement [3], die medio 2016 is vastgesteld door het

## KOG.

Gegevensprincipes zijn richtinggevende uitspraken die ertoe bijdragen dat de gegevenshuishouding van

UWV als samenhangend geheel wordt ingericht. De gegevensprincipes van UWV zijn op 22 maart 2013 be-

krachtigd door de Raad van Bestuur. [4]. MDM geeft invulling aan een aantal van deze principes:

Principe 7 UWV legt geen redundante gegevensverzamelingen aan.

Gegevensredundantie is de situatie waarin één voorkomen van een gegevenswaarde meer dan één maal

wordt opgeslagen en waarin die meerdere voorkomens van gegevenswaarden gelijktijdig worden bewaard in

verschillende administraties. Theoretisch is er immers alleen de master waarin de gegevens zijn opgeslagen

In de praktijk zien we dat, bijvoorbeeld om performanceredenen, er wel redundantie wordt toegestaan. Dit

conform het Beleid Gegevensredundantie [5].In dit beleid staat ook dat wijzigingen in de bron moeten door-

werken naar de afnemende informatiesystemen, opdat er geen inconsistenties optreden (uitgangspunt van

MDM). Dit valt mede onder gegevensprincipe 8.

Bij een goed ingevoerd MDM, d.w.z. eenmalige opslag en volledig geautomatiseerde meervoudige uitvraag,

zou een situatie van ‘geen redundantie’ kunnen bestaan. Juist dan is het zaak dat de eigenaar weet wat zijn

afnemers wensen op het gebied van de inhoud van de gegevens, om de eenmalige uitvraag, meervoudig

gebruik in stand te kunnen houden. Het luistert dan immers extra nauw, met redundantie konden onge-

wenste situaties buiten de deur gehouden worden. Dan is men geheel afhankelijk van de Master. Zie het

toepassen van de Basisregistraties met Terugmeldfunctionaliteit: Master Data in optima forma [6].

Principe 8 UWV past de waarde van een gegeven uitsluitend aan op aangeven van de bron waaruit het

gegeven is verkregen.

Dit is het principe van Single point of control. Aanpassing van gegevenswaarden is uitsluitend toegestaan

vanuit één centraal punt, de gegevensbron. De bron blijft verantwoordelijk en bepalend voor de precieze be-

tekenis en waarde van het gegeven.

UWV wijzigt gegevens alleen, als de bron daartoe opdracht heeft gegeven. Dit principe is niet alleen van toe-

passing op gegevens die van buiten de organisatie komen; ook intern moet dit principe worden toegepast.

Het woord bron heeft hier een meervoudige betekenis. Een gegeven komt uit een proces (indienen aan-

vraag, vaststellen bruto uitkering) Dit proces kun je als de bron zien. Dit gegeven wordt ergens opgeslagen

in een bron. Deze laatste bron is de single point of control. Vandaar uit moeten de redundante registraties

aangepast worden. Ook wordt met het woord bron aangeduid de natuurlijke persoon of de rechtspersoon die

een gegeven dat ook daadwerkelijk door UWV wordt gebruikt of vastgelegd, aan UWV verstrekt.

Vanuit het gezichtspunt van MDM zijn ook de volgende principes in beeld:

Principe 1 De UWV-gegevenshuishouding is gestandaardiseerd.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

7 van 14

MDM heeft behoefte aan standaardisering, omdat de afnemende systemen behoefte hebben aan eenduidige

en voorspelbare leveringen (zowel bulk als vraag-antwoord). Tevens is het voor nieuwe afnemers makkelij-

ker om op een bestaande betrouwbare standaard aan te sluiten. Meervoudig gebruik en integratie van gege-

vens wordt bevorderd. Daar draagt MDM zelf ook aan bij.

Principe 2 UWV geeft inzicht in en draagt zorg voor de kwaliteit van haar gegevens.

Doordat gegevens op een plek worden beheerd worden inconsistenties, behorend tot de hoofdoorzaken van

verminderde kwaliteit, voorkomen

Principe 9 UWV biedt degene over wie UWV gegevens registreert of verwerkt, op verzoek inzicht in de

inhoud en het gebruik van die geregistreerde gegevens.

Doordat gegevens op één plek worden beheerd is het relatief eenvoudig om de burger zijn gegevens te laten

inzien, en de mogelijkheid tot correctie te bieden. Wat de burger getoond moet worden is beschreven in de

## AVG.

Naast invulling geven aan deze principes, heeft MDM meer doelen:

MDM levert de organisatie een eenduidig organisatiebreed beeld van belangrijke onderwerpen (bijvoorbeeld

klanten).

Dit draagt bij aan:

• Verbeterde klantenservice

Door een eenduidig en bedrijfsbreed klantbeeld is het mogelijk om de klant beter te helpen en/of

op maat gesneden dienstverlening en producten aan te bieden. Dit vereist wel een permanente fo-

cus op gegevenskwaliteit.

• Verbeterd productmanagement

Een eenduidig beeld van producten en producteigenschappen, afnemers en leveranciers leidt tot

een slagvaardig productmanagement.

• Verbeterd risicomanagement

Het bepalen van risico’s kan gebeuren op basis van eenduidige gegevens. Daarnaast is er minder

kans op fouten (en dus risico’s) door het verminderen van het aantal plekken waar bijvoorbeeld

gegevensopslag, duplicatie en transformatie gebeurt. Een eenduidig klantbeeld helpt bij het vast-

stellen van het juiste risicoprofiel.

• Automatiseren werkprocessen

Hieronder verstaan we onderwerpen die te maken hebben met efficiënt en effectief werken, zoals

automatisering werkprocessen, digitaliseren dienstverlening en STP (Straight Through Processing).

STP staat of valt met eenduidige gegevens in de bedrijfs- en werkprocessen. Inconsistentie van

gegevens leidt tot uitworp en handmatig herstel.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

8 van 14

MDM bevordert een overzichtelijke en beheersbare gegevenshuishouding.

Dit draagt bij aan:

• Snel reageren op veranderingen

Applicaties kunnen voor het merendeel van de gegevensbehoefte gebruik maken van de geconsoli-

1.

deerde gegevens in een als master aangewezen informatiesysteem Hierdoor kan de ontwikkeling

van de ‘gegevenskant’ van een applicatie eenvoudiger en tegen minder kosten plaatsvinden.

• Verbeterde efficiency gegevensbeheer en kostenreductie

Dubbele opslag van gegevens is nadelig voor de uitvoering van bedrijfsprocessen maar heeft ook

tot gevolg dat alle beheeractiviteiten, tooling en infrastructuur meervoudig uitgevoerd zijn met bij-

behorende kosten. Het door Master Data Management gecreëerde eenduidige gegevensbeeld leidt

dus ook tot een vermindering van kosten.

• Verbeterde gegevenskwaliteit

Er ontstaan problemen wanneer organisatieonderdelen dezelfde gegevens (redundantie) verzame-

len en de redundant opgeslagen gegevens niet bijgewerkt worden vanuit de bron. Dit leidt tot extra

kosten: telkens opnieuw bepalen van de juiste gegevens en de locatie ervan.

MDM voorkomt dit. Tevens is het mogelijk de kwaliteit van gegevens te monitoren door eenduidige

metadata, gestandaardiseerde waardebereiken en gestandaardiseerde business rules.

• Consistente, snellere rapportage en verbeterde besluitvorming

Correcte en volledige Master Data zijn ook het fundament voor goede stuur- en verantwoordingsin-

formatie.

Rapportage gebeurt op basis van dezelfde gegevens – met dezelfde definities – die door de busi-

ness gebruikt worden. Complexe transformaties – wellicht op verschillende plekken – zijn niet meer

nodig. Hierdoor is het mogelijk om rapportages consistent en sneller op te leveren. Dit leidt weer

tot een betere en snellere besluitvorming.

• Betere compliance (voldoen aan wet- en regelgeving)

Als er een eenduidig en kwalitatief hoogwaardig gegevensbeeld bestaat, inclusief bijbehorende me-

tadata, en de gegevensprocessen in kaart zijn gebracht is het mogelijk om op eenvoudige wijze

inzicht te bieden in de gegevenshuishouding en de vereiste wijzigingen aan te brengen. Een voor-

beeld daarvan is ‘Privacy by Design’, zoals beschreven in de AVG; de invloed van MDM beperkt het

aantal kopieën van privacygevoelige gegevens.

Governance2

Door de combinatie van Master Data Management en Data kan eenvoudiger en sneller

worden voldaan aan de eisen van wet- en regelgeving.

1

Een materiesysteem of een aparte Master Data Management repository (centraal of gedistribueerd).

2

UWV definitie Data Governance: de organisatie, de bevoegdheden en de verantwoordelijkheden die nodig zijn voor het

besturen van, het beheersen van en het verantwoorden over de UWV-brede functie Gegevensmanagement

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

9 van 14

4 Beleid

Uit het eerdere onderzoek is duidelijk geworden, dat er binnen UWV al veel gebeurt op het gebied van MDM.

Dit document beschrijft een ambitieniveau, gebaseerd op de bestaande ontwikkelingen. Allereerst worden de

randvoorwaarden in kaart gebracht. Daarna wordt het vaststellen van de UWV Master Data en het gewenste

ambitieniveau besproken.

4.1 Invullen randvoorwaarden

Voor het goed laten functioneren van MDM dient aan een aantal randvoorwaarden voldaan te worden. Dit wil

niet zeggen dat de randvoorwaarden 100% moeten zijn ingevuld, voor er met het MDM an sich gestart kan

worden.

4.1.1 De gegevenshuishouding is in kaart gebracht

## (CGM)3

Met het publiceren van de eerste versie van het Canoniek Gegevensmodel in juli 2016 is een begin

gemaakt met het inzichtelijk maken van de belangrijkste gegevens binnen de UWV Gegevenshuishouding

[7]. Het CGM baseert zich daarbij op het bedrijfsobjectmodel en de gegevensmodellen van de applicaties

van de divisies (FUGEMs) [8]. Hierbij moet wel worden aangetekend dat zowel het CGM als de FUGEMs nooit

‘af’ zijn: wijzigingen in het applicatielandschap zullen ook consequenties hebben voor de gegevensmodellen.

Vereist is, dat FUGEMs en CGM op orde zijn: Compleet, Correct, Tijdig en Consistent.

Hiernaast is er inzicht nodig in de koppelingen tussen de informatiesystemen: welke gegevens worden er

tussen welke applicaties uitgewisseld?

4.1.2 De gegevens zijn bekend en gedefinieerd

Het CGM en de FUGEMs geven ook definitie en waardenbereik van de afzonderlijke gegevens. Dit maakt her-

gebruik van gegevens gemakkelijker.

4.1.3 De gegevensuitwisseling is gestandaardiseerd

## UWV4.

Beleidsmatig is de gegevensuitwisseling gestandaardiseerd door de vastgestelde Berichtstandaard

Hierin is bepaald dat de gegevensuitwisseling binnen UWV conform het CGM moet zijn, zowel wat de gege-

vensdefinities als de gegevensstructuur betreft. Door gestandaardiseerde uitwisseling is het koppelen van

systemen makkelijker [9].

4.1.4 Governance van de gegevenshuishouding is ingericht

De gegevenseigenaar is de partij binnen UWV die verantwoordelijk is voor de bepaling en het beheer van de

gegevensbeschrijving en/of het beheer en de sturing op de kwaliteit van de gegevenswaarde. Gegevenseige-

naarschap gaat dus niet over het ‘bezit’ van gegevens. Het gaat veel meer om verantwoordelijkheid dragen

voor en het goed inhoudelijk beheren van gegevens in het belang van de eigen processen maar ook in het

belang van de processen van derden (in- en extern). Dit is cruciaal voor goed MDM.

Het Beleid Gegevenseigenaarschap 2.0 is vastgesteld in februari 2014 [10]. De toedeling van het eigenaar-

schap is gestart in het vierde kwartaal van 2016.

3

Het Canoniek Gegevensmodel (CGM) is het standaard gegevensmodel van de belangrijkste gegevens die binnen UWV in

omloop zijn. Ook de samenhang tussen de UWV gegevens staat in het CGM. Het CGM geeft dus goed inzicht in de gege-

venshuishouding van UWV.

4

Het doel van de UWV Berichtstandaard is het ondersteunen van de gegevensuitwisseling binnen UWV en met externe

partijen. De ondersteuning betreft de beschrijving van het proces van berichtontwikkeling en de onderdelen van een be-

richt. Dit is een interne standaard; deze wordt niet opgelegd aan externe partijen.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

10 van 14

4.2 Vaststellen van de UWV Master Data

De eerste stap voor het vaststellen van de UWV Master Data is het vaststellen van de objecten waarover ge-

gevens verzameld worden. De volgende stap is de selectie van gegevens die aangemerkt kunnen worden als

Master Data. Als laatste moet worden vastgesteld in welke applicatie – of applicaties – de gegevens worden

onderhouden.

4.2.1 Over welke objecten worden Master Data verzameld?

Om een eerste beeld te krijgen van welke onderwerpen in aanmerking komen voor MDM wordt het UWV Be-

drijfsobjectmodel [11] gehanteerd. UWV gaat uit van één UWV-breed bedrijfsobjectmodel, dat voor alle be-

langhebbenden herkenbaar is. Voor het overzicht maken we een onderscheid tussen kernobjecten en domei-

nobjecten. De huidige versie van het bedrijfsobjectmodel bevat de kernobjecten van UWV. De domeinobject-

modellen, die voor een groot deel al binnen de divisies zijn opgesteld, worden medio 2017 in het bedrijfsob-

jectmodel opgenomen. Door de relatie te leggen met de bedrijfsfuncties (de domeinen) wordt hergebruik

van bedrijfsobjecten op hoog niveau zichtbaar.

4.2.2 Welke gegevens worden aangemerkt als Master Data?

Over de diverse bedrijfsobjecten zijn veel verschillende gegevens vastgelegd. Het is uiteraard niet de bedoe-

ling om alles aan te merken als Master Data; alleen de gegevens die bedrijfsbreed gebruikt worden en waar-

van de organisatie het vertrouwen heeft dat deze het dichtst de werkelijkheid benaderen komen in aanmer-

king.

Hiervoor kan het CGM worden ingezet: te beginnen met het selecteren van de entiteiten die vallen onder de

in de vorige stap geselecteerde bedrijfsobjecten, en vervolgens het selecteren van gegevens – vastgelegd in

attributen – die gedeeld worden door meer informatiesystemen. Het CGM brengt de belangrijkste gegevens

van UWV in kaart, en biedt dus een logisch vertrekpunt. Daarnaast bieden de registraties van berichten, ser-

vices en gegevensleveringen inzicht in welke gegevens daadwerkelijk worden gedeeld, en welke niet.

Vervolgens dient te worden bepaald of er voor de betreffende gegevens een ‘single point of control’ nodig is.

Dit is het geval als het gegeven op meerdere plaatsen wordt onderhouden.

De bepaling van de Master Data dient in overleg met de betrokken partijen plaats te vinden: de gegevens-

eigenaar, de partij die de gegevens onderhoudt en de gebruikers (‘afnemers’) van de gegevens. Nadat er

overeenstemming op dit niveau is bereikt, kan via de functionele gegevensmodellen (FUGEMs) bekeken wor-

den in welke applicaties de gegevens daadwerkelijk worden voorkomen.

Vervolgens dient, op basis van in het vervolgtraject vast te stellen criteria, te worden bepaald welk informa-

tiesysteem de master is. Tot deze criteria behoren in ieder geval gegevenskwaliteit en eigenaarschap.

4.2.3 Voorbeelden van Master Data Registraties

De Master Data van UWV dienen nog officieel te worden bepaald. In de praktijk fungeren al bepaalde infor-

matiesystemen als mastersysteem voor bepaalde gegevens. Het master data management eromheen dient

nog te worden ingericht.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

11 van 14

Persoonsgegevens

De persoonsgegevens worden uiteraard in zeer veel informatiesystemen gebruikt. De basis voor de per-

soonsgegevens is de Basisregistratie Personen (BRP). De set gegevens die UWV hiervan ontvangt wordt

vastgelegd in de UWV Persoonsadministratie (UPA), en van daaruit ter beschikking gesteld. UPA is daarmee

de aangewezen master voor de NAW gegevens, huwelijk/geregistreerd partnerschap, nationaliteit en andere

BRP-gegevens. Andere gegevens binnen UPA, die niet afkomstig zijn uit BRP, krijgen op termijn hoogstwaar-

schijnlijk ook de status van mastergegeven. Denk aan het correspondentieadres.

Werkgevergegevens

UWV gebruikt het begrip Werkgever in verschillende contexten. Zo kennen we de werkgever in de loonaan-

gifte als inhoudingsplichtige, en in het Handelsregister als onderneming. Dit staat verder uitgewerkt op het

diagram ‘werkgever in context’ in het CGM.

Polisdomein

De master voor de werkgevergegevens die via het Loonheffingennummer worden geïdentificeerd, en door de

Belastingdienst worden aangeleverd, is de facto de Werkgeversadministratie (WGA) in het Polisdomein. Deze

bevat inhoudingsplichtigen en hun administratieve eenheden.

De werkgevergegevens uit het Handelsregister zullen tezijnertijd ook in het Polisdomein landen.

Integratie en synchronisatie van beide mastersets is hierbij belangrijk.

Dienstverbanden

De dienstverbanden zijn in de vorm van inkomstenverhoudingen afkomstig uit de loonaangifteketen. Ze zijn

vastgelegd in de Polisadministratie (Polis+). Polis+ is daarmee de aangewezen master voor de betreffende

loonaangifte-gegevens.

Uitkeringen

Vanuit master data management optiek hebben we bij de uitkeringen een complexe situatie.

De materiesystemen voor de diverse wetten zijn in principe masters, maar de uitkeringen komen in de vorm

van inkomstenverhoudingen ook terug in de Polisadministratie.

In feite is hier sprake van twee sets masterdata: uitkeringsgegevens en inkomstenverhoudingsgegevens. Dit

zijn twee verschillende objecten met wellicht inhoudelijk enkele overeenkomstige kenmerken en op voorko-

menniveau met dezelfde waarde.

4.3 Het gewenste ambitieniveau

Dit beleid leidt niet tot een groots en meeslepend Master Data programma, maar heeft als ambitie om de

doorontwikkeling van de huidige situatie te beschrijven. Immers, door de toepassing van de huidige gege-

vensprincipes – waarbij vooral het hergebruik van gegevens voorop staat – hanteert UWV een vorm van Ma-

ster Data Management. Er is dus geen behoefte aan een nieuwe koers, maar aan bestendiging van de hui-

dige ontwikkelingen.

De volgende beleidsuitspraken geven richting aan de verdere ontwikkeling.

 De Master Data dienen te worden vastgesteld, op basis van opgestelde criteria. Zie hiervóór par.

4.2.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

12 van 14

 Er dienen voor de verschillende systemen die Master Data bevatten en beschikbaar stellen overleg-

structuren te worden ingericht waarin de gegevenseigenaar, de systeemeigenaar en afnemers/ge-

bruikers zitting hebben.

Er moet een eenduidig beheerproces worden ingericht voor het up-to-date houden van de structuur



van de Master Data en de inhoud van de Master Data.

Er dienen naast het beheer van de Master Data (de voorkomens) ook secundaire beheerprocessen



processen5

te worden ingericht. Hierbij kan worden gedacht aan ITIL-gerelateerde als:

o

change management (bijvoorbeeld: er wordt een nieuw gegeven toegevoegd aan systeem X,

wordt dat een mastergegeven, wie keurt dat goed en welke systemen, processen, procedures

en standaarden moeten daarvoor aangepast worden?);

o

incident management (bijvoorbeeld incidenten en issues waarbij de kwaliteit van Master Data

of MDM een rol heeft gespeeld, dienen inzichtelijk te zijn en er moet opvolging aan gegeven

worden);

o

service level management (bijvoorbeeld vaststellen en bewaken van dienstenniveaus ten aan-

zien van het onderhouden van Master Data);

compliance management (bijvoorbeeld waarborgen dat MDM als geheel en Master Data spe-

o

cifiek voldoen en blijven voldoen aan relevante interne en externe wet- en regelgeving).

Er dient een PDA-cyclus te worden ingericht die de uitvoering van de afspraken monitort en waar



nodig verbeteringen aanbrengt

5 Samenhang met ontwikkelingen binnen UWV

Het beschreven ambitieniveau, van geleidelijkheid en aansluiten bij bestaande ontwikkelingen, past ook bin-

nen de huidige en de gewenste situatie beschreven in het UWV Informatie Plan (UIP), en het programma

## DEC/DEF.

Project BRP, de ontwikkeling van DEC/DF en het Reference Data Management geven al invulling aan het be-

leid.

5.1 UWV Informatieplan en MDM

De MDM aspecten in het UIP omvatten met name de onderdelen E-Werken, E-dienstverlening en Gegevens-

huishouding [12]. Het programma E-werken streeft naar ‘straight through processing’; het automatisch ver-

werken van aanvragen. Dit is alleen mogelijk als de relevante (klant)gegevens vanuit één bron beschikbaar

zijn. Hierin past ook de ontwikkeling van een divisieoverstijgend CRM. Verder is er sprake van het vereen-

voudigen van het applicatielandschap, wat leidt tot het centraliseren van gegevens.

In het kader van e-Dienstverlening wordt gestreefd naar ontkoppeling tussen de portalen en het achterlig-

gende systeemlandschap. Hiertoe wordt een onderscheid gemaakt tussen een klantinteractielaag, en een

ondersteunende laag, die onder meer gegevens uit de materiesystemen ter beschikking stelt.

Hierbij dienen de principes van MDM in acht te worden genomen.

5

Ontleend aan: Keesjan van Unen e.a. Master Data Management: do’s & don’ts, in Compact_ 2012 2

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

13 van 14

Binnen het onderdeel Gegevenshuishouding ligt de nadruk op diverse ‘masterdata’ systemen. Denk hierbij

aan de loonaangifte in de Polisadministratie, het Landelijk Doelgroep Register (LDR) en de UWV Persoonsad-

ministratie (UPA). In dit kader zijn de volgende veranderingen aan de orde: het centraal in UPA beheren van

persoonsgegevens; het aansluiten op externe gegevensbronnen, en het realiseren dan wel doorontwikkelen

van interne bronnen.

5.2 Het programma DEC/DF

6streeft

Het programma DEC/DF naar een gegevenshuishouding, waarin het beschikbaar stellen van gege-

vens uit de bronsystemen richting de diverse afnemerkanalen evenals het meten, rapporteren en het maken

van afspraken over de kwaliteit van die gegevens gemeenschappelijk wordt georganiseerd [13]. Ook streeft

DEC/DF ernaar om snel te kunnen inspelen op veranderende behoeften in het proces van reflectief sturen en

verantwoorden.

De kern van de aanpak is het efficiënt beschikbaar stellen van een beperkte set standaard gegevens, in

combinatie met een aantal gestandaardiseerde leverkanalen. De concepten van standaard gegevens en pa-

rametriseerbare leveringen zijn al operationeel op gegevens uit het Polisdomein en kunnen breder toegepast

worden.

5.3 Project BRP, tenzij

Het doel van project BRP is adressen en bankrekeningnummers centraal te gebruiken en voor medewerkers

inzichtelijk te maken in welke situatie zij welk soort adres (RNI/GBA-adres, Verblijfadres, en Corresponden-

tieadres) moeten gebruiken. Voor de klant moet duidelijk worden welk adres zij wanneer moeten doorgeven

aan UWV of de gemeente. Een tweede doel is de implementatie van RNI binnen UWV.

Al deze gegevens worden centraal beheerd (in UPA) en van daaruit middels services ter beschikking gesteld.

Dit is daarmee een goed voorbeeld van MDM.

5.4 Reference data management

In april 2016 is het beleid Reference Data management [2] vastgesteld. In 2017 wordt de uitvoering daar-

van door middel van een of meer pilots beproefd. Reference data kan beschouwd worden als een onder-

klasse van Masterdata. Dit type gegevens worden gebruikt om bedrijfsgegevens te classificeren, en bevatten

een vast waardebereik gedurende een bepaalde periode in de tijd.

6 Tenslotte

Het hier beschreven ambitieniveau is goed uitvoerbaar. Aan een aantal belangrijke voorwaarden – zoals het

## CGM7

standaardiseren van de gegevensbeschrijvingen – is voldaan, en het kan ingezet worden voor het

vaststellen van de Master Data.

Ook de daadwerkelijke toepassing van MDM binnen UWV is op een aantal plekken al gaande of gepland.

Het is nu zaak om eenduidige afspraken en beheerprocessen voor deze en toekomstige initiatieven en ont-

wikkelingen te gaan maken, met het oog op een optimaal functionerende gegevenshuishouding.

6

Het programma zal voorjaar 2017 in de lijn belegd worden, waarbij het gedeelte van de Datafabriek onder DWH als pro-

ject wordt voortgezet. Het DEC wordt verder opgepakt bij de uitwerking van IV-transitie 'Vraagsturing'.

7

N.B. Het CGM bevat nog niet de gegevens uit de secundaire systemen. Zo is de Grote geldstroom is niet beschreven,

deze vormt een belangrijk onderdeel van de masterdata in de context van Sturen & Verantwoorden.

Beleid Master Data

Management

Datum

28 december 2022

Versie

1.1.1

Pagina

14 van 14

7 Gerelateerde documenten

De in dit document genoemde beleids- en/of architectuurdocumenten van de Data Office UWV zijn beschik-

baar op de Digitale Werkplek onder Data Office UWV, Producten en Kaders.

[1] Data Office, „Onderzoek Master Data Management, versie 1.0,” 18 December 2014.

[2] Data Office, „Beleid Reference Data UWV : voor het beheren en beschikbaar stellen van reference

data. versie 3.0,” 18 April 2016.

[3] Data Office, „Strategische Focus Gegevensmanagement,” 6 Juli 2016.

[4] Data Office, „Gegevensprincipes UWV : Principes voor het besturen, inrichten en beheersen van de

UWV-gegevenshuishouding , versie 1.1,” 11 Februari 2013.

[5] Data Office, „Omgaan met gegevensredundantie, versie 1.0,” 5 Februari 2008.

[6] Digitale overheid, „Kwaliteit en terugmelden,” [Online]. Available:

https://www.digitaleoverheid.nl/beleid/naar-een-gegevenslandschap/themas/kwaliteit-en-

terugmelden/. [Geopend 6 Maart 2017].

[7] Data Office, „Canoniek Gegevensmodel UWV, releasedatum 26 juli 2016,” 26 Juli 2016.

[8] Data Office, „Standaard Functioneel Gegevensmodel,” 6 Juli 2012.

[9] Data Office, „Berichtstandaard UWV : Proces berichtontwikkeling en onderdelen van een bericht, versie

3.1,” 17 Augustus 2015.

[1] Data Office, „Beleid Gegevenseigenaarschap, versie 2.0,” 10 Februari 2014.

[11] Data Office, „Standaard Bedrijfsobjectmodel,” 31 Januari 2012.

[12] CIO Office, „UWV Informatieplan 2017 – 2021 : Puzzelen met prioriteiten,” 15 Februari 2017.

[13] Gegevensdiensten, „Programma Data Expertise Centrum / Data fabriek,” 2016.

[14] Data Office, „Advies Contactgegevens van de burger,” 30 Maart 2016.

---

Bron: [Besluit Woo-verzoek IT strategie UWV](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-it-strategie-uwv) · [Bijlage 2 Beleid Master Data Management versie 1.1.1 (PDF, 600 kB)](https://www.uwv.nl/assets-kai/files/fbafb48e-590a-4e4e-8bc1-c0780b9c0ac1/bijlage-2-beleid-master-data-management.pdf)
