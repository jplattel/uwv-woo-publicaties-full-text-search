---
source_id: 2026-05-01-woo-besluit-over-korting-inkomen-vrijwillig-verzekerden/2026-05-01-5-registreren-inkomsten-in-uzs
publication_slug: 2026-05-01-woo-besluit-over-korting-inkomen-vrijwillig-verzekerden
pdf_slug: 2026-05-01-5-registreren-inkomsten-in-uzs
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2026/woo-besluit-over-korting-inkomen-vrijwillig-verzekerden
pdf_url: https://www.uwv.nl/assets-kai/files/a11eec02-e860-4f4b-b6d0-a89af5fb45dd/5-registreren-inkomsten-in-uzs.pdf
publication_title: Woo-besluit over korting inkomen vrijwillig verzekerden
publication_date: '2026-05-01T06:00:00Z'
publication_type: WOO publicatie
pdf_label: Bijlage 5. Registreren inkomsten in UZS (PDF, 353 kB)
retrieved_at: '2026-06-30T11:24:34+00:00'
sha256: a827c1ad30c329d2bdac7d606e2ad10ba478f88d196880541ae632ee342f5e7b
page_count: 10
ocr_used: true
---

Home » Handboeken » Proces Backoffice ZW » UC » Afhandelen inkomstenkorting » Verwerken inkomsten » Registreren inkomsten in UZS

## Proces Backoffice ZW

## Registreren inkomsten in UZS

Bepalen duur korting Verwerken inkomsten

◄ ►

Procesinformatie Algemeen

Wie Uitkeringsconsulent (UC)

Divisie Uitkeren – Ziektewet

Samenvatting Je registreert het kortingsbedrag in UZS.

Input

Intern Proces ZW

Termijnen en procesacties

Beslistermijn

Doorlooptijd

Acties

Voor het registreren van de inkomsten in UZS heb je een inkomstenbedrag per dag berekend en is de duur van de inkomsten bekend. Nu

registreer je de korting in UZS.

Je bepaalt om welke situatie het gaat:

## •

Een voorlopige korting

## •

Een schorsing in afwachting van de inkomsten

## •

Een schorsing opheffen na ontvangst van informatie over de inkomsten

## •

Een korting van (VUT-/pre)pensioeninkomsten

## •

Een definitieve korting

## •

Een herziening van een definitieve korting

## •

Een beëindiging van de korting

## •

Een heropening van de korting

## •

Het splitsen van een geregistreerde korting

## •

Een administratieve splitsing van een dossier in combinatie met een korting

## •

Een korting vanwege een tweede recht

Als een geval in het automatische proces zit, registreer je de korting ook meteen in UZS. Na toekenning zet UZS de juiste brief automatisch

klaar en ontvang je signaal UZZ0334 Afhandelen uitgaande brief in je werklijst.

Let op:

1: De status van het geval moet zijn toegewezen om de brief automatisch klaar te zetten. Als dat nog niet het geval is, zorgt de

statusovergang naar ‘Toegewezen’ dat de brief alsnog wordt klaargezet. Op dat moment verschijnt signaal ‘UZZ0334 Afhandelen

uitgaande brief’ om de kortingsbrief te controleren en fiatteren. Als de beschikking nog niet is verstuurd, worden bij correcties de eerder

opgeslagen regels in het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ automatisch verwijderd.

2: Het kan voorkomen dat je aan de hand van deze werkinstructie de inkomsten opnieuw moet registreren in het scherm ‘Beheren

gedeeltelijke werkhervatting’. Het signaal ‘UZZ0436 Beoordeel melding gedeeltelijk werken’ wordt dan onterecht gezet. Dit signaal kun je

na afhandeling van deze werkinstructie fiatteren.

3: Als de cliënt inkomsten in het weekend ontvangt, kun je deze inkomsten niet op deze dagen in UZS verwerken omdat je over

weekenddagen geen uitkering betaalt. Je verdeelt deze inkomsten daarom over de uitkeringsdagen van de direct voorafgaande week.

Alleen als er geen direct voorafgaande week is, verdeel je de inkomsten over de opvolgende week.

Is er geen direct voorafgaande week en betaal je uitkering over een weekenddag(en) vanwege Ziezazo, dan kort je de inkomsten op de

weekenddag(en) dat de inkomsten zijn ontvangen.

3: Als je op grond van no-risk een korting hebt geregistreerd in het tweede ziektejaar van een uitkering en UZS zet de brief SET12K246 of

SET12K247 klaar, dan wijzig je in de brief handmatig het uitkeringspercentage van 100 naar 70. De bedragen staan wel juist in de brief.

## Registreren voorlopige korting

Je hebt een voorlopig kortingsbedrag per dag berekend.

Je voert de volgende acties uit:

## •

Open het scherm Beheren gedeeltelijke werkhervatting.

## •

Registreer een nieuwe regel met de juiste gegevens.

## •

Selecteer in het veld <Herkomst bedrag per dag> ‘Voorlopig kortingsbedrag’. Selecteer bij een voorlopige korting vanwege zelfstandige

arbeid ‘Voorlopig kortingsbedrag zelfstandige’.

## •

Registreer de startdatum van de voorlopige korting in het veld <Begindatum>.

Let op: Je registreert een voorlopige korting alleen per toekomende datum.

## •

Als je een einddatum hebt vastgesteld, registreer je die in het veld <Einddatum>.

## •

Sla de gegevens op.

## •

Vink het selectievak aan en klik daarna op de knop “Registreer korting”. Selecteer ‘Voorlopige korting’.

UZS zet 1 van de volgende voorlopige kortingsbrieven automatisch klaar:

## •

SET12K244 ‘Voorlopige korting uitbetaling (nw kort scherm)’

## •

SET12K245 ‘Voorlopige korting uitbetaling (nw kort scherm)’ (WG)

Bij het registreren van een voorlopige korting zet UZS automatisch signaal UZZ0624 Beoordeel de kortingsregel(s) met de status ‘voorlopig’

of ‘schorsing’ of UZZ0625 Beoordeel de kortingsregel(s) met de status ‘voorlopig’ bij zelfstandige arbeid met een datum in de toekomst als

het veld <Herkomst bedrag per dag> is gevuld met ‘Voorlopig kortingsbedrag’ of ‘Voorlopig kortingsbedrag zelfstandige’.

## Schorsen in afwachting van inkomsten

Je hebt bepaald dat je geen voorlopige korting kunt berekenen. Je hebt met de cliënt afgesproken dat je de uitkering schorst in afwachting

van de inkomsten.

Je voert de volgende acties uit:

## •

Open het scherm Beheren gedeeltelijke werkhervatting.

## •

Selecteer in het veld <Herkomst bedrag per dag> ‘Schorsing zonder kortingsbedrag’.

## •

Registreer de ingangsdatum van de inkomsten in het veld <Begindatum>.

## •

Laat de velden <Einddatum> en <Bedrag per dag> leeg.

## •

Sla de gegevens op.

## •

Vink het selectie vak aan en klik op de knop “Registreer korting”. Kies ‘Schorsing in afwachting van inkomsten’. UZS zet automatisch een

schorsing op het dossier.

In het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ wordt het veld <Korting per dag> gevuld met 0,00 en worden de velden

<Brievensetcode> en <Status brief> automatisch gevuld.

UZS zet 1 van de volgende voorlopige kortingsbrieven automatisch klaar:

## •

SET12K240 ‘Schorsing in afwachting van verdiensten (nw kort scherm)’

## •

SET12K241 ‘Schorsing in afwachting van verdiensten (nw kort scherm)’ (WG)

Bij het registreren van een schorsing zet UZS automatisch signaal UZZ0624 Beoordeel de kortingsregel(s) met de status ‘voorlopig’ of

‘schorsing’ met een datum in de toekomst.

## Opheffen schorsing na ontvangst informatie over inkomsten

Je hebt informatie ontvangen over de inkomsten van het gedeeltelijk werken en bepaald dat je de schorsing kunt opheffen.

Er zijn 2 situaties:

Er is geen gedeeltelijk werken

Je voert de volgende acties uit:

## •

Open het scherm Beheren gedeeltelijke werkhervatting.

## •

Selecteer de regel met status korting ‘Schorsing’ en registreer in het veld <Einddatum> dezelfde datum als de ingangsdatum.

## •

Sla de gegevens op.

## •

Vink het selectievak van de regel aan en klik op de knop “Registreer korting”. Selecteer ‘Opheffen schorsing na ontvangst inkomsten’.

## •

Hef in het scherm Registreren schorsing de schorsing op volgens de werkinstructie Schorsen.

UZS zet 1 van de volgende voorlopige ontschorsingsbrieven automatisch klaar:

## •

SET12K242 ‘Beëindiging schorsing in afwachting van verdiensten (nw kort scherm)’

## •

SET12K243 ‘Beëindiging schorsing in afwachting van verdiensten (nw kort scherm)’ (WG)

Inkomsten zijn bekend

Voordat je de definitieve inkomsten registreert, ontschors je de uitkering en daarvoor voer je de volgende acties uit:

## •

Open het scherm Beheren gedeeltelijke werkhervatting.

## •

Bepaal of het om een definitief of voorlopig kortingsbedrag gaat:

## •

Definitief kortingsbedrag: registreer een nieuwe kortingsregel volgens ‘Registreren definitieve korting’. Als je vanwege een voorlopige

korting eerder een kortingsregel met dezelfde ingangsdatum hebt geregistreerd, beëindig je die kortingsregel met dezelfde datum als

de ingangsdatum.

## •

Voorlopig kortingsbedrag: registreer een nieuwe kortingsregel volgens Registreren voorlopige korting.

## •

Vink het selectievak van de regel aan en klik op de knop “Registreer korting”. Selecteer ‘Definitieve korting’ of ‘Voorlopige korting’.

## •

Verstuur 1 van de volgende ontschorsingsbrieven:

## •

SET12K242 ‘Beëindiging schorsing in afwachting van verdiensten (nw kort scherm)’

## •

SET12K243 ‘Beëindiging schorsing in afwachting van verdiensten (nw kort scherm)’ (WG)

## •

Hef de schorsing op in het scherm ‘Registreren schorsing’ volgens de werkinstructie Schorsen.

## •

Ga verder met de situatie die je wil afhandelen voor het registreren van de inkomsten.

## Korten (VUT-/pre)pensioeninkomsten

Je opent het scherm Registreren korting pensioeninkomsten/gedeeltelijke KBZ. Je krijgt dan de informatiemelding ‘De eerste ziektedag is

gelijk aan of groter dan 1-7-2011’. Je negeert deze informatiemelding en klikt op de knop “OK”.

Je voert de volgende acties uit:

## •

Registreer in het veld <Vanaf> de startdatum van de inkomsten vanwege arbeid.

## •

Registreer in het veld <Tot en met> de eventuele einddatum van de inkomsten vanwege arbeid.

## •

Laat het veld <Soort> staan op ‘Kortingsbedrag (inkomsten i.v.m. arbeid)’.

## •

Registreer in het veld <Gemiddelde inkomsten per dag> het berekende inkomstenbedrag per dag.

## •

Sla de gegevens op en open het scherm Correspondentie bij geval.

## •

Verstuur SET12K330 ‘Korting overige inkomsten en combinatie met inkomsten uit werk (tijdelijk)’.

## Registreren definitieve korting

Je opent het scherm Beheren gedeeltelijke werkhervatting en voert een nieuwe regel op met de juiste gegevens.

Je voert de volgende acties uit:

## •

Registreer in het veld <Bedrag per dag> het berekende inkomstenbedrag per dag.

## •

Sla de gegevens op.

## •

Registreer in het veld <Memo> een motivatie als je een bestaande inkomstenregel hebt gewijzigd.

## •

Vink het selectievak aan van de kortingsregels die je definitief wil verwerken.

## •

Selecteer onder de knop “Registreer korting”: ‘Definitieve korting’.

Het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ opent automatisch. Meer informatie over het registreren in dit scherm lees je bij

Verwerking geregistreerde korting.

Als de status van het geval ‘Toegewezen’ is, wordt 1 van de volgende kortingsbrieven automatisch klaargezet:

## •

SET12K246 ‘Korting in verband met inkomsten (nw kort scherm)’

## •

SET12K247 ‘Korting in verband met inkomsten (nw kort scherm)’ (WG)

De korting is geregistreerd. Einde instructie.

## Herzien definitieve korting

Je opent het scherm Beheren gedeeltelijke werkhervatting. Je wijzigt de aanwezige definitieve inkomstenregel met de juiste einddatum.

Een herziening van het bedrag verwerk je in een nieuwe inkomstenregel. Een herziening van het bedrag en beëindiging van de korting

verwerk je in dezelfde nieuwe inkomstenregel (zie ook de instructie van het scherm ‘Beheren gedeeltelijke werkhervatting’).

Je voert de volgende acties uit:

## •

Wijzig de einddatum en/of het bedrag per dag en sla de gegevens op.

## •

Registreer in het veld <Memo> een motivatie als je een bestaande inkomstenregel hebt gewijzigd.

## •

Selecteer de kortingsregels die je definitief wil verwerken door het selectievak aan te vinken.

## •

Selecteer onder de knop “Registreer korting”: ‘Herziening van de definitieve korting’.

Het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ opent automatisch. Meer informatie over het registreren in dit scherm lees je bij

Verwerking geregistreerde korting.

Als de status van het geval ‘Toegewezen’ is, zet UZS 1 van de volgende herzieningsbrieven automatisch klaar:

## •

SET15H409 ‘Herziening korting (nw kort scherm)’

## •

SET15H408 ‘Herziening korting (nw kort scherm)’ (WG)

De korting is geregistreerd. Einde instructie.

## Beëindigen korting

Er zijn inkomsten verwerkt in het scherm Beheren gedeeltelijke werkhervatting die al zijn doorgezet naar het scherm ‘Registreren korting

inkomsten uit arbeid/KBZ’ zonder een einddatum.

Er zijn de volgende situaties:

## •

Er staat een nieuwe regel met een bedrag per dag van € 0,00. De status van deze regel is ‘In beh MVB’ of ‘In beh UD’.

## •

Er staat geen nieuwe regel. Je hebt bericht ontvangen dat de inkomsten uit gedeeltelijk werken tijdens ziekte beëindigd zijn.

## Nieuwe regel met bedrag per dag € 0,00 en status ‘In beh MVB’ of ‘In beh UD’

Je voert de volgende acties uit:

## •

Bij de nieuwe regel met een bedrag per dag van € 0,00 bel je de werkgever of cliënt en vraag je of de inkomsten uit gedeeltelijk werken

tijdens ziekte zijn beëindigd:

## •

Inkomsten zijn niet beëindigd, het gaat om een andere wijziging: corrigeer het bedrag en registreer verder volgens Registreren

definitieve korting.

## •

Inkomsten zijn beëindigd: verwerp in het scherm Beheren gedeeltelijke werkhervatting de regel met het bedrag per dag van € 0,00. Ga

verder met de volgende actie.

## •

Registreer bij de lopende kortingsregel in het veld <Einddatum> de datum direct voorafgaand aan de datum die in het veld <Begindatum>

staat van de verworpen regel met het bedrag per dag van € 0,00.

## •

Registreer een motivatie in het veld <Memo>.

## •

Sla de gegevens op.

## •

Vink het selectievak aan.

## •

Selecteer onder de knop “Registreer korting”: ‘Beëindiging van de korting’. Het scherm Registreren korting inkomsten uit arbeid/KBZ

opent automatisch.

## •

Klik op de knop “Simuleren betaalbaarstelling”.

## •

Sla de gegevens op.

In het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ is de originele kortingsregel nu gevuld met de einddatum in het veld <Tot en

met>. Er is een nieuwe regel met eenzelfde <Volgnr GW> toegevoegd met de einddatum in het veld <Vanaf>. Deze regel is noodzakelijk

zodat UZS automatisch 1 van de volgende beëindigingsbeslissingen klaarzet:

## •

SET12K250 ‘Beëindiging korting in verband met inkomsten (nw kort scherm)’

## •

SET12K251 ‘Beëindiging korting in verband met inkomsten (nw kort scherm)’ (WG)

De korting is beëindigd. Einde instructie.

## Geen nieuwe regel en bericht ontvangen inkomsten uit gedeeltelijk werken tijdens

## ziekte beëindigd

Je voert de volgende acties uit:

## •

Open het scherm Beheren gedeeltelijke werkhervatting.

## •

Registreer in het veld <Einddatum> de datum direct voorafgaand aan de datum waarop het gedeeltelijk werken tijdens ziekte is

beëindigd.

## •

Registreer een motivatie in het veld <Memo>.

## •

Sla de gegevens op.

## •

Vink het selectievak aan.

## •

Selecteer onder de knop “Registreer korting”: ‘Beëindiging van de korting’.

## •

Klik op de knop “OK”. Het scherm Registreren korting inkomsten uit arbeid/KBZ opent automatisch.

## •

Klik op de knop “Simuleren betaalbaarstelling”.

## •

Sla de gegevens op.

In het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ is de originele kortingsregel nu gevuld met de einddatum in het veld <Tot en

met>. Er is een nieuwe regel met eenzelfde <Volgnr GW> toegevoegd met de einddatum in het veld <Vanaf>. Deze regel is noodzakelijk

zodat UZS automatisch 1 van de volgende beëindigingsbeslissingen klaarzet:

## •

SET12K250 ‘Beëindiging korting in verband met inkomsten (nw kort scherm)’

## •

SET12K251 ‘Beëindiging korting in verband met inkomsten (nw kort scherm)’ (WG)

De korting is beëindigd. Einde instructie.

## Heropenen korting

Het dossier is heropend en opnieuw toegekend.

Je beoordeelt of de korting nog steeds geldt:

## •

Korting geldt niet meer: controleer in het scherm Beheren gedeeltelijke werkhervatting of de laatste korting is beëindigd:

## •

Laatste korting is beëindigd: voer geen verdere actie uit.

## •

Laatste korting is niet beëindigd: ga verder met ‘Korting geldt nog steeds’ hieronder.

## •

Korting geldt nog steeds: voer de volgende acties uit:

## •

Open het scherm ‘Beheren gedeeltelijke werkhervatting’.

## •

Selecteer de juiste kortingsregel en verwijder de datum in het veld <Einddatum>.

## •

Vink het selectievak van de juiste kortingsregel aan.

## •

Selecteer onder de knop “Registreer korting”: ‘Heropening van de korting’. Het scherm Registreren korting inkomsten uit arbeid/KBZ

opent automatisch.

## •

Klik op de knop “Simuleren betaalbaarstelling”.

## •

Sla de gegevens op.

In het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ is in de originele kortingsregel het veld <Tot en met> nu leeggemaakt. Er is een

nieuwe regel met eenzelfde <Volgnr GW> toegevoegd met in het veld <Vanaf> de ‘oude’ einddatum en het veld <Tot en met> is gevuld met

de datum ‘Vanaf’ – 1 dag. Deze regel is noodzakelijk zodat automatisch 1 van de volgende beslissingen wordt klaargezet:

## •

SET12K252 ‘Korting ivm inkomsten na beëindigde claim (nw kort scherm)’

## •

SET12K253 ‘Korting ivm inkomsten na beëindigde claim met wg (nw kort scherm)’

## Splitsen geregistreerde korting

Er zijn 2 situaties waarin je een kortingsperiode handmatig splitst:

## •

Bij een wijziging in de hoogte van het dagloon die ligt in de kortingsperiode (pop-up).

## •

Als er in de kortingsperiode overlap is met een weigering (bij ‘Simuleren betaalbaarstelling’ is de uitkomst een 0-bedrag).

## Splitsen op basis van wijziging in hoogte dagloon (pop-up)

Je hebt bij het verwerken van de inkomsten in het scherm Beheren gedeeltelijke werkhervatting een pop-upmelding ontvangen waarin de

dagloonwijziging in de kortingsperiode staat.

Je voert de volgende acties uit:

## •

Klik de pop-upmelding weg.

## •

Registreer in het veld <Einddatum> de datum splitsing.

## •

Registreer een motivatie voor de splitsing in het veld <Memo>.

## •

Maak een nieuwe regel met als startdatum de datum splitsing en de eventuele einddatum van de originele kortingsperiode.

## •

Vink voor de kortingsregel het selectievak aan.

## •

Klik op de knop “Registreer korting” en selecteer ‘Definitieve korting’.

Het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ opent automatisch. Meer informatie over de vulling van dit scherm lees je bij

Verwerking geregistreerde korting.

Als de status van het geval ‘Toegewezen’ is, wordt 1 van de volgende kortingsbrieven automatisch klaargezet:

## •

SET12K246 ‘Korting in verband met inkomsten (nw kort scherm)’

## •

SET12K247 ‘Korting in verband met inkomsten (nw kort scherm)’ (WG)

De korting is geregistreerd. Einde instructie.

## Splitsen op basis van overlap met weigering

Je hebt bij het registreren van de korting in het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ een 0-bedrag bij ‘Simuleren

betaalbaarstelling’.

Je voert de volgende acties uit:

## •

Sluit het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ en verwerp de regel in het scherm Beheren gedeeltelijke werkhervatting.

Vink daarvoor het selectievak aan en klik op de knop “Verwerpen’.

## •

Bepaal bij een weigering de datum van splitsing door de ‘einddatum weigering’ op te zoeken in het scherm Registreren weigering.

## •

Maak 2 nieuwe regels. Eén regel met de originele startdatum en datum splitsing als einddatum en 1 regel met als startdatum de datum

splitsing en de eventuele einddatum van de originele kortingsperiode.

## Administratief splitsen dossier in combinatie met korting

Er zijn 3 situaties waarin je een wijziging verwerkt door een administratieve splitsing.

## Administratief splitsen door wijziging betaalbestemming

De cliënt gaat uit dienst en de inkomsten uit (gedeeltelijk) werken stoppen

Je voert de volgende acties uit:

## •

Beëindig de korting voordat je het dossier administratief splitst.

## •

Verwerk de beëindiging volgens Beëindigen korting.

De cliënt gaat uit dienst en de inkomsten uit (gedeeltelijk) werken continueren

De inkomsten uit (gedeeltelijk) werken worden bij administratief splitsen automatisch overgenomen in het administratief voortgezette

geval.

Controleer na het administratief splitsen in het scherm Correspondentie bij geval van het voorgezette geval of er onterecht klaargezette

kortingsbrieven zijn en verwijder die.

## Administratief splitsen door wijziging uitkeringspercentage

De cliënt heeft recht op een lager uitkeringspercentage en de inkomsten uit (gedeeltelijk) werken continueren.

De inkomsten uit (gedeeltelijk) werken worden bij administratief splitsen automatisch overgenomen in het administratief voorgezette geval.

Je voert de volgende acties uit:

## •

Selecteer in het scherm Beheren gedeeltelijke werkhervatting de inkomstenregels die een start/einddatum hebben na de datum van de

administratieve splitsing en wijzig de status van deze regels door op de knop “Verwerpen” te klikken.

## •

Registreer nieuwe kortingsregels die toegepast moeten worden op het administratief voortgezette geval. Je gebruikt de datum van de

administratieve splitsing als begindatum.

## •

Ga verder met Herzien definitieve korting en start met de eerste stap.

## Administratief splitsen door wijziging werkgever

Het loonheffingennummer van de werkgever wijzigt en het dienstverband loopt door. De korting wordt automatisch overgenomen in het

administratief voorgezette geval. Je verwerkt geen wijzigingen.

## Registreren korting vanwege tweede recht

De cliënt heeft inkomsten bij een nieuwe werkgever die gekort worden op een lopende ZW-uitkering en vanuit deze nieuwe werkgever

ontstaat een nieuw ZW-recht. Bij het ontstaan van het nieuwe ZW-recht worden de inkomsten vanuit de werkgever vervangen door het

‘Dagloon ZW nieuw recht’.

Je voert de volgende stappen uit:

## •

Registreer in het scherm Beheren gedeeltelijke werkhervatting een nieuwe kortingsregel met als ingangsdatum de eerste uitkeringsdag

van het tweede recht en als bedrag per dag het dagloon op de eerste uitkeringsdag van het tweede recht.

## •

Selecteer in het veld <Inkomsten 2de recht> ‘Ja’ en sla de melding op.

## •

Selecteer onder de knop “Registreer korting”: ‘Herziening van de definitieve korting’.

Bij het toepassen van korting in het tweede recht mag je maar 1 regel selecteren. Het scherm ‘Registreren korting inkomsten uit

arbeid/KBZ’ opent automatisch.

## •

Voor het aanmaken van de brief voer je volgende acties uit:

## •

Open het scherm Correspondentie bij geval.

## •

Maak brief SET12K249 ‘Korting dagloon 2e recht (nw kort scherm)’ aan.

## •

Klik in het scherm ‘Brievenset variabelen’ op de knop “Korting”. Het scherm ‘Selecteren korting’ opent.

## •

Selecteer de juiste kortingsregel door de regel aan te vinken.

## •

Klik op de knop “Ok”. Je komt terug in het scherm ‘Brievenset variabelen’. UZS heeft de velden <Korting van kortingsperiode>,

<Inkomsten kortingsperiode>, <Bruto uitkering in kortingsperiode> en <Begindatum (beëindiging) korting> gevuld.

## •

Vul handmatig het veld <Naam nieuwe werkgever>.

## •

Controleer of het dagloon van het tweede recht hoger is dan het dagloon van het eerste recht:

## •

Zo ja: wijzig handmatig het bedrag in het veld <Korting van kortingsperiode> naar 70% van het dagloon van het tweede recht.

## •

Zo nee: wijzig het kortingsbedrag niet.

## •

Fiatteer de brief.

De regel waarop de herziening van toepassing is, wordt afgesloten in het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’. In deze

regel wordt het veld <Tot en met> gevuld met de datum in het veld <Vanaf> -1.

De korting is geregistreerd, einde instructie.

## Verwerking geregistreerde korting

Nadat je op de knop “Registreer korting” hebt geklikt, verwerkt UZS de inkomsten automatisch. Het scherm Registreren korting inkomsten

uit arbeid/KBZ opent automatisch.

De volgende velden en gegevens zijn dan gevuld:

## •

<Status korting> toont de gekozen status van de verwerkte regel.

## •

<Volgnummer GW> toont het volgnummer van de eerder geselecteerde regel.

## •

<Vanaf> en <Tot en met> zijn gevuld met de datums van de geselecteerde regel.

## •

<Gemiddelde inkomsten per dag> is gevuld met het bijbehorende bedrag uit de geselecteerde regel.

## •

<Soort korting> wordt automatisch gevuld met de waarde ‘Loon gedeeltelijk werken/KBZ’.

## •

<Ongekorte bruto uitkering per dag> wordt gevuld met de uitkomst van de berekening ‘dagloon x uitkeringspercentage’.

## •

<Korting per dag> wordt gevuld met de uitkomst van de berekening ‘SV-loon uit de geselecteerde regel x uitkeringspercentage’.

## •

<Gekorte bruto uitkering per dag> wordt gevuld met de berekening van ‘Ongekorte bruto uitkering per dag – de berekening van Korting

per dag’.

## •

<Briefcode> wordt automatisch gevuld met de briefcode van de relevante kortingsbrief.

## •

<Dagtekening brief> wordt automatisch gevuld.

## •

<Status brief> wordt automatisch gevuld met 1 van de volgende waarden:

## •

Concept

## •

Gepland

## •

Te fiatteren

## •

Gefiatteerd

## •

Verzonden

## •

Handmatig

## •

Fout

## •

Meerdere brieven

## •

## DHH

## •

De regel waarop de herziening van toepassing is, wordt in het scherm ‘Registreren korting inkomsten uit arbeid/KBZ’ afgesloten in het

overzicht ‘Kortingen’. In deze regel wordt het veld <Tot en met> gevuld met de datum in het veld <Vanaf> -1.

## Verwerken meerdere kortingen in brief

Als je meerdere kortingen tegelijk in 1 brief verwerkt, wijzig je handmatig de kortingsbrief die UZS heeft klaargezet.

Je voert hiervoor de volgende acties uit:

## •

Ga naar het scherm Correspondentie bij geval.

## •

Selecteer de kortingsbrief en klik op de knop “Wijzigen”.

## •

Om meerdere kortingen in 1 brief te verwerken: klik in het scherm ‘Brievenset variabelen’ op de knop “Korting”. Als deze knop niet actief

is, kun je in de brief geen korting of meerdere kortingen selecteren.

## •

In het scherm ‘Selecteer korting’ toont het blok “Selecteer korting” de kortingen die je eerder hebt geregistreerd. Vink in de kolom

‘Selectie korting’ de regels aan van de kortingen die je in de brief wil vermelden.

## •

Klik op de knop “Ok”.

## •

Klik op de knop “Brievenset aanmaken” en vervolgens op de knop “Fiatteren” om de brief te versturen.

Output

Cliënt Brieven:

## •

SET12K244 ‘Voorlopige korting uitbetaling (nw kort scherm)’

## •

SET12K240 ‘Schorsing in afwachting van verdiensten (nw kort

scherm)’

## •

SET12K242 ‘Beëindiging schorsing in afwachting van

verdiensten (nw kort scherm)’

## •

SET12K191 ‘Korting in verband met inkomsten (uitsluitend

eerste ziektedag vanaf 1-7-2011)

## •

SET12K246 ‘Korting in verband met inkomsten (nw kort scherm)’

## •

SET15H409 ‘Herziening korting (nw kort scherm)’

## •

SET12K250 ‘Beëindiging korting in verband met inkomsten (nw

kort scherm)’

## •

SET12K252 ‘Korting ivm inkomsten na beëindigde claim (nw kort

scherm)’

## •

SET12K249 ‘Korting dagloon 2e recht (nw kort scherm)’

Telefoon

Vragen of inkomsten uit gedeeltelijk werken tijdens ziekte zijn

beëindigd

Werkgever Brieven:

## •

SET12K245 ‘Voorlopige korting uitbetaling (nw kort scherm)’

## (WG)

## •

SET12K241 ‘Schorsing in afwachting van verdiensten (nw kort

scherm)’ (WG)

## •

SET12K243 ‘Beëindiging schorsing in afwachting van

verdiensten (nw kort scherm)’ (WG)

## •

SET12K195 ‘Korting i.v.m. inkomsten (uitsluitend eerste

ziektedag vanaf 1-7-2011) (WG)

## •

SET12K247 ‘Korting in verband met inkomsten (nw kort scherm)’

## (WG)

## •

SET15H408 ‘Herziening korting (nw kort scherm)’ (WG)

## •

SET12K251 ‘Beëindiging korting in verband met inkomsten (nw

kort scherm)’ (WG)

## •

SET12K253 ‘Korting ivm inkomsten na beëindigde claim met wg

(nw kort scherm)’

## •

SET12K330 ‘Korting overige inkomsten en combinatie met

inkomsten uit werk (tijdelijk)’

Telefoon

Vragen of inkomsten uit gedeeltelijk werken tijdens ziekte zijn

beëindigd

## •

Intern Registraties in UZS

## •

Signaal ‘UZZ0334 Afhandelen uitgaande brief’

## •

Signaal ‘UZZ0624 Beoordeel de kortingsregel(s) met de status

‘voorlopig’ of ‘schorsing’’

## •

Signaal ‘UZZ0625 Beoordeel de kortingsregel(s) met de status

‘voorlopig’ bij zelfstandige arbeid’

Systeemacties

Zie ‘Acties’.

Hulpmiddelen

Overzicht Systemen UWV

Wijzigingshistorie

Wettelijke basis, aanvullende informatie

Toelichting

Wetsartikelen

◄ ►

---

Bron: [Woo-besluit over korting inkomen vrijwillig verzekerden](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2026/woo-besluit-over-korting-inkomen-vrijwillig-verzekerden) · [Bijlage 5. Registreren inkomsten in UZS (PDF, 353 kB)](https://www.uwv.nl/assets-kai/files/a11eec02-e860-4f4b-b6d0-a89af5fb45dd/5-registreren-inkomsten-in-uzs.pdf)
