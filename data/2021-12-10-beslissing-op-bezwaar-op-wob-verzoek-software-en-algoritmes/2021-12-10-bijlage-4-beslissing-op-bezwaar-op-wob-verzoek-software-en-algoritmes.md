---
source_id: 2021-12-10-beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes/2021-12-10-bijlage-4-beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes
publication_slug: 2021-12-10-beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes
pdf_slug: 2021-12-10-bijlage-4-beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/wob-publicaties/2021/beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes
pdf_url: https://www.uwv.nl/assets-kai/files/4571f499-a1ce-4b2d-a549-36131e8727c5/bijlage-4-beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes.pdf
publication_title: Beslissing op bezwaar op Wob-verzoek software en algoritmes
publication_date: '2021-12-10T00:00:00Z'
publication_type: WOB publicatie
pdf_label: Bijlage 4 bij beslissing op bezwaar op Wob-verzoek software en algoritmes
  (PDF, 1 MB)
retrieved_at: '2026-06-30T14:13:14+00:00'
sha256: c3797999d35b5d3b0419ca2e4af6e16d08c9b323cc91c35f6cec3264d5328d58
page_count: 52
ocr_used: false
---

Beleidsdocument model risico management

1

Beleidsdocument model

risico management

Datum

29 september 2021

Status

Auteur

cc

10.2.e

Wob

Versie

1.2

Ons kenmerk

-

Pagina

2 van 52

0 Document versiegeschiedenis

Document versies

Versie Datum Verandering

0.1 Draft versie document

0.8 10 mei 2021 Commentaar verwerkt van

10.2.e

Wob

0.9 16 juni 2021 Los datacomponent in

modelontwikkeling toegevoegd

en aantal andere kleine

verfijningen

1.0 23 juni 2021 Commentaar verwerkt van

1.1 25 augustus 2021 Commentaar verwerkt van

/ DT handhaving

inclusief extra review document

verantwoordelijken

1.2 29 september 2021 Commentaar verwerkt van GD

en AD

Goedkeuring

Versie Datum Comité Goedkeuring

© UWV Uitvoeringsinstituut werknemersverzekeringen.

Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd, opgeslagen in een geautomatiseerd

gegevensbestand of openbaar gemaakt, in enige vorm of op enige wijze, hetzij elektronisch, mechanisch, door

fotokopieën, opnamen of op enig andere manier zonder voorafgaande schriftelijke toestemming van de uitgever.

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

3 van 52

Inhoud

0 Document versiegeschiedenis 2

1 Introductie 5

1.1 Doel van dit document 5

1.2 Onderdelen raamwerk 5

1.3 Scope 5

1.4 Document management 6

2 Definities 7

2.1 Model definitie 7

2.2 Modelrisico 8

3 Model tier 10

3.1 Vaststellen model tier 10

4 Rollen en verantwoordelijkheden 12

4.1 Overzicht van rollen in het model risico management raamwerk 12

4.2 Governancestructuur 14

4.3 Verantwoordelijkheden in het model risico management

raamwerk 14

4.3.1 Verantwoordelijkheden coalitie risicoscans (eerste

besluitvormingslinie) 15

4.3.2 Verantwoordelijkheden data eigenaar (eerste verdedigingslinie) 16

4.3.3 Verantwoordelijkheden model eigenaar (eerste verdedigingslinie) 16

4.3.4 Verantwoordelijkheden model gebruik kwaliteitstoets (eerste en

tweede verdedigingslinie) 17

4.3.5 Verantwoordelijkheden model ontwikkelaar (eerste en tweede

verdedigingslinie) 17

4.3.6 Verantwoordelijkheden model validator (tweede

verdedigingslinie) 18

4.3.7 Verantwoordelijkheden model risico manager (eerste en tweede

verdedigingslinie) 19

4.3.8 Verantwoordelijkheden interne audit (derde verdedigingslinie) 19

4.3.9 Verantwoordelijkheden functionaris gegevensbescherming (derde

verdedigingslinie) 19

4.3.10 Verantwoordelijkheden Ethische toetsing (derde

verdedigingslinie) 19

3

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

4 van 52

4.3.11 Verantwoordelijkheden cliëntenraad (vierde verdedigingslinie) 19

4.3.12 Verantwoordelijkheden Nationale ombudsman (vierde

verdedigingslinie) 20

4.3.13 Verantwoordelijkheden autoriteit persoonsgegevens (vierde

verdedigingslinie) 20

5 Modellevenscyclus 21

5.1 Stappen in de modellevenscyclus 21

5.1.1 Model initiatie en wijziging 23

5.1.2 Model ontwikkeling 27

5.1.3 Model validatie 29

5.1.4 Model implementatie en testen 34

5.1.5 Model goedkeuring 34

5.1.6 Model gebruik 37

5.1.7 Model monitoring 38

5.1.8 Model ontmanteling 41

6 Documenten raamwerk 43

6.1 Overzicht documenten raamwerk 43

7 Model inventaris 48

7.1 Componenten model inventaris 48

8 Rapportage 49

8.1 Typen model risico management rapportages 49

Appendices 51

Appendix 1 – Verklarende woordenlijst 51

Appendix 2 – Lijst van tabellen en figuren 52

4

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

5 van 52

1 Introductie

1.1 Doel van dit document

Het beleidsdocument model risico management (hierna: “beleidsdocument”) beschrijft hoe UWV omgaat

met modellen gericht op de toezichtsfunctie en wie waartoe verantwoordelijkheid draagt. Met het model

risico management raamwerk beheerst UWV haar modelrisico’s en stel het haar werknemers in staat om

transparant, correct en integer met modellen te kunnen werken. UWV stelt de ambitie om met haar model

risico management raamwerk voorop te lopen in het waarborgen dat de ontwikkeling en beheersing van

modellen robuust is en compliant is met wet- en regelgeving. Conform het Kompas Data Ethiek en in

navolging van de ROEP-kernwaarden – Respect, Openheid, Eigen Verantwoordelijkheid en Professionaliteit,

helpt ook dit model en deze datatoepassing het beschikbare budget, tijd en menskracht op een betere

manier in te zetten. Dit document kan gezien worden als een nadere uitwerking van het ethisch kompas

met betrekking tot risicoscans.

Dit document is voortgekomen en opgesteld op basis van onder andere JV richtlijnen, ARK-richtlijnen,

sessies en workshops binnen UWV en vakkennis van leveranciers uit de markt.

1.2 Onderdelen raamwerk

In dit beleidsdocument worden de volgende onderdelen beschreven:

Hoofdstuk 2 beschrijft de definitie van een model en van modelrisico’s voor UWV

-

Hoofdstuk 3 beschrijft de model tiering methodologie

-

Hoofdstuk 4 beschrijft de rollen en verantwoordelijkheden van de model stakeholders

-

Hoofdstuk 5 beschrijft de gehanteerde modellevenscyclus van UWV, inclusief de onderliggende

-

stappen

Hoofdstuk 6 beschrijft het documenten raamwerk die binnen het model risico beleid vallen van

-

## UWV

Hoofdstuk 0 beschrijft de model inventaris en uit welke onderdelen het bestaat

-

Hoofdstuk 0 beschrijft de verschillende model risico management rapportages

-

1.3 Scope

Het beleidsdocument is op het moment van schrijven van toepassing op de volgende modellen:

Risicoscan Verblijf buitenland

-

Risicoscan Verwijtbaar werkloos

-

Risicoscan Sollicitatie activiteiten

-

Dit beleidsdocument is van toepassing op alle divisies en medewerkers binnen UWV en in het bijzonder op

de afdelingen en medewerkers die eigenaar zijn van of betrokken zijn bij de bovengenoemde risicoscans.

Het gaat hierbij om activiteiten die te maken hebben met de toezichtsfunctie van UWV.

5

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

6 van 52

1.4 Document management

management1.

De model risico manager van UWV is de eigenaar van het beleidsdocument model risico De

risicoscans2.

implementatie en aansturing van het model risico management beleid ligt bij de coalitie

Het beleidsdocument model risico management kan worden aangepast wanneer nieuwe inzichten of

wijzigingen optreden. Het beleidsdocument moet minimaal jaarlijks worden getoetst op actuele

gebeurtenissen door de model risico manager. Wijzigingen in het beleidsdocument dienen te worden

goedgekeurd door de coalitie risicoscans.

1

UWV heeft op dit moment nog geen model risico manager aangewezen. Wij stellen voor dat hoofd R & I formeel

model risico manager wordt. Tot die tijd is het hoofd R & I verantwoordelijk voor het document.

2

UWV heeft op dit moment nog geen coalitie risicoscans. Ons voorstel is dat de Commmissie Data Gedreven Werken

deze rol op zich gaat nemen. Tot die tijd is het hoofd R & I verantwoordelijk voor het document.

6

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

7 van 52

2 Definities

UWV heeft besloten om niet meer de term risicomodel te gebruiken in haar communicatie. We spreken

voortaan van risicoscans. In dit hoofdstuk dienen we toch af en toe de term (risico)model te gebruiken.

Immers, model kent definities vanuit zowel praktijk als wetenschap die we niet zomaar een op een

kunnen vervangen door het woord ‘scan’. De modellen die we binnen UWV gebruiken rondom risico’s

zullen echter altijd risicoscan heten.

Dit hoofdstuk beschrijft de definities die UWV hanteert voor een model en modelrisico. Daarnaast

beschrijft dit hoofdstuk de checklist waaraan een model kandidaat getoetst moet worden.

2.1 Model definitie

De scope van het model risico management raamwerk wordt bepaald door de definitie van een model. Door

UWV wordt de volgende definitie van een model gehanteerd:

Een model wordt gedefinieerd als:

een combinatie van data, aannames en theorieën,

-

die (herhaaldelijk) verwerkt worden,

-

met behulp van een kwantitatieve methode of een systeem (eventueel aangevuld met expert

-

judgement),

in kwantitatieve schattingen die een vereenvoudiging van een werkelijke relatie

-

vertegenwoordigen,

bedoeld voor interne of externe besluitvorming die uitlegbaar is aan onze klanten of de

-

maatschappij.

Figuur 1 geeft schematisch weer wat een model is. Een model verzamelt gegevens zoals data, aannames

en scenario’s en gebruikt een methode (bijvoorbeeld statistisch of wiskundig) om kansberekeningen of

schattingen te kunnen doen. De kansberekeningen en schattingen kunnen gebruikt worden voor het

ondersteunen van beslissingen binnen UWV. De uiteindelijke beslissing wordt altijd door een persoon

genomen, niet door het model.

Risicoscan

Figuur 1: Definitie van een model

Bij het vaststellen of een model kandidaat als model geclassificeerd moet worden, moeten de volgende

vragen beantwoord worden:

7

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

8 van 52

Tabel 1: Checklist model definitie

# Vraag Antwoord

1 Gebruikt de model kandidaat aannames en data als input? Ja/Nee

2 Verwerkt de model kandidaat informatie in kwantitatieve schattingen, selecties of Ja/Nee

voorspellingen?

3 Is de model kandidaat een vereenvoudigde weergave van een reële relatie tussen Ja/Nee

waargenomen kenmerken, waarden en gebeurtenissen?

4 Worden de schattingen van de model kandidaat gebruikt in besluitvorming van de Ja/Nee

toezichtsfunctie die voortkomt uit de uitvoering van overheidsbeleid?

Indien alle vragen met “Ja” beantwoord zijn, wordt de model kandidaat als een model beschouwd en mag

het model het model risico management raamwerk als richtlijn gebruiken.

2.2 Modelrisico

Door UWV wordt de volgende definitie van modelrisico gehanteerd:

Modelrisico kan worden gedefinieerd als de kans op fouten bij het initiëren, (her)ontwikkelen,

valideren, implementeren en testen, goedkeuren, gebruiken, monitoren of buiten gebruik stellen

van modellen. Dit kan vervolgens leiden tot onnauwkeurige, niet conforme model uitkomsten dan

wel verkeerd geïnterpreteerde model uitkomsten die invloed hebben op beslissingen in de

organisatie.

Het verkeerd toepassen van de modeluitkomsten kan de volgende gevolgen hebben (merk op dat meerdere

gevolgen vaak tegelijkertijd optreden):

Impact op de klanten van UWV

-

Reputatieschade voor UWV

-

Inbreuk op privacywetgeving

-

Slechte (strategische) besluitvorming

-

Financiële impact

-

Bovenstaande modelrisico’s worden groter naarmate het model:

Vaker gebruikt wordt

-

Voor het verkeerde doeleinde gebruikt wordt

-

Uitkomsten geeft die verschillende betekenissen kunnen hebben

-

Grotere onzekerheid over de kwaliteit van inputs en aannames heeft

-

Hogere model materialiteit heeft (zie paragraaf 3.1)

-

Hoge model complexiteit heeft

-

Door meerdere personen gebruikt wordt

-

Software gebruikt dat niet up-to-date is of niet goed ondersteund wordt door de gebruikte hardware

-

binnen UWV

8

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

9 van 52

Er kan tenslotte nog een onderscheid gemaakt worden tussen individueel modelrisico en geaggregeerd

modelrisico:

a. Individueel modelrisico komt voort uit aannames, data, methodologieën of andere factoren

specifiek voor een model zoals het ontwikkelen, beheersen, toepassen en uitleggen van een model.

b. Geaggregeerd modelrisico is de som van de individuele modelrisico’s, met in aanvulling daarop de

risico’s uit de interactie en afhankelijkheden tussen modellen. Het gebruik van gemeenschappelijke

aannames, data, methodologieën of andere factoren kunnen leiden tot meer risico omdat zij effect

hebben op meerdere modellen en hun output.

Modelrisico’s worden onderzocht en vastgesteld tijdens model validatie en modelmonitoring (hoofdstuk 5).

Hieruit kunnen bevindingen voortkomen die inzicht geven in de modelrisico’s. Deze bevindingen worden

geclassificeerd op kans en mogelijke impact op dimensies als de modeluitkomst of modelgebruik.

9

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

10 van 52

3 Model tier

In dit hoofdstuk wordt beschreven wat wordt verstaan onder model tier en waar de model tier betrekking

op heeft in de werkzaamheden binnen de scope van het model risico management raamwerk. Daarnaast

staat in dit hoofdstuk beschreven hoe model kwaliteit wordt gemeten.

3.1 Vaststellen model tier

Elk model binnen de scope van het model risico management raamwerk wordt in een model tier

(gelaagdheid) geplaatst die de mate weerspiegelt van de mogelijke impact van verkeerd model gebruik.

De tier van een model heeft invloed op de volgende aspecten van model risico management

werkzaamheden:

Scope van de initiële model validatie

-

Frequentie en scope van periodieke validaties

-

Model monitoringsproces

-

Model wijzigings- en goedkeuringsproces

-

De tier van een model wordt bepaald door twee variabelen:

1) Materialiteit: De impact die een model heeft op de dienstverlening en klanten van UWV

2) Complexiteit: De moeilijkheidsgraad voor een persoon om het model te begrijpen, ontwikkelen,

valideren of gebruiken

scorekaart3

Beide variabelen worden met behulp van een en expert judgement bepaald. Op basis van de

antwoorden op de vragen in de scorekaart (en expert judgement) kunnen de volgende waarden uitkomen

voor beide variabelen:

Laag

-

Gemiddeld

-

Hoog

-

Op basis van een model’s materialiteit en complexiteit, kan de model tier bepaald worden door de model

eigenaar. De model tier wordt uitgedrukt als “Tier 1”, “Tier 2” of “Tier 3”. Een model in Tier 1 kan tot

relatief veel impact leiden bij verkeerd model gebruik en een model in Tier 3 kan tot relatief weinig impact

leiden bij verkeerd model gebruik. In Tabel 2 wordt een overzicht gegeven van de model tiers.

3

De scorekaarten voor het bepalen van de materialiteit en complexiteit van een model zijn momenteel

nog niet beschikbaar.

10

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

11 van 52

Tabel 2: Overzicht model tiers

Tier Lage complexiteit Gemiddelde Hoge complexiteit

complexiteit

Lage materialiteit Tier 3 Tier 3 Tier 2

Gemiddelde Tier 3 Tier 2 Tier 1

materialiteit

Hoge materialiteit Tier 2 Tier 1 Tier 1

De bepaalde model tier kan gebruikt worden als input voor het validatieplan en voor de model monitoring

planning en scope.

11

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

12 van 52

4 Rollen en verantwoordelijkheden

Dit hoofdstuk beschrijft de rollen en verantwoordelijkheden die horen bij het model risico management

raamwerk. De rollen vormen samen de governancestructuur van UWV. De governancestructuur wordt

visueel weergegeven in paragraaf 4.2. Paragraaf 4.3 beschrijft de verantwoordelijkheden voor elk van de

genoemde rollen in meer detail.

4.1 Overzicht van rollen in het model risico management raamwerk

Binnen het overzicht van rollen en verantwoordelijkheden wordt onderscheid gemaakt tussen

besluitvormingslinies en verdedigingslinies, waarbij dit document ingaat op de verdedigingslinies. Tabel 3

geeft een overzicht weer van de rollen van de verschillende verdedigingslinies in het model risico

management raamwerk.

Tabel 3: Overzicht verdedigingslinies model risico management raamwerk

Rol Functie Beschrijving

Directeur van Is verantwoordelijk voor de (kwaliteit

- -

desbetreffende van de) data in de bronsystemen die

divisie die data binnen de verantwoordelijkheid van de

Data eigenaar invoert divisie valt

Is verantwoordelijk voor het juiste

-

gebruik van de juiste data die binnen de

verantwoordelijkheid van de divisie valt

Directeur van Is eindgebruiker van het model en

- -

Model eigenaar desbetreffende bepaalt de vereisten van het model

Eerste

divisie

linie

Directeur Mag het model op dagelijkse basis

- -

Model gebruiker uitvoering of gebruiken en gebruikt de uitkomsten

portefeuillehouder van het model voor beslissingen

Hoofd R&I Ontwikkelt modellen op verzoek van de

- -

Model ontwikkelaar

model eigenaar

Hoofd R&I Is eigenaar van en beheert

- -

Model risico manager beleidsdocumenten binnen Model Risico

Management

BC&K’s van divisies Doet kwaliteitsmetingen op het gebruik

- -

van het model

Analyseert de uitkomsten van de

-

Tweede Model gebruik

toetsen op de aanwezigheid van een

linie kwaliteitstoets

menselijke bias/vooroordeel (het

toetsen maakt deel uit van externe

validatie)

12

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

13 van 52

Vooralsnog extern; Valideert of modellen geschikt zijn om

- -

te gebruiken

Model validator

Hoofd R&I Periodiek monitoren van modellen op

- -

basis van de monitoring metrieken

Model ontwikkelaar

(model)

BC&K dHH Controle op alle processtappen binnen

- -

elke fase van de modellevenscyclus

Model ontwikkelaar

(proces)

Hoofd R&I Monitort en overziet alle modellen en

- -

het model risico management raamwerk

Model risico manager

AD Voert interne audits, certificeringen en

- -

controles uit en monitort compliance

met relevante wet- en regelgeving en

Interne audit overige kaders en beleidsdocumenten

van UWV, onafhankelijk van de

projectactiviteiten die in de eerste en

tweede linie worden uitgevoerd

Derde

linie FG Toetst de

- -

Functionaris

gegevensbeschermingseffectbeoordeling

gegevensbescherming

(“GEB”) trajecten

Commisie Data- Toetsing van de risicoscan in lijn met de

- -

ethiek kaders en uitgangspunten uit het UWV-

Ethische toetsing

brede ethische kompas voor data-

toepassingen.

Toetsen of model risico management

-

Cliëntenraad activiteiten uitlegbaar zijn naar klanten

Externe

toe

advisering

Behandelt klachten van burgers over

-

en

Nationale onbehoorlijk optreden van UWV indien

toetsing

ombudsman de burger het geschil niet met UWV kan

oplossen

13

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

14 van 52

Autoriteit Controleert dat UWV zich aan de

-

persoonsgegevens privacywetgeving houdt

4.2 Governancestructuur

UWV heeft op basis van de rollen en verantwoordelijkheden beschreven in paragraaf 4, een overzicht van

weer4.

de twee besluitvormingslinies en vier verdedigingslinies ingericht. Figuur 2 geeft dit schematisch

Figuur 2: Overzicht verdedigingslinies UWV

4.3 Verantwoordelijkheden in het model risico management raamwerk

Deze paragraaf beschrijft de verschillende rollen binnen het model risico management raamwerk waarbij

onderscheid gemaakt wordt tussen besluitvormingslinies en verdedigingslinies. De eerste

besluitvormingslinie (coalitie risicoscans) besluit over (continuerend) gebruik van de modellen en de tweede

4De

externe auditor is ook belangrijk in de governancestructuur maar bepaalt zelf haar werkzaamheden

onafhankelijk van het model risico management beleid van UWV.

14

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

15 van 52

besluitvormingslinie (senior management en Directie) is eindverantwoordelijk voor voor de kwaliteit en het

uitvoeren van de model risico management werkzaamheden. Binnen de verdedigingslinies wordt

onderscheid gemaakt tussen vier linies. De eerste verdedigingslinie (data eigenaar, model eigenaar, model

gebruiker, model ontwikkelaar en model risico manager) doet kwaliteitsmetingen met betrekking tot het

bouwen van het model en het model risico management raamwerk. De tweede verdedigingslinie (model

gebruiker, model validator, model ontwikkelaar en model risico manager) identificeert, beoordeelt en

rapporteert over model risico’s, het uitgevoerde model gebruik en het naleven van het model risico

management raamwerk. De derde verdedigingslinie (interne audit, functionaris gegevensbescherming en

ethische toetsing) controleert de werking van het gehele raamwerk. De vierde verdedigingslinie (Autoriteit

persoonsgegevens, cliëntenraad, Nationale ombudsman) kunnen extern advies geven op vragen met

betrekking tot de modellen in het model risico management raamwerk.

Onderstaande beschrijvingen geven een beeld van de verantwoordelijkheden die horen bij bepaalde rollen.

De nadere uitwerking op meer detailniveau staat vermeld in de bijbehorende beleidsdocumenten.

4.3.1 Verantwoordelijkheden coalitie risicoscans (eerste besluitvormingslinie)

De coalitie risicoscans heeft de volgende verantwoordelijkheden binnen het model risico management

raamwerk:

Bespreken van informatie in de model inventaris zoals de model materialiteit, model kwaliteit,

-

Bias/uitgangspunten, etc.

Goedkeuren van model validaties (en daarmee goedkeuring van model gebruik)

-

Goedkeuring van uitgebreide monitoring inclusief de validatie op de uitgebreide monitoring

-

Goedkeuring van opgestelde actieplannen op basis van bevindingen uit model validatie,

-

(uitgebreide) model monitoring of interne audit

Goedkeuring voor continuerend modelgebruik naar aanleiding van bevindingen en resulterende

-

actieplannen uit uitgebreide monitoring

Goedkeuren en aanpassen van de jaarlijkse planning van validatieactiviteiten

-

Rapporteren van de uitkomsten van alle coalitie risicoscans vergaderingen naar senior

-

management en de directie

Goedkeuren van model initiatie voor nieuwe modellen

-

Goedkeuren van model ontmanteling

-

Bespreken (en waar nodig escaleren) van opgetreden modelincidenten

-

Goedkeuren en aanpassen van de jaarlijkse planning van ontwikkelingsactiviteiten

-

Keurt het model ontwikkelingsplan goed, inclusief het budget en de mankracht

-

Besluit of externe adviseurs zoals de cliëntenraad of de National ombudsman betrokken moeten

-

worden voor een model in gebruik genomen wordt

In de coalitie risicoscans zitten:

Directeur Handhaving

-

Directeur Uitkeren

-

Directeur Uitvoering WERKbedrijf

-

Directeur GegevensDiensten

-

Hoofd R&I

-

Model eigenaren die een andere functie hebben dan bovenstaande

-

Hoofd model validatie (pas relevant na opzetten validatiefunctie)

-

15

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

16 van 52

Medewerker Juridische Zaken

-

Op verzoek van de coalitie risicoscans kan de functionaris gegevensbescherming aansluiten om

advies te geven over vraagstukken rondom de algemene verordening gegevensbescherming (“AVG”).

De coalitie risicoscans neemt beslissingen op basis van consensus.

Verantwoordelijkheden5

4.3.2 data eigenaar (eerste verdedigingslinie)

De data eigenaar heeft de volgende verantwoordelijkheden binnen het modelrisico management raamwerk:

Is verantwoordelijk voor de (kwaliteit van de) data in de bronsystemen die binnen de

-

verantwoordelijkheid van de divisie valt

Is verantwoordelijk voor het juiste gebruik van de juiste data die binnen de verantwoordelijkheid

-

van de divisie valt.

Verantwoordelijkheden6

4.3.3 model eigenaar (eerste verdedigingslinie)

De model eigenaar heeft de volgende verantwoordelijkheden binnen het modelrisico management

raamwerk:

Is verantwoordelijk voor de geschiktheid van het model en de berekening van de output door het

-

model7

Is verantwoordelijk voor het juiste gebruik van het model

-

Houdt de informatie in de modelinventaris bij voor elk model waar de modeleigenaar

-

verantwoordelijk voor is en zorgt daarmee dat de informatie tijdig en accuraat is

Ziet toe dat het model de processen in de modellevenscyclus correct doorloopt (hoofdstuk 5)

-

Identificeert vervolgacties voor een model op basis van aanleidingen, zoals externe

-

gebeurtenissen of model validatie- en monitoringbevindingen

Is verantwoordelijk voor het maken en laten goedkeuren van actieplannen (inclusief het beheren

-

van het benodigde budget en de mankracht) op basis van bevindingen en aanbevelingen naar

aanleiding van een model validatie, (uitgebreide) model monitoring of interne audit

Is verantwoordelijk voor het opvolgen van goedgekeurde actieplannen die opgesteld zijn op basis

-

van de bevindingen van een model validatie, (uitgebreide) model monitoring of interne audit

Ziet toe dat per model een heldere beschrijving is van de werking en opbouw van het model

-

Ziet toe op het uitvoeren en actualiseren van de GEB

-

Vastleggen uitkomstmodel en eventuele vervolgacties als gevolg van deze uitkomst. Hier kan

-

over gerapporteerd worden

5

De verantwoordelijke is bevoegd om werkzaamheden te delegeren. Echter blijft de persoon wel

eindverantwoordelijk voor het uitvoeren van de werkzaamheden. Werkzaamheden die gedelegeerd zijn,

moeten worden gedocumenteerd in de model documentatie.

6

De verantwoordelijke is bevoegd om werkzaamheden te delegeren. Echter blijft de persoon wel

eindverantwoordelijk voor het uitvoeren van de werkzaamheden. Werkzaamheden die gedelegeerd zijn,

moeten worden gedocumenteerd in de model documentatie.

7

Sprake kan zijn van deeleigenaarschap waarbij andere personen verantwoordelijk zijn voor bijvoorbeeld

de correctheid van de data van het model of voor de statistische kwaliteit van het model. In zo’n

structuur blijft de modeleigenaar hoofdverantwoordelijke voor het model.

16

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

17 van 52

Verantwoordelijkheid om keuze te maken model te blijven gebruiken.

-

De model eigenaar moet een directeur zijn binnen UWV en moet bevoegd zijn om keuzes te maken over

mankracht en budget. Aan elk model in scope van dit beleidsdocument wordt een model eigenaar

toegewezen door de coalitie risicoscans.

4.3.4 Verantwoordelijkheden model gebruik kwaliteitstoets (eerste en tweede

verdedigingslinie)

De model gebruik kwaliteitstoets heeft de volgende verantwoordelijkheden binnen het model risico

management raamwerk:

Gebruikt het model conform het beoogde modelgebruik zoals vastgelegd in de model

-

documentatie

Rapporteert tijdig fouten in het model of andere observaties van het model aan de model

-

eigenaar en ter informatie naar de validatie afdeling en model risico manager

Documenteert hoe de model uitkomsten gebruikt zijn voor een bepaalde klant

-

Doet kwaliteitsmetingen op het gebruik van het model

-

bias/vooroordeel8.

Laat modellen toetsen op de aanwezigheid van een menselijke

-

Indien gewenst wordt onderscheid gemaakt tussen de dagelijkse gebruiker en de hoofdgebruiker.

a. De dagelijkse gebruiker gebruikt het model en rapporteert schriftelijk de model uitkomsten aan de

hoofdgebruiker

b. De hoofdgebruiker is verantwoordelijk voor beslissingen die worden genomen op basis van de

model uitkomsten indien deze verantwoordelijkheid niet bij de model eigenaar is belegd.

4.3.5 Verantwoordelijkheden model ontwikkelaar (eerste en tweede verdedigingslinie)

De model ontwikkelaar heeft de volgende verantwoordelijkheden binnen het model risico management

raamwerk:

Ontwikkelen van modellen conform het beleidsdocument en de standaarden voor de model

-

ontwikkeling van UWV

Uitvoeren (of uitbesteden) van ontwikkelingsactiviteiten conform de planning

-

Schrijven van model documentaties conform de model documentatietemplate

-

Periodiek monitoren van modellen op basis van de monitoring metrieken

-

Verstrekken van updates van de lopende ontwikkelingsactiviteiten aan het hoofd van het model

-

ontwikkelingsteam

Informeren van de coalitie risicoscans over de voortgang van model ontwikkelingstrajecten

-

Maken en opvolgen van actieplannen op basis van eigen bevindingen vanuit (uitgebreide)

-

monitoring.

8

Bias of Vooroordeel: Vooringenomenheid is een groot gewicht voor of tegen een idee of ding, meestal

op een manier die bevooroordeeld of oneerlijk is. Vooroordelen kunnen aangeboren of aangeleerd zijn.

Mensen kunnen vooringenomenheid ontwikkelen voor of tegen een individu, een groep of een

overtuiging.

17

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

18 van 52

Verantwoordelijk voor het controleren of de gedefinieerde processen binnen de verschillende

-

fasen van de modellevenscyclus, zoals gedefinieerd in hoofdstuk 5, volledig en juist worden

doorlopen.

In de context van een model validatie:

Opstellen van een model ontwikkelingspakket (zie sub paragraaf 0)

-

Beschikbaar zijn voor Q&A sessies met model validatoren

-

Opstellen van actieplannen op basis van bevindingen uit model validaties of interne audits

-

Opgestelde actieplannen laten goedkeuren door de coalitie risicoscans

-

Opvolgen van opgestelde actieplannen

-

Het hoofd van het model ontwikkelingsteam is daarnaast verantwoordelijk voor:

Opstellen van de jaarlijkse planning van ontwikkelingsactiviteiten in samenwerking met (de

-

voorzitter van) de coalitie risicoscans

Opstellen van de jaarlijkse planning van uitgebreide monitorings in samenwerking met alle

-

belanghebbenden

Goedkeuren van model ontwikkelingspakket.

-

4.3.6 Verantwoordelijkheden model validator (tweede verdedigingslinie)

De model validator heeft de volgende verantwoordelijkheden binnen het model risico management

raamwerk:

Uitvoeren (of uitbesteden) van validatiewerkzaamheden, zoals model validaties en validaties van

-

uitgebreide monitoringsrapporten, conform de planning, het beleidsdocument en de standaarden

voor model validatie van UWV

Externe toetsing van het model

-

Opstellen van een validatieplan conform het beleidsdocument en de standaarden voor model

-

validatie

Opstellen van een validatierapport conform het model validatie rapporttemplate

-

Verstrekken van updates van de lopende validatie-activiteiten aan het hoofd van het model

-

validatieteam

De exacte invulling van de validatiefunctie is op dit moment nog niet bepaald. De validatiefunctie zal in

een later stadium, zodra voldoende modellen beschikbaar zijn, bepaald worden vanwege de benodigde

functiescheiding, waarbij ook de rol als hoofd validatie dient te worden ingevuld.

Het hoofd van het model validatieteam is daarnaast verantwoordelijk voor:

Goedkeuren van een validatieplan

-

Coördineren van model validaties die door derde partijen gedaan worden volgens het

-

beleidsdocument en de standaarden van model validatie (hoofdstuk 6)

Opstellen van de jaarlijkse planning van validatieactiviteiten in samenwerking met (de voorzitter

-

van) de coalitie risicoscans

Presenteren van de (concept) validatierapporten en adviseren van de coalitie risicoscans over het

-

model oordeel

Informeren aan de coalitie risicoscans over de status van open bevindingen en aanbevelingen uit

-

reeds uitgevoerde validaties.

18

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

19 van 52

4.3.7 Verantwoordelijkheden model risico manager (eerste en tweede verdedigingslinie)

De model risico manager heeft de volgende verantwoordelijkheden binnen het model risico management

raamwerk:

Houdt alle model risicodocumenten (zie ook hoofdstuk 6) bij en communiceert met de coalitie

-

risicoscans en het senior management en de directie indien wijzigingen nodig zijn

Houdt toezicht op de dagelijkse uitvoering en invulling van het model risico management beleid

-

## UWV9

binnen

Rapporteert periodiek aan de coalitie risicoscans en aan senior management en de directie over

-

individuele en geaggregeerde modelrisico’s en andere modelrisico informatie binnen UWV

Houdt model incidenten bij

-

Stuurt het model risico management beleid aan voor alle modellen in scope van het model risico

-

management raamwerk

Adviseren over risico mitigerende maatregelen over de gehele modellevenscyclus

-

Monitoren dat observaties gevonden in model validaties en interne audit op tijd geadresseerd zijn

-

door eigenaren van de goedgekeurde actieplannen

Monitoren dat modellen tijdig (periodiek) gevalideerd worden

-

Monitoren dat modellen periodiek gemonitord worden door model ontwikkelaar en toeziet dat de

-

juiste processen worden geïnitieerd indien een model minder goed functioneert

Toezicht houden op de naleving van de beleidsdocumenten met betrekking tot het risico

-

management beleid.

4.3.8 Verantwoordelijkheden interne audit (derde verdedigingslinie)

Het interne audit team is zelf verantwoordelijk voor het opstellen van hun audit- en controleprocessen

langs de as van bestaande UWV protocollen, waaronder ISO en overige standaarden. Het interne audit

team dient wel een jaarlijkse planning op te stellen voor hun audit- en controleprocessen.

4.3.9 Verantwoordelijkheden functionaris gegevensbescherming (derde verdedigingslinie)

De functionaris gegevensbescherming heeft de volgende verantwoordelijkheden binnen het model risico

management raamwerk:

Toetst onafhankelijk de GEB rapporten.

-

4.3.10 Verantwoordelijkheden Ethische toetsing (derde verdedigingslinie)

De Etische toetsing adviseert UWV gevraagd en ongevraagd over (ethische) keuzes in modellen.

4.3.11 Verantwoordelijkheden cliëntenraad (externe advisering en toetsing)

De cliëntenraad heeft de volgende verantwoordelijkheid binnen het model risico management raamwerk:

Kan input geven op specifieke modellen of dat model risico management activiteiten transparant

-

en uitlegbaar zijn naar UWV’s klanten

Kan zelfstandig, ongevraagd en proactief advies geven op het gehele proces van MRM en

-

specifieke modellen.

9

Bijvoorbeeld: houden alle andere rollen zich aan hun specifieke verantwoordelijkheden.

19

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

20 van 52

4.3.12 Verantwoordelijkheden Nationale ombudsman (externe advisering en toetsing)

De Nationale ombudsman heeft de volgende verantwoordelijkheid binnen het model risico management

raamwerk:

Behandelt klachten van burgers over onbehoorlijk optreden van UWV indien de burger het geschil

-

niet met UWV kan oplossen.

4.3.13 Verantwoordelijkheden autoriteit persoonsgegevens (externe advisering en toetsing)

De autoriteit persoonsgegevens heeft de volgende verantwoordelijkheden binnen het model risico

management raamwerk:

Beoordeelt in hoeverre UWV zich aan de privacywetgeving houdt

-

Behandelt privacyklachten van personen.

-

20

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

21 van 52

5 Modellevenscyclus

De modellevenscyclus beschrijft alle stappen in het leven van een model. De modellevenscyclus begint bij

het idee voor een nieuw model en eindigt bij het ontmantelen van een model. In dit hoofdstuk wordt

beschreven welke stappen gedefinieerd zijn in de modellevenscyclus van UWV en welke processen bij elk

van de stappen in de modellevenscyclus horen.

5.1 Stappen in de modellevenscyclus

UWV heeft een modellevenscyclus gedefinieerd die bestaat uit acht stappen. Tabel 4 geeft een overzicht

weer van de stappen in de modellevenscyclus. Figuur 3 geeft een grafisch overzicht weer van de

modellevenscyclus. De modellevenscyclus is sequentieel maar in de modellevenscyclus zijn stappen waar

het mogelijk is om een stap terug te gaan. Zo kunnen tijdens model ontwikkeling zaken naar voren komen,

waardoor het model terug moet naar de stap model initiatie. Als een model gevalideerd wordt en afgekeurd

wordt, zal het model terug moeten naar de stap model ontwikkeling. Wanneer een model goedgekeurd

mag worden, kunnen implementatiefouten aan het licht komen. Dan zal het model terug moeten naar de

stap model implementatie en testen. Zodra het model in gebruik genomen wordt, moet het model ook

gemonitord worden, waardoor het model tussen de stappen model gebruik en model monitoring beweegt.

In de volgende sub paragrafen worden de procedures per stap in de modellevenscyclus gedefinieerd

inclusief de verantwoordelijken. De verantwoordelijke is bevoegd om werkzaamheden te delegeren. Echter

blijft de persoon wel eindverantwoordelijk voor het uitvoeren van de werkzaamheden.

Tabel 4: Stappen in de modellevenscyclus

Stap Beschrijving

Specificatie en goedkeuring voor model initiatie

-

Uitvoeren model definitie checklist om de modellen te

-

1. Model initiatie en wijziging onderscheiden van niet-modellen

Uitvoering GEB

-

Uitvoering doelstellingen

-

Ontwikkeling van het model, methodologie, aannames en

-

datakwaliteit

2. Model ontwikkeling

Goedkeuring voor model door de model eigenaar

-

## GEB10

Finalisatie

-

Validatie (initieel of periodiek) van het model

-

Onderzoek naar eventuele bias/vooroordelen in de

-

3. Model validatie

uitgangspunten en periodiek aan de hand van de resultaten

Advisering over het model oordeel

-

10

Het finaliseren van de GEB is een iteratief proces waarin de afdeling R&I en uitvoering bij elkaar komen.

21

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

22 van 52

Implementatie en testen van het model gebaseerd op de

-

gevalideerde en goedgekeurde methodologie conform het

4. Model implementatie en

beleidsdocument voor model implementatie

testen

Onderzoek naar eventuele bias/vooroordelen in de

-

uitgangspunten aan de hand van de resultaten

Goedkeuring op model gebruik voor het vastgestelde gebruik

-

5. Model goedkeuring

door de relevante organen

Vaststelling dat het model gebruikt wordt voor de

-

goedgekeurde doeleinden conform het model gebruik

beleidsdocument

6. Model gebruik beoordeeling of de GEB op basis van model specifieke

-

metrieken wordt nageleefd

Controleren dat aan het minimaal aantal random

-

beoordelingen voldaan wordt

Monitoring van onder andere model kwaliteit, model gebruik,

-

prestaties, complexiteit en datakwaliteit conform het model

monitoring beleidsdocument

7. Model monitoring

Onderzoek naar eventuele bias/vooroordelen in de

-

uitgangspunten aan de hand van de resultaten

Initiatie van een model wijziging indien nodig

-

Intrekken van gebruik van het model (of een specifieke versie

-

8. Model ontmanteling

daarvan)

22

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

23 van 52

Figuur 3: De acht stappen in de modellevenscyclus

5.1.1 Model initiatie en wijziging

In deze stap van de modellevenscyclus wordt een besluit genomen om een nieuw model of nieuwe model

versie te ontwikkelen, waarbij onder andere gekeken wordt naar noodzaak en waarde. In Tabel 5 en

23

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

24 van 52

Tabel 6 worden beschreven welke procedures uitgevoerd dienen te worden en wie daar verantwoordelijk

voor zijn.

Tabel 5: Procedures model initiatie

Stap 1a. Model initiatie

Procedures Verantwoordelijke

Model definitie Invullen checklist model definitie Model eigenaar

- -

Invullen model initiatieformulier Model eigenaar

- -

Voorstel voor model tier

-

Model

initiatieformulier

Goedkeuren model initiatieformulier Coalitie risicoscans

- -

en GEB

Uitvoeren GEB-proces Model eigenaar

- -

Model inventaris Invullen verplichte velden model inventaris Model eigenaar

- -

24

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

25 van 52

Figuur 4: Schematische weergave procedures voor model initiatie

25

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

26 van 52

Tabel 6: Procedures model wijziging

Stap 1b. Model wijziging

Procedures Verantwoordelijke

Invullen model wijzigingsformulier Model eigenaar

- -

Model Goedkeuren model wijzigingsformulier Coalitie risicoscans

- -

wijzigingsformulier inclusief de classificatie van de model wijzing

en GEB (kleine wijziging of grote wijziging)

Aanpassen GEB Model eigenaar

- -

Wijzigen model informatie in de model Model eigenaar

- -

Model inventaris

inventaris

Figuur 5: Schematische weergave procedures voor model wijziging

26

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

27 van 52

5.1.2 Model ontwikkeling

In deze stap van de modellevenscyclus wordt het model ontwikkeld inclusief de model dataset, het ontwerp,

de methodologie en de aannames. In onderstaande tabel wordt beschreven welke procedures uitgevoerd

dienen te worden en wie daar verantwoordelijk voor zijn.

Tabel 7: Procedures voor model ontwikkeling

Stap 2. Model ontwikkeling

Procedures Verantwoordelijke

Aanwijzen van het hoofd voor Model eigenaar

- -

ontwikkeling van het model en

model ontwikkelaar(s)

Vaststellen modelvereisten en

-

Intake

daarbij horende data vereisten

Toestemming verkrijgen bij data

-

eigenaar voor het gebruik van de

data

Toets op de beschikbaarheid van Model eigenaar

- -

noodzakelijke data

Toets op de datakwaliteit

-

noodzakelijke (input) data

conform het datakwaliteit

raamwerk

GEB check en eventueel GEB

-

Opstellen van datakwaliteit Model eigenaar

- -

documentatie in de datakwaliteit

documentatie template

Dataset ontwikkeling

Samenstellen van de model Model ontwikkelaar

- -

dataset en vastleggen van het

data collectie proces conform het

beleidsdocument model dataset

ontwikkeling

Vaststellen van de datakwaliteit

-

van de model dataset conform het

datakwaliteit raamwerk

Opstellen van model dataset Model ontwikkelaar

- -

constructie en model datakwaliteit

documentatie in de model dataset

27

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

28 van 52

constructie en datakwaliteit

documentatie template

Goedkeuren model dataset - Hoofd model ontwikkeling

-

inclusief documentatie voor

modelontwikkeling

Schrijven van het model Hoofd model ontwikkeling

- -

ontwikkelingsplan op basis van het

model initiatieformulier / model

Model Ontwikkelingsplan

wijzigingsformulier

-

Goedkeuren van ontwikkelingsplan Model eigenaar

- -

Ontwikkelen van het model - Hoofd model ontwikkeling

conform het beleidsdocument

model ontwikkeling en de

standaarden voor model

ontwikkeling

Ontwikkelen van monitoring testen Hoofd model ontwikkeling

- -

Controleren van monitoring testen Model validator

- -

Model Ontwikkeling

Opstellen van de model Model ontwikkelaar

- -

documentatie in de model

documentatie template

Opstellen en afronden GEB Hoofd model ontwikkeling

- -

Afgeronde GEB goedkeuren Functionaris

- -

Gegevensbescherming

Voorbereiden van het model Model ontwikkelaar

- -

ontwikkelingspakket, bestaande

ten minste uit:

a. Datakwaliteit documentatie

b. Model documentatie

c. Kalibratiecode

d. Handleiding voor de

Model ontwikkelingspakket

kalibratiecode

e. Model dataset constructie en

datakwaliteit documentatie

f. Dataset van het model

g. Presentaties en notulen van

expert sessies

h. GEB

28

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

29 van 52

Goedkeuren van model Hoofd model ontwikkeling

- -

ontwikkelingspakket

Ontwikkelingspakket opsturen Model ontwikkelaar

- -

naar de model validator(en)

Figuur 6: Schematische weergave procedures voor model ontwikkeling

5.1.3 Model validatie

In deze stap van de modellevenscyclus wordt het model gevalideerd volgens het beleidsdocument en de

standaarden voor model validatie. Het doel van een validatie is om te analyseren of een model geschikt is

voor het beoogde gebruik. Een model validator dient onafhankelijk te zijn van het model

ontwikkelingsproces. In onderstaande tabel wordt beschreven welke procedures uitgevoerd dienen te

worden en wie daar verantwoordelijk voor zijn. Aangezien de validatiefunctie nog niet is ingevuld wordt

onderscheid gemaakt tussen een intern ingevulde validatiefunctie en een externe validatie.

29

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

30 van 52

Tabel 8: Procedures voor interne model validatie functie

Stap 3. Model validatie

Procedures Verantwoordelijke

Intake Aanwijzen model validator(en) Hoofd model validatie

- -

Schrijven van het model validatieplan op basis Model validator

- -

van de type validatie (initieel, periodiek of op

wijziging gebaseerd), inclusief de

Validatieplan

validatieprocedures

Goedkeuren van validatieplan Hoofd model validatie

- -

Bepaalt definitieve model tier Hoofd model validatie

- -

Uitvoeren van validatieprocedures Model validator

- -

Validatie

Opstellen van het model validatierapport in de Model validator

- -

model validatierapport template

Voorbereiden van het model validatiepakket, Model validator

- -

bestaande ten minste uit:

Model validatierapport

-

Q&A template

-

Model

Advies model oordeel

-

validatiepakket

Goedkeuren van model validatiepakket Hoofd model validator

- -

Validatiepakket opsturen naar de coalitie Model validator

- -

risicoscans

Model oordeel Besluiten of het model geïmplementeerd mag Coalitie risicoscans

- -

worden

30

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

31 van 52

Figuur 7: Schematische weergave procedures voor model validatie

31

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

32 van 52

Tabel 9: Procedures voor externe model validatie

Stap 3. Model validatie

Procedures Verantwoordelijke

Intake Aanwijzen model validator(en) Coalitie risicoscans

- -

Schrijven van het model validatieplan op basis Externe validator

- -

van de type validatie (initieel, periodiek of op

wijziging gebaseerd), inclusief de

Validatieplan

validatieprocedures

Goedkeuren van validatieplan Coalitie risicoscans

- -

Uitvoeren van validatieprocedures Externe validator

- -

Validatie

Opstellen van het model validatierapport in de Externe validator

- -

model validatierapport template

Voorbereiden van het model validatiepakket, Externe validator

-

bestaande ten minste uit:

Model validatierapport

-

Q&A template

-

Model

Advies model oordeel

-

validatiepakket

Goedkeuren van model validatiepakket Coalitie risicoscans

- -

Validatiepakket opsturen naar de coalitie Externe validator

- -

risicoscans

Model oordeel Besluiten of het model geïmplementeerd mag Coalitie risicoscans

- -

worden

32

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

33 van 52

Figuur 8: Schematische weergave procedures voor externe model validatie

33

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

34 van 52

5.1.4 Model implementatie en testen

In deze stap van de modellevenscyclus wordt het model geïmplementeerd en getest gebaseerd op de

gevalideerde en goedgekeurde methodologie. Model implementatie en testen worden uitgevoerd volgens

het OTAP proces binnen UWV. In onderstaande tabel wordt beschreven welke procedure uitgevoerd dient

te worden en wie daar verantwoordelijk voor is.

Tabel 10: Procedure model implementatie en testen

Stap 4. Model implementatie en

testen

Procedures Verantwoordelijke

Stappen doorlopen zoals beschreven in het Hoofd model ontwikkeling

- -

## OTAP11 FAT12, GAT13,

proces (zoals installeren

Implementatie van het model in de productie omgeving, etc.)

en testen Toetsen testresultaten met de GEB

-

Toetsen testresultaten met model uitkomsten

-

voor implementatie

5.1.5 Model goedkeuring

In deze stap van de modellevenscyclus wordt het model (conditioneel) goedgekeurd om te gebruiken voor

het vastgestelde gebruik door de relevante organen (coalitie risicoscans of een extern adviesorgaan). Een

conditionele goedkeuring kan gegeven worden indien concrete actieplannen zijn voor nog openstaande

tekortkomingen die een lage impact hebben. De conditionele goedkeuring vindt plaats op het model

inclusief de actieplannen, waarbij de goedkeuring ingetrokken wordt wanneer de actieplannen niet

uitgevoerd zijn binnen de afgesproken termijn. In onderstaande tabel wordt beschreven welke procedure

uitgevoerd dient te worden en wie daar verantwoordelijk voor is.

Tabel 11: Procedures model goedkeuring

Stap 5. Model goedkeuring

Procedures Verantwoordelijke

Identificeren of extern advies (van bijvoorbeeld Coalitie risicoscans

- -

Identificatie

de nationale ombudsman, de cliëntenraad, etc.)

extern advies

nodig is voor (aspecten van) het model

11

Ontwikkeling, test, acceptatie en productie. Het OTAP beleid van UWV moet nog vertaald worden voor

de risicomodellen, omdat bij het ontwikkelen van de modellen al gebruik gemaakt wordt van productie

data.

12

Functional acceptance test

13

Gebruikersacceptatietest

34

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

35 van 52

Model Verzamelen benodigde model informatie voor Model ontwikkelaar

- -

gebruikspakket de externe partij

Verwerken feedback externe partij Model ontwikkelaar

- -

Goedkeuring

(Conditioneel) goedkeuren van het gebruik van Coalitie risicoscans

- -

model

het model

35

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

36 van 52

Figuur 9: Schematische weergave procedures voor model goedkeuring

36

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

37 van 52

5.1.6 Model gebruik

In deze stap van de modellevenscyclus wordt vastgesteld of het model gebruikt wordt voor de

goedgekeurde doeleinden en wordt beoordeeld of de GEB op basis van model specifieke metrieken wordt

nageleefd. Ook wordt gemonitord dat, naast beoordelingen op basis van modeluitkomsten, voldoende

random geselecteerde beoordelingen plaatsvinden om vooringenomenheid te minimaliseren. In de

specifieke modeldocumentatie staat gespecificeerd wat precies onder voldoende verstaan wordt. In

onderstaande tabel wordt beschreven welke procedure uitgevoerd dient te worden en wie daar

verantwoordelijk voor is.

Tabel 12: Procedures model gebruik

Stap 6. Model gebruik

Procedures Verantwoordelijke

Controleren of voldoende random geselecteerde Model eigenaar

- -

cases meegenomen worden in het gebruik

Controleren van modeluitkomsten met vier Model gebruiker

- -

Controleren

ogenprincipe

model gebruik

Monitoren of het model gebruikt wordt Model eigenaar

- -

waarvoor het model ontwikkeld en goedgekeurd

is

37

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

38 van 52

Figuur 10: Schematische weergave procedures voor model gebruik

5.1.7 Model monitoring

In deze stap van de modellevenscyclus wordt het model gemonitord op verschillende facetten zoals model

kwaliteit, prestaties, materialiteit, complexiteit en datakwaliteit. Ook de feedback van gebruikers en

eventuele bezwaren van mogelijke slachtoffers zijn onderdeel van de monitoring. Binnen het model

monitoring beleidsdocument wordt onderscheid gemaakt tussen een normale monitoring en een uitgebreide

monitoring, waarbij jaarlijks minimaal een model monitoring uitgevoerd dient te worden. In de model

monitoring levenscyclusstap kan een model wijziging geïnitieerd worden. In onderstaande tabel wordt

beschreven welke procedure uitgevoerd dient te worden en wie daar verantwoordelijk voor is.

38

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

39 van 52

Tabel 13: Procedures model monitoring

Stap 7. Model monitoring

Procedures Verantwoordelijke

Selecteren van de modellen voor monitoring Hoofd model ontwikkeling

- -

Bepaling van het type monitoring en aantal Hoofd model ontwikkeling

- -

monitoringen per model (normaal en

Monitoring uitgebreid) in een bepaalde termijn

Resultaten opslaan en verwerken in het model Model ontwikkelaar

- -

monitoring rapport in het desbetreffende

model monitoring template

Voorbereiden van het model Model ontwikkelaar

- -

monitoringspakket, bestaande ten minste uit:

i. Model monitoring rapport

j. Code model monitoring testen

Model

k. Model monitoring dataset constructie en

monitoringsspakket

datakwaliteit documentatie

(alleen bij

l. Model monitoring dataset

uitgebreide

m. Presentaties en notulen van expert sessies

monitoring)

Goedkeuren van model monitoringspakket Hoofd model ontwikkeling

- -

Monitoringspakket opsturen naar de model Model ontwikkelaar

- -

validator(en)

Monitoring Controleren monitoring uitkomsten Model validator

- -

validatie

Model oordeel Besluiten of het model in gebruik mag blijven Model eigenaar

- -

Model wijziging Initiëren model wijziging of ontmanteling Model eigenaar

- -

39

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

40 van 52

Figuur 11: Schematische weergave procedures voor model monitoring

40

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

41 van 52

5.1.8 Model ontmanteling

In deze stap van de modellevenscyclus wordt het model gebruik ingetrokken. Een model kan pas worden

ingetrokken wanneer wordt besloten door de coalitie risicoscans om geen gebruik meer te maken van het

model of indien een nieuwe model versie is goedgekeurd door de coalitie risicoscans. In onderstaande tabel

wordt beschreven welke procedure uitgevoerd dient te worden en wie daar verantwoordelijk voor is.

Tabel 14: Procedures model ontmanteling

Stap 8. Model ontmanteling

Procedures Verantwoordelijke

Opstellen model ontmantelingsformulier Model ontwikkelaar

- -

inclusief besluit archivering model

Model

ontmantelings-

Goedkeuren model ontmanteling Coalitie risicoscans

- -

formulier

Model ontmantelen Model eigenaar

- -

41

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

42 van 52

Figuur 12: Schematische weergave procedures voor model ontmanteling

42

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

43 van 52

6 Documenten raamwerk

Deze paragraaf beschrijft de documenten die onderdeel uitmaken van het model risico management

raamwerk van UWV. Tabel 15 geeft hoogover weer welke documenten per stap in de modellevenscyclus

zijn en Tabel 16 beschrijft de thema’s van elk document.

6.1 Overzicht documenten raamwerk

Voor elk levenscyclus stap worden documenten ontwikkeld die met meer details beschrijven welke

processen gevolgd moeten worden (beleidsdocumenten), hoe de processen uitgevoerd moeten worden

(standaarden) of helpen het werk te standaardiseren (formulieren, templates, etc.). De onderstaande

tabellen geeft een overzicht van de documenten die onderdeel gaan uitmaken van het model risico

management raamwerk van UWV en de inhoud van de documenten.

Tabel 15: Overzicht documenten

Levenscyclus stap Documenten Eigenaar

Beleidsdocument model risico

-

Model risico manager

-

management (dit document)

Overkoepelend

Beleidsdocument datakwaliteit Model risico manager

- -

Beleidsdocument model wijziging Model risico manager

- -

Model initiatieformulier Model eigenaar

- -

1. Model initiatie

en wijziging

Model wijzigingsformulier Model eigenaar

- -

Ingevulde GEB (standaard UWV) Model eigenaar

- -

Beleidsdocument model dataset Hoofd model

- -

constructie ontwikkeling

Beleidsdocument model datakwaliteit Hoofd model

- -

ontwikkeling

Beleidsdocument model ontwikkeling Hoofd model

- -

ontwikkeling

2. Model

ontwikkeling

Standaarden model ontwikkeling Hoofd model

- -

ontwikkeling

-

Template model documentatie Hoofd model

- -

ontwikkeling

Model documentatie Hoofd model

- -

ontwikkeling

43

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

44 van 52

Beleidsdocument model validatie Hoofd model validatie

- -

Standaarden model validatie Hoofd model validatie

- -

3. Model

validatie

Template model validatierapport Hoofd model validatie

- -

Model validatierapport Hoofd model validatie

- -

4. Model Beleidsdocument model implementatie Model risico manager

- -

implementatie

Test rapport Model eigenaar

- -

en testen

Beleidsdocument model goedkeuring Model risico manager

- -

5. Model

Beslisboom raadplegen extern advies Model risico manager

- -

goedkeuring

Checklist model goedkeuring Model eigenaar

- -

6. Model gebruik Beleidsdocument model gebruik Model risico manager

- -

Beleidsdocument model monitoring Hoofd model

- -

ontwikkeling

7. Model

monitoring

Standaarden model monitoring Hoofd model

- -

ontwikkeling

8. Model Model ontmantelingsformulier Model eigenaar

- -

ontmanteling

Tabel 16: Beschrijving documenten per stap in de modellevenscyclus

Stap Overkoepelend

Beschrijving

Beleidsdocument model risico Huidig document

-

management

Management samenvatting

-

Model context en doeleinde

-

Beschrijving doelgroep

-

Model keuzes

-

Data

-

Model methodologie

-

Model documentatie

Model aannames en expert judgement

-

Model kalibratie, prestatie indicatoren en resultaten

-

Model testen

-

Model limitaties

-

Model implementatie

-

Compliance met relevante regelgeving / kaders

-

44

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

45 van 52

Managemant samenvatting

-

Context en doeleinde

-

Beleidsdocument datakwaliteit Dimensies van datakwaliteit

-

Uit te voeren testen per datakwaliteit dimensie

-

Compliance met relevante regelgeving / kaders

-

Stap 1. Model initiatie en wijziging

Beschrijving

Typen model wijzigingen

-

Beleidsdocument model

Kleine wijziging versus een grote wijziging

-

wijziging

Proces model wijziging

-

Model doeleinde(n)

-

Model scope

-

Model initiatieformulier Verwachte impact model

-

Argumentatie voor het model

-

Verwachte limitaties model

-

Model trigger

-

Reden van wijziging

-

Beschrijving wijziging

-

Model wijzigingsformulier

Model materialiteit

-

Verwachte impact

-

Classificatie wijziging (kleine wijziging of grote wijziging)

-

Beschrijving van de (voorgenomen) gegevensverwerking

-

Rechtmatigheid van de gegevenswerking

-

## GEB

Inventarisatie van risico’s en mitigerende maatregelen

-

Acceptatie van de restrisico’s door modeleigenaar

-

Stap 2. Model ontwikkeling

Beschrijving

Managemant samenvatting

-

Context en doeleinde

-

Beschrijving datastroom van brondata naar model dataset

-

Beleidsdocument model

Governance binnen de datastroom

-

dataset constructie

Beschrijving datakwaliteit brondata

-

Beschrijving datakwaliteit model dataset

-

Dataset constructiestappen en code

-

Managemant samenvatting

-

Beleidsdocument model

Context en doeleinde

-

datakwaliteit

Dimensies van datakwaliteit

-

45

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

46 van 52

Uit te voeren testen per datakwaliteit dimensie

-

Compliance met relevante regelgeving / kaders

-

Modeleigenaarschap

-

Modelontwikkelingstraject (van model initiatie tot aan model

-

Beleidsdocument model

herontwikkeling)

ontwikkeling

Rollen en verantwoordelijkheden

-

Vendor en andere modellen van derden

-

Welke modellen gebruikt mogen worden

-

Standaarden model Welke criteria gebruikt moeten worden om tot een model keuze te

-

ontwikkeling komen

Inrichting expert judgement proces

-

Wordt door model ontwikkelaars gebruikt voor het opstellen van

-

model documentatie

Template model ontwikkeling

Zorgt ervoor dat de model documentatie consistent en compleet is

-

voor alle modellen

Stap 3. Model validatie

Beschrijving

Beoordeling model materialiteit en model complexiteit

-

Validatie domeinen en verantwoordelijken voor elk domein

-

Beleidsdocument model Type model validaties

-

validatie Model validatieproces

-

Impact model tier op validatieproces

-

Onafhankelijkheid van een model validatie

-

Gedetailleerde validatieprocedures per validatie domein

-

Standaarden model validatie

Wordt gebruikt voor het opstellen van een model validatierapport

-

Template model

Zorgt ervoor dat het model validatierapport consistent is voor alle

-

validatierapport

model validaties

Stap 4. Model implementatie en testen

Beschrijving

Beleidsdocument model OTAP proces en verantwoordelijkheden

-

implementatie

Model testen in productie-omgeving

-

Test rapport

Stap 5. Model goedkeuring

46

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

47 van 52

Beschrijving

Beleidsdocument model Goedkeuringsproces

-

goedkeuring Wanneer extern advies vragen

-

Beslisboom raadplegen Vragenlijst om te bepalen of extern advies moet worden

-

extern advies

Overzicht van vragen die beantwoord moeten worden voordat een

-

Checklist model goedkeuring

model goedgekeurd kan worden, inclusief bijbehorende documenten

Stap 6. Model gebruik

Beschrijving

Vier ogenprincipe voor modeluitkomsten

-

Beleidsdocument model

gebruik

Monitoren model gebruik

-

Stap 7. Model monitoring

Beschrijving

Type van monitorings

-

Frequentie van monitoren

-

Beleidsdocument model

Domeinen model monitoring

-

monitoring

Proces model monitoring en verantwoordelijkheden

-

Impact model tier op monitoring

-

Standaarden model Metrieken monitoring

-

monitoring Drempelwaarden metrieken monitoring

-

Stap 8. Model ontmanteling

Beschrijving

Model Argumentatie waarom model wordt ontmanteld

-

ontmantelingsformulier

47

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

48 van 52

7 Model inventaris

Dit hoofdstuk beschrijft uit welke componenten de model inventaris bestaat en wat de minimale informatie

is die in de model inventaris moet worden opgenomen indien een model initiatie is goedgekeurd of wanneer

een model een wijziging ondergaat.

7.1 Componenten model inventaris

De model inventaris bestaat uit de volgende componenten:

1) Model lijst: overzicht van alle modellen in scope van het model risico management raamwerk

2) Model validaties lijst: Overzicht van alle uitgevoerde model validaties van de modellen in de model

lijst

3) Model bevindingen lijst: Overzicht van alle validatie- en monitoring bevindingen van de modellen

in de model validaties lijst

4) Model monitoring lijst: Overzicht van de laatste (goedgekeurde) (uitgebreide) monitoring van alle

modellen

5) Documenten lijst: Lijst met alle model risico documenten en documentatie van de modellen in

scope van het model risico management raamwerk

Als een model initiatie is goedgekeurd dient de model eigenaar de model informatie te verwerken in de

model lijst. De minimale informatie die de model eigenaar moet invullen is:

Model naam

-

Model eigenaar

-

Afdeling model eigenaar

-

Model type

-

Model gebruik

-

Model gebruiker

-

Afdeling model gebruiker

-

(Voorlopige) model materialiteit

-

(Voorlopige) model complexiteit

-

(Voorlopige) model tier

-

Acceptatie van de uitlegbaarheid

-

De rest van de gegevens in de model inventaris worden ingevuld zodra de informatie beschikbaar is.

48

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

49 van 52

8 Rapportage

Dit hoofdstuk beschrijft welke typen rapportages ten aanzien van model risico management zullen

worden ontwikkeld met op hoofdlijnen de inhoudsopgave van elk rapport.

8.1 Typen model risico management rapportages

Er worden drie typen rapportages ontwikkeld omtrent model risico management binnen UWV. De

rapportages zijn uiteengezet in onderstaande tabel.

Tabel 17: Overzicht model risico management rapportages

Rapportage Inhoud Frequentie

Overzicht van modellen inclusief: Elke vier

-

Tier maanden

-

Model kwaliteit

-

Modellen in gebruik, inclusief mogelijke

-

Rapportage voor de groepsraad

incidenten of opmerkingen

Toelichting op model risico

-

management werkzaamheden

afgelopen 4 maanden

Ten minste: Elke maand

-

Overzicht van modellen inclusief:

-

Materialiteit

-

Complexiteit

-

Tier

-

Model kwaliteit

-

Levenscyclusstap

-

Waarden monitoring metrieken

-

Algemene model risico Toelichting op model risico

-

management rapportage management werkzaamheden

afgelopen maand

Laatste status van het model risico

-

management raamwerk

Overkoepelende factoren op de

-

modellen of landschap

Status model validaties, inclusief

-

Overzicht openstaande bevindingen en

-

vervaldata

Overzicht van modellen inclusief: Elke vier

- -

Tier maanden

-

Rapportage voor functionarissen

Model kwaliteit

-

persoonsgegevens

Modellen in gebruik, inclusief mogelijke

-

incidenten of opmerkingen

49

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

50 van 52

Overzicht van de statussen van de

-

GEB’s inclusief einddata GEB’s

50

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

51 van 52

Appendices

Appendix 1 – Verklarende woordenlijst

Tabel 18: Lijst van afkortingen gebruikt in dit document

Afkorting Beschrijving

AVG Algemene verordening gegevensbescherming

GEB Gegevensbeschermingseffectbeoordeling

51

Beleidsdocument model

risico management

Datum

29 september 2021

Versie

1.2

Pagina

52 van 52

Appendix 2 – Lijst van tabellen en figuren

Tabel 1: Checklist model definitie ................................................................................................... 8

Tabel 2: Overzicht rollen model risico management raamwerk ............... Error! Bookmark not defined.

Tabel 3: Stappen in de modellevenscyclus ..................................................................................... 21

Tabel 4: Procedures model initiatie ............................................................................................... 24

Tabel 5: Procedures model wijziging ............................................................................................. 26

Tabel 6: Procedures voor model ontwikkeling ................................................................................. 27

Tabel 7: Procedures voor model validatie ....................................................................................... 30

Tabel 8: Procedure model implementatie en testen ......................................................................... 34

Tabel 9: Procedures model goedkeuring ........................................................................................ 34

Tabel 10: Procedures model gebruik ............................................................................................. 37

Tabel 11: Procedures model monitoring ......................................................................................... 39

Tabel 12: Procedures model ontmanteling ..................................................................................... 41

Tabel 13: Overzicht model tiers .......................................................... Error! Bookmark not defined.

Tabel 14: Overzicht documenten .................................................................................................. 43

Tabel 15: Beschrijving documenten per stap in de modellevenscyclus ............................................... 44

Tabel 16: Overzicht model risico management rapportages .............................................................. 49

Tabel 17: Lijst van afkortingen gebruikt in dit document .................................................................. 51

Figuur 1: Definitie van een model ................................................................................................... 7

Figuur 2: Overzicht four lines of defence model UWV ............................ Error! Bookmark not defined.

Figuur 3: De acht stappen in de modellevenscyclus ......................................................................... 23

Figuur 4: Schematische weergave procedures voor model initiatie .................................................... 25

Figuur 5: Schematische weergave procedures voor model wijziging .................................................. 26

Figuur 6: Schematische weergave procedures voor model ontwikkeling ............................................. 29

Figuur 7: Schematische weergave procedures voor model validatie ................................................... 31

Figuur 8: Schematische weergave procedures voor model goedkeuring ............................................. 36

Figuur 9: Schematische weergave procedures voor model gebruik .................................................... 38

Figuur 10: Schematische weergave procedures voor model monitoring ... Error! Bookmark not defined.

Figuur 11: Schematische weergave procedures voor model ontmanteling .......................................... 42

52

---

Bron: [Beslissing op bezwaar op Wob-verzoek software en algoritmes](https://www.uwv.nl/nl/wet-open-overheid/wob-publicaties/2021/beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes) · [Bijlage 4 bij beslissing op bezwaar op Wob-verzoek software en algoritmes (PDF, 1 MB)](https://www.uwv.nl/assets-kai/files/4571f499-a1ce-4b2d-a549-36131e8727c5/bijlage-4-beslissing-op-bezwaar-op-wob-verzoek-software-en-algoritmes.pdf)
