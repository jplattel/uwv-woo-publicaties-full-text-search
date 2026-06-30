---
source_id: 2024-05-15-woo-besluit-gegevensuitwisseling-uwv-en-belastingdienst/2024-05-15-bijlage-4-webservice-loonaangiftegegevens-cws-la-productbeschrijving-voor-afnemers
publication_slug: 2024-05-15-woo-besluit-gegevensuitwisseling-uwv-en-belastingdienst
pdf_slug: 2024-05-15-bijlage-4-webservice-loonaangiftegegevens-cws-la-productbeschrijving-voor-afnemers
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2024/woo-besluit-gegevensuitwisseling-uwv-en-belastingdienst
pdf_url: https://www.uwv.nl/assets-kai/files/13222050-8a6e-4f96-b259-56bfaf1a2ad7/bijlage-4-webservice-loonaangiftegegevens-cws-la-productbeschrijving-voor-afnemers.pdf
publication_title: Woo-besluit gegevensuitwisseling UWV en Belastingdienst
publication_date: '2024-05-15T00:00:00Z'
publication_type: WOO publicatie
pdf_label: Bijlage 4. Webservice Loonaangiftegegevens (CWS-LA) - Productbeschrijving
  voor afnemers (PDF, 759 kB)
retrieved_at: '2026-06-30T13:01:21+00:00'
sha256: 56ccdba8efb8db480039f644136c97183905d9cabd181df0f46d4da634a3a184
page_count: 8
ocr_used: true
---

Webservice

Loonaangiftegegevens

Productbeschrijving

## Inhoud

1 Inleiding .................................................................................................. 3

2 Productbeschrijving ................................................................................... 4

2.1 Product ............................................................................................. 4

2.2 Populatie/selectie ............................................................................... 4

2.3 Gegevensset ...................................................................................... 4

2.3.1 Vraagbericht ................................................................................... 4

2.3.2 Antwoordbericht .............................................................................. 5

2.3.3 Selectie- en filtermogelijkheden ......................................................... 6

2.4 Berichtspecificaties ............................................................................. 6

2.4.1 Informatiepakket ............................................................................. 6

2.4.2 Productspecificatie ........................................................................... 7

2.5 Distributiekanaal & beveiligingsklasse .................................................... 7

3 Contact .................................................................................................... 8

Productbeschrijving voor afnemer

Pagina 2 van 8

Productcode W21 - Versie 0.5 – januari 2023

1 Inleiding

In deze productbeschrijving vindt u informatie over het beveiligde product ‘Webservice

Loonaangiftegegevens’. Het product wordt ook wel een ‘Configureerbare Webservice

(CWS)’ genoemd. Hiermee kunt u realtime actuele en relevante loonaangiftegegevens

opvragen van burgers. Met deze webservice ontvangt u alleen de gegevens die u nodig

heeft om uw taak uit te voeren.

De gegevens kunt u op elk moment opvragen en direct ontvangen in uw applicatie. De

applicatie is 7 dagen per week en 24 uur per dag beschikbaar. De applicatie beantwoordt

95% van de vragen binnen 3 seconden. Dit wordt gemeten vanaf het moment dat de

vraag binnenkomt en het antwoord wordt teruggezonden.

Heeft u vragen? Stuur dan een e-mail naar @uwv.nl

Productbeschrijving voor afnemer

Pagina 3 van 8

Productcode W21 - Versie 0.5 – januari 2023

2 Productbeschrijving

2.1 Product

Productcode : W21

Productnaam : Webservice Loonaangiftegegevens (CWS-LA)

De webservice levert loonaangiftegegevens van personen uit de polisadministratie.

Ook levert het product een beperkte gegevensset van de inhoudingsplichtigen uit de

werkgeversadministratie.

2.2 Populatie/selectie

De webservice levert loonaangiftegegevens op basis van een burgerservicenummer

(BSN) en ‘datum aanvraag selectieperiode’.

2.3 Gegevensset

U kunt met een vraagbericht de loonaangiftegegevens van een persoon opvragen door

het BSN in te voeren in de webservice. De ontvangst van een vraagbericht is de trigger

voor het proces. Het systeem valideert het vraagbericht en stelt de juiste gegevens

samen (op basis van de configuratie). Daarna ontvangt u het antwoordbericht met de

samengestelde, actuele gegevens.

Database

loonaangll(e

## __ RM û ' N

## “E anTwoorD “ ganwoom *

Proportionele

configuratie

afgestemd op

taakuitvoering

en doelbinding

2.3.1 Vraagbericht

In de tabel hieronder leest u hoe het vraagbericht eruit komt te zien.

## BERICHT

## [ _ Header |

## BerichtIdentificatie.Berichttype.VersieMajor | Het le en het 2e cijfer van het

versienummer uit de UwvML xsd

bestandsnaam van het vraagbericht

## BerichtIdentificatie.Berichttype.VersieMinor | Het 3e en het 4e cijfer van het

versienummer uit de UwvML xsd

bestandsnaam van het vraagbericht

Productbeschrijving voor afnemer Pagina 4 van 8

Productcode W21 - Versie 0.5 - januari 2023

## GEGEVENSVRAAG

Datum aanvang selectieperiode Verplicht attribuut. De datum van de eerste

dag van de periode waarop de vraag

betrekking heeft.

Datum einde selectieperiode Optioneel attribuut. De datum van de

laatste dag van de periode waarop de vraag

betrekking heeft.

Tijdstip beschouwing Optioneel attribuut. De datum en tijd die

opgegeven kan worden om de gegevens die

op dat moment geldig zijn op te halen (dit

veld wordt niet ondersteund en wordt

genegeerd als deze is gevuld).

## CONTRACT GEGEVENSLEVERING

Contractnummer gegevenslevering Verplicht attribuut. Het nummer dat de

overeenkomst met een GEGEVENSAFNEMER

identificeert.

Datum aanvang contract Verplicht attribuut. De datum van de eerste

gegevenslevering dag waarop het CONTRACT

GEGEVENSLEVERING geldig is.

## GEGEVENSAFNEMER CONFIGURATIE

Versienummer gegevensafnemer Verplicht attribuut. Het versienummer dat

configuratie voor deze configuratie is toegekend.

## NATUURLIJK PERSOON

Burgerservicenummer Het burgerservicenummer op basis waarvan

loonaangiftegegevens opgevraagd kunnen

worden.

2.3.2 Antwoordbericht

De gegevens ontvangt u op maat. Ook krijgt u een informatiepakket waarin alle

gegevenselementen beschreven staan die u kunt aanvragen (zie paragraaf 2.4.1).

U kunt gegevens selecteren uit de volgende groepen van de Loonaangifte (LA):

 natuurlijk persoon

adres (dit is het adres uit de loonaangifte)



inkomstenverhouding



administratieve eenheid



 inkomstenperiode

inkomstenopgave



sector risicopremiegroep inkomstenverhouding



De loonaangifte bestaat uit:

 persoonsgegevens van een natuurlijk persoon, zoals:

het burgerservicenummer



 de naam

de geboortedatum





gegevens over de inkomstenverhouding tussen de administratieve eenheid of

onderneming en een natuurlijk persoon, waaruit een natuurlijk persoon loon of een

uitkering ontving of ontvangt, zoals:

het nummer van de inkomstenverhouding



het personeelsnummer



de begin- en einddatum van de inkomstenverhouding



Productbeschrijving voor afnemer

Pagina 5 van 8

Productcode W21 - Versie 0.5 – januari 2023

 het loonheffingennummer van de administratieve eenheid of onderneming waarbij de

inkomstenverhouding geregistreerd is; de gegevens uit de inkomstenopgave, zoals:

de begin- en einddatum van het aangiftetijdvak waarover de inkomstenopgave



gaat

het aantal sv-dagen



het aantal verloonde uren



de inkomstengegevens



 de gegevens uit de inkomstenperiode, zoals:

de begin- en einddatum van de inkomstenperiode



de code ‘Soort Inkomstenverhouding’



de indicatie premiekortingen



de indicaties verzekerd voor Ziektewet, WW, WAO/IVA/WGA



Naast gegevens uit de loonaangifte kunt u ook gegevens ontvangen van de werkgever

die bij de betreffende loonaangifte horen. Deze gegevens bestaan uit:

de naam



het adres



de aangiftefrequentie die in de werkgeversadministratie staat



U kunt gegevens selecteren uit de volgende groepen van de werkgeversadministratie:

administratieve eenheid



rechtspersoon/samenwerkingsverband



natuurlijk persoon



 adres

2.3.3 Selectie- en filtermogelijkheden

Om de gegevens op maat te ontvangen, kunt u bij de configuratie selecteren en filteren

op:

gegevens die horen bij specifieke code ‘Soort Inkomstenverhoudingen’



gegevens over een bepaalde maximale periode



 inkomstenopgaves met nihil bedragen uitsluiten

VIP-gegevens



2.4 Berichtspecificaties

2.4.1 Informatiepakket

U ontvangt van ons een informatiepakket met technische informatie over:

functioneel koppelvlak document (FKD)



Request en Response bericht in Word, XSD’s, UWVml



UWVml berichten (in xsd):



o

headerbericht

o

applicatiefout

o

basetypes

2.4.2 Productspecificatie

Ook ontvangt u een productspecificatie. Deze bestaat uit de volgende informatie:

Productbeschrijving voor afnemer

Pagina 6 van 8

Productcode W21 - Versie 0.5 – januari 2023

## e Productspecificatie van de configuratie (opsomming van de geselecteerde

## gegevenselementen en de toegepaste filters)

## e Voorbeelden van vraag(request)- en antwoord(response)berichten

## 2.5 Distributiekanaal & beveiligingsklasse

## Het product gebruikt Digikoppeling en UWV Systeem Integratie. De beveiligingsklassen

## zijn vanaf 2.

3 Contact

## UWV Gegevensdiensten

Neem contact op over:

- techniek/berichtenverkeer

## - functionele vragen over koppeling

Productbeschrijving voor afnemer Pagina 7 van 8

Productcode W21 - Versie 0.5 - januari 2023

- wijzigingsverzoeken

- inhoudelijke vragen over gegevens

Op werkdagen bereikbaar van 8.00 tot 17.00 uur

Email: @uwv.nl

Telefoon: UWV Zakelijk 088 - 898 20 10 (lokaal tarief – belkosten zijn afhankelijk van uw

telefoonaanbieder)

Productbeschrijving voor afnemer

Pagina 8 van 8

Productcode W21 - Versie 0.5 – januari 2023

---

Bron: [Woo-besluit gegevensuitwisseling UWV en Belastingdienst](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2024/woo-besluit-gegevensuitwisseling-uwv-en-belastingdienst) · [Bijlage 4. Webservice Loonaangiftegegevens (CWS-LA) - Productbeschrijving voor afnemers (PDF, 759 kB)](https://www.uwv.nl/assets-kai/files/13222050-8a6e-4f96-b259-56bfaf1a2ad7/bijlage-4-webservice-loonaangiftegegevens-cws-la-productbeschrijving-voor-afnemers.pdf)
