---
source_id: 2023-12-18-besluit-woo-verzoek-de-source-code-stap-aanvraagsysteem/2023-12-18-bijlage-1-stap-programma-van-eisen
publication_slug: 2023-12-18-besluit-woo-verzoek-de-source-code-stap-aanvraagsysteem
pdf_slug: 2023-12-18-bijlage-1-stap-programma-van-eisen
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-de-source-code-stap-aanvraagsysteem
pdf_url: https://www.uwv.nl/assets-kai/files/153b0ac1-fcea-4db5-bfb2-764adb2368b6/bijlage-1-stap-programma-van-eisen.pdf
publication_title: Besluit Woo-verzoek De source code STAP aanvraagsysteem
publication_date: '2023-12-18T00:00:00Z'
publication_type: WOO publicatie
pdf_label: Bijlage 1 STAP programma van eisen (PDF, 3 MB)
retrieved_at: '2026-06-30T13:15:30+00:00'
sha256: c7af338126c2a1e35134304af4b21286f40bfcdc239d63844d8abc274e2fccf8
page_count: 75
ocr_used: false
---

Programma van Eisen

STAP-applicatie

STAP-Regeling 2022

Versie 1.0

15-10-2020

Programma van Eisen STAP-applicatie

## Inhoudsopgave

## 1. INLEIDING .................................................................................................................................. 1

## 2. PROCESPLAAT STAP

................................................................................................................................... 2

## 3. ROLLEN EN/OF UITVOERENDE FUNCTIONARISSEN ...................................................................... 3

## 4. BESCHRIJVING PORTALEN ........................................................................................................... 4

## 5. RELATIE PROCESSEN EN PORTALEN ............................................................................................. 5

## 6. KOPPELVLAKKEN ........................................................................................................................ 6

## 6.1 OVERZICHT KOPPELVLAKKEN ................................................................................................................ 6

## 6.2 SCHOLINGSREGISTER ............................................................................................................................ 9

...................................................................................10

## 6.2.1 KOPPELINGEN MET HET SCHOLINGSREGISTER

## 6.2.2 TECHNIEK .........................................................................................................................................................10

## 6.2.3 ALTERNATIEF SCENARIO (VANGNET) ...............................................................................................................11

## 7. KENGETALLEN .......................................................................................................................... 12

## 8. FUNCTIONELE REQUIREMENTS EN BIJBEHORENDE PROCESSEN ................................................. 13

## 8.1 GENERIEKE REQUIREMENTS .................................................................................................................13

## 8.2 INFORMEREN .......................................................................................................................................16

## 8.3 INLOGGEN BURGER EN CONTROLEREN ................................................................................................18

## 8.3.1 INLOGGEN BURGER ..........................................................................................................................................18

## 8.3.2 WACHTRIJFUNCTIONALITEIT ............................................................................................................................18

## 8.3.3 CONTROLEREN AANVRAAGRECHT ...................................................................................................................19

## 8.3.4 OPVRAGEN TOELICHTING .................................................................................................................................20

## 8.4 AANVRAGEN DIGIVAARDIGEN .............................................................................................................22

## 8.4.1 INDIENEN AANVRAAG ......................................................................................................................................23

## 8.4.2 UPLOADEN BEWIJS VAN AANMELDING ...........................................................................................................25

## 8.5 AANVRAGEN NIET-DIGIVAARDIGEN .....................................................................................................26

## 8.5.1 LEVEREN BEWIJS VAN AANMELDING ...............................................................................................................28

## 8.6 MATCHEN BVA EN BESCHIKKEN AANVRAAG ........................................................................................29

## 8.7 AFBREKEN EN MUTEREN SCHOLINGSACTIVITEIT ..................................................................................33

## 8.8 INLOGGEN OPLEIDER EN LEVEREN BEWIJS VAN DEELNAME .................................................................35

## 8.8.1 INLOGGEN OPLEIDER .......................................................................................................................................35

## 8.8.2 LEVEREN BEWIJS VAN DEELNAME ...................................................................................................................36

## 8.8.3 RAPPELLEREN BEWIJS VAN DEELNAME ............................................................................................................37

## 8.9 INKOPEN ..............................................................................................................................................38

## 8.10 MATCHEN BVD EN BESCHIKKEN VASTSTELLING ...................................................................................39

## 8.10.1 MATCHEN BEWIJS VAN DEELNAME .................................................................................................................40

## 8.10.2 ONDERZOEKEN MISSTANDEN ..........................................................................................................................41

Versie 1.0

Programma van Eisen STAP-applicatie

## 8.11 OPSTELLEN BESCHIKKING OF BRIEF ......................................................................................................43

## 8.12 VERZENDEN EN ONTVANGEN VIA DIV ..................................................................................................45

## 8.12.1 VERZENDEN ......................................................................................................................................................45

## 8.12.2 ONTVANGEN ....................................................................................................................................................45

## 8.13 TERUG- EN INVORDEREN .....................................................................................................................47

## 8.13.1 OPHALEN OPLEIDERGEGEVENS ........................................................................................................................47

## 8.13.2 AANMAKEN BESCHIKKING- EN FACTURATIEGEGEVENS ...................................................................................48

## 8.14 AFHANDELEN BEZWAAR DOOR STAP–MEDEWERKER ..........................................................................49

## 8.14.1 INDIENEN BEZWAAR DIGITAAL ........................................................................................................................49

## 8.14.2 INDIENEN BEZWAAR FYSIEK .............................................................................................................................50

## 8.14.3 BEHANDELEN BEZWAAR ..................................................................................................................................51

## 8.14.4 BEHANDELEN VOORPROCEDURE BEZWAAR STAP ...........................................................................................51

## 8.14.5 REGISTREREN EN TERMIJNBEWAKING .............................................................................................................52

## 8.15 VRAAGAFHANDELEN ............................................................................................................................54

## 8.15.1 VRAAGAFHANDELEN EERSTE LIJN ....................................................................................................................54

## 8.15.2 VRAAGAFHANDELEN TWEEDE LIJN ..................................................................................................................54

## 8.16 BEHEREN UITSLUITINGSLIJST ................................................................................................................56

## 8.17 STURING EN VERANTWOORDING ........................................................................................................57

## 8.17.1 VERANTWOORDINGSNIVEAU’S ........................................................................................................................57

## 8.17.2 PROCESS MINING .............................................................................................................................................58

## 8.17.3 STURINGSINFORMATIE.....................................................................................................................................59

## 8.18 LOGGING EN MONITORING ..................................................................................................................60

## BIJLAGE 1 : USER STORIES KOPPELINGEN SCHOLINGSREGISTER ........................................................ 61

## BIJLAGE 2 : BEZWAAR EN BEROEP ................................................................................................... 64

## BIJLAGE 3 : AFKORTINGEN- EN BEGRIPPENLIJST ............................................................................... 71

Vertrouwelijkheid:

De lezer/gebruiker van dit document wordt geacht de inhoud daarvan vertrouwelijk te behandelen, tenzij uit de

toelichting of bronvermelding blijkt dat de informatie als openbaar kan worden beschouwd.

Versie 1.0

Programma van Eisen STAP-applicatie

## 1. Inleiding

UWV gaat de uitvoering verzorgen van de ‘Subsidieregeling leer- en

ontwikkelbudget voor de STimulering van de Arbeidmarkt Positie van natuurlijke

personen met een band met de Nederlandse arbeidsmarkt’, verder STAP te

noemen. Het doel is om personen die een band hebben met de Nederlandse

arbeidsmarkt met financiële ondersteuning, de STAP-subsidie, in staat te stellen om

scholingsactiviteiten te volgen ter versterking van hun arbeidsmarktpositie.

Een individuele burger kan jaarlijks een STAP-budget van maximaal € 1000,-

ontvangen voor het volgen van een scholingsactiviteit. Alle burgers hebben recht op

STAP-budget tussen de leeftijd van 18 en AOW-leeftijd. Burgers die recht hebben

op een voorliggende publieke financieringsbron (zoals bijvoorbeeld

studiefinanciering) kunnen een beroep doen op een aparte lijst van

scholingsactiviteiten voor het STAP-budget. Het totale jaarlijkse subsidiebudget

wordt in tranches beschikbaar gesteld: Het UWV biedt zes keer per jaar een

subsidieaanvraag aan om de piek te verspreiden zodat burgers even veel kans

hebben om een subsidie aan te vragen.

Het ministerie van Sociale zaken en Werkgelegenheid (SZW) stelt een lijst

beschikbaar van scholingsactiviteiten en opleidingsinstituten die voldoen aan de

door het ministerie SZW gestelde kwaliteitseisen. Deze lijst vormt het zogenoemde

Scholingsregister. Burgers kunnen met het STAP-budget uitsluitend

scholingsactiviteiten volgen die in dit Scholingsregister zijn opgenomen.

De regeling gaat uit van een digitaal verwerkingsproces. Bij zijn aanvraag overlegt

de burger een Bewijs van Aanmelding voor de betreffende scholingsactiviteit en

opleidingsinstituut. Dit bewijs geldt als zekerheid dat hij zich heeft aangemeld bij

het opleidingsinstituut en met de scholing zal starten.

UWV betaalt – conform de regeling - het subsidiebedrag op een toegekende

aanvraag rechtstreeks aan het betreffende opleidingsinstituut.

De burger, aan wie een STAP-budget is toegekend, krijgt een inspannings-

verplichting opgelegd. Hij dient de scholingsactiviteit met een diploma of certificaat

af te ronden, dan wel een (nader te bepalen) aanwezigheidspercentage te hebben

behaald. Deze aanwezigheid moet blijken uit het Bewijs van Deelname dat het

opleidingsinstituut binnen 6 maanden na de einddatum van de scholingsactiviteit

oplevert. Wordt geen van de resultaten behaald, dan bestaat de mogelijkheid om

de subsidie terug te vorderen. Afhankelijk van de reden en wie verantwoordelijk is

voor het niet succesvol afronden van de scholing (opleidingsinstituut of burger)

dient UWV volgens de regeling de subsidie bij de veroorzaker terug te vorderen.

Terugvordering van de subsidie zal in ieder geval plaatsvinden als er sprake is van

het niet starten van de opleiding dan wel dat door (opzettelijk) toedoen van het

opleidingsinstituut een (van de) verplichting(en) niet wordt nagekomen. Als door

toedoen van de burger de opleiding niet wordt afgerond, kan UWV de subsidie

eveneens terugvorderen.

De regeling is beoogd om in werking te treden per 1 januari 2022

(met voorafgaand een kleinschalige proefimplementatie).

Versie 1.0 pagina 1 van 72

Programma van Eisen STAP-applicatie

## 2. Procesplaat STAP

Versie 1.0 pagina 2 van 72

Programma van Eisen STAP-applicatie

## 3. Rollen en/of uitvoerende functionarissen

Bij de beschrijving van de business requirements maken we gebruik van de

volgende rollen die in meer of mindere mate ingezet zullen worden voor de

uitvoering van de STAP-regeling. Vooralsnog voorzien we onderstaande rollen,

maar hierin kan gedurende de inrichting nog verandering plaatsvinden. We gaan uit

van een beheermodule waarin gebruikers- en rollenbeheer door een beheerder van

UWV configureerbaar is.

Benaming rol Omschrijving rol

Burger

De aanvrager van de STAP-subsidie die voornemens is om

de opleiding te volgen.

Opleider

De professional (=individu) of opleidingsinstituut

(=organisatie) die in het Scholingsregister is aangegeven

als de partij die de geselecteerde scholingsactiviteit verzorgt

en daarvoor de STAP-subsidie uitbetaald krijgt.

STAP-FB Medewerker die via een beheermodule elementen zoals

stamtabellen, autorisaties en workflows kan toevoegen

(Functioneel beheer)

en/of wijzigen.

Tevens beheerder van de ‘uitsluitingslijslijst met

geblokkeerde BSN’s’ (wellicht via een separate autorisatie).

STAP-medewerker

Medewerker van de STAP-unit (van UWV) die zich

bezighoudt met de verwerking van STAP-subsidie

aanvragen. Denk hierbij aan budget aanvragen, controles

(uitvalafhandeling), mutaties en (tweedelijns) contact met

burgers en opleiders.

STAP-terug- en Een medewerker van STAP die zich specifiek richt op het

terug- en invorderen van STAP-subsidie.

invordermedewerker

UWV-klantcontact- Een medewerker van die vanuit zijn/haar expertise

inzagerechten heeft in de STAP- applicatie en daardoor

medewerker

zijn/haar werkzaamheden kan uitvoeren. Het gaat hier dus

om de eerstelijns medewerkers van het Klantcontact Center

(al of niet binnen de STAP-unit te organiseren).

UWV-Adviseur

Een medewerker van UWV-Werkplein die vanuit zijn/haar

rol een aanvraag kan indienen namens een niet-

digivaardige burger.

UWV-FEZ Een medewerker van UWV Financieel Economische Zaken.

Deze medewerkers verzorgen de betaling van de STAP-

medewerker

subsidie middels inkooporders en e-facturen.

UWV-B&B- Een medewerker van de afdeling Bezwaar & Beroep van

UWV. Deze medewerker heeft sec toegang tot het B&B-

medewerker

proces/workflow en de dossiers/gegevens binnen de STAP-

applicatie.

Een service provider die e-facturen t.b.v. UWV ontvangt,

eFacturatie-

waar nodig converteert, en doorstuurt naar UWV

voorziening

(Peoplesoft).

Versie 1.0 pagina 3 van 72

Programma van Eisen STAP-applicatie

## 4. Beschrijving portalen

De regeling wordt zoveel als mogelijk digitaal uitgevoerd. De nieuwe STAP-

applicatie bestaat uit diverse portalen die met elkaar samenwerken.

Benaming portaal Beschrijving portaal

STAP-site of In dit portaal worden de volgende zaken getoond:

Voorportaal of

- STAP-informatie voor burger en opleider.

informatieportaal

Tonen beschikbaar budget voor de lopende tranche.

-

- Overzicht data van de komende tranches.

- Pre-check.

## - FAQ.

Raadplegen Scholingsregister.

-

- Toegang tot / doorlinken naar Digitaal

Arbeidsmarktadvies (DAMA)

- Toegang tot / doorlinken naar Burgerportaal.

- Toegang tot / doorlinken naar Opleidersportaal.

- Contactinformatie.

STAP-Burgerportaal Toegang en authenticatie tot het Burgerportaal vindt

plaats via DigiD. In dit Burgerportaal zullen de volgende

zaken naar voren komen:

- Aanvraag STAP-subsidie.

Het dossier van de burger m.b.t. STAP.

-

- Mogelijkheid tot maken van bezwaar.

- Meldingen doorgeven (afbreken scholingsactiviteit).

STAP- Toegang en authenticatie tot het Opleidersportaal vindt

Opleidersportaal plaats via eHerkenning. In dit Opleidersportaal zullen de

volgende zaken naar voren komen:

- Overzicht van de scholingsactiviteiten die bij de

betreffende opleider horen.

- Het overzicht van de opleider m.b.t. welke burger

STAP-subsidie heeft voor welke scholingsactiviteit.

- Mogelijkheid tot maken van bezwaar.

- Meldingen doorgeven (afbreken scholingsactiviteit).

- Indienen van het Bewijs van Deelname.

UWV- Mogelijkheid voor aanvragen STAP-subsidie voor niet-

Werkpleinportaal digivaardigen door een UWV-Adviseur.

STAP- In dit portaal moet de STAP-medewerker de mogelijkheid

Medewerkersportaal hebben voor inzage in het proces en dossiers, mutaties

kunnen doorvoeren, beschikkingen kunnen opstellen,

handmatig matchen van Bewijs van Aanmelding en Bewijs

van Deelname, meldingen aan aanvragen kunnen

registreren, klachten kunnen vastleggen en moet Bezwaar

en Beroep verwerkt kunnen worden.

In dit portaal moeten handmatig statussen vastgelegd

kunnen worden, omtrent betalingen en terug- en

invorderen.

Het Medewerkersportaal moet ook (beperkte)

registratiemogelijkheden en inzage bieden voor de STAP-

B&B-medewerkers en Eerste lijns support.

Versie 1.0 pagina 4 van 72

Programma van Eisen STAP-applicatie

## 5. Relatie processen en portalen

Portaal Processen

STAP-site of,

- Informeren

Pre-check

-

Voorportaal of

- Doorlinken naar Burgerportaal (aanvraag) en

informatieportaal

Opleidersportaal

- Doorlinken naar Scholingsregister en digitaal

arbeidsmarktadvies.

Burgerportaal

- Inloggen burger

Controleren aanvraagrecht

-

- Aanvragen digivaardigen

- Uploaden Bewijs van Aanmelding

- Informeren belastende beschikking

- Afbreken scholingsactiviteit

- Indienen bezwaar.

Opleidersportaal

- Inloggen opleider

- Afbreken scholingsactiviteit

- Uploaden Bewijs van Deelname

- Indienen bezwaar.

UWV-Werkpleinportaal

- Inloggen medewerker (SSO)

- Aanvragen niet-digivaardigen

- Leveren Bewijs van Aanmelding

- Controleren aanvraagrecht

- Informeren belastende beschikking.

STAP-Medewerkersportaal

- Inloggen medewerker (SSO)

Informeren belastende beschikking

-

- Beschikken aanvraag

- Ophalen opleidergegevens

- Aanmaken beschikking- en

facturatiegegevens

- Rappelleren op Bewijs van Deelname

- Afronden beschikking

- Matchen Bewijs van Deelname

Opstellen beschikking

-

- Beslissen bezwaar

- Voorbehandelen bezwaar

Afhandelen bezwaar

-

- Ingebrekestelling bezwaar

- Afhandelen beroep

Vraagafhandelen (tweedelijns).

-

Versie 1.0 pagina 5 van 72

Programma van Eisen STAP-applicatie

## 6. Koppelvlakken

6.1 Overzicht koppelvlakken

Benaming koppeling Beschrijving koppeling

Koppeling met DigiD (via Authenticatie op het Burgerportaal via DigiD, te

leveren en in te richten door de Leverancier.

Logius)

Het is nog onbekend of de Registratie Niet-

Ingezetenen (RNI) de familieleden van burgers van

de Europese Unie en grensarbeiders kan bieden en,

zo ja, met welke mate van volledigheid.

Koppeling met eHerkenning

Authenticatie op het Opleidersportaal via

eHerkenning, te leveren en in te richten door de

Leverancier.

Koppeling met BRP (via Het ophalen van persoonsgegevens uit de BRP, te

leveren en in te richten door de Leverancier in

RvIG)

afstemming met Logius en RvIG.

Single Sign On/ADFS

De applicatie dient direct via Single Sign On

benaderd te kunnen worden door de daartoe

geautoriseerde medewerkers. Hiertoe dient een

ADFS-koppeling te worden gerealiseerd met

achterliggende autorisaties via het Autorisatie

Beheer Systeem (ABS) van UWV.

Koppeling met We voorzien twee scenario’s die beiden onderdeel

moeten zijn van de aanbieding:

Scholingsregister

1) Voorkeursscenario:

(opdrachtgever SZW)

Real-time-koppeling waartoe webservices worden

geboden. De STAP-applicatie (en bijbehorende

Nader uitgewerkt in de

portalen) zorgen voor het proces en de

volgende paragraaf

presentatie. Op basis van een zoekopdracht van

de burger roept de STAP-applicatie de

(betreffende) webservice aan. Afhankelijk van de

gerichtheid van de zoekopdracht worden er één,

meerdere of alle scholingsactiviteiten

geretourneerd. Dat kunnen er dus duizenden zijn

waarmee het nodig is de resultaten te pagineren.

2) Vangnetscenario:

Een periodieke (dagelijkse) levering van kopie

van de gegevens uit het Scholingsregister. Deze

gegevens moeten dan worden opgeslagen in een

eigen Scholingsregister-kopie binnen de STAP-

applicatie. De STAP-applicatie (en bijbehorende

portalen) zorgen voor het proces en de

presentatie. Op basis van een zoekopdracht van

de burger bevraagt de STAP-applicatie de eigen

Scholingsregister-kopie. Afhankelijk van de

gerichtheid van de zoekopdracht worden er één,

meerdere of alle scholingsactiviteiten

geretourneerd. Dat kunnen er dus duizenden zijn

waarmee het nodig is de resultaten te pagineren.

Versie 1.0 pagina 6 van 72

Programma van Eisen STAP-applicatie

Koppeling of link met UWV beschikt over producten en instrumenten die

een eerste basis voor het digitaal

Digitaal ArbeidsMarkt-

arbeidsmarktadvies kunnen vormen. Zo stelt UWV al

Advies-applicatie (DAMA)

een aantal jaar informatie over kansrijke beroepen

van UWV

beschikbaar, bijvoorbeeld overzichten van beroepen

met moeilijk vervulbare vacatures.

Aangezien de DAMA-applicatie parallel wordt

verworven en ingericht aan de STAP-applicatie, is de

mate van integratie tussen beide applicaties nog

niet bekend. Wellicht wordt gestart met het

simpelweg doorlinken via een hyperlink/button.

Binnen dit Programma van Eisen valt ook de

doorontwikkeling naar een verdere integratie

waarbij op een aantal plekken in de STAP-applicatie

gegevens worden aangeleverd aan DAMA en worden

ontvangen vanuit DAMA en gepresenteerd in STAP.

Koppeling met 1) Dagelijkse aanlevering van printbestanden aan

DIV ter printen, couverteren en verzenden.

Documentaire Informatie

Tussen de STAP-applicatie en DIV moet een

Voorziening (DIV) van UWV

batch-interface worden gerealiseerd. De batch

zal bestaan uit documenten in PDF/A-formaat

met metagegevens/ XML ticket en zal dagelijks

worden aangeleverd.

2) DIV verzorgt de levering van gedigitaliseerde

post met metadata naar UWV STAP. Tussen de

DIV en de STAP-applicatie moet dan een batch-

interface worden gerealiseerd. De batch zal

bestaan uit documenten in PDF/A-formaat met

metagegevens/XML ticket en zal dagelijks

worden aangeleverd.

Aanlevering van de batchbestanden dient te voldoen

aan UWV standaarden en zal plaatsvinden via MQ of

SFTP met inzet van het UWV Systeem Integratie

Platform (zie de Non Functional Requirements).

Koppeling met Peoplesoft 1) Dagelijkse aanlevering van batchbestanden aan

PeopleSoft met opdrachten om STAP-subsidie te

## (FEZ)

betalen, in PeopleSoft bekend als

bestelaanvragen.

2) Dagelijkse aanlevering van batchbestanden met

terug- en invorderopdrachten.

Aanlevering van de bestanden zal naar verwachting

plaatsvinden via SFTP dan wel via webservices

(nader te bepalen en af te stemmen) met inzet van

het UWV Systeem Integratie Platform.

Versie 1.0 pagina 7 van 72

Programma van Eisen STAP-applicatie

Koppeling met applicatie Tussen de applicatie van een klantcontactcenter en

de STAP-applicatie moet een interface worden

van een klantcontactcenter

gerealiseerd teneinde terugbelverzoeken aan de

STAP-unit te kunnen aanbieden.

Het is nog onbekend door wie het contactcenter

geleverd gaat worden (mogelijk het KCC van UWV).

De applicatie-interface kan op dit moment dan ook

niet verder worden gespecificeerd, maar te denken

valt aan een Exchange vergaderverzoek met daarin

de vraag van de burger.

Daarbij moeten de klantcontactcentermedewerkers

in de STAP-applicatie inzage hebben in de FAQ’s en

moet via autorisatie ingericht worden dat zij vanuit

een separate rol middels zoekfunctionaliteit inzage

hebben in de relevante gegevens en documenten,

zonder deze te kunnen wijzigen of verwijderen.

Koppeling met de exchange- De mails die vanuit de STAP-applicatie worden

verzonden (zoals de rappels naar opleiders en

server van UWV

reminders naar burgers) moeten mogelijk via de

exchange-server van UWV worden verzonden.

Alternatief is verzending via een mailserver van de

Leverancier. Nader af te stemmen en te bepalen.

Gegevenslevering ten Bestandlevering (en eventuele voorbewerking van

de data), dan wel de STAP-applicatie toegankelijk

behoeve van Sturing en

maken voor een ETL-tool, is afhankelijk van de nog

verantwoording

te maken keuze van de in te zetten BI-tooling. Aan

de Leverancier wordt gevraagd aan te geven welke

wijze van bestandslevering/openstelling zij kunnen

ondersteunen. Dit aanvullend op de gevraagde

functionaliteit ‘binnen de STAP-applicatie zelf’ zoals

beschreven in paragraaf 8.17.

Generieke ontsluitbaarheid

Alle in de STAP portaal en/of applicatie vastgelegde

gegevens dienen door de Opdrachtgever, ongeacht

waar en hoe deze gegevens staan opgeslagen en

ongeacht of de gegevens na ontvangst zijn bewerkt

of niet, te kunnen worden ontsloten voor andere

applicaties van UWV. Dit dient te gebeuren middels

beveiligde gegevenslevering of webservices. De

content, berichten en protocollen van deze

gegevensleveringen en webservices dienen te

voldoen aan vastgestelde internationale, nationale

en/of open interoperabiliteitsstandaarden voor zover

deze voor het werkingsgebied beschikbaar zijn.

Versie 1.0 pagina 8 van 72

Programma van Eisen STAP-applicatie

6.2 Scholingsregister

Om te beoordelen of de subsidie ingezet wordt voor een goede opleiding, moeten

de opleidingen voldoen aan een aantal kwaliteitseisen. Om de regeling goed te

kunnen uitvoeren, dient STAP snel inzicht te hebben in opleidingen die daaraan

voldoen. Deze worden beschikbaar gesteld via een zogenoemd Scholingsregister.

De verantwoordelijkheid voor dit Scholingsregister ligt bij het ministerie van SZW,

dit omdat het beoordelen van de kwaliteit van opleidingen buiten de expertise en

bevoegdheden van UWV ligt. SZW heeft verklaard de realisatie van dit register op

zich te nemen.

Het is van groot belang dat STAP tijdig over dit register kan beschikken om de

STAP-subsidie per 1-1-22 te kunnen uitvoeren.

Het Scholingsregister bestaat grofweg uit:

1. De samengestelde dataset:

Verschillende data uit verschillende bronnen vormen samen

de dataset die nodig is voor de uitvoering van de STAP-

regeling. Deze bevat:

Gegevens over opleider gaan over het scholingsinstituut,



keurmerk en leveranciersgegevens om onder meer

betaling te kunnen doen.

Gegevens over opleiding gaan over inhoud van de



opleiding, duur, subsidiabele kosten.

Gegevens over scholingsactiviteit, deze bevatten locatie,



datum, tijd, vorm.

Gegevens die nodig zijn voor monitoring en evaluatie.



2. De technische omgeving waarbinnen de data ontsloten

wordt, de bouw van het register:

Dit is de digitale omgeving waarin de geleverde data

toegankelijk gemaakt wordt met als doel het makkelijk

vinden en selecteren van de scholingsactiviteit door de

burger, en op basis van de onderliggende gegevens het

subsidieaanvraagproces te kunnen starten.

3. Beheer van de data, poortwachtersfunctie:

Om de kwaliteit van de opleidingen voor de burgers te

waarborgen is een poortwachtersfunctie nodig om een

goede selectie te maken van de opleiders die opgenomen

worden in het register (onder meer op basis van

keurmerken) en opleiders te kunnen verwijderen bij

signalen over misbruik en oneigenlijk gebruik.

Voor het ontvangen van signalen over misbruik dient een

meldpunt ingericht te worden door de poortwachter.

Versie 1.0 pagina 9 van 72

Programma van Eisen STAP-applicatie

Het Scholingsregister heeft als primair doel het bieden van alle scholingsactiviteiten

waarvoor STAP-subsidie kan worden verstrekt. Het Scholingsregister moet daartoe

vanuit de STAP-applicatie (het Voorportaal, het Burgerportaal en de

Medewerkersportalen) worden benaderd waarmee verschillende gegevens (bij

voorkeur real-time via webservices) worden ontsloten.

6.2.1 Koppelingen met het Scholingsregister

Bij de aanvraag en het verwerken van de STAP aanvragen zijn de volgende

koppelvlakken voorzien.

De nummering die hierbij is aangehouden, is conform de huidige nummering die

gehanteerd wordt in de afstemming met SZW en DUO, deze laatste is de partij die

het Scholingsregister in opdracht van SZW gaat realiseren.

Koppelvlak Beschrijving

5 Met koppelvlak 5 wordt het voor de burger mogelijk om in de

STAP-voorportaal inzage te krijgen in het Scholingsregister om,

met behulp van een aantal zoeksleutels te kunnen zoeken naar

welke passende scholingsactiviteiten de mogelijkheid geven op

een STAP-subsidie.

9 Vanuit koppelvlak 9 wordt het voor de burger mogelijk om in de

STAP-Burgerportaal met behulp van een aantal zoeksleutels te

kunnen zoeken naar de juiste scholingsactiviteit om die te kunnen

selecteren voor de STAP-subsidie aanvraagprocedure..

15 Bij koppelvlak 15 wordt het voor de STAP-medewerker mogelijk

gemaakt om vanuit het STAP-medewerkerportaal inzage te krijgen

in het Scholingsregister om, met behulp van een aantal

zoeksleutels te kunnen zoeken om alle gegevens van de opleider,

opleiding en scholingsactiviteit van nu en in het verleden te

kunnen achterhalen.

In Bijlage 1 zijn de koppelingen nader uitgewerkt in user stories en is als voorbeeld

is aanvullend een request-reply uitwerking opgenomen.

6.2.2 Techniek

Koppelingen 5, 9 en 15 zijn request-reply en worden webservices conform de

Digikoppeling koppelvlak standaard WUS, het acroniem voor WSDL, UDDI en SOAP.

WUS is voor de “bevragingen” (synchroon, request-response).

Uitzoekpunt hierbij is nog de granulariteit van de webservice. Er is gevraagd om

één services die o.b.v. de zoekcriteria voldoende scholingsactiviteiten levert met

daarbij de opleiding en de opleiders. DUO is gewend dat webservices resultaten

leveren op objectniveau. De aanpak van DUO zou betekenen dat er logica in de

STAP-applicatie moet komen om per scholingsactiviteit de opleiding en de opleider

er bij te vinden. Welke vorm het gaat worden is nog niet besloten en is afhankelijk

van hetgeen DUO kan gaan bieden.

Zie de Non Functional Requitrements voor de verdere (technische) uitwerking van

dit koppelvlak.

Versie 1.0 pagina 10 van 72

Programma van Eisen STAP-applicatie

6.2.3 Alternatief scenario (vangnet)

Op het moment van het opstellen van dit Programma van Eisen is het niet volledig

zeker dat het Scholingsregister het gevraagde kan leveren; het gaat hierbij vooral

de vraag-en antwoordservices teneinde real-time de opleidingsgegevens te kunnen

tonen in het voorportaal en het Burgerportaal.

Wanneer STAP onverhoopt niet tijdig over de vereiste functionaliteit van het

volledige Scholingsregister kan beschikken moet er het alternatief geboden kunnen

worden in de vorm van dagelijkse bestandsaanlevering met een kopie van de

relevante gegevens uit het Scholingsregister (nader te bepalen, maar er kan

gedacht worden aan een dagelijkse download van een csv-bestand).

De Leverancier dient er bij zijn inschrijving dan ook rekening mee te houden dat

binnen de STAP-applicatie een eigen Scholingsregister-kopie moet worden

opgeslagen (een database met opleiders-, opleidings- en

scholingsactiviteitgegevens), welke gevoed wordt vanuit het Scholingsregister via

een eenmalige initiële batchvulling en vervolgens dagelijks en/of per tranche een

mutatiebestand dan wel een totaalbestand waaruit mutaties (nieuwe en vervallen

opleiders) afgeleid moeten worden. Het moet mogelijk zijn om in het

Opleidersportaal hiervoor extra beheermogelijkheid te realiseren op het inlezen van

de gegevens.

Met de beschikbaarheid van de opleidingsgegevens in de eigen STAP-

applicatieomgeving, moet ook de zoekfunctionaliteit in de STAP-applicatie in de

STAP-applicatie zelf worden gerealiseerd. Deze zoekfunctionaliteit dient het snel en

efficiënt zoeken naar de juiste scholingsactiviteit te ondersteunen. Te denken valt

aan trapsgewijs zoeken (van opleider naar onderliggende opleidingen naar

onderliggende scholingsactiviteiten) via scrollen en ingave van een deel van de

benaming. Zie hiertoe de user stories in Bijlage 1.

Versie 1.0 pagina 11 van 72

Programma van Eisen STAP-applicatie

## 7. Kengetallen

Aangezien het systeem gebruikt zal worden voor de uitvoering van een nieuw

product binnen UWV zijn er geen historische indicatoren omtrent de

capaciteitsvereisten. De onderstaande getallen zijn daarom een schatting op basis

van verwachte belasting van het systeem.

Definitief:

Totaalbudget STAP-subsidies: ca. €200 miljoen per jaar



Totaalaantal aanvragen: 200.000-300.000



Subsidieaanvraag per aanvraag : maximaal €1.000,-



Totaalaantal toekenningen per persoon: 1 per kalenderjaar



Aantal aanvraagmomenten (tranches): 6 tranches verdeeld over



kalenderjaar

Budget STAP-subsidies per tranche: ca. €33.000.000,-



Maximaal aantal toegekende subsidieaanvragen



per tranche: 30.000 – 50.000

Geschat aantal FTE: circa 150



Onder geschatte FTE vallen alle medewerkers die een relatie met STAP

hebben, dus de STAP-medewerkers, STAP-B&B-medewerkers,

UWV-Adviseurs, Functioneel beheerders etc.

Educated guess

Tijdsduur “bewaren” onafgemaakte aanvraag: 1 maand (onder



voorbehoud)

Aantal verstuurde beschikkingsdocumenten: ca. 636.000 per jaar



Aantal soorten beschikkingen en brieven: ca. 20 sjablonen



Aantal soorten reacties op bezwaar ca. 10 sjablonen



Aantal potentiele scholingsactiviteiten in Meer dan 15.000



Scholingsregister: opleidingen

Aantal mogelijke opleiders in Scholingsregister: ca. 500 – 2.000 opleiders



Maximaal lopende aanvragen per dossier: max. 3 lopende aanvragen



Aantal keren DigiDgebruik (aanvragen, bezwaren):ca. 900.000 per jaar



Less-educated guess

Burgers oriënteren voorportaal: ca. 80.000 per tranche



Aantal keren eHerkenning gebruik (e-factuur,



indienen Bewijs van Deelname, bezwaren, etc.): ca. 10.000 per tranche

Aantal verwachte niet-digivaardige aanvragen ca. 2.500 per tranche



Inhoud dossier: Minimaal 5 beschikkingen



Verwacht aantal bezwaarschriften: ca. 1.000 per tranche



Aantal verwachte vragen bij callcenter: ca. 20.000 per tranche



Verwachte terugbelverzoeken: ca. 10.000 per tranche



Openingstijden: 24 x 7 beschikbaar



Aantal dossiers: ca. 300.000 nieuwe



dossiers per jaar. (1

miljoen dossiers open).

Versie 1.0 pagina 12 van 72

Programma van Eisen STAP-applicatie

## 8. Functionele Requirements en bijbehorende

## processen

Legenda:

In dit hoofdstuk zijn per proces zijn de functionele requirements opgesteld.

Daarbij zijn de requirements ingedeeld in nice to have en must have. De zwarte

requirements zijn must haves en de blauwe requirements zijn nice to haves.

8.1 Generieke requirements

1. Rollen per medewerker

a. Mogelijkheid tot toekenning van verschillende rollen en autorisaties

per werknemer.

b. Mogelijkheid tot het kunnen identificeren welke werknemer welke taak

uitvoert/heeft uitgevoerd.

2. Audio-technische ondersteuning

a. Mogelijkheid om extra functionaliteit te bieden die dient ter

ondersteuning van aanvragers met visuele beperkingen. Zie ook de

verwijzing naar EN 301549 en WCAG in de Non Functional

Requirements.

3. Statussen dossier

b. Statustoekenning/Statusaanpasbaarheid van dossiers (Status:

aanvraag ontvangen, aanvraag handmatig gematcht,

verleningsbeschikking verzonden, afwijzingsbeschikking verzonden,

etc.).

c. Het opslaan van alle statussen-historie, zodat de aanvraag

gereconstrueerd kan worden (achteraf kunnen zien op welk moment

een dossier een bepaalde status had, c.q. van status is veranderd).

4. Werkverdeling

a. Werkverdeling door middel van “werkbakjes” (c.q. signaallijsten)

b. Sorteer/filtermogelijkheden (op datum ontvangst, registratienummer,

BSN, naam etc.) en een generiek zoekveld à la Google om snel een

casus te kunnen vinden op basis van (deel van) BSN, naam, adres etc.

c. De mogelijkheid tot inrichting van één of meerdere centrale

werkvoorraden/werkbakken waaruit verschillende medewerkers

werken, waarbij herkenbaar is welke casussen bij welke medewerkers

in behandeling zijn en waarbij deze casussen ‘gelockt’ zijn voor de

andere medewerkers.

d. Casussen die in behandeling zijn bij een medewerker, moeten direct of

na een instelbare periode vrijgegeven/overgedragen kunnen worden

naar andere medewerkers, bijvoorbeeld in geval van afwezigheid.

Versie 1.0 pagina 13 van 72

Programma van Eisen STAP-applicatie

5. Digitaliseren

a. Opslagmogelijkheid om gedigitaliseerde documenten in de STAP-

applicatie aan het bijbehorende dossier toe te voegen via een upload

van een bestand vanuit de UWV-kantoorautomatiseringsomgeving.

6. Notificaties en kanaalsturing

a. Het versturen van mailnotificaties als er een voor de burger bestemd

document in het dossier wordt geüpload. Deze mailnotificatie bevat

een link naar het document waarmee deze in het Burgerportaal (na

inloggen via DigiD) door de burger kan worden geopend. Hiertoe dient

via het Burgerportaal de mailvoorkeur te kunnen worden aangegeven

met invoer van een mailadres (‘kanaalsturing’) en in de STAP-

applicatie een mailadresbestand te worden opgebouwd op basis

waarvan mailnotificaties kunnen worden verzonden.

7. Dossiervorming

a. Overall: Opslag en schoning van de gegevens en documenten in de

verschillende dossiers waarbij wordt voldaan aan de vigerende

archiefwet- en regelgeving. Dit betreft onder meer veilige opslag en

toegang en schoning.

b. Inzage van documenten die gekoppeld zijn aan een dossier, op basis

van documenttype gerelateerd aan rol. Dit betreft zowel burgers als

opleiders als de diverse STAP-medewerkers. Hierbij is het

vanzelfsprekend voorwaardelijk dat burgers en opleiders uitsluitend

documenten in kunnen zien behorende bij hun eigen casus(sen) én

waarvan is ingesteld dat de betreffende documenttypen voor hen

inzichtelijk mogen zijn.

c. Alle vanuit de STAP-applicatie aangemaakte en door burgers, opleiders

en STAP-medewerkers geregistreerde gegevens, dienen

geautomatiseerd toegevoegd te worden aan het betreffende dossier

d. Alle vanuit de applicatie aangemaakte en door burgers, opleiders en

STAP-medewerkers geüploade documenten, dienen geautomatiseerd

toegevoegd te worden aan het betreffende dossier, inclusief metadata.

e. Per type subsidie (vooralsnog alleen STAP) dienen bewaartermijnen

instelbaar te zijn. Na afloop van deze termijn komen de dossiers op

een handmatig goed te keuren selectielijst, waarna de onderliggende

gegevens in bulk te vernietigen zijn. Het betreft zowel vernietiging van

databasegegevens (met in te richten welke gegevens eventueel

bewaard moeten blijven voor rapportages) als documenten/

archiefstukken.

Versie 1.0 pagina 14 van 72

Programma van Eisen STAP-applicatie

8. Sjabloonfunctionaliteit

a. De applicatie moet functionaliteit bieden waarmee briefsjablonen

kunnen worden ingericht, met gebruikmaking van generieke en

specifieke tekstblokken, data-tekst integratie, vulling van velden

middels vrije tekst en selectie/pull-down menu’s. De eerste inrichting

van de in paragraaf 8.11en 8.14.5 genoemde sjablonen, dienen door

Leverancier in samenwerking met projectteam plaats te vinden.

Wijzigingen en uitbreidingen dienen door de beheerder van UWV

uitgevoerd te worden.

9. Aanleveren brief/printbestanden

a. De STAP-applicatie moet voorzien in het geautomatiseerd aanleveren

van alle in de STAP-applicatie gegenereerde brieven en beschikkingen

aan DIV (afdeling Documentaire Informatie Voorziening) welke het

printen, couverteren en verzenden verzorgt. De briefbestanden dienen

te worden aangeleverd in PDF/A-formaat en te zijn voorzien van

voorzien van (nader te bepalen) metadata.

10.Opleidingsomgeving

a. Mogelijkheid tot het gebruik van een opleidingsmodule voor alle

portalen binnen de STAP-applicatie (los van testomgevingen en incl.

koppelingen waardoor simulatie van het proces mogelijk is in en over

de verschillende modules).

b. Educatie door de Leverancier omtrent het gebruik van alle portalen

binnen de STAP-applicatie gedurende een vooraf bepaalde tijdsperiode

11.Beheeromgeving

a. Een beheermodule om zelf vanuit een Functioneel Beheer rol

elementen zoals stamtabellen, autorisaties en workflows toe te voegen

en/of te wijzigen.

Versie 1.0 pagina 15 van 72

Programma van Eisen STAP-applicatie

8.2 Informeren

Procesbeschrijving:

In het proces informeren wordt de burger via het STAP-Voorportaal van informatie

voorzien. De burger opent [URL STAP-website] en wordt aldaar geïnformeerd over

de STAP- regeling, het uitvoeren van de pre-check, de beschikbare

scholingsactiviteiten voor het STAP-budget, de arbeidsmarktinformatie, en de FAQ.

Hierbij wordt gebruik gemaakt van de STAP-website (voorportaal) en een koppeling

met het Scholingsregister en met DAMA.

Het UWV wil door middel van het voorportaal de burger digitaal van

informatie voorzien, zodat de burger alle informatie met betrekking tot de

STAP-regeling op een overzichtelijke manier kan bestuderen.

In dit proces worden er geen gegevens opgeslagen.

1. Informeren algemene informatie STAP-regeling

a. Weergave van algemene informatie.

b. Weergave van de aanvraagtranches op het gebied van o.a. start en

einddatum van (lopende) tranche.

c. Weergave van verplichte criteria en voorwaarden die verbonden zijn

aan het (mogen) doen van een aanvraag.

Versie 1.0 pagina 16 van 72

Programma van Eisen STAP-applicatie

2. Teller/statusbalk STAP-budget

a. Weergave van een teller/statusbalk die zo accuraat mogelijk aan kan

geven wat de huidige stand van het budget van de lopende tranche is.

3. Uitvoeren pre-check

a. Uitvoeren pre-check op basis van uitvraag gegevens bij klant (zoals

uitvraag of klant woonachtig is in Nederland, of hij volksverzekerd is,

leeftijd).

b. Doel van de pre-check is om burgers kennis te laten maken met hoe

een aanvraag werkt en of zij over de benodigde

informatie/kwalificaties beschikken om er doorheen te komen.

c. Mogelijkheid van een (met business rules aanpasbare)

beslissingsboom die mensen door de vragen heen loodst.

d. Weergave van de reden tot afwijzing in het geval van een negatieve

uitslag uit de pre-check.

4. Informeren FAQ

a. Aanwezigheid van een FAQ lijst.

b. Splitsing van de FAQ lijst zodat vragen voor opleiders apart staan (in

het Opleidersportaal) van vragen voor burgers.

c. Zoekfunctie om te kunnen zoeken naar een specifieke vraag.

5. Informeren arbeidsmarkt.

a. Link/button naar raadplegen arbeidsmarktinformatie (DAMA), zie

paragraaf 6.1 onder ‘Overzicht Koppelvlakken’.

6. Informeren burger scholingsactiviteiten

a. Weergave van de scholingsactiviteiten uit het Scholingsregister, zie

paragraaf 6.2 onder ‘Overzicht Koppelvlakken’.

b. Duidelijkheid omtrent de voorwaarden en rechten die verbonden zijn

aan de weergegeven scholingsactiviteiten.

c. Uitgebreide zoek/filtermogelijkheden die het zoeken naar de juiste

scholingsactiviteit vergemakkelijken.

d. Mogelijkheid tot een andere weergavemodus bij burgers met

afwijkende rechten (bijvoorbeeld aanvragers tot 30 jaar).

7. Doorlinken naar Burgerportaal

a. Link/button naar het Burgerportaal.

8. Doorlinken naar Opleidersportaal

a. Link/button naar het Opleidersportaal (voor opleiders die zich wellicht

oriënteren via het Burgerportaal).

Versie 1.0 pagina 17 van 72

Programma van Eisen STAP-applicatie

8.3 Inloggen burger en controleren

8.3.1 Inloggen burger

Procesbeschrijving:

De burger logt in met DigiD, waarna aan de hand van het opgehaalde BSN een

koppeling wordt gemaakt met het BRP. Hierna wordt automatisch het MIJNSTAP-

portaal geopend.

Er wordt hier een koppeling gemaakt met BRP en DigiD (Logius).

Als UWV-STAP wil ik met DigiD burgers laten inloggen op het

Burgerportaal, zodat de burger geïdentificeerd kan worden.

Als UWV-STAP wil ik het aanvraagrecht automatisch kunnen controleren,

zodat er zekerheid is over het feit of de burger recht heeft op de subsidie.

1. Inloggen Burger

a. Koppeling met DigiD (Logius).

b. Inlogmogelijkheid met DigiD voor toetreding tot het Burgerportaal.

c. Inloggen met DigiD resulteert in de verkrijging van de BSN van de

burger.

2. Machtigen

a. Gemachtigden moeten middels DigiD Machtigen kunnen toetreden tot

het Burgerportaal.

8.3.2 Wachtrijfunctionaliteit

Er wordt een piek van aanvragen verwacht bij het openstellen van de STAP-regeling

en bij de start van iedere tranche. Bij voorkeur dient de STAP-applicatie deze grote

hoeveelheid aan gelijktijdige aanvragen direct en gelijktijdig te kunnen verwerken

zodat de burgers hier geen hinder van ondervinden. Het is echter aannemelijk dat

hiertoe een onevenredige inzet van softwareontwikkeling en hardwarecapaciteit

vereist is. Het is derhalve acceptabel wanneer deze pieken deels worden

opgevangen met inzet van ‘wachtrijfunctionaliteit’ waarbij de pieken kunnen

worden gespreid. De maximale wachttijd mag hierbij niet langer zijn dan 10

minuten waarbij via een voortgangsbalk wordt getoond wanneer de aanvraag kan

worden gestart.

Versie 1.0 pagina 18 van 72

Programma van Eisen STAP-applicatie

8.3.3 Controleren aanvraagrecht

Procesbeschrijving:

Nadat de burger zijn aanvraag start, controleert het systeem of de burger in het

huidige kalenderjaar al een subsidie aangevraagd heeft en of de burger op het

moment van aanvragen op de uitsluitingslijst staat. Vervolgens worden aan de

hand van de uit de BRP opgehaalde persoonsgegevens getoetst of de burger aan de

eisen voor de aanvraag voldoet. Daarna wordt er een set persoonlijke vragen

gesteld om een beter beeld te krijgen van de burger. Nadat alle vragen zijn

beantwoord wordt weergegeven of de burger recht heeft op subsidie en de

aanvraag kan indienen. Indien de burger geen recht heeft op subsidie, maar toch

van mening is dat hij recht heeft, kan hij een toelichting geven op zijn

subsidieaanvraag en de aanvraag alsnog doorzetten. Als de burger geen toelichting

geeft stop de subsidieaanvraag. Na het indienen van de aanvraag worden alle

gegevens opgeslagen in een klantdossier.

Er worden hier koppelingen gemaakt met de uitsluitingslijst.

Versie 1.0 pagina 19 van 72

Programma van Eisen STAP-applicatie

1. Automatische controles

Bij de controles is de volgorde niet van belang, wel dat alle stappen worden

gedaan. Belangrijk is om inzichtelijk te krijgen wat de meest efficiënte

volgorde is als er op elk punt burgers uit (kunnen) vallen.

a. Bij de start van een aanvraag dient automatisch te worden

gecontroleerd of de burger op het moment van aanvraag niet in het

huidig kalenderjaar al een subsidie heeft ontvangen.

b. Bij start aanvraag check op Uitsluitingslijst (lijst met geblokkeerde

BSN’s). Zie paragraaf 8.16.

c. Koppeling met het BRP.

d. Check op BRP-gegevens, leeftijd en woonplaats.

e. Set met persoonlijke vragen voor de burger.

2. Recht op aanvraag

a. Indien recht op aanvraag wordt subsidieaanvraag doorgezet.

b. Indien geen recht van aanvraag, in werking treden van proces

‘Opvragen toelichting’. Indien er toelichting wordt gegeven kan de

burger door met de subsidieaanvraag, anders wordt de aanvraag

stopgezet.

3. Opslaan gegevens bij inloggen

a. Opslag contactgegevens (e-mail/telefoonnummer) in het dossier van

de burger.

b. Opslag NAW-gegevens in het dossier van de burger.

8.3.4 Opvragen toelichting

Procesbeschrijving:

Wanneer de burger tijdens het aanvraagproces blijkt dat de burger geen recht

(meer) heeft om een subsidieaanvraag in te dienen dan krijgt de hij of zij de

mogelijkheid om alsnog de aanvraag door te zetten. Als de burger akkoord is met

de afwijzingsreden en niet kiest om de aanvraag door te zetten dan wordt de

aanvraag afgebroken. Als de burger hier wel voor kiest moet de aanvraag

voortgezet worden. Vervolgens dient de burger in een argumentatieveld op te

kunnen geven waarom hij of zij van mening is alsnog recht te hebben. Als dit

opgegeven is kan de aanvraag weer voortgezet worden, met als gevolg dat deze in

het handmatig beoordelingsproces wordt afgehandeld alwaar de toelichting actief

getoond dient te worden (bijvoorbeeld via een pop-up melding of een duidelijk

zichtbare indicatie).

Versie 1.0 pagina 20 van 72

Programma van Eisen STAP-applicatie

Als UWV-STAP wil ik burgers de mogelijkheid geven om toelichting te

bieden wanneer hij of zij van mening is alsnog recht op een

subsidieaanvraag te hebben, zodat deze burgers niet onterecht verhinderd

worden om een aanvraag in te dienen.

1. Mogelijkheid tot toelichting

a. Duidelijke weergave van afwijzingsreden voor de burger.

b. Keuzemogelijkheid voor de burger om een toelichting te geven

wanneer de burger van mening is alsnog recht te hebben op subsidie.

c. Mogelijkheid voor de UWV-Adviseur om doorgegeven toelichting aan

de aanvraag toe te voegen.

d. Handmatig afhandelen van deze aanvragen waarbij de toelichting

actief getoond wordt (bijvoorbeeld via een pop-up melding of een

duidelijk zichtbare indicatie).

Versie 1.0 pagina 21 van 72

Programma van Eisen STAP-applicatie

8.4 Aanvragen digivaardigen

Procesbeschrijving:

Als de burger is ingelogd kan hij starten met het indienen van zijn aanvraag. Hier

worden de gegevens van de burger gecontroleerd met de voorwaarden van de

subsidieaanvraag. Daarnaast wordt ook gecheckt of de burger op de uitsluitingslijst

(zie paragraaf 8.16) staat en of de burger al een subsidie heeft gebruikt in het

huidige kalenderjaar. De burger dient hierna snel en effectief de scholingsactiviteit

te kunnen selecteren waarvoor hij of zij een STAP-aanvraag wil doen en de start-

en einddatum in te geven. Vervolgens wordt de burger gevraagd om een set

persoonlijke vragen te beantwoorden die helpen bij het creëren van

sturingsinformatie.

Daarna wordt er automatisch gecontroleerd of burger aan de subsidievereisten

voldoet. Als de burger hieraan voldoet, of een toelichting aanvult, zodat hij er aan

voldoet kan het Bewijs van Aanmelding bij de aanvraag worden toegevoegd. Als de

burger dit documentbestand uploadt, wordt automatisch de scholingsactiviteit

ingevuld op basis van de documentgegevens. Daarna kan de burger al zijn

gegevens controleren op mogelijke fouten en worden de voorwaarden

weergegeven, waarna de burger deze moet accepteren om de subsidieaanvraag in

te dienen. De burger ziet daarna een scherm waarin wordt bevestigd dat de

subsidieaanvraag is ingediend en kan het Bewijs van Aanmelding (digitaal aan hem

verstrekt door de Opleider) downloaden.

In het Burgerportaal worden koppelingen gemaakt met het Scholingsregister.

Ook moet het mogelijk zijn om een dossier op te slaan bij een aanvraag waarbij de

checks hebben aangegeven dat er geen recht is op de subsidie en de burger heeft

aangegeven een beschikking tot afwijzing te willen ontvangen. Hierbij bieden we de

burger de mogelijkheid om een zgn. beschikking tot afwijzing op te laten vragen.

De logging en monitoring van de poging is onderdeel van het dossier om te kunnen

achterhalen waarom de poging tot aanvraag (technisch) niet geslaagd is.

Versie 1.0 pagina 22 van 72

Programma van Eisen STAP-applicatie

Het UWV-STAP wil burgers digitaal subsidie laten aanvragen in zes

tranches, om de aanvraag zo automatisch, volledig en efficiënt mogelijk af

te handelen.

8.4.1 Indienen aanvraag

1. Invoeren aanvraag

a. Ophalen en invoegen van BRP-gegevens zoals ze op het moment van de

aanvraag bekend zijn, tonen en overnemen.

b. Weergave van een melding voor de start van een aanvraag met de tekst:

“heeft u uw Bewijs van Aanmelding bij de hand?”

c. Controleren van aanvraagrecht (paragraaf 8.3.3)

d. In werking treden van proces ‘Opvragen toelichting’ (paragraaf 8.3.4)

wanneer blijkt dat de burger op dit moment geen recht (meer) heeft op

het doen van een aanvraag.

e. Voor de burger zichtbare weergave van de gegevens die door middel van

het BRP aan hem gekoppeld zijn (BRP-gegevens, NAW, geboortedatum,

link met Nederlandse arbeidsmarkt).

f. Selecteren scholingsactiviteit (zie onder 2) en invoeren start- en

einddatum opleiding.

g. Uploaden Bewijs van Aanmelding, zie paragraaf 8.4.2.

h. Aanvullende mogelijkheid tot directe matching van de persoons- en

opleidingsgegevens afgeleid uit het Bewijs van Aanmelding met de BRP-

gegevens en de geselecteerde opleidingsactiviteit, zie ook paragraaf 8.6.

i. Beantwoording van een set persoonlijke vragen ten behoeve van het het

creëren van sturingsinformatie (bijvoorbeeld omtrent de hoogst genoten

opleiding van de burger of de huidige werkzaamheden die hij verricht).

j. Mogelijkheid tot het downloaden van een overzicht/samenvatting van de

aanvraag.

2. Selecteren scholingsactiviteit - Zie ook user story koppelvlak 19 in Bijlage 1

a. Koppeling met het Scholingsregister.

b. Zoek/filtermogelijkheden die het zoeken naar de juiste scholingsactiviteit

vergemakkelijken.

c. Invoerveld waarbij de invoer van tekst automatisch resulteert in een

suggestie van gelijknamige scholingsactiviteiten (auto complete).

d. Daarnaast via invoer van een unieke code per scholingsactiviteit, welke in

het Bewijs van Aanmelding is opgenomen, de bijbehorende

opleidingsgegevens afleiden en tonen. Nader uit te werken of hier nog de

mogelijkheid moet worden geboden een andere keuze te maken.

e. Garantie dat de het aanvraagproces enkel naar de volgende stap kan

wanneer een scholingsactiviteit is geselecteerd.

f. Invoeging van aanduiding (opslag in het systeem) welke versie van het

Scholingsregister is gebruikt bij de aanvraag.

Versie 1.0 pagina 23 van 72

Programma van Eisen STAP-applicatie

3. Budgetbeschikbaarheid

a. Stopzetting van het kunnen aanvragen in het geval dat er geen budget

voor de lopende tranche meer beschikbaar is.

b. Bij indienen van de aanvraag nogmaals een check op

budgetbeschikbaarheid.

c. In werking treden van proces 2b onder 8.3.3 (afbreken aanvraag)

wanneer bij de laatste budgetcheck blijkt dat er op dit moment geen

budget meer beschikbaar is.

d. Ontvangst van een melding wanneer een burger op de aanvraagknop

drukt in het geval van een stopzetting door gebrek aan budget (als

beschreven bij a).

e. Weergave van een teller die zo accuraat mogelijk aan kan geven wat de

huidige stand van het budget is.

f. De hoogte van het beschikbare bedrag moet per tranche

parametiseerbaar zijn.

4. Afronden aanvraag

a. Aanvraag dient enkel verstuurd te worden indien alle velden zijn ingevuld

en alle benodigde documenten zijn bijgevoegd.

b. Opslag van de volledige aanvraag wordt opgeslagen in een dossier van

de burger.

c. Mogelijkheid voor de burger om een bewijs van de aanvraag als PDF-

bestand te downloaden.

d. Een directe melding via het portaal dat de aanvraag in goede orde is

ontvangen.

e. Invoeging van een timestamp (datum, tijdstip) aan ingediende

aanvragen.

f. De burger moet voor een default in te stellen periode de mogelijkheid

hebben na (bewust of onbewust) uit te hebben gelogd, opnieuw in te

kunnen loggen en een eerder gestarte aanvraag te kunnen voltooien.

Hierbij mogen de gegevens vanuit beveiligingsoverwegingen niet worden

opgeslagen in de front- end maar dienen opnieuw te worden opgehaald

uit de back-end.

5. Voorwaarden en consequenties

a. Weergave van de voorwaarden en consequenties voordat de burger zijn

aanvraag verstuurt.

b. Duidelijke vermelding aan de burger dat na het accepteren van de

voorwaarden en consequenties dat na het indienen van de aanvraag niets

meer aan de aanvraag gewijzigd kan worden.

c. Aanvinkbutton waardoor de burger kan bevestigen dat hij de aanvraag

naar waarheid heeft ingevuld.

d. Weergave van alle ingevulde velden voorafgaand aan het definitief

indienen van de aanvraag, met mogelijkheid terug te keren naar de

aanvraag indien wijziging gewenst is.

Versie 1.0 pagina 24 van 72

Programma van Eisen STAP-applicatie

e. Weergeven van het beschikkingsnummer dat aan de ingediende aanvraag

wordt verbonden, inclusief een duidelijke melding dat dit het nummer is

dat STAP gebruikt om aanvragen te identificeren. Daarnaast weergave

van alle voor de STAP-unit bekende gegevens die aan de aanvraag

verbonden zijn.

f. Inzage lopende en afgeronde subsidieaanvragen (gegevens, status en

documenten).

8.4.2 Uploaden Bewijs van Aanmelding

Om de aanvraag compleet te maken moet er een Bewijs van Aanmelding worden

aangeleverd. De burger voegt een Bewijs van Aanmelding toe aan de aanvraag (via

een upload bij de aanvraag in het Burgerportaal). Dit (digitale) Bewijs van

Aanmelding wordt door de opleider verstrekt (gemaild) aan de burger. De opleider

kan het Bewijs van Aanmelding op twee manieren aanbieden aan de burger:

1. Een gestandaardiseerd xml-bestand;

2. Een gestandaardiseerd pdf-bestand voorzien van metagegevens.

Er wordt met opleiders gewerkt aan een standaard voor het Bewijs van

Aanmelding. Dit moet op dit moment nog uniform worden afgesproken.

1. Aanleveren Bewijs van Aanmelding door burger

a. Inlogmogelijkheid op het Burgerportaal door middel van DigiD.

b. Mogelijkheid om op twee verschillende manieren een Bewijs van

Aanmelding te leveren via het Burgerportaal: Upload XML-bestand of

upload pdf-bestand.

c. Automatische opslag van het aangeleverde Bewijs van Aanmelding en de

bijbehorende gegevens in het dossier van de burger.

d. Afleiden en opslaan van relevante metadata ter verdere

verwerking/matching.

e. Indien niet overeengekomen en bereikt kan worden dat aanlevering via

gestandaardiseerde xml/pdf-bestanden plaats gaat vinden, wordt

mogelijk toch toegestaan dat het Bewijs van Aanmelding een

pdf/jpeg/png bestand (zonder metadata) is. In dat geval wordt gevraagd

of het mogelijk is op basis van OCR/ICR de betreffende gegevens (zoals

BSN, scholingsactiviteit en startdatum) af te leiden.

Versie 1.0 pagina 25 van 72

Programma van Eisen STAP-applicatie

8.5 Aanvragen niet-digivaardigen

Procesbeschrijving:

Een niet-digivaardige burger vraagt subsidie aan door naar het UWV-werkplein te

komen en zijn identiteit te laten controleren. Met deze identiteitscontrole kan de

UWV-Adviseur aan de hand van het BSN de BRP-gegevens ophalen en automatisch

laten controleren of de burger aan de eisen van de opleiding voldoet. Daarna wordt

een automatische check gedaan of de burger op de uitsluitingslijst staat en of de

burger al eerder subsidie heeft genoten in het huidige kalenderjaar. Als de burger

niet aan de voorwaarden van de subsidie heeft voldaan kan hij op verzoek een

beschikking tot afwijzing geprint meekrijgen. Als aan alle voorwaarden is voldaan

voert de medewerker de scholingsactiviteit in en wordt het Bewijs van Aanmelding

geüpload, door middel van het overnemen van een digitaal document of inscannen

van het Bewijs van Aanmelding. De burger ondertekent dat hij akkoord is met de

aanvraag en alle voorwaarden, waarna de medewerker dit digitaliseert (via de

scanner in de UWV-kantoorautomatiseringsomgeving) en in het systeem upload bij

de aanvraag. Hierna wordt de volledig ingevulde aanvraag ingediend door de UWV-

Adviseur. Als laatste wordt de volledige aanvraag uitgeprint en overhandigd aan de

burger, zodat hij een bewijs heeft van zijn aanvraag voor een STAP subsidie.

Er wordt gebruik gemaakt van de STAP-applicatie, waarin de medewerker een

aanvraag indient voor de burger.

Er worden koppelingen gemaakt naar BRP en DigiD.

Als niet-digivaardige wil ik een subsidie kunnen aanvragen via de

medewerker van het werkplein van het UWV, zodat ik een

opleidingsbudget te krijgen en mijn arbeidsmarktpositie te versterken.

1. Adviseur

a. Mogelijkheid om namens de klant dezelfde stappen te doorlopen, zoals

beschreven voor digivaardige aanvragen, met uitzondering van het

inloggen middels DigiD (‘zij-invoer’).

b. Een medewerker moet een dossier handmatig kunnen aanmaken.

Versie 1.0 pagina 26 van 72

Programma van Eisen STAP-applicatie

2. Indienen aanvraag

a. Mogelijkheid om een aanvraag te doen door invoeren van een UWV-

Adviseur.

b. Mogelijkheid voor de UWV-Adviseur om via SSO/ADFS in te loggen op het

UWV-Medewerkersportaal.

c. Directe weergave van de hoogte van het resterende budget voor de

lopende tranche.

d. Mogelijkheid om door middel van het identiteitsbewijs van de niet-

digivaardige burger het BSN te herleiden om vervolgens een koppeling te

maken met de bijbehorende gegevens uit het BRP.

e. Mogelijkheid tot digitaliseren van documenten en deze te kunnen

uploaden ter toevoeging aan het dossier.

f. Een niet-digivaardige burger dient een fysiek document te ondertekenen

(vanuit de STAP-applicatie aan te maken en te printen vanuit de UWV-

kantoorautomatiseringsomgeving) wat bewijst dat hij akkoord is met de

voorwaarden, zodat hij dit later niet kan ontkennen.

g. Voor het definitieve indienen van de aanvraag nog een keer kunnen

controleren of er nog budget beschikbaar is

h. In werking treden van proces 2b onder 8.3.3 (afbreken aanvraag)

wanneer bij de laatste budgetcheck blijkt dat er op dit moment geen

budget meer beschikbaar is.

3. Controleren aanvraagrecht

a. Een niet-digivaardige burger dient dezelfde automatische controles als

een digivaardige burger te ondergaan (proces 2C).

b. In werking treden proces 2D wanneer uit de automatische controles blijkt

dat de burger geen recht (meer) heeft.

c. Opslag van de volledige aanvraag in het dossier van de niet-digivaardige

burger.

d. Invoeging van een timestamp (datum, tijdstip) aan ingediende

aanvragen.

Versie 1.0 pagina 27 van 72

Programma van Eisen STAP-applicatie

8.5.1 Leveren Bewijs van Aanmelding

Ook voor het niet-digivaardige proces geldt dat er een Bewijs van Aanmelding moet

worden toegevoegd aan de aanvraag. Bij een niet-digivaardige wordt een (fysiek)

document (gedigitaliseerd) door de UWV-Adviseur en toegevoegd aan de aanvraag.

1. Leveren Bewijs van Aanmelding niet-digivaardige

a. Mogelijkheid van digitalisering van fysiek aangeleverde bewijzen van

aanmelding.

b. Opslag gedigitaliseerde bewijzen van aanmelding in het dossier van de

desbetreffende niet-digivaardige aanvraag.

2. Voorkomen uitval

a. Aangezien de scan en upload van het Bewijs van Aanmelding door de

UWEV-adviseur geen metadata bevat, zou deze in de uitvalafhandeling

terecht komen (zie paragraaf 8.6). Er van uitgaande dan de UWV-

Adviseur controleert of de aangevraagde opleidingsgegevens stroken met

het Bewijs van Aanmelding, dient dit voor deze aanvragen te worden

voorkomen.

Versie 1.0 pagina 28 van 72

Programma van Eisen STAP-applicatie

8.6 Matchen BvA en beschikken aanvraag

Procesbeschrijving:

De binnengekomen subsidieaanvraag wordt automatisch gematcht aan de hand van

het Bewijs van Aanmelding met de ingevulde opleiding en de persoonsgegevens.

Als dit overeenkomt wordt de aanvraag automatisch beschikt en ontvangt de

burger een beschikking tot verlening, daarnaast wordt een bestelaanvraag gestuurd

naar FEZ.

Als het Bewijs van Aanmelding niet direct matcht, dan wordt dit handmatig

gecontroleerd en gematcht. Als dit gematcht is, dan wordt dit deze automatisch

beschikt en verwerkt, zoals hiervoor beschreven.

Indien de aanvraag van toelichting is voorzien wordt dit handmatig gecontroleerd

door de STAP-medewerker of de burger alsnog recht heeft op subsidie.

Als het Bewijs van Aanmelding niet matcht met de inschrijving dan wordt de

subsidieaanvraag afgekeurd en treedt het proces ‘informeren belastende

beschikking’ in werking.

Het UWV wil het beschikken zo veel mogelijk automatiseren, op een

manier dat het beschikken zo effectief en efficiënt mogelijk verloopt en dat

er zo min mogelijk fouten worden gemaakt en zoveel mogelijk subsidie kan

worden verstrekt.

1. Inloggen STAP-medewerker

a. Inlogmogelijkheid voor medewerkers door middel van ADFS/SSO.

Dit geldt voor alle STAP-medewerkers, dus ook de B&B-STAP-

medewerkers, de UWV-adviseurs en eventueel de

klantcontactcentermedewerkers.

Versie 1.0 pagina 29 van 72

Programma van Eisen STAP-applicatie

2. Matchen

a. Inzage in het dossier van de burgers om de relevante documenten voor

het matchingsproces in te kunnen zien.

b. Automatisch matchen van de scholingsactiviteit en start/einddatum van

de aanvraag met de onderliggende gegevens geëxtraheerd uit de

xml/pdf-upload van het Bewijs van Aanmelding.

c. Aanbieden aan de handmatige uitvalafhandeling in het geval dat de

scholingsactiviteiten niet overeenkomen of niet afgeleid kunnen worden

uit de bestandsgegevens van het geüploade Bewijs van Aanmelding.

d. De mogelijkheid voor de STAP-medewerker op basis van

handmatige/visuele beoordeling en eventueel (telefonisch) contact met

de burger, de aanvraag alsnog akkoord te bevinden (en daarmee alsnog

te ‘matchen’) dan wel af te wijzen. Dit laatste gaat gepaard met het

opstellen van een afwijzingsbeschikking, zie paragraaf 8.11.

e. Voor de aanvragen van niet digivaardigen ingevoerd door de UWV-

Adviseur, bevat de scan en upload van het Bewijs van Aanmelding geen

metadata. Deze moeten echter niet in de uitvalafhandeling terecht

komen, maar moeten direct de status ‘gematched’ krijgen.

N.B. Afhankelijk van de betrouwbaarheid van de aanlevering van de Bewijzen

van Aanmelding met de juiste metadata, voorzien we de mogelijkheid meer

controles ‘aan de voorkant’ (direct bij het uploaden van het Bewijs van

Deelname) plaats te laten vinden:

Met de gegevens uit het Bewijs van Aanmelding wordt dan direct gecontroleerd

of de persoonsgegevens overeenkomen met de BRP-gegevens en of de

scholingsactiviteit overeenkomt met hetgeen is geselecteerd/ingegeven bij de

aanvraag. Als de gegevens uit het Bewijs van Aanmelding niet leesbaar zijn,

ontbreken of niet overeenkomen, dan wordt de burger de mogelijkheid geboden

te laten verklaren (vinkje) dat de persoon op het BvA de aanvrager is (eventueel

met weergave van de BRP-NAW-gegevens) en/of de scholingsactiviteit te laten

corrigeren en/of een ander BvA te uploaden.

Bovenstaande moet onderdeel zijn van de aanbieding/inschrijving.

3. Toelichting

a. Indien toelichting bij de subsidieaanvraag is gegeven, moet hier

handmatig door de STAP-medewerker worden gecontroleerd of de burger

alsnog recht heeft op subsidie.

b. Indien alsnog recht op subsidie dan dient de aanvraag conform het

automatische beschikkingsproces te worden gevolgd.

c. Indien geen recht dan belt de STAP-medewerker de burger om te

informeren over de belastende beschikking. De STAP-applicatie dient een

notitieveld te bevatten om (een samenvatting van) het resultaat van dit

telefoongesprek te registeren.

d. Automatisch opstellen van beschikking tot afwijzing bij geen recht.

Versie 1.0 pagina 30 van 72

Programma van Eisen STAP-applicatie

4. Beschikken

a. Gematchte aanvragen dienen volledig geautomatiseerd te leiden tot een

Beschikking tot verlening (‘straigh through processing’).

b. Niet gematchte aanvragen dienen (na handmatige uitvalafhandeling) te

leiden tot een automatisch aangemaakte Beschikking tot afwijzing

c. Toevoeging van het beschikkingsnummer op de aangemaakte

beschikkingen.

d. Levering van de beschikkingen geschiedt per post (zie paragraaf 8.12.1),

tenzij de burger in het Burgerportaal aangeeft zijn correspondentie in het

Burgerportaal gepresenteerd te willen krijgen (zie paragraaf 8.1 punt 6).

e. Automatisch doorsturen van aanvragen die zijn goedgekeurd

(beschikking tot verlening) als bestelaanvraag naar FEZ (PeopleSoft).

5. Opslaan data

Een dossier kent drie statussen, namelijk open, gesloten en heropend. Vanaf de

datum dat een dossier gesloten wordt, gaat de archiveringstermijn van 7 jaar in

werking, waarna het vernietigd wordt. Als een dossier open blijft zal deze niet

gearchiveerd worden en kunnen er nog documenten aan toegevoegd worden.

Als een dossier heropend wordt, vervalt de archiveringstermijn, en vangt een

nieuwe archiveringstermijn van 7 jaar aan zodra het heropende dossier opnieuw

gesloten wordt.

a. Opslag van een open dossier voor de duur van de opleiding en daarna

wettelijke termijn.

b. Te allen tijde dient de status van het (open) dossier inzichtelijk te zijn.

c. Archivering van gegevens zodra het dossier wordt gesloten, conform

bovenstaand beschreven.

d. Vernietiging van dossiers na archiveringstermijn, dit na bevestiging door

Functioneel beheerder op basis van ‘vernietigingsoverzichten’.

e. Alle opgestelde beschikkingen dienen toegevoegd te worden aan het

bijbehorende dossier.

f. Hierbij moet worden voldaan aan de AVG-eisen waarmee de

medewerkers de documenten mogen zien van de casussen die zij in

behandeling nemen/hebben en de burgers en opleiders alleen de

documenten die aan hen persoonlijk zijn gericht.

6. Reminders

a. De STAP-applicatie dient geautomatiseerd een mailnotificatie op een

generiek instelbare periode voor aanvang van zijn scholingsactiviteit naar

de burger te versturen.

b. Mailnotificatie heeft een aanhef met de naam van de burger en de inhoud

bevat een vooraf gedefinieerde vaste tekst.

Versie 1.0 pagina 31 van 72

Programma van Eisen STAP-applicatie

7. Doelbinding

Met beperking van de uploadmogelijkheden (niet te bieden bij mutaties door de

burger), gaan we ervan uit dat het zeer sporadisch zal voorkomen dat we

‘onvoorspelbaar’ vertrouwelijke/gezondheids-gegevens binnenkrijgen.

Vooralsnog treffen we hier geen specifieke doelbindingsmaatregelen op. Mocht

uit de ervaring blijken dat ontvangst van dergelijke gegevens toch regelmatig

plaatsvindt, dan voorzien we een eenvoudige/werkbare oplossing welke door de

STAP-applicatie ondersteund moet worden:

a. De STAP-medewerker voert de vereiste registraties uit (we kunnen

immers niet voorkomen dat de eerste medewerker deze informatie onder

ogen krijgt) waarna het document/de informatie kan worden ‘dichtgezet’

voor anderen (waarbij wel inzichtelijk moet zijn dat de informatie is

ingediend maar niet wat de inhoud hiervan is).

b. Bij het eventueel inloggen door een UWV-B&B-medewerker moet dit

document/deze informatie wel zichtbaar zijn.

Versie 1.0 pagina 32 van 72

Programma van Eisen STAP-applicatie

8.7 Afbreken en muteren scholingsactiviteit

Procesbeschrijving:

Bij het tussentijds beëindigen of het annuleren van de scholingsactiviteit moeten de

burger en opleider aan de meldingsplicht voldoen door onverwijld te laten weten

dat zij de scholingsactiviteit niet met succes kunnen volgen/afronden. De UWV-

STAP-medewerker kan de wijziging bekijken en doorvoeren, waarbij eventueel het

geld terug- en ingevorderd kan worden bij de opleider.

Een wijziging kan op meerdere manieren aangegeven worden, namelijk door de

opleider en door de burger. Dit kan tijdens verschillende momenten in het proces

gebeuren, waardoor op verschillende manieren gereageerd moet worden op het

wijzigen van de aanvraag.

Afhankelijk van of er een bestelaanvraag is gestuurd, zal ad hoc hierop geregeerd

worden of er moet worden terug- en ingevorderd of dat de bestelaanvraag kan

worden geannuleerd.

Dit gebeurt in de STAP-applicatie en de aanlevering van annulering van de

bestelaanvraag wordt verstuurd naar Peoplesoft FEZ.

Versie 1.0 pagina 33 van 72

Programma van Eisen STAP-applicatie

Het UWV wil burgers en opleiders de mogelijkheid bieden om mutaties

omtrent de scholingsactiviteit door te geven, zodat een subsidieaanvraag

kan worden geannuleerd wanneer deze niet doorgaat.

1. Wijzigingen door digivaardigen

a. Indienen wijzigingen/mutaties vanuit het Burgerportaal via button/link

vanuit de betreffende beschikking. N.B. Dit betreft een eenvoudige

melding zonder documentupload aangezien we mutaties van burgers

accepteren zonder eventuele terug- en invordering en hierbij ook geen

bewijslast vragen. Een upload zou leiden tot grotere kans op ontvangst

van vertrouwelijke/gezondheidsgegevens hetgeen we willen vermijden.

b. De burger dient een standaard webformulier in te vullen met gesloten

vragen over de reden van annuleren/afbreken van de scholingsactiviteit.

c. Het standaard webformulier dient te bestaan uit vragen over

verwijtbaarheid, reden tot annuleren/afbreken, beschikkingsnummer en

overig invulveld.

2. Wijzigingen door niet-digivaardige burger per post

a. Mogelijkheid tot ‘zij-invoer’ bij ontvangst wijzigingen/mutaties via DIV

gedigitaliseerde post (zie paragraaf 8.12.2) in geval van niet-

digivaardigen, inclusief uploadfunctionaliteit voor het bijvoegen van

stukken.

3. Wijziging door opleider

a. Indienen wijzigingen/mutaties vanuit het Opleidersportaal via button/link

vanuit de betreffende beschikking. Hiermee heeft de opleider de

mogelijkheid om onverwijld te laten weten dat de scholingsactiviteit niet

wordt gestart/niet doorgaat.

b. De opleider dient een standaard webformulier in te vullen met gesloten

vragen wat aangeeft dat een scholingsactiviteit vervroegd is beëindigd of

niet zal plaatsvinden.

4. Verwerken door medewerker

a. In het geval dat er nog geen bestelaanvraag is gestuurd, moet de

aanvraag worden afgebroken en dient een beschikking tot intrekking te

worden opgesteld en naar de burger gestuurd te worden.

b. In het geval dat een bestelaanvraag is gestuurd en er nog niet betaald is,

moet de aanvraag worden afgebroken en dient een inkoopannulering

naar de opleider via het verrichten van een handeling in Peoplesoft en

een beschikking tot intrekking naar de burger opgesteld en verstuurd te

worden.

c. In het geval dat een bestelaanvraag is gestuurd en er wel betaald is,

moet de aanvraag worden afgebroken en dient een beschikking tot terug-

en invordering naar de opleider en een beschikking tot intrekking naar de

burger opgesteld en verstuurd te worden.

d. Het Medewerkersportaal moet een registratieveld bevatten ter toelichting

op de verwerking van de mutatie door de STAP-medewerker.

e. Opslag van alle vormen van wijziging in het dossier van de

desbetreffende aanvraag.

Versie 1.0 pagina 34 van 72

Programma van Eisen STAP-applicatie

8.8 Inloggen Opleider en leveren Bewijs van Deelname

8.8.1 Inloggen Opleider

De opleider logt in op het Opleidersportaal met eHerkenning, waarna aan de hand

van de identificatie en authenticatie het KvK nummer wordt opgehaald. Deze wordt

vervolgens gematcht aan het Scholingsregister, waardoor de opleider na inloggen

enkel de scholingsactiviteiten die hij zelf in beheer heeft kan zien. Tevens kan hij in

het Opleidersportaal zijn gegevens beheren, meldingen doorgeven, (waaronder

afbreken scholingsactiviteit), bewijzen van deelname uploaden, documenten

raadplegen, bezwaren indienen, etc.

Er wordt hier een koppeling gemaakt met eHerkenning en het Scholingsregister.

1. Koppeling met eHerkenning, volledig door Leverancier in te richten.

2. Inlogmogelijkheid voor opleiders voor toegang tot het Opleidersportaal door

middel van eHerkenning.

3. Door middel van eHerkenning wordt het KvK-nummer van de opleider voor STAP

opgehaald en ingevuld.

Na het inloggen dient het Opleidersportaal het volgende te bieden:

a. Overzicht van de scholingsactiviteiten die bij de betreffende opleider

horen, dit op basis van de koppeling met (een kopie van) het

Scholingsregister.

b. Overzicht van welke burger STAP-subsidie heeft voor welke

scholingsactiviteit bij deze opleider.

c. Mogelijkheid tot maken van bezwaar.

d. Meldingen doorgeven (waaronder afbreken scholingsactiviteit).

e. Indienen van het Bewijs van Deelname (zie volgende paragraaf).

Versie 1.0 pagina 35 van 72

Programma van Eisen STAP-applicatie

8.8.2 Leveren Bewijs van Deelname

De opleider kan het Bewijs van Deelname (in te dienen per aanvraag van een

burger) op twee manieren leveren, namelijk door het Bewijs van Deelname in te

dienen via het Opleidersportal (per aanvraag), of door het invullen van een

webformulier dat dezelfde informatie opvraagt als de eisen aan het Bewijs van

Deelname.

Het bestand (set van gegevens) zal in de volgende vormen binnen moeten komen:

3. Een gestandaardiseerd xml-bestand;

4. Een gestandaardiseerd pdf-bestand voorzien van metagegevens.

5. Invoer via een webformulier welke onderdeel is van het Opleidersportaal.

Het webformulier wordt vervolgens binnen de STAP-applicatie geconverteerd, zodat

er meta-gegevens aan het Bewijs van Deelname zitten die door de STAP-applicatie

gelezen kunnen worden. Beide manieren resulteren in het ontvangen van een

Bewijs van Deelname.

Er wordt met opleiders gewerkt aan een standaard voor het Bewijs van Deelname.

Dit moet op dit moment nog uniform worden afgesproken.

2. Aanleveren Bewijs van Deelname door opleider

a. Inlogmogelijkheid op het Opleidersportaal door middel van eHerkenning.

b. Mogelijkheid om op drie verschillende manieren een Bewijs van

Deelname te leveren via het Opleidersportaal: Upload XML-bestand,

upload pdf-bestand voorzien van metagegeven en invullen van

webformulier.

c. Het systeem dient bij het uploaden van het Bewijs van Deelname, real

time een automatische syntax-check te doen en direct een melding aan

de opleider te geven indien het bestand niet voldoet aan de eisen.

d. Opslag van aangeleverd Bewijs van Deelname en bijbehorende gegevens

in het dossier van de desbetreffende aanvraag.

Versie 1.0 pagina 36 van 72

Programma van Eisen STAP-applicatie

8.8.3 Rappelleren Bewijs van Deelname

Als er geen Bewijs van Deelname wordt geleverd dan krijgt het systeem een

generiek instelbare tijdstrigger wat duidelijk maakt dat er tot op heden niets is

ontvangen, waarna automatisch een rappel wordt verstuurd naar de opleiders die

een e-factuur hebben gestuurd. Wanneer het Bewijs van Deelname alsnog geleverd

wordt, kan deze meegenomen worden in het beschikkingsproces. Mocht het Bewijs

van Deelname uitblijven dan treedt, wanneer de afgesproken inlevertermijn

verstreken is, het terug- en invorderproces in werking.

Het UWV wil een rappel versturen naar opleiders die niet tijdig een Bewijs

van Deelname aanleveren.

1. Versturen rappel

a. Automatisch versturen van rappel naar opleider per e-mail als een Bewijs

van Deelname na instelbare periode (vooralsnog drie maanden) na

eindigen scholingsactiviteit niet is ontvangen.

b. Verstuurde rappel opslaan in het dossier.

2. Gehoor aan rappel gegeven

a. Binnengekomen bewijzen van deelname als gevolg van een rappel dienen

naar het “afronden beschikking” proces doorgestuurd te worden.

3. Geen gehoor aan rappel gekregen

a. Een instelbare periode na het verzenden van een rappel waarbij geen

Bewijs van Deelname is ontvangen, dient de STAP-applicatie het proces

van terug- en invorderen te triggeren.

b. Dit leidt een signaal aan een STAP-medewerker waarna na zijn

goedkeuring geautomatiseerd een beschikking wordt aangemaakt en een

bericht naar PeopleSoft wordt verzonden.

Versie 1.0 pagina 37 van 72

Programma van Eisen STAP-applicatie

8.9 Inkopen

Procesbeschrijving:

Als de subsidieaanvraag is gematcht, dan wordt automatisch een bestelaanvraag

gestuurd aan PeopleSoft. PeopleSoft ontvangt de bestelaanvraag en verstuurt een

inkooporder naar de opleider met een beschikkingsnummer. Dit nummer vermeldt

de opleider op zijn e-factuur die hij verstuurt naar de eFacturatie-voorziening,

zodat er automatisch gematcht kan worden.

Het UWV wil het inkoopproces automatisch laten verlopen, door het UWV-

STAP een bestelaanvraag te laten sturen naar FEZ, zodat zij deze gegevens

kunnen opslaan en converteren naar een inkooporder naar de opleider.

1. Bestelaanvraag

a. Na automatische beschikking dient een bestelaanvraag automatisch te

worden opgesteld en, conform een af te spreken SLA, naar PeopleSoft

gestuurd te worden.

b. De opgestelde bestelaanvraag dient onder meer het opleider-id, het

beschikkingsnummer en de gegevens van de burger te bevatten. De

opleider dient het beschikkingsnummer en de gegevens van de burger op

het bewijs van deelname te vermelden. Op de e-factuur dient de opleider

alleen het beschikkingsnummer te vermelden.

Versie 1.0 pagina 38 van 72

Programma van Eisen STAP-applicatie

8.10 Matchen BvD en beschikken vaststelling

Procesbeschrijving:

Een Bewijs van Deelname moet worden ontvangen en automatisch worden

gematcht met een aanvraag van een burger. Als er geen match plaatsvindt dan

wordt er handmatig gematcht. Vervolgens wordt er gekeken naar de inhoud van de

bewijzen van deelname, zodat gedetermineerd kan worden wat het resultaat van

de scholingsactiviteit is. Wanneer dit is bepaald wordt het mogelijk om de correcte

beschikking hiervoor op te stellen en treedt dus het proces opstellen beschikking in

werking. Als er niet aan de vereisten wordt voldaan, dan wordt er gekeken naar

verwijtbaarheid. Als de opleider verwijtbaar is, dan wordt het subsidiebedrag terug-

en ingevorderd. Als de burger verwijtbaar is dan kan er sprake zijn dat de burger

wordt uitgesloten van toekomstige aanvragen voor een periode van twee jaar. Als

de burger wordt uitgesloten dan zal een beschikking tot uitsluiting worden

gestuurd.

In dit proces wordt er contact opgenomen met de opleider of burger om te

achterhalen wat de oorzaak is van het niet succesvol afronden van de

scholingsactiviteit. Dit is een ad hoc proces, waarna besloten wordt wat het

resultaat is.

Versie 1.0 pagina 39 van 72

Programma van Eisen STAP-applicatie

8.10.1 Matchen Bewijs van Deelname

Het UWV wil door middel van een Bewijs van Deelname het resultaat van

de scholingsactiviteit achterhalen, zodat een beschikking tot vaststelling of

intrekking kan worden gestuurd of er kan worden terug- en ingevorderd.

1. Matchen Bewijs van Deelname

a. Inzage voor de STAP-medewerker in het dossier van de opleiders om de

relevante documenten voor het matchingsproces in te kunnen zien.

b. Automatisch matchen van Bewijs van Deelname aan dossier door middel

van het beschikkingsnummer en de onderliggende gegevens

geëxtraheerd uit de xml/pdf/webform-aanlevering.

c. Niet succesvol geautomatiseerde matches van Bewijs van Deelname

worden aangeboden aan een handmatig beoordelingsproces waarna deze

al of niet alsnog gematched kunnen worden.

d. Gematchte bewijzen van deelname krijgen automatisch een resultaat

toegekend die de vervolgstappen bepaalt.

e. Automatisch opstellen van beschikkingen naar aanleiding van geslaagde

(geautomatiseerde dan wel handmatig) gematchte Bewijzen van

Deelname. Deze beschikkingen ook opslaan in het dossier.

2. Scheiding Bewijs van Deelname

a. Scheiding van bewijzen van deelname met de uitslag “succesvol

afgerond” van de bewijzen van deelname met de uitslag “niet succesvol

afgerond”.

3. Uitkomsten succesvol Bewijs van Deelname

a. In het geval van een Bewijs van Deelname met de uitkomst “succesvol

afgerond” dient een beschikking tot vaststelling opgesteld en verstuurd te

worden (zie paragraaf 8.11).

b. Sluiting van het dossier om de aanvraag af te ronden, waarna archivering

plaatsvindt.

Versie 1.0 pagina 40 van 72

Programma van Eisen STAP-applicatie

4. Uitkomsten niet succesvol Bewijs van Deelname

a. In het geval van bewijzen van deelname met de uitkomst ‘niet succesvol

afgerond door toedoen van de burger’ dient de desbetreffende burger

opgeslagen te kunnen worden in de uitsluitingslijst (hetgeen altijd

gepaard dient te gaan met een ‘handmatige’ beoordeling’).

b. In het geval van bewijzen van deelname met de uitkomst ‘niet succesvol

afgerond door toedoen van de opleider’ dient het terug- en

invorderproces in werking te treden indien de opleider al betaald is.

c. In het geval van bewijzen van deelname met de uitkomst ‘niet succesvol

afgerond door toedoen van de opleider’ dient de burger een beschikking

tot intrekking te ontvangen (zie paragraaf 8.11). Deze beschikking tot

intrekking kan, afhankelijk van de omstandigheden, de burger de

mogelijkheid geven om in het lopende kalenderjaar een nieuwe aanvraag

te doen.

8.10.2 Onderzoeken misstanden

Procesbeschrijving:

In dit proces wordt gekeken naar de verwijtbaarheid van de burger en/of opleider

wanneer uit het Bewijs van Aanmelding is gebleken dat er mogelijke misstanden

zijn. In dat geval wordt er eerst contact op genomen met de burger, zodat deze

ook de mogelijkheid krijgt om zijn kant van het verhaal door te geven. Vervolgens

wordt de misstand gecategoriseerd. Afhankelijk van de uitkomst van deze

categorisatie kan de burger op de uitsluitingslijst geplaatst worden, de opleider

door te geven aan de beheerder van het Scholingsregister, of kan er geen

verwijtbaarheid zijn.

Versie 1.0 pagina 41 van 72

Programma van Eisen STAP-applicatie

Als UWV-STAP medewerker wil ik misstanden onderzoeken, zodat met

zekerheid gezegd kan worden dat de regeling correct wordt nageleefd.

1. Onderzoeken misstanden

a. Mogelijkheid tot telefonisch contact met de burger om te kunnen

verifiëren dat de burger inderdaad verwijtbaar is.

b. Mogelijkheid tot het toekennen van de status “onderzoek” aan dossiers.

c. Registratie van vergaarde informatie uit het onderzoeken van misstanden

in de bijbehorende dossiers via invoer van gegevens en upload van

documenten.

d. Mogelijkheid om burger op de uitsluitingslijst te plaatsten afhankelijk van

de geconstateerde misstanden.

e. Automatisch opstellen van de bijbehorende beschikking.

Versie 1.0 pagina 42 van 72

Programma van Eisen STAP-applicatie

8.11 Opstellen beschikking of brief

Procesbeschrijving:

Afhankelijk van het resultaat wordt er een beschikking opgesteld. Er is hierbij keuze

uit circa 20 aantal sjablonen, waarbij automatisch wordt gekozen welke beschikking

of hieraan gerelateerd document, gestuurd moet worden.

Er worden geautomatiseerd beschikkingen/brievenbestanden aangeleverd aan DIV.

Er zal hier een koppeling gemaakt moeten worden met DIV.

Versie 1.0 pagina 43 van 72

Programma van Eisen STAP-applicatie

Als UWV-STAP medewerker wil ik dat voor verschillende beschikkingen

hetzelfde proces van beschikkingen opstellen wordt gebruikt, ongeacht het

resultaat, zodat uniformiteit wordt gewaarborgd en het automatisch en

parallel kan verlopen.

1. Beschikkingen

a. Automatisch opstellen van verschillende beschikkingen. De trigger moet

voor het soort beschikking (sjabloon) zorgen.

b. Mogelijkheid tot het handmatig aanmaken van een gewijzigde nieuwe

beschikking op basis van een eerder afgegeven beschikking. Dit onder

meer als gevolg van een vraag of een bezwaarprocedure.

c. In het geval van een belastende beschikking dient het proces ‘informeren

belastende beschikking’ in werking te treden.

d. Opgestelde beschikking voorzien van (nader te bepalen) metadata in

PDF/A-formaat, geautomatiseerd aanleveren aan DIV. (zie paragraaf 6.1

en 8.12.1).

e. Toevoeging van facturatiegegevens in het geval van een beschikking tot

terug- en invordering.

f. Opgestelde beschikking of brief automatisch opslaan in dossier.

g. Functionaliteit waarmee sjablonen kunnen worden ingericht, zie

paragraaf 8.1 punt 11.

h. Bij aanmaken dwangbevel worden handmatig gegevens toegevoegd aan

het dwangbevel (bedrag).

Vooralsnog voorzien we de volgende documenten die door het systeem

geleverd moeten worden (nader vast te stellen en uit te werken):

- Ontvangstbevestiging burger

Uitstel nemen beslissing

-

- Opvragen ontbrekende gegevens

- Beschikking tot afwijzing

- Beschikking tot verlening (burger)

- Beschikking tot intrekking burger

- Ontbreken gegevens factuur opleider

- Rappel

- Ontvangstbevestiging Bewijs van Deelname aan opleider

Beschikking tot vaststelling burger

-

- Ontvangstbevestiging bezwaarschrift

- Terug/invorderingsbeschikking (= factuur)

Versie 1.0 pagina 44 van 72

Programma van Eisen STAP-applicatie

8.12 Verzenden en ontvangen via DIV

8.12.1 Verzenden

Het genoemde proces is essentieel voor de uitvoering van de STAP-subsidie, maar

wordt niet in de STAP-applicatie uitgevoerd. Hieronder de uitleg van het proces.

Van belang is hier wel de bestands/gegevensaanlevering (bestaande uit

documenten bestaan uit documenten in PDF/A-formaat) aan DIV zoals beschreven

in paragraaf 8.1, paragrraf 6.1 onder ‘Koppeling met Documentaire Informatie

Voorziening (DIV) van UWV’ en de in de Non Functional Requirements.

Procesbeschrijving:

Afhankelijk van het resultaat wordt er een beschikking tot vaststelling of

beschikking tot intrekking naar de burger (en opleider) verstuurd door DIV en is het

proces afgerond. Daarnaast wordt ook andere correspondentie/brieven vanuit de

Stap-applicatie aangemaakt en ter verzending aangeboden. Dit proces wordt

uitgevoerd door DIV.

8.12.2 Ontvangen

Als UWV-STAP wil ik (centraal) bij DIV ingekomen post gedigitaliseerd en

voorzien van metadata ontvangen, deze kunnen oppakken vanuit een

separate werkbaken kunnen koppelen aan een bestaand of nieuw dossier.

Procesbeschrijving:

Ondanks het streven zo veel als mogelijk een gedigitaliseerd proces in te richten en

af te dwingen, kan niet worden voorkomen dat burgers papieren stukken opsturen

naar de verschillende postbussen van UWV. Dergelijke stukken worden bij de

centrale postverwerking van de Documentaire Informatie Voorziening (DIV)

Versie 1.0 pagina 45 van 72

Programma van Eisen STAP-applicatie

geïdentificeerd als zijnde STAP-post en vervolgens gedigitaliseerd en voorzien van

metadata aangeboden aan de STAP-applicatie (zie ‘Koppeling met Documentaire

Informatie Voorziening’ in paragraaf 6.1).

De STAP-applicatie dient deze gedigitaliseerde documenten te ontvangen en in een

werkbak aan te bieden aan (een separate rol van) de STAP-medewerker. Deze

STAP-medewerker moet een gedigitaliseerd documenten uit de werkbak aan het

bijbehorende dossier kunnen toevoegen dan wel via de ‘zij-invoer’ een aanvraag of

een Bezwaar-en beroepscasus kunnen starten waarvan het document onderdeel uit

gaat maken.

Bij het toevoegen van het document aan een dossier of het starten van een nieuw

dossier, dienen de metadata van het document te kunnen worden hernoemd.

1. Ontvangen en verwerken inkomende post

a. DIV dient STAP-post gedigitaliseerd en voorzien van (nader te bepalen)

metadata in PDF/A-formaat door te sturen naar de STAP-Unit.

b. Presenteren van deze digitale poststukken en relevante metadata in een

werkbak met specifieke autorisatie.

c. Kunnen koppelen (‘verhuizen’) van de digitale poststukken aan een

bestaand of nieuw aan te maken dossier (kan ook een B&B-dossier zijn).

d. Nader te bepalen hoe signalering plaatsvindt aan de medewerker die de

verdere afhandeling moet uitvoeren.

Versie 1.0 pagina 46 van 72

Programma van Eisen STAP-applicatie

8.13 Terug- en invorderen

Het genoemde proces is essentieel voor de uitvoering van de STAP-subsidie, maar

wordt slechts gedeeltelijk in de STAP-applicatie uitgevoerd. De STAP-applicatie

dient klantgegevens te registreren, een beschikking tot terug- en invorderen (incl.

factuur) aan te maken en deze naar DIV te kunnen sturen. Daarna worden de

vervolgstappen in Peoplesoft verder genomen met betrekking tot invorderen.

Hieronder de uitleg van de processen die in de STAP-applicatie dienen te gebeuren,

namelijk het aanmaken factuur (beschikking), ophalen klantgegevens en het

updaten dossier.

8.13.1 Ophalen opleidergegevens

Procesbeschrijving

Om de beschikking tot terug- en invordering (is het factuur) samen te kunnen

stellen, moeten ook klantgegevens beschikbaar zijn. Deze gegevens worden uit het

Scholingsregister gehaald en moeten in Peoplesoft terecht komen. Voordat deze

gegevens worden opgehaald moet er worden gecontroleerd of de opleider al

uitbetaald is. Mocht dit niet het geval zijn, dan wordt de melding uitgeschakeld en

wordt de inkooporder ingetrokken. Als de opleider nog niet heeft betaald, dan moet

er gekeken worden of de opleider al als debiteur in Peoplesoft staat. Als deze nog

niet als debiteur in Peoplesoft staat moet de debiteur handmatig worden

opgevoerd, namelijk door het omzetten van een crediteur naar debiteur met

aanvullende gegevens.

Als UWV-STAP wil ik de subsidie kunnen terug- en invorderen bij de

opleider en kunnen terug- en invorderen bij de burger wanneer zij zich

niet aan hun verplichtingen houden, zodat we geld kunnen terug- en

invorderen bij diegene die de regeling niet correct heeft gebruikt.

1. Ophalen debiteurgegevens

a. Handmatig kunnen controleren of de partij waarop ingevorderd dient te

worden daadwerkelijk een uitbetaling van STAP heeft ontvangen (geen

koppeling vereist).

b. Handmatig kunnen tot opzoeken of debiteur al in Peoplesoft staat (geen

koppeling vereist).

Versie 1.0 pagina 47 van 72

Programma van Eisen STAP-applicatie

c. Indien de beoogde debiteur nog niet in Peoplesoft staat deze als crediteur

kunnen selecteren.

d. Indien de beoogde debiteur nog niet in Peoplesoft staat een kenmerk te

plaatsen bij de crediteur.

e. Indien de beoogde debiteur nog niet in Peoplesoft staat bij de crediteur

aanvullende gegevens kunnen opvoeren.

f. Indien de beoogde debiteur nog niet in Peoplesoft staat de debiteur alsnog

in Peoplesoft zetten.

8.13.2 Aanmaken beschikking- en facturatiegegevens

Procesbeschrijving:

Zodra een terug- en invordering vereist is krijgt een UWV-STAP terug- en

invordermedewerker een signaal waardoor hij op de hoogte wordt gesteld dat een

beschikking/factuur tot terug- en invordering vereist is. Deze wordt vervolgens

opgemaakt met de gegevens die tijdens het proces “ophalen scholingsregister” zijn

opgehaald. Hierbij wordt een betalingskenmerk toegevoegd alvorens hij wordt

gekoppeld aan de bijbehorende beschikking tot terug- en invordering en gestuurd

kan worden conform het proces “opstellen beschikking”.

1. Aanmaken facturatiegegevens

a. Signaal naar de UWV-STAP Invordermedewerker dat de opmaak van een

factuur vereist is.

b. Klantgegevens ophalen en gebruiken voor aanmaak van factuur.

c. Opstelling van een beschikking tot terugvordering conform het proces

“opstellen beschikking” met opname van factuur(betalingskenmerk).

d. Koppeling van de STAP-applicatie (batch) met Peoplesoft Facturering. Dat

vervolgens een debiteurenpost aanmaakt in Peoplesoft debiteuren,

waarmee het op de hoogte gesteld wordt van de nieuwe terug- en

invorderingen.

e. Bij een onterecht gebleken terug/invordering (debetfactuur) moet deze

ook ingetrokken kunnen worden: er moet een creditfactuur naar de

opleider en PeopleSoft gestuurd kunnen worden.

Versie 1.0 pagina 48 van 72

Programma van Eisen STAP-applicatie

8.14 Afhandelen Bezwaar door STAP–medewerker

Procesbeschrijving:

Een burger of opleider logt in op het burger/Opleidersportaal, waarna hij klikt op

bezwaarschrift en aangeeft op welke beschikking hij bezwaar wil maken. Hij vult

het formulier in en dient daarmee zijn bezwaar in.

In het Medewerkersportaal wordt ingelogd, waarna gegevens worden opgehaald

samen met een ingevuld bezwaarschrift.

Dit gebeurt in de STAP-applicatie, waarin eerst STAP-medewerkers de

voorprocedure uitvoeren door eigen fouten te corrigeren.

8.14.1 Indienen bezwaar digitaal

Versie 1.0 pagina 49 van 72

Programma van Eisen STAP-applicatie

8.14.2 Indienen bezwaar fysiek

Het UWV-STAP wil de bezwaarschiften zoveel mogelijk zelf oppakken om

de afdeling Bezwaar en Beroep zo min mogelijk te belasten.

UWV-STAP wil de communicatie met B&B gestructureerd afbakenen, zodat

de wisselwerking tussen UWV-STAP en B&B snel en efficiënt verloopt.

1. Indienen bezwaar

a. Indienen bezwaren via Burgerportaal en Opleidersportaal middels

button/link vanuit de betreffende beschikking naar separaat webformulier

met verplichte en optionele velden en met uploadfunctionaliteit voor het

bijvoegen van stukken. Dit webformulier is onderdeel van de STAP-

applicatie.

b. In de bezwaarfunctionaliteit moet aangegeven worden welk dossier en

over welke bijbehorende beschikking bezwaar wordt gemaakt, aangezien

op meerdere beschikkingen bezwaar kan worden gemaakt.

c. Uploaden van bewijsstuk toevoegen bij bezwaar.

d. Bezwaren aan dossiers toevoegen.

e. Automatisch bij ontvangen bezwaar de einddatum van reactie bezwaar

toevoegen.

Versie 1.0 pagina 50 van 72

Programma van Eisen STAP-applicatie

8.14.3 Behandelen bezwaar

8.14.4 Behandelen voorprocedure bezwaar STAP

Versie 1.0 pagina 51 van 72

Programma van Eisen STAP-applicatie

1. Ontvangst bezwaar en check op evidente fout

a. Inlogmogelijkheid voor STAP-B&B-medewerkers door middel van

## ADFS/SSO.

b. Ontvangen bezwaren die via de STAP-portalen/webforms zijn ingediend.

c. Ontvangen bezwaren via door DIV gedigitaliseerd post (zie paragraaf

8.12.2).

d. Mogelijkheid tot het uploaden van fysieke bezwaren door de UWV-

Adviseur.

e. Geautomatiseerd plaatsen van alle (gedigitaliseerde) bezwaren in

algemene werkbak ‘voorprocedure bezwaar’, welke toereikende

zoek/sorteermogelijkheden moet hebben.

f. Mogelijkheid tot invoeren van de benodigde (meta)gegevens bij

ontvangst van door DIV en UWV-Adviseur gedigitaliseerde bezwaren.

g. Routeren bezwaar uit werkbak ‘voorprocedure bezwaar’ naar specifieke

STAP-medewerker.

h. Inzicht hebben in welke medewerker welke bezwaren afhandelt.

i. Afsluiten ‘voorprocedure bezwaar’ met constatering evidente fout en

wijziging beschikking (zie paragraaf 8.11).

j. Afsluiten ‘voorprocedure bezwaar’ met geen evidente fout en doorsturen

naar (werkbak van) STA-B&B-Medewerker.

k. Bewaking/signalering werkvoorraad ‘voorprocedure bezwaar’ op

afhandeltermijn langer dan twee werkdagen

l. Bezwaren kunnen zoeken op basis van registratienummer, (inlog)Naam

behandelaar, signaal datum, signaal reden, wettelijke einddatum, status,

BSN, type zaak.

8.14.5 Registreren en termijnbewaking

Versie 1.0 pagina 52 van 72

Programma van Eisen STAP-applicatie

Complexe bezwaren worden doorgezet naar een STAP-B&B-medewerker die deze

bewaren in de STAP-applicatie afhandelt met zo min mogelijk functionaliteiten).

Het proces van bezwaar en beroep bestaat uit drie functionaliteiten in het systeem,

namelijk uploaden, downloaden en registreren. In dit hoofdstuk wordt deze

functionaliteit kernachtig besproken. Een verdieping hiervan met de bijbehorende

processtappen is te vinden in bijlage 2. Hier is tevens een impressie van de

registratievelden in de STAP- en STAP-B&B-medewerkersvensters, de indeling van

de STAP-B&B-werkbakjes en de briefsjablonen te vinden.

a. Er dienen twee eenvoudige termijnbewakingen te worden ingericht: Die

voor de voorbehandeling door de STAP-medewerker en die van de

afhandeling door de STAP-B&B-medewerker. De applicatie dient een

instelbare periode voorafgaand aan de termijnafloop een signalering aan

de betreffende medewerker te geven dat de termijn bijna afloopt.

b. Aan beide processen/rollen wordt één registratievenster geboden in het

STAP-portaal met (een beperkt) aantal velden zoals vrije

(notitie)velden, selectiemenu’s/pull-downs, vinkboxjes, etc. Dit zonder

verdere achterliggende business rules/algoritmes en achterliggende

workflows (met uitzondering van twee basale businessrules t.b.v.

termijnbewaking).

c. Het moet mogelijk zijn documenten te uploaden welke daarmee

onderdeel uitmaken van het klant-/bezwaardossier.

d. Vanuit de verschillende registratievensters moeten brieven aangemaakt

kunnen worden (circa 10 sjablonen, aanvullend op de in paragraaf 8.11

genoemde sjablonen). Zie paragraaf 8.1 punt 11.

Versie 1.0 pagina 53 van 72

Programma van Eisen STAP-applicatie

8.15 Vraagafhandelen

8.15.1 Vraagafhandelen Eerste lijn

Het genoemde proces is essentieel voor de uitvoering van de STAP-subsidie, maar

wordt niet in de STAP-applicatie uitgevoerd. Hieronder de uitleg van het proces.

Vraagafhandelen (telefonisch eerste lijn).

Procesbeschrijving:

Er komt een vraag binnen bij de eerstelijns medewerker. Als de vraag wordt

beantwoord wordt deze afgerond. Als de vraag niet kan worden beantwoord wordt

er een terugbelverzoek ingediend bij de tweedelijns STAP-medewerker die het

dossier in behandeling heeft (gehad). Daarna kan de tweedelijns medewerker op

diens eigen moment de vraag oppakken en beantwoorden. Op deze twee manieren

kan de vraag afgerond worden.

8.15.2 Vraagafhandelen Tweede lijn

Procesbeschrijving:

In dit proces ontvangen tweedelijns medewerkers binnen de STAP-unit een

terugbelverzoek van het Klantcontact Center. De STAP-medewerker gaat met dit

terugbelverzoek aan de slag en zoekt een antwoord bij de vraag, waarna hij dit

telefonisch terugkoppelt aan de burger.

Het UWV wil tweedelijns vragen via een terugbelverzoek ontvangen, zodat

vragen gereguleerd beantwoord kunnen worden en burgers geholpen

kunnen worden.

Versie 1.0 pagina 54 van 72

Programma van Eisen STAP-applicatie

1. Webformulier

a. Webformulier op Voorportaal (met ingave van indienergegevens),

Opleidersportaal en Burgerportaal, ter indienen van vragen.

b. Het webformulier moet verplicht een e-mailadres bevatten, zodat de

vraag/klacht teruggekoppeld kan worden aan de burger/opleider.

2. De tweede lijn

a. Ontvangen van gestandaardiseerd terugbelverzoek van de eerstelijns

medewerker met de naam van de klant, de vraag van de klant, het

telefoonnummer en de bereikbaarheid van de klant. Dit via een via

een koppeling met een nader te bepalen klantcontactsysteem.

b. Mogelijkheid tot registreren van toelichting/resultaat in de STAP-

applicatie en terugkoppeling van deze gegevens aan de eerstelijns

medewerker via een koppeling met een nader te bepalen

klantcontactsysteem.

Versie 1.0 pagina 55 van 72

Programma van Eisen STAP-applicatie

8.16 Beheren uitsluitingslijst

In de STAP-applicatie dient een uitsluitingslijst beheerd te worden. Hier

worden burgers toegevoegd die voor max. 2 jaar worden uitgesloten van

de regeling en daarna weer een subsidie mogen aanvragen.

1. Beheren uitsluitingslijst

a. Beheren van een uitsluitingslijst door een separate autorisatierol.

b. Inzage van de uitsluitingslijst.

c. Handmatig kunnen toevoegen en verwijderen van burgers aan de

uitsluitingslijst.

d. Automatisch verwijderen van burgers op de uitsluitingslijst als een

instelbare maximumtermijn is overschreden. De maximumtermijn

moet default in te stellen zijn (vooralsnog 2 jaar) en bij opvoer

eventueel aanpasbaar zijn voor de betreffende burger.

Versie 1.0 pagina 56 van 72

Programma van Eisen STAP-applicatie

8.17 Sturing en Verantwoording

Als UWV STAP wil ik informatie verzamelen om te kunnen sturen op en

verantwoording af te leggen over de processen die betrekken hebben op

de STAP-subsidieregeling, zodat de uitvoering van de STAP-regeling met

behulp van deze informatie o.a. beoordeeld kan worden op effectiviteit en

efficiëntie.

8.17.1 Verantwoordingsniveau’s

Om te kunnen sturen en verantwoorden dient er op verschillende manieren

gegevens/informatie vanuit de applicatie beschikbaar te zijn:

Operationeel

Rapportages verbonden aan het operationele (dagelijkse) proces worden geleverd

door de applicatie.

De rapportages moeten eenvoudig aangepast kunnen worden.

- De rapportages moeten filters bevatten die eenvoudig aanpasbaar en

uitbreidbaar zijn.

- De rapportages bevatten detailniveau informatie die ondersteunend zijn voor het

primaire proces.

- De rapportages bieden de mogelijkheid om van een hoger aggregatieniveau

door te drillen naar detailniveau.

- De rapportages zijn realtime beschikbaar in het Medewerkersportaal, op basis

van rol/autorisatie.

- De rapportages zijn beveiligd op functie, rol en naam.

De vraag aan de Leverancier is hoe zij bovenstaande kan leveren en uit te leggen

hoe ze dit doet.

Tactisch

Op tactisch niveau wil UWV de stuurrapportages zelf kunnen faciliteren in de vorm

van dashboards.

- De database van STAP is toegankelijk voor een rechtstreekse data-connectie.

- De dashboards kennen een beveiligingsniveau op functie, rol en naam.

- De dashboards bestaan uit (K)PI’s welke samengesteld kunnen worden in

de vorm van business rules en normering door het UWV.

- De (K)PI’s kennen een weergave in moderne vormen zoals stoplichten en

grafieken.

- De (K)PI’s geven de mogelijkheid om de KPI als startpunt te gebruiken voor

analyse naar oorzaken. De actualiteit is voor de dashboards op dag-niveau en

voor de analyse op realtime-/dag-niveau.

Versie 1.0 pagina 57 van 72

Programma van Eisen STAP-applicatie

Strategisch

Op strategisch niveau (verantwoording) wil UWV de informatieproducten zelf

kunnen faciliteren.

- De leverancier stelt hiervoor het functioneel en technisch datamodel

beschikbaar.

- Bestandlevering (en eventuele voorbewerking van de data), dan wel de STAP-

applicatie toegankelijk maken voor een ETL-tool, is afhankelijk van de nog te

maken keuze van de in te zetten BI-tooling. Aan de Leverancier wordt gevraagd

aan te geven welke wijze van bestandslevering/openstelling zij kunnen

ondersteunen..

8.17.2 Process mining

UWV overweegt process mining toe te passen.

Om de processen van de STAP-regeling te kunnen volgen door middel van process

mining is het van belang dat de processtappen gelogd worden. De

minimumvereisten zijn als volgt:

1. Minimale datavereisten:

a. Case ID: een nummer of code die voor de burger gedurende de hele

STAP-aanvraag hetzelfde blijft. Bijvoorbeeld BSN-nummer of een

Aanvraagnummer.

b. Activiteiten: de daadwerkelijk uitgevoerde stappen. Bijvoorbeeld de

verschillende statussen van aanvraag tot uitbetaling of de afdelingen die

de aanvragen behandelen.

c. Timestamp: een datumregistratie van het moment dat de activiteit is

uitgevoerd. Bij voorkeur een start- en einddatum van de activiteit.

2. De historie van de aanvraag moet bewaard worden. Indien een aanvraag van

status verandert dienen ook de voorheen doorlopen statussen bewaard te

worden in de database.

3. Aangezien de aanvraag door meerdere UWV systemen zal lopen, is het nodig

dat de Case ID gelijk is aan de Case ID uit de andere systemen. Met andere

woorden er moet een volgnummer zijn van de burger die in ieder systeem gelijk

is.

4. Om de process mining analyse waardevol te maken, dienen naast de minimale

datavereisten ook extra kenmerken (attributen) bewaard te worden. Deze extra

attributen kunnen pas gedefinieerd worden wanneer het proces meer vorm

krijgt. Voorbeelden van attributen zijn: kantoor, afdeling, bedrag subsidie,

woonplaats burger, instituut opleiding, en naam opleiding.

5. De data set moet in Excel of CSV bestand kunnen worden opgeleverd en

aanvullend moet de STAP-applicatie toegankelijk zijn voor een ETL-tool. Dit is

afhankelijk van de nog te maken keuze van de in te zetten BI-tooling. Aan de

Leverancier wordt gevraagd aan te geven welke wijze van

bestandslevering/openstelling zij kunnen ondersteunen.

Versie 1.0 pagina 58 van 72

Programma van Eisen STAP-applicatie

8.17.3 Sturingsinformatie

UWV verwacht van de STAP-applicatie dat de data op een manier wordt opgeslagen

zodat rapportage op de drie niveaus Operationeel, Tactisch en Strategisch

ondersteund wordt.

De database zal hiervoor aan de eisen van een moderne database moeten voldoen

en een datamodel zowel functioneel, als technisch ter beschikking stellen aan het

UWV. Het UWV zal op basis van de wet, het STAP-proces en de verantwoording

naar de wetgever de informatiebehoefte gaan bepalen. De informatiebehoefte zal

eisen stellen aan het datamodel in de manier waarop data wordt opgeslagen en

beschikbaar gesteld wordt. Voorbeelden van deze sturingsinformatie-eisen en de

basale informatiebehoefte is hierna opgenomen, maar deze lijst is niet uitputtend:

Subsidieaanvragen

a. Aantal subsidie aanvragen worden door middel van timestamps

inzichtelijk gemaakt.

b. Aantal verleende/afgewezen subsidieaanvragen worden inzichtelijk

gemaakt.

Persoonsgegevens

a. Bij het indienen van de aanvraag worden verschillende (niet verplichte)

vragen aan de burger gesteld, zoals de hoogst genoten opleiding, huidige

arbeidsmarktpositie, aard van huidige werkzaamheden, welk jaar van de

opleiding. Deze invoer wordt bij dossier vastgelegd.

Op basis hiervan moeten overzichten op voornoemde aspecten kunnen

worden gegenereerd (bijvoorbeeld indeling aanvragen over een bepaalde

periode naar hoogst genoten opleiding).

Aanvraag beschikken

a. Het systeem moet bijhouden hoeveel aanvragen handmatig en

automatisch worden gematcht.

Afbreken scholingsactiviteit

a. Werkvoorraden moeten worden bijgehouden gericht op intrekkingen

en annuleringen van scholingsactiviteiten.

Rappelleren

a. Inzichtelijk hebben van welke opleiders geen/of niet op tijd een Bewijs

van Deelname aanleveren.

Vraag afhandelen

a. De data die gegenereerd wordt uit de telefoongesprekken (eerste lijns)

dienen te kunnen worden gecategoriseerd (bijvoorbeeld via een

vinkbox of pull-down door de vraagafhandelaar te selecteren) op basis

waarvan overzichten moeten kunnen worden gegenereerd.

b. Bijhouden welke telefoontjes verkeerd zijn verbonden en moeten

worden doorgeschakeld naar K&S en omgedraaid.

Versie 1.0 pagina 59 van 72

Programma van Eisen STAP-applicatie

8.18 Logging en Monitoring

Alle toegangen tot de STAP-applicatie (registraties en raadplegingen) dienen



zodanig te worden gelogd dat auditrails kunnen worden gegenereerd waarmee

inzichtelijk wordt wie wanneer toegang heeft gehad tot welke gegevens (dit

geldt zowel voor de burger, als de opleider, als de medewerker als de

functioneel beheer).

Dit zowel vanuit de casus bezien (welke medewerkers hebben wanneer een



bepaalde casus ingezien/bewerkt en welke gegevens betreft dit) als vanuit de

medewerkers (welke casussen heeft een medewerker in een op te geven periode

ingezien/bewerkt en welke gegevens betreft dit).

Deze logginggegevens/ audittrails dienen inzichtelijk gemaakt te kunnen worden



in een dashboard. En dienen via een separate autorisatie/rol opgevraagd te

kunnen worden.

Versie 1.0 pagina 60 van 72

Programma van Eisen STAP-applicatie

Bijlage 1 : User stories Koppelingen Scholingsregister

We hebben de volgende userstories met DUO gedeeld voor de specifieke

koppelvlakken met het Scholingsregister, als voorbeeld is aanvullend een request-

reply uitwerking opgenomen. De nummering die hierbij is aangehouden, is conform

de huidige nummering die gehanteerd wordt in de afstemming met SZW en DUO

Koppelvlak 5: Inzage via Voorportaal

• Ik wil als burger trapsgewijs kunnen zoeken naar / filteren op

scholingsactiviteiten waarvoor ik STAP-subsidie kan krijgen en die voor mij

interessant zijn op basis van diverse zoeksleutels (vakgebied/sector,

locatie/regio, opleidingsniveau, opleider, opleiding, scholingsactiviteit, prijs

(≤€1000/>€1000), startdatum en duur), zodat ik de

opleiders/opleidingen/scholingsactiviteiten zie die aan de ingevoerde zoekcriteria

voldoen.

• Ik wil als burger de contactgegevens (min. hyperlink naar de website) van de

opleiders zien die aan mijn wensen voldoen, zodat ik contact met hen kan

zoeken.

Ik wil als STAP de burger uitsluitend scholingsactiviteiten tonen uit het

•

Scholingsregister die in de komende 12 maanden gaan starten, zodat STAP in de

presentatie aan de burger kan tonen in welke aanvraagperiode zij de STAP-

subsidie moeten aanvragen.

• Ik wil als STAP de burger uitsluitend scholingsactiviteiten tonen die voor hun

leeftijdscategorie (18-30 of 30-AOW gerechtigde leeftijd) gelden, zodat de burger

geen scholingsactiviteiten te zien krijgt die niet van toepassing zijn.

• Ik wil als STAP uitsluitend scholingsactiviteiten ontvangen die voorzien zijn van

volledige en gevalideerde gegevens (min. startdatum, einddatum, locatie, STAP-

subsidiebedrag, KvK-nummer IBAN), zodat de burger geen scholingsactiviteiten

te zien krijgt die in het STAP-proces niet verwerkt kunnen worden.

• Ik wil als STAP gepagineerd de scholingsactiviteiten ontvangen (max 10-15

regels per keer), zodat we dit aan de burger een overzichtelijk geheel kunnen

tonen.

Versie 1.0 pagina 61 van 72

Programma van Eisen STAP-applicatie

Koppelvlak 9: Selectie scholingsactiviteit via Voorportaal

• Ik wil als burger snel en effectief (selectie opleider -> opleiding ->

scholingsactiviteit) de scholingsactiviteit kunnen selecteren waarvoor ik een

STAP-aanvraag wil doen, zodat ik snel en effectief mijn aanvraag kan afronden.

• Ik wil al burger de scholingsactiviteit kunnen terugvinden door het gebruik van

een unieke code per scholingsactiviteit, zodat ik snel en effectief mijn aanvraag

kan afronden.

Ik wil als burger dezelfde benaming van de scholingsactiviteit te zien krijgen

•

zoals deze in het BvA staat, zodat ik eenvoudig de juiste scholingsactiviteit kan

kiezen.

• Ik wil als STAP de burger uitsluitend scholingsactiviteit tonen uit het

Scholingsregister die in de komende 3 maanden gaan starten, zodat de burger

geen scholingsactiviteiten te zien krijgt die niet van toepassing zijn.

• Ik wil als STAP de burger uitsluitend scholingsactiviteiten tonen die voor hun

leeftijdscategorie (18-30 of 30-AOW gerechtigde leeftijd) gelden, zodat de burger

geen scholingsactiviteiten te zien krijgt die niet van toepassing zijn.

• Ik wil als STAP uitsluitend scholingsactiviteiten ontvangen die voorzien zijn van

volledige en gevalideerde gegevens (min. startdatum, einddatum, locatie, STAP-

subsidiebedrag, KvK-nummer, IBAN), zodat de burger geen scholingsactiviteiten

te zien krijgt die in het STAP-proces niet verwerkt kunnen worden.

• Ik wil als STAP bij de keuze uit het Scholingsregister van de burger alle gegevens

van de desbetreffende keuze overnemen, zodat deze gegevens in de aanvraag

worden meegenomen.

Ik wil als STAP gepagineerd de scholingsactiviteiten ontvangen (max 10-15

•

regels per keer), zodat we dit aan de burger een overzichtelijk geheel kunnen

tonen.

Versie 1.0 pagina 62 van 72

Programma van Eisen STAP-applicatie

Koppelvlak 15: : Inzage en ‘tijdreizen’ via Medewerkersportaal

• Ik wil als STAP-medewerker alle gegevens uit het Scholingsregister kunnen

achterhalen over opleider, opleiding en scholingsactiviteit, zodat ik goed kan

reageren op vragen en/of problemen.

• Ik wil als STAP-medewerker kunnen tijdreizen in het Scholingsregister, zodat ik

kan achterhalen welke mutaties er bij de opleider/opleiding/scholingsactiviteit

hebben plaatsgevonden.

Versie 1.0 pagina 63 van 72

Programma van Eisen STAP-applicatie

## Bijlage 2 : Bezwaar en Beroep

2.1 Procesverloop B&B afhandeling

1) Voorbehandelen bezwaar

a. Inzage in onderliggende stukken primaire proces (STAP).

b. Inzage in gegevens STAP-applicatie.

c. Registratie primaire medewerker beslissing indien van toepassing bij

bezwaarproces. Alle informatie m.b.t. primaire beslissing moet bij

bezwaarprocedure beschikbaar/ raadpleegbaar zijn.

d. Registratie datum primaire beslissing onderliggend aan bezwaar

Deze datum moet in bezwaarproces vanuit primaire beslissingsproces

overgenomen worden. Kan niet in een Excel vastgelegd worden. Is absoluut

noodzakelijk i.v.m. berekening wettelijke termijn.

e. Registratie ontvangstdatum bezwaar

Registratie datering bezwaar vanwege de brieven.

f. Registratie wel/geen verzuim en soort verzuim (bezwaar niet volledig).

g. Brief ter correctie van verzuim aanmaken en versturen.

h. Registratie verzuim hersteld j/n en datum waarop verzuim is hersteld.

i. Brief Beslissing op bezwaar niet-ontvankelijk als verzuim niet (tijdig) is hersteld.

j. Bewaken herstel verzuim (4 weken).

k. Verlengen periode herstel verzuim.

l. Registreren soort bezwaar (code geschil).

m. Registreren van gemachtigde.

n. Postadres brieven/beschikkingen wijzigen in die van de gemachtigde. Gegevens

gemachtigde moeten naast de gegevens indiener vastgelegd worden en

beschikbaar blijven. Zo wordt een beslissing op bezwaar geadresseerd aan

indiener, maar met een begeleidende brief gestuurd naar gemachtigde.

o. Aanmaken en versturen van ontvangstbevestiging bezwaar.

p. Vastleggen en schriftelijk bevestigen telefonische afspraken.

q. Vastleggen termijn afhandeling bezwaar, rekening houdend met datum opheffing

verzuim.

2) Afhandelen bezwaar

a. Klant wil wel/geen hoorzitting plannen.

b. Datum, tijd en locatie hoorzitting.

c. Brief uitnodiging hoorzitting.

d. Hoorzitting wel/niet gehouden.

e. Reden hoorzitting niet gehouden.

f. Verslag hoorzitting

g. Wel/geen aanvullende informatie opvragen.

h. Brief voor aanvragen aanvullende informatie aanmaken en versturen.

i. Rappelbrief voor aanvragen aanvullende informatie aanmaken en versturen.

j. Aanvullende informatie wel/niet ontvangen.

k. Bewaken termijn aanvullende informatie ontvangen.

l. Opstellen en versturen beschikking op bezwaar (BOB).

m. Registreren oordeel BOB (gelijk, niet gelijk, niet ontvankelijk gegrond, ongegrond,

niet-ontvankelijk) en verzenddatum.

n. Informeren belanghebbende(n).

o. Informeren STAP-uitvoering bij gegrond bezwaar.

p. Verdagen bezwaartermijn met standaard 6 weken.

q. Opstellen en versturen brief verdaging bezwaar beslistermijn.

r. Verdagen bezwaar beslistermijn met toestemming indiener.

s. Opstellen en versturen brief verdaging bezwaar beslistermijn met toestemming

indiener.

t. Bewaken en signaleren verstrijken bezwaar beslistermijn inclusief

verdagingstermijn

Versie 1.0 pagina 64 van 72

Programma van Eisen STAP-applicatie

3) Afhandelen ingebrekestelling (niet voldaan aan bezwaar beslistermijn)

a. Ontvangst en registeren ingebrekestelling.

b. In gebrekestelling routeren naar behandelend B&B medewerker.

c. Registeren resultaat beoordeling geldigheid ingebrekestelling.

d. Aanmaken en versturen ontvangstbevestiging ingebrekestelling met afwijzing.

e. Aanmaken en versturen ontvangstbevestiging ingebrekestelling met toekenning

dwangsom.

f. Betaalbaar stellen dwangsom.

g. Registeren termijn afhandeling ingebrekestelling.

h. Bewaken en signaleren bereiken einde termijn afhandeling ingebrekestelling.

4) Afhandelen beroep – Medewerkersportaal

a. Ontvangst en registratie kennisgeving van beroep of beroepsschrift, opnemen

nieuw beroepsproces aan werkvoorraad. Vastgelegd moet worden of het een BR of

HB zaak betreft. Die zijn grotendeels gelijk.

Een dergelijk proces moet meer dan 1x vastgelegd kunnen worden.

Ook moet vastgelegd worden wie BR/HB heeft aangespannen bij welke instantie

en met welk procedurenummer.

b. Registratie en bewaking termijn opstellen verweerschrift. Bij HB verweerschrift

en/of Beroepschrift. UWV kan uitstel aanvragen.

c. Opstellen en verzenden verweerschrift. Alleen bij BR. Bij HB kunnen zowel

verweerschrift en beroepschrift gemaakt worden (beroepschrift als UWV in HB

gaat).

d. Wel/geen hoger beroep ingesteld. HB instellen wordt pas aan het einde van de

beroepszaak beoordeeld.

e. Registratie partijen die hoger beroep hebben ingesteld.

f. Toewijzen beroepsproces aan B&B medewerker. Dit moet eerder. Zolang er geen

medewerker is toegewezen, wordt er ook geen beroepschrift/ verweerschrift

gemaakt.

g. Toewijzen beroepsproces aan B&B medewerker. Dit moet eerder. Zolang er geen

medewerker is toegewezen, wordt er ook geen beroepschrift/ verweerschrift

gemaakt.

h. Registratie datum, tijd, locatie, naam rechter van de zitting

i. Wel/geen zitting gehouden registreren.

j. Opstellen verslag zitting.

k. Registreren betrokken B&B medewerkers: zaakeigenaar, administratief

medewerker, zittingjurist. Een zittingjurist wordt past vastgelegd zodra er een

uitnodiging voor een zitting is ontvangen.

l. Wel/Geen vereenvoudigde uitspraak; soort vereenvoudigde uitspraak.

m. Wel/Geen registeren Normale uitspraak.

n. Wel/Geen registeren hoger beroep.

o. Wel/Niet aanpassen beslissing o.b.v. uitspraak, zo nodig doorgeven aan primaire

uitvoering.

p. Betaalbaar stellen van proceskosten.

Versie 1.0 pagina 65 van 72

Programma van Eisen STAP-applicatie

2.2 Inhoud registratievelden

Randvoorwaarden:

Medewerkers B&B hebben toegang tot alle

gegevens die geleid hebben tot de primaire

1 beslissing.

Hieronder valt specifiek de stand van het

budget op het moment van aanvragen subsidie

2 (voorintake formulier)

Medewerkers B&B hebben toegang tot het

elektronisch archief van STAP (lezen en

3 uploaden)

Aandachtspunten

Dus het systeem STAP, alle opgeslagen

Excel termijn bepaling

-

documenten, alle systemen waarmee STAP

- Apart tab met paar brieven

4 linkt.

- Andere brieven

Telefoon notitie, op te nemen in dossier

-

- Inrichting werkbak(ken)

- Beschrijving proces + wat waar hoe te doen

Afhandelen bezwaar

Signalen

Vast te leggen gegevens door STAP

- Management informatie

Naam Soort Bron Verplicht

- Hoe werken de brieven vanuit STAP applicatie

Registratienummer

- Bezwaren kunnen ook op pwebserviceer binnenkomen

Datum primaire beslissing Datum Appl STAP Ja

- Kunnen burgers zelf documenten uploaden in de

Datum ontvangst bezwaarschrift Datum Portal STAP Ja

- STAP B&B applicatie?

Naam medewerker STAP Keuzelijst Appl STAP Ja - Alle rubrieken moeten overschreven kunnen worden

Bijvoorbeeld

Ingetrokken, Gegrond,

Ongegrond, doorgezet

Beslissing STAP medewerker Keuzelijst naar B&B

Datum doorsturen naar B&B Datum Appl STAP Geautomatiseerd

Versie 1.0 pagina 66 van 72

Programma van Eisen STAP-applicatie

Vast te leggen gegevens door B&B

Naam Soort Bron Verplicht

Registratienummer STAP Ja

Datum primaire beslissing Datum Appl STAP Ja

Datum ontvangst bezwaarschrift Datum Portal STAP Ja

Wettelijke einddatum Datum Ja

Naam medewerker B&B Keuzelijst Appl STAP Ja Gevuld vanuit autorisatie

NAW gegevens 4x Tekst (100) Nee 4 regels per adres (Naam;tav;adres;postcode+plaats)

NAW gegevens 4x Burger + Gemacht Burger; Opleider; Gemacht opleider

Notitieveld om aantekeningen te kunnen maken

Signaal datum Datum Nee

Reden signaal Tekst (35) Nee

Datum ontvangst bevestiging indiener Datum Ja

Is er een gemachtigde Ja / Nee Ja

Is er Verzuim Ja / Nee Ja

Verzuim afgehandeld Ja / Nee Ja als is er verzuim = Ja

Indiener Keuzelijst Ja Burger ; Opleider; Anders

MeerPartijenProcedure van toepassing Ja

Hoorzitting houden Ja / Nee Ja

Datum Hoorzitting Datum Ja als HZ houden = Ja

Locatie Hoorzitting Tekst (50) Ja als HZ houden = Ja

Bezwaar ingetrokken Radio button met Intrekking Ja

Beslissing Op Bezwaar (BOB) indiener

verzonden Radio button met BOB Ja

Datum BOB of intrekking Datum Ja

Dictum BOB Keuzelijst Ja als BOB verzonden Gegrond; Ongegrond; Niet ontvankelijk

Is er Verdaagd Aan / Uit Nee Standaard = Uit

Zaak afgerond Aan / Uit Nee Standaard = Uit

Versie 1.0 pagina 67 van 72

Programma van Eisen STAP-applicatie

Afhandelen beroepsprocessen Aandachtspunten

Het moet mogelijk zijn meerdere beroepsprocessen

Naam Soort Bron Verplicht te registreren

Registratienummer Ja Aparte tab met een aantal standaard brieven

Datum ontvangst beroepschrift Datum Ja Notitieveld om aantekeningen te kunnen maken

Beroepsschriften (en alle verdere communicatie met

Indiener beroepsproces Keuzelijst Ja de rechtbanken) zullen op pwebserviceer binnenkomen

Naam medewerker B&B Keuzelijst Ja UWV moet ook zelf een hoger beroep kunnen aanmaken

Type zaak Keuzelijst Ja Beroep, hoger beroep, voorlopige voorziening

NAW gegevens 4x Tekst (100) Ja 4 regels per adres (Naam;tav;adres;postcode+plaats)

NAW gegevens 4x Nee Burger + Gemacht Burger; Opleider; Gemacht opleider

Signaal datum Datum Nee

Reden signaal Tekst (35) Nee

Zitting Ja / Nee Ja

Datum zitting Datum Ja

Locatie zitting Tekst (50) Ja

Datum uitspraak Datum Ja

Soort uitspraak Keuzelijst Ja

Dictum uitspraak Keuzelijst Ja

Zaak afgerond Aan / Uit Nee Standaard = Uit

Versie 1.0 pagina 68 van 72

Programma van Eisen STAP-applicatie

2.3 Werkbakken

Werkbakindelingen

Te tonen

Registratienummer

(inlog)Naam behandelaar

Signaal datum

Signaal reden

Wettelijke einddatum

Status

Type zaak

## BSN

Kunnen zoeken op

Registratienummer

(inlog)Naam behandelaar

Signaal datum

Signaal reden

Wettelijke einddatum

Status

## BSN

Type zaak

Er moet op iedere kolom gesorteerd kunnen worden

Er moet gezocht kunnen worden met wildcards bij tekst velden

Versie 1.0 pagina 69 van 72

Programma van Eisen STAP-applicatie

2.4 Brieven/Sjablonen

Mogelijke brieven bezwaar

Naam NAW van

Ontvangsbevestiging Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Uitnodiging HZ Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Bevestiging intrekking Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Telefoon notitie Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Vrije brief Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

BOB Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Begeleidende brief Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

De gekozen NAW gegevens worden automatisch meegegeven aan de brief

Alle gemaakte brieven kunnen opgenomen worden in het elektronisch dossier

Opnemen in elektronisch dossier d.m.v. aparte knop Opslaan in archief

Per brief een datum veld Verzonden op

Iedere brief moet meerdere keren aangemaakt kunnen worden

Mogelijke brieven beroep

Naam NAW van

Verweerschrfit Keuzelijst Rechtbank, Centrale Raad van Beroep

Beroepschrift Keuzelijst Rechtbank, Centrale Raad van Beroep

Beantwoording Keuzelijst Rechtbank, Centrale Raad van Beroep

vraagstelling Keuzelijst Rechtbank, Centrale Raad van Beroep

Telefoon notitie Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Vrije brief Keuzelijst Rechtbank, Centrale Raad van Beroep, Burger + Gemacht Burger; Opleider; Gemacht opleider

Wijzigingsbeslissing Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Begeleidende brief Keuzelijst Burger + Gemacht Burger; Opleider; Gemacht opleider

Versie 1.0 pagina 70 van 72

Programma van Eisen STAP-applicatie

Bijlage 3 : Afkortingen- en Begrippenlijst

Afkorting/begrip Verklaring, eventueel met toelichting

ABS Autorisatie Beheer Systeem

AD Active Directory

ADFS Active Directory Federation Services

AVG Algemene Verordening Gegevensbescherming

B&B Bezwaar & Beroep (UWV-onderdeel)

Beschikking tot afwijzing Een beschikking waarbij de ontvanger geïnformeerd

wordt dat zijn/haar subsidieaanvraag is afgewezen

Beschikking tot verlening Een beschikking waarbij de ontvanger geïnformeerd

wordt dat zijn/haar subsidieaanvraag is toegewezen

Beschikking tot Een beschikking waarbij de ontvanger geïnformeerd

vaststelling wordt dat zijn/haar scholingsactiviteit met succes is

afgerond

Beschikking tot Een beschikking waarbij de ontvanger geïnformeerd

intrekking wordt dat zijn/haar scholingsactiviteit niet succesvol

is afgerond. Afhankelijk van de context van de

aanvraag kan hierbij het recht (terug)gegeven

worden om in het lopende jaar een nieuwe aanvraag

te doen

Beschikking tot uitsluiting Een beschikking waarbij de ontvanger geïnformeerd

wordt dat hij/zij voor een bepaalde tijd (max 2 jaar)

zal worden uitgesloten van het mogen doen van een

subsidieaanvraag

Beschikking tot Een beschikking waarbij de ontvanger geïnformeerd

invordering wordt dat hij/zij de uitbetaalde subsidie terug moet

betalen aan STAP

BRP Basis Registratie Personen

BSN BurgerServiceNummer

BvA Bewijs van Aanmelding

BvD Bewijs van Deelname

C-ICT Concern Informatie- & Communicatie Technologie

(UWV-onderdeel)

CIO Chief Information Officer

CISO Chief Information Security Officer

CSV Comma Seperated Value

DAMA Digitaal ArbeidsMarktAdvies-applicatie

DigiD Digitaal ID; gestandaardiseerd authenticatiesysteem

voor personen

DOC(x) Document

DXC Hosting Leverancier UWV

EER Europees Economische Ruimte

eHerkenning Gestandaardiseerd authenticatiesysteem voor

organisaties

FB DIV Facilitair Bedrijf Documentaire Informatie Voorziening

(UWV-onderdeel)

FEZ Financieel Economische Zaken (UWV-onderdeel)

GUI-formaten Graphical User interface

IAM Identity – and Access Management

Versie 1.0 pagina 71 van 72

Programma van Eisen STAP-applicatie

ICR Intelligent Character Recognition

ISO International Organization for Standardization

IV InformatieVoorziening

JPG Joint Photographic experts Group (bestandsformaat)

NRTO Nederlandse Raad voor Training en Opleiding

(vereniging particuliere opleiders)

OCR Optical Character Recognition

PDF Portable Document Format (bestandsformaat)

PNG Portable Network Graphics (bestandsformaat)

RNI Registratie Niet-Ingezetenen (onderdeel BRP)

RTF Rich Text Format

SaaS Software as a Service (IT-term)

SIP Systeem IntegratiePlatform (van UWV).

SSO Single Sign-On (IT-term)

STAP STimulering ArbeidsmarktPositie

SZW Sociale Zaken en Werkgelegenheid (ministerie)

TDA Test Data Anonimisering

Tiff Tagged Image File Format

Uitsluitingslijst Lijst waarin burgers die aantoonbaar verwijtbaar

gehandeld hebben met een toegekende subsidie zijn

opgenomen met als doel deze te blokkeren bij het

doen van een nieuwe subsidieaanvraag

UWV Uitvoeringsinstituut WerknemersVerzekeringen

(zelfstandig bestuursorgaan)

XML Extensible Markup Language

Versie 1.0 pagina 72 van 72

---

Bron: [Besluit Woo-verzoek De source code STAP aanvraagsysteem](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2023/besluit-woo-verzoek-de-source-code-stap-aanvraagsysteem) · [Bijlage 1 STAP programma van eisen (PDF, 3 MB)](https://www.uwv.nl/assets-kai/files/153b0ac1-fcea-4db5-bfb2-764adb2368b6/bijlage-1-stap-programma-van-eisen.pdf)
