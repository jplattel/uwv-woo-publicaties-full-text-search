---
source_id: 2026-07-21-woo-besluit-over-aanbesteding-nieuw-erp-systeem/2026-07-21-referentie-architectuur
publication_slug: 2026-07-21-woo-besluit-over-aanbesteding-nieuw-erp-systeem
pdf_slug: 2026-07-21-referentie-architectuur
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2026/woo-besluit-over-aanbesteding-nieuw-erp-systeem
pdf_url: https://www.uwv.nl/assets-kai/files/85c5f4a8-3d6f-4b9c-8d12-b7f2d735d19e/referentie-architectuur.pdf
publication_title: Woo-besluit over aanbesteding nieuw ERP-systeem
publication_date: '2026-07-21T22:00:00Z'
publication_type: WOO publicatie
pdf_label: Referentie architectuur (PDF, 6 MB)
retrieved_at: '2026-08-11T06:58:29+00:00'
sha256: 851fd0d41c33c1d0f56f146b79a8ad508c67bff80b4c898ef05a63320dbfa778
page_count: 15
ocr_used: false
---

Lite Versie GIV Integratiediensten Referentie Architectuur

## GIV

## Integratiediensten

## Referentie Architectuur

## Lite

Versie 1. 2

Datum: 04-05-2023

Pagina: 1 / 14 ©2023 UWV

Lite Versie GIV Referentie architectuur

Integratiediensten

## Versie

Datum Status Korte /

beschrijving aanleiding wijziging

Concept

0.1 25-10-2022 Eerste draft

1.0 03-11-2022 Definitief

11 20-01-2023 mbt cloud MQ FT

Opmerking aansluiting toegevoegd.

en

1.2 04-05-2023 mbt tot het FTPs.

Opmerking gebruik

van

## EE EE:

(geanonimiseerd) (geanonimiseerd) (geanonimiseerd) (geanonimiseerd)

door:

Opgesteld

## leuwv.nl

(geanonimiseerd) (geanonimiseerd)

Voor

opmerkingen:

vragen

## 14 UWV

©2023

Pagina: 2/

## Lite Versie GIV Integratiediensten Referentie architectuur

## Inhoudsopgave

## VERSIEBEHEER. 2

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## INHOUDSOPGAVE. 3

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 1 INLEIDING. 4

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 1. 1 Doel het

## Document. 4

## van

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 1. 2 Scope.

## 4

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 2 KADERSTELLING. 5

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 2. 1 Integratiediensten. 5

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 2. 2 Positionering GIV/ID. 5

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 2. 3 UWV Service richtlijnen. 6

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 2. 4 Beveiliging. 9

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 2. 5 OTAP beleid. 9

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 3 TRANSPORT SERVICES. 10

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 3. 1 Transport Policy Service. 10

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 3. 2 Transport Message Queue Service. 10

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 3. 3 Transport File Transfer Service. 11

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## 4 BIJLAGEN. 12

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Afkortingen.

## 4. 1 12

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## of de Provider.

## 4. 2 Terms Service Service 13

## van

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Profielen.

## 4. 3 Service Contract 13

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Pagina: 3 / 14 ©2023 UWV

Lite Versie GIV Integratiediensten Referentie architectuur

Inleiding

## 1

1. 1Doel het Document

van

beschrijft Services

Dit document de belangrijkste uitgangspunten het gebruik de Transport

voor van van

## GIV (GIV/ID).

UWV Integratiediensten Dit document is gebaseerd de uitgebreid beschreven UWV

op

referentie Services. betreft referentie

architectuur Transport Het hier de verplicht te gebruiken

voor

referentie

architectuur integratie interne externe applicaties services. Deze architectuur

voor van en en

Om

is echter niet extern gebruik beschikbaar. deze reden is lite versie externe partijen

voor er een voor

referentie

aanbestedingstrajecten. Het is vertaling de belangrijkste elementen uit de UWV

en een van

architectuur integratie. Het doel dit document is partijen bekend te maken met de

voor van om

integratierichtlijnen UWV het koppelen systemen het UWV eco-systeem.

van voor van aan

1. 2Scope

Dit document richt zich de integratievraagstukken tussen externe partijen cloudvoorzieningen

op en

,

standaardpakketen volgens de wijze UWV kan wil integreren met andere partijen.

waarop en

Pagina: 4 / 14 ©2023 UWV

Lite Versie GIV Integratiediensten Referentie architectuur

## KADERSTELLING

## 2

2. 1Integratiediensten

biedt gestandaardiseerde transport services applicaties services met elkaar te

## GIV/ID

aan om c. q.

verbinden. Voor het koppelen met UWV is inhoudelijke de niet

berichttransformatie (van payload)

gewenst omdat ontwikkeltraject nodig is. Er zal daarom te allen tijde worden gestuurd

er een voor op

,

de bestaande standaard transport services beschreven in dit document. Dit betekent dat

plaatsvinden de te koppelen systemen niet in de Proxies

transformaties Service GIV/ID.

aan en van

Indien sprake is service ontsluiting divisie heen ontsluiting

of

externe

van over grenzen naar

partijen altijd worden voldaan de UWV integratie

Referentiearchitectuur GIV/ID.

moet

aan voor van

2. 2Positionering GIV/ID

UWV basis het Technical Model raamwerk haar eigen UWV

heeft TOGAF Reference Technical

op van

uitgewerkt.

Reference Model (UTRM)

Figuur 1: Het UTRM

geeft

De services die Integratiediensten levert vallen binnen de services Transport. Figuur

2

groep

hiervan overzicht. De implementatie deze transport services worden zogenaamde

‘Service

een van

Service

genoemd. Een Proxy bevat alle technische aspecten het managed ontsluiten

Proxies’

voor van

Een Proxy bevat nooit Daarnaast is de ontvangende

Services. Service bedrijfsregels of bedrijfslogica.

partij altijd de eindverantwoordelijke de validatie de berichten.

voor van

Pagina: 5 / 14 ©2023 UWV

Lite Versie GIV Integratiediensten Referentie architectuur

2. 3UWV Service richtlijnen

hoofdstuk hoofdlijnen

In dit zijn de service richtlijnen in beschreven. Deze richtlijnen hebben

betrekking de wijze ontwerpen registreren implementeren services. Veelal gelden

op van en van

,

deze richtlijnen ook partijen anders dan UWV gekoppeld moeten worden met UWV

voor wanneer

,

hoofdstuk Services

services applicaties. In 4 wordt beschikbare Transport beschreven wat de

en per

belangrijkste uitgangspunten zijn.

Service definitie

Voor de uitwerking de Richtlijnen is gekozen de Archimate als basis te

van ervoor om

nemen:

Service: “An defined

Application application service represents explicitly exposed application

an

behavior. ”

Component: of

Application An application component represents encapsulation application

an

functionality

aligned to implementation structure which is modular and replaceable.

,

Hierbij is service equivalent is de applicatie service application component equivalent

een aan en een

applicatie.

aan een

1

Richtlijn Beschrijving rationale

## #REF

en

heeft

Een service altijd Er moet altijd eindverantwoordelijke zijn het beheer

## REF000

een een voor

eigenaar service. De verantwoordelijkheid kan gedelegeerd

van een

worden verschillende teams is altijd

1

over maar er

,

eindverantwoordelijke noodzakelijk.

De contactgegevens zijn verplicht worden bij UWV externe partijen

en voor

opgeslagen in de UWV Servicebibliotheek.

Een service moet duidelijk Indien service klein eenvoudig is

REF001 (veelal

een een en genoeg

eenvoudig doel dienen gerelateerd business dan wordt de

capability)

maar aan een

,

aanpasbaarheid service groter de

van een en

onderhoudbaarheid beter. Als service te rijk

een aan

wordt zullen kwaliteitsattributten als

functionaliteit

,

onderhoudbaarheid wendbaarheid veranderbaarheid in het

, ,

gedrang komen. De interne cohesie service dient hoog

van een

te zijn. Veelal betekent dit dat veranderingen in het datamodel

binnen de service context vallen. Dit vermindert de

communicatie met andere services aanzienlijk wordt de

en

sterk verlaagd. Het duidelijke doel uit zich ook

afhankelijkheid

vaak in eenduidige

een naam.

De naamgeving service dient helder eenduidig te zijn de correcte

van en voor

registratie in de UWV Servicebibliotheek.

Een service is bij voorkeur Dit betekent dat service

REF002 state/informatie

een geen mag

stateless bijhouden gerelateerd service requests uit het verleden. In

aan

principe zal de service binnenkomend request ongeacht de

een

instantie moeten verwerken. Dit is essentieel

hetzelfde

een

uitgangspunt schaalbaarheid mogelijk te maken. Dit

om

betekent ook dat 'consumers' services de state moeten

van

bijhouden het dat is gekoppeld de

van proces aan

bedrijfsfunctie.

1

Alleen de richtlijnen toepassing externe partijen cloudvoorzieningen standaard pakketen zijn in deze

van op en opgenomen

,

lijst. Hierdoor is de nummering niet opeenvolgend.

Pagina: 6 / 14 ©2023 UWV

Lite Versie GIV Integratiediensten Referentie architectuur

Wanneer niet kan worden voldaan de bovenstaande richtlijn dan moet dit

aan

,

tijdig kenbaar gemaakt worden UWV te komen toch goede

aan om een

integratie.

heeft heeft (met

Een service altijd Een service duidelijk contract zowel business als

## REF003

een een

contracten)

contract technische met de buitenwereld waarin precies

staat wat verwacht worden de service. Best practice

mag van

het contract eerst te stellen alvorens te beginnen met

om op

realiseren.

Technische Service Contracten zijn verplicht worden gezamenlijk opgesteld

en

vastgelegd in de UWV Servicebibliotheek. Voor service provider zijn

en

zogenaamde Terms of Service tevens noodzakelijk.

Een service is altijd Een service goede beschrijving omtrent het gebruik

REF004 heeft

een

gedocumenteerd bij voorkeur developer portal

of zelf

ervan en een een

beschrijvende waartegen gebruikers de service

interface

van

,

kunnen ontwikkelen testen.

en

Elk te koppelen service provider is verplicht beschrijving te leveren die

een op

informatie

voldoende bevat te kunnen koppelen. Er zijn verschillende

om

WSDL Swagger

documentatie mogelijk als: openAPI etc. Maar

vormen van

, ,

infrastructuur

denk ook security documentatie.

aan en

heeft

Een service standaard Wanneer services het log aggregation pattern implementeren

## REF007

een

,

wijze logging wordt trouble shooten vele malen makkelijker. De logstandaard

van

beschrijft

welke elementen minimaal lokaal gelogd moeten

worden zodat deze eenvoudig geconsolideerd kunnen worden

,

in centrale omgeving analysedoeleinden. Inzicht

een voor en

overzicht met betrekking tot gebruik services wordt

van van

hiermee mogelijk.

UWV heeft aantal solutions beschikbaar het logging

een voor aggegreren van

informatie.

Een service moet correct Een service moet ontworpen zijn met de gedachte dat in

REF008 fouten fouten

kunnen optreden. De dient adequeaat hierop te

afhandelen infrastructuur software

kunnen Vaak worden de wel

software fouten

reageren. nog

ontworpen de niet. Denk

infrastructuurfouten

mee maar aan

,

vollopen netwerk problemen etc. is hiervoor

## REF007

queues

,

randvoorwaardelijk integrale inzicht te hebben!

om

Uiteraard geldt dit alle services applicaties.

voor en

Een service moet nodig in Een service is geheel techniek

REF010 functionaliteit

waar een van en

,

staat zijn meerdere instanties Een service controle alle

heeft (runtime)

van gegevens. over

te kunnen draaien. onderdelen die nodig zijn goede autonome werking.

zichzelf

voor een

Deze richtlijn is vooral belang als grote aantallen request worden

van er

verwacht. In het technische Service Contract wordt dit by design vastgelegd.

Een service communiceert volgens Websphere

REF013 (s)FTP HTTP(s) MQ SOAP REST.

, , , ,

standaard protocollen

Een service kent service traceerbaarheid te verwezenlijken zal service alle

REF015 Om

voor een

requests altijd correlatie communicatie moeten

identificeren.

een

identificatie

In de berichtenstructuur moet plek zijn correlatie identificatie.

voor een

Pagina: 7 / 14 ©2023 UWV

Lite Versie GIV Integratiediensten Referentie architectuur

Een service moet geregistreerd Een service moet vindbaar zijn.

## REF017

worden in centrale

een

servicebibliotheek

Elke service provider service wordt vastgelegd in de UWV

en consumer

Servicebibliotheek.

UWV doet dit externe partijen.

voor

Een service dient health check Het moet mogelijk zijn services die in productie draaien te

## REF018

een om

interface

te hebben kunnen controleren hun toestand. Dit is veelal

op een

beheerinterface heeft.

die bij voorkeur standaard

een vorm

Een service dient alleen de strikt In relatie tot service duidelijk doel

REF019 REF001 heeft

een een en

noodzakelijk elementen in de contract niet worden uitgebreid met subdoelen.

en mag zomaar

service te Bij voorkeur contract

interface first!

op nemen.

API’s/service interfaces.

Dit leidt veelal tot meerdere

Een service kent beperkt Een service kent naast de huidige versie maximaal versies in

## REF020 2

een

interface (eventueel toekomst)

aantal versies het verleden in de productieomgeving.

OTA afgeweken

Voor kan hiervan worden.

2

open/closed

Indien dit niet mogelijk is kan principe worden

een

gehateerd.

Een service valideert invoer Een service zal gelang de noodzaak basis

## REF021

naar op van een

invoervalidatie sematisch

(minimale) (inhoudelijk functioneel

, ,

bepalen verwerkt kan worden

technisch) of of

en een aanvraag

niet.

registratie:

Service Servicebibliotheek

2. 3. 1

in haar de UWV In deze applicatie worden alle

GIV/ID heeft portfolio Servicebibliotheek. interfaces

Application Programming als services geregistreerd. Daarnaast regelt de UWV

(API’s: Interfaces)

ook de Management. Voor externe partijen regelt UWV deze

Servicebibliotheek Service Life Cycle

registratie.

Service Contracten

2. 3. 2

Tevens dient in de UWV gewerkt te worden met zogenaamde technische service

Servicebibliotheek

contracten in relatie tot de de service provider waarin het gebruik

‘terms of service’

van van een

,

wordt vastgelegd voorhand.

interface

op

2

Open-closed Principle (OCP) states: Objects entities should be for extension but closed for modification.

or open

Pagina: 8 / 14 ©2023 UWV

Lite Versie GIV Referentie

architectuur

Integratiediensten

2.4

Beveiliging

_Informatiebeveiliging

2.4.1

GIV/ID de UWV IB&P zullen in dit document niet verder worden

volgt Security richtlijnen toegelicht.

en

Dit onderdeel valt onder '08 Informatie zie ook: 1: Het UTRM. Dit ook

beveiliging’, Figuur geldt

voor

& Access In dit document wordt beantwoord hoe UWV dit

Identity Management (IAM).

met

name

verbindingen partijen standaardpakketten.

met externe

toepast

voor en

Class

Confidentiality

2.4.2

Hieronder de UWV risicoklasses beschreven de

gemapt

zijn (confidentiality classes)

en

op

functionele- technische

beveiligingsinrichtingen.

en

## (geanonimiseerd) (geanonimiseerd)

Omschrijving

Klasse Functioneel niveau

0 Niet Niet

vertrouwelijke beveiligd

gegevens

die beschikbaar Betekent dat hackers

Openbaar publiekelijk vrij

kunnen worden de data

gesteld. gemakkelijk bij

kunnen komen.

1 Minimale

Reguliere beveiliging

persoonsgegevens

deze niet kunnen

zolang

Interne

## Betekent dat met

## een

tot

worden de

gerekend

## Ô

het nie

eetje proberen

informatie

ii

bijzondere

persoonsgegevens

. ,

Aan

mogelijk

is

conform WPB art.16.

de data komen.

bij

te

2 Defaultklasse UWV. Gemiddelde

beveiliging

voor

die

Vertrouwelijke

gegevens

©

„

Vertrouwelijk dat

Betekent

voor een

niet brede

kennisneming

voor

met

hacker

professionele

bedoeld.

zijn

á

beetje proberen

een

die vallen onder

Gegevens

niet

het de

mogelijk bij

is

WPB art.16

te

data komen.

2+ Klasse 2+ Zie klasse 2

geldt

voor

## Vertrouwelijk

bijzondere

persoonsgegevens.

die vallen onder

Gegevens

Maximale

beveiliging

art

WPB 9 lid 4.

3

Betekent dat het

voor

Strikt

hackers

professionele

vertrouwelijk

is

moeilijk

om

de data komen.

bij

te

Geheim

OTAP beleid

2.5

Voor software binnen het rekencentrum UWV OTAP beleid.

deployments (on premise) geldt

van een

OTAP Productie. De is dat elke of

Testen,

Ontwikkeling, Acceptatie bedoeling wijziging

staat

voor en

deze In het UWV beleid is

vernieuwing automatisering opeenvolgend doorlopen.

moet

stappen

op

dat elke worden.Voor

vastgelegd eigen gescheiden omgeving gebruikt

tevens moet

stap

voor een

is alleen

deployments, bijvoorbeeld cloudoplossingen, Acceptatie-

externe

er een en

beschikbaar.

Productieomgeving

## 9 14 UWV

©2023

Pagina: /

Lite Versie GIV Referentie

architectuur

Integratiediensten

## TRANSPORT SERVICES

3

externe

Dit hoofdstuk Services

beschrijft Transport partijen, cloudvoorzieningen

voor en

de

standaardpakketten bijbehorende uitgangspunten:

en

Service

3.1

Transport

Policy

met

De Service is de verkeer

interne,

Transport Policy primaire transportdienst synchroon

voor

externe

overheidspartijen.

en

Invullin:

Aspect

## ___

(geanonimiseerd) (geanonimiseerd)

Protocol formaat

en

UWV standaarden UWV het maken berichten

datamodellen,

Gegevensstandaard

voor van

interfaces. Cloud- kunnen aansluiten

standaardpakketten

moeten

en en

de UWV Standaard.

volgens

Voor ontsluiten UWV de

DigiKoppeling overheidspartijen volgt Digikoppeling

van en naar

2.0 standaard. Tevens is het ook de voorkeur andere

partijen.

voor

## (geanonimiseerd) (geanonimiseerd)

kunnen aansluiten Information & Event

Logging monitoring Cloudpartijen Security

moeten

en

op

Dit onderdeel valt onder ’08 Informatie

Management (SIEM). beveiliging’,

zie ook: 1: Het UTRM.

Figuur

met

Bericht Deze wordt berichten de

grootte

transportdienst gebruikt enkelvoudige

voor

MSP2 Service Contract middels standaard

## MSP1,

profielen (zie Profielen)

HTTP. Wanneer is MSP3 dan zal HTTP

## MSP4,

sprake altijd

er van en

worden

toegepast.

streaming

berichten Deze kan de RRP1 t/m RRP7 ondersteunen Service

Frequentie transportdienst (zie

van

Contract

Profielen).

## Foutafhandeling

De hanteert het ‘fail fast rather than block’ Dit

transportdienst principe.

betekent dat fouten het niet wacht time-out

ontstaan,

wanneer een

op

snel zal de

teruggeven

mogelijk foutmeldingen

maar zo een om resources

te

is dat de niet

is,

vrij spelen. Belangrijk transportdienst persistent

weer

de verzendende dient

partij retry-mechanisme.

te

voor een

zorgen

extra

Standaard Minimaal 100 de

latency transportdienst.

ms voor

Cloud Indien wordt statische IP dan kan UWV

adressen,

aansluiting gebruik gemaakt

er van

de als trusted worden IP zal

partij gekenmerkt. Bij dynamische

partner

worden forward Dit heeft

gebruik gemaakt

moeten

van een reverse

proxy.

niet de voorkeur. IP adressen via de worden

Dynamische

reverse

proxy

niet

toegestaan.

Tabel 1 Aansluitvoorwaarden Service.

Transport

Policy

Service

3.2 Queue

Transport

Message

De Queue Service is de verkeer

Transport Message primaire transportdienst asynchroon

met

voor

interne

partijen standaardpakketten.

en

/

## 14 UWV

©2023

Pagina: 10

Lite Versie GIV Referentie

architectuur

Integratiediensten

Aspect Invulling

(geanonimiseerd) (geanonimiseerd)

Protocol formaat

en

Uwv standaarden UWV het maken berichten

datamodellen,

Gegevensstandaard

voor van

moeten

interfaces. Cloud- kunnen aansluiten

standaardpakketten

en en

de UWV Standaard.

volgens

(geanonimiseerd)

kunnen aansluiten Information & Event

Logging monitoring Cloudpartijen Security

moeten

en

op

Dit onderdeel valt onder ’08 Informatie

Management (SIEM). beveiliging’,

zie ook: 1: Het UTRM.

Figuur

Bericht Deze wordt

grootte

transportdienst gebruikt enkelvoudige meervoudige

voor en

met

berichten de MSP2 Service Contract

## MSP1,

profielen (zie Profielen).

berichten Deze kan de RRP1 t/m RRP7 ondersteunen Service

Frequentie transportdienst (zie

van

Contract

Profielen).

Cloud Indien wordt IP

statische

adressen,

aansluiting gebruik gemaakt

van

er

kan UWV

dan de als trusted worden

partij

partner

IP zal

gekenmerkt. Bij dynamische gebruik gemaakt

moeten

Dit heeft niet de

worden forward

van een reverse

proxy.

IP via

voorkeur. adressen de

Dynamische

reverse

proxy

worden niet

toegestaan.

Tabel 2 Aansluitvoorwaarden Service

Transport Queue

Message

File Transfer Service

3.3

Transport

extern

De File Transfer Service is de het zowel intern als

Transport primaire transportdienst

voor van

bestanden.

grote

Aspect Invulling

## (geanonimiseerd) (geanonimiseerd)

Protocol formaat

en

Uwv standaarden UWV het maken berichten

datamodellen,

Gegevensstandaard

voor van

moeten

interfaces. Cloud- kunnen aansluiten

standaardpakketten

en en

de UWV Standaard.

volgens

Voor ontsluiten UWV de

DigiKoppeling overheidspartijen volgt Digikoppeling

van en naar

2.0 standaard. Tevens is het ook de voorkeur andere

partijen.

voor

## (geanonimiseerd) (geanonimiseerd)

moeten kunnen aansluiten Information & Event

Logging monitoring Cloudpartijen Security

en

op

Dit onderdeel valt onder ’08 Informatie

Management (SIEM). beveiliging’,

zie ook: 1: Het UTRM.

Figuur

met

Bericht Deze wordt berichten de

grootte

transportdienst gebruikt meervoudige

voor

MSP3 MSP4 Service Contract

profielen (zie Profielen).

en

berichten Deze kan berichten de RRP1 t/m RRP4

Frequentie transportdienst meervoudige

van voor

ondersteunen Service Contract

(zie Profielen).

Cloud Indien IP

wordt statische

adressen,

aansluiting gebruik gemaakt

van

er

dan kan UWV trusted

de als worden

partner

partij

IP zal moeten

gekenmerkt. Bij dynamische gebruik gemaakt

Dit

worden forward heeft niet de

van

een reverse

proxy.

voorkeur. IP

adressen via de

Dynamische

reverse

proxy

worden

niet

toegestaan.

Tabel 3 Aansluitvoorwaarden File Transfer Service.

Transport

## 11 14 UWV

©2023

Pagina: /

Lite Versie GIV Integratiediensten Referentie architectuur

Bijlagen

4

4. 1Afkortingen

Overzicht afkortingen

gebruikte in dit document.

van

met

Afkorting Verklaring eventueel toelichting

,

AMG API Management Gateway

API Application Programming Interface

DK Logius DigiKoppeling

ebMS ebXML Messaging Service

FT File Transfer

GIV/ID GIV Integratiediensten

HTTPS Hypertext Transfer Protocol Secure

ICAP Internet Content Adaptation Protocol

JSON JavaScript Object Notation

management

LCM Life cycle

MQ Message Queue

RA Referentie Architectuur

REST Representational transfer

state

SAML Security Assertion Markup Language

SIEM Security Information & Event Management

SOAP Simple Object Access Protocol

TLS Transport Layer Security

UTRM UWV Technical Reference Model

## WUS WSDL UDDI SOAP

en

,

XML Extensible Markup Language

Pagina: 12 / 14 ©2023 UWV

Lite Versie GIV Integratiediensten Referentie architectuur

4. 2Terms of Service de Service Provider

van

of Service geeft

De Terms is registratie onderdeel de service provider wat de

een van en aan grenzen

of Service

het gebruik de service in kwestie. In de Terms staan de eisen alle

voor van waaraan

functie

service gezamenlijk minimaal moeten voldoen waarbij de service provider haar

consumers

,

steeds correct kan aanbieden.

nog

Interface Performance

4. 2. 1

Size

Maximum Message

(Example

What is the maximum size that will be allowed to send to the service maximum

message

request)

size is 4MB

message per

Service

Average Requests Rate

(Example of

Fill in the rate limiting minute the service handle

500

average per can an average

customer).

transactions minute

per per

Service

Maximum Requests Rate

(Example of

Fill in the rate limiting minute the service handle maximum transactions

10

per can a per

customer)

minute

per

Concurrent Service

Maximum Requests

(Example second)

How concurrent service calls the service handle second

100

many can per per

Interface

4. 2. 2 Usage

Utilisation Period

of (Example from 24/7)

Use service during which hours only till

08:00 17:00

or

Network Type

(Example Network)

Which network type is being used Internet Intranet Diginet Private

, , ,

Data Exchange Format Type

format SuwiML JSON SubML

Data exchange used: UwvML XML

, , , ,

Communication Standard

## SAML SUWI

This is the communication standard used: Digikoppeling Transactie standaard

, ,

Confidentiality Class

Confidentional Class (Example information

within UWV is low risk like public and is

0-3 0 3

very very

information of person)

high like medical

a

3Service

4. Contract Profielen

De service contracten maken gebruik snel te komen tot inschatting.

profielen

van om een

Request Rate Message

Profile (RRP) Size Profile (MSP)

en

de request rate size in makkelijker hanteerbare te verdelen zijn beide

Om staffels

en message voor

rubrieken gemaakt. Daarbij is verschillende onderscheid

gedefinieerde profielen

voor er over assen

gemaakt: Enkelvoudig bulk berichten rubriek het maximale gemiddelde aantal

of profiel.

en per en per

Voor meervoudige berichten

(bulk)

Meervoudige berichten kunnen met maximum minuten gestuurd worden hebben

1x 15

een van per en

minimale berichtgrootte 4 MB. Er is minimaal aantal keren dat bericht gestuurd kan

een van geen een

worden. De maximale berichtgrootte is MB.

1500

Pagina: 13 / 14 ©2023 UWV

Lite Versie GIV Integratiediensten Referentie architectuur

Request Rate Max Average Unit

Profile (RRP)

month 5 month

RRP1: 1x 1 0.

<

per per

month to week 4 month

RRP2: 1x 1x 2

per per per

week to day 7 5 week

RRP3: 1x 1x 3.

per per per

RRP4: day to day

1x 1x 15 96 48

per per per

minutes

Message Max Average

Size Profile (MSP) (MB) (MB)

4 MB and MB

## MSP3: 20 20 12

MB and bigger

## MSP4: 20 1500 750

Voor enkelvoudige berichten

Enkelvoudige berichten kunnen met maximum berichten minuut gestuurd worden

1000

een van per

met maximale berichtgrootte 4 MB. Er is minimaal aantal keren dat bericht

en een van geen een

gestuurd kan worden noch minimale berichtgrootte.

een

,

Request Rate Max Average Unit

Profile (RRP)

RRP5: minute minute

100 100 50

<

per per

to minute minute

## RRP6: 100 500 500 250

per per

RRP7: minute minute

500 1000 500

>

per per

Message Max Average

Size Profile (MSP) (MB) (MB)

Up to 5 KB 5 KB 5 KB

## MSP1: 2.

Between 5 KB and 4 MB 4 MB MB

## MSP2: 2

Pagina: 14 / 14 ©2023 UWV

## Toelichting grondslagen

In dit document kunt u secties vinden die onleesbaar zijn gemaakt. Deze informatie is

achterwege gelaten op basis van de Wet open overheid (Woo). De letter die hierbij is vermeld

correspondeert met de bijbehorende grondslag in onderstaand overzicht.

J Art. 5.1 lid 2 sub e

Het belang van de openbaarmaking van deze informatie weegt niet op tegen het belang van

de eerbiediging van de persoonlijke levenssfeer van betrokkenen

N Art. 5.1 lid 2 sub i

Het belang van de openbaarmaking van deze informatie weegt niet op tegen het belang van

het goed functioneren van de Staat, andere publiekrechtelijke lichamen of bestuursorganen

---

Bron: [Woo-besluit over aanbesteding nieuw ERP-systeem](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2026/woo-besluit-over-aanbesteding-nieuw-erp-systeem) · [Referentie architectuur (PDF, 6 MB)](https://www.uwv.nl/assets-kai/files/85c5f4a8-3d6f-4b9c-8d12-b7f2d735d19e/referentie-architectuur.pdf)
