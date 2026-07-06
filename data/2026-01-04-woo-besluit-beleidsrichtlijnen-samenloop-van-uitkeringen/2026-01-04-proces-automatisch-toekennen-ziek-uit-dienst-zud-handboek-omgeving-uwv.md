---
source_id: 2026-01-04-woo-besluit-beleidsrichtlijnen-samenloop-van-uitkeringen/2026-01-04-proces-automatisch-toekennen-ziek-uit-dienst-zud-handboek-omgeving-uwv
publication_slug: 2026-01-04-woo-besluit-beleidsrichtlijnen-samenloop-van-uitkeringen
pdf_slug: 2026-01-04-proces-automatisch-toekennen-ziek-uit-dienst-zud-handboek-omgeving-uwv
source_page_url: https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2025/woo-besluit-beleidsrichtlijnen-samenloop-van-uitkeringen
pdf_url: https://www.uwv.nl/assets-kai/files/0fdee76b-3291-45fe-9a76-df4b07aaf9a3/proces-automatisch-toekennen-ziek-uit-dienst-(zud)---handboek-omgeving---uwv.pdf
publication_title: Woo-besluit beleidsrichtlijnen samenloop van uitkeringen
publication_date: '2026-01-04T23:00:00Z'
publication_type: WOO publicatie
pdf_label: Proces automatisch toekennen Ziek uit dienst (ZUD) - Handboek omgeving
  - UWV (PDF, 424 kB)
retrieved_at: '2026-07-06T10:07:30+00:00'
sha256: e1df939e1845adaade259b1caf03b2c49042c17b8a27e18ca55723d61d0f86b7
page_count: 6
ocr_used: false
---

Home » Handboeken » Proces Backoffice ZW » UD » Automatisch proces » Proces automatisch toekennen Ziek uit dienst (ZUD)

Doorzoek handboek Proces Backoffice ZW

Toon meer velden Wis filters

## Proces Backoffice ZW

## Proces automatisch toekennen Ziek uit dienst (ZUD)

◄ ►

Procesinformatie Algemeen

Er is een automatisch proces waarmee UZS de claimfase van ZW-aanvragen Ziek uit dienst (ZUD) volledig uitvoert.

Aanvragen die van IDC naar Claim zijn overgedragen, worden aangeboden aan het proces ‘Automatisch toekennen’. Dit heet ook het

automatisch claimproces.

In dit proces voert UZS (met uitzondering van het controleren van de gegevens in Suwinet) de volgende handelingen van de claimfase uit

zonder jouw tussenkomst:

## •

Bepalen of het een gladde aanvraag is

## •

Bepalen van recht, hoogte en duur

## •

Toekennen van de aanvraag

## •

Versturen van de toekenningsbrief

Wie Uitkeringsdeskundige (UD)

Divisie Uitkeren – Ziektewet

Samenvatting Beschrijving van het automatisch proces in UZS van een aanvraag

Ziek uit dienst (ZUD).

Input

Cliënt Aanvraag Ziek uit dienst (ZUD)

Termijnen en procesacties

Beslistermijn

Doorlooptijd

Acties

## Processchema automatisch toekennen Ziek uit dienst (ZUD)

Je kunt ook een uitvergrote versie van het processchema (pdf) bekijken.

## Procesbeschrijving automatisch toekennen Ziek uit dienst (ZUD)

## Aanvraag ZUD met status ‘IB’

UZS selecteert de aanvragen die in aanmerking komen voor het automatisch proces.

De voorwaarden om een aanvraag in het automatisch proces op te nemen zijn:

## •

De aanvraag:

## •

heeft de status ‘In behandeling’ (IB);

## •

is niet eerder afgewezen;

## •

is niet van een eigenrisicodrager;

## •

is niet eerder door het automatisch proces gegaan;

## •

is geen administratief voortgezet geval.

## •

Er moet een rechtsgrond zijn die recht op uitkering geeft.

Als de aanvraag aan de voorwaarden voldoet, selecteert UZS de vangnetcategorie waarin de aanvraag thuishoort en de filters die het

automatisch proces voor de aanvraag moet doorlopen. Voor de vangnetcategorie ZUD zijn dit de filters:

## •

ZUD Controle 4A

## •

ZUD Claim 2A

## •

ZUD Claim 2B

Let op: Als je tijdens het automatisch proces de vangnetcategorie wijzigt, heeft UZS in de meeste gevallen niet alle filters die bij de

gewijzigde categorie horen doorlopen. Daarom haal je de aanvraag altijd uit het automatisch proces en handel je die verder handmatig

af.

Na het selecteren van de vangnetcategorie en de filters controleert UZS of het automatisch proces voor de aanvraag mag doorgaan. Het

automatisch proces mag niet doorgaan als de ‘Datum ingang claim’ niet bekend is of in de toekomst ligt:

## •

Als het automatisch proces mag doorgaan, vult UZS in het scherm Beheren automatisch proces in het blok “Historie statusovergangen

automatisch proces RHD” het veld <Status> met ‘Claim fase gestart’.

## •

Als het automatisch proces niet mag doorgaan, vult UZS het veld <Status> met ‘Claimcontroles afgerond’ en zet signaal UZZ0438 Nog

niet toe- of afgewezen aanvraag: uitval automatisch proces voor je klaar.

## Opvragen dagloon

Voor de vangnetcategorie ZUD stelt het automatisch proces het dagloon vast. UZS verstuurt hiervoor een verzoek aan de dagloonmodule

(DMO) om het dagloon te berekenen.

UZS controleert gedurende 10 seconden of het resultaat van de dagloonberekening is ontvangen. Als UZS geen resultaat ontvangt, wacht

UZS 1 dag en controleert dan opnieuw of het resultaat is ontvangen. Is het resultaat na de wachtdag nog steeds niet ontvangen, dan vult

UZS in het scherm Beheren automatisch proces het veld <Reden uitval DMO> en gaat het automatisch proces verder.

Als UZS het resultaat van DMO ontvangt, dan verwerkt UZS het dagloon dat DMO heeft berekend. Als DMO met de gegevens uit Polis geen

dagloon kan berekenen, dan vult UZS het veld <Reden uitval DMO>. Ongeacht het resultaat, gaat het automatisch proces verder.

Alleen als DMO het dagloon niet kan berekenen omdat de koppeling tussen DMO en andere systemen niet werkt, zet UZS de aanvraag als

het kan 1 dag in de wacht (Wachttijd B). De volgende dag stuurt UZS opnieuw het verzoek aan DMO om het dagloon te berekenen. Heeft

UZS geen tijd meer om te wachten, dan vult UZS het veld <Reden uitval DMO> en gaat het automatisch proces verder.

## Controleren voorwaarden

Voordat het controleren van de gegevens van de aanvraag begint, controleert UZS of de aanvraag ZUD aan de volgende voorwaarden

voldoet:

## •

De soort aanvraag is ‘Ziek uit dienst (ZW)’

## •

De soort verzekeringsbasis is ‘Dienstverband’

## •

De status is ‘In behandeling’ (IB)

Als de aanvraag voldoet aan deze voorwaarden, voegt UZS de <Status> ‘Geval automatisch afhandelen’ toe in het scherm ‘Beheren

automatisch proces’.

Als de aanvraag niet voldoet aan de voorwaarden, dan valt de aanvraag uit het automatisch proces en zet UZS signaal UZZ0438 Nog niet

toe- of afgewezen aanvraag: uitval automatisch proces voor je klaar. UZS voegt in het scherm Beheren automatisch proces de regels ‘Geval

handmatig afhandelen’ en ‘Claimcontroles afgerond’ toe.

## ZUD Controle 4A

Met dit filter controleert UZS of de gegevens aanwezig zijn die het automatisch proces nodig heeft om de aanvraag af te handelen. Omdat

UZS geen controle in Suwinet kan uitvoeren, zet UZS bij iedere aanvraag ZUD signaal UZZ0563 Beoordelen resultaat controlefilter voor je

klaar.

Je handelt filterregel 193 dus altijd handmatig af. De aanvragen ZUD gaan toch wel allemaal het automatisch proces in omdat er andere

voordelen zijn: UZS berekent het dagloon automatisch en als na het afhandelen van het controlefilter alle andere filters akkoord zijn, handelt

het automatisch proces de rest van de claimbeoordeling af.

In het scherm Raadplegen filterresultaat kun je zien welke gegevens ontbreken als je het roodgekleurde filter selecteert. Als achter een

filterregel het veld <Akkoord> is gevuld met ‘Nee’, dan vul je de gegevens aan met behulp van de werkinstructie Afhandelen filterresultaat

claim. Door het aanvullen van de gegevens voorkom je uitval uit het automatisch proces en kan het automatisch proces gegevens

controleren, het dagloon berekenen en daardoor meer aanvragen afhandelen. Als je de gegevens niet (tijdig) kunt aanvullen, valt de

aanvraag pas uit het automatisch proces na filter ‘ZUD Claim 2B’.

Filterregels ZUD Controle 4A

Nummer Filterregel

4 Er is een geldige arbeidsverhouding

5 Rekeningnummer werknemer is bekend bij directe uitkering

8 Adresgegevens komen overeen

10 Er is een voorkeur correspondentieadres of domicilieadres

bekend

11 Buitenlandse werknemer heeft een geldige verblijfstitel

16 Artikel 46 is niet van toepassing

40 Het betreft een directe uitkering

55 Er is geen andere lopende ziekmelding

56 Er is geen sprake van een verwijtbare te late ziekmelding

88 De eerste ziektedag valt op een dag waarop verzekerde werkt

105 Er is geen lopende MLA melding

170 De machtiging is verwerkt of niet van toepassing

171 Loonheffingskorting wordt toegepast

172 DMO heeft het dagloon bepaald of n.v.t.

187 Arbeidsovereenkomst is voor bepaalde tijd

188 Het aantal opvolgende arbeidsovereenkomsten binnen 6

maanden is maximaal 3

189 Er is geen sprake van eerdere beëindiging

190 Totale duur van opvolgende AOK is niet langer dan de

toegestane periode

192 Er is geen sprake van faillissement

193 Gegevens komen overeen met Suwinet

## Filter ZUD Claim 2A

Na filter ZUD Controle 4A volgt filter ZUD Claim 2A. Anders dan bij het controlefilter bevat dit filter controles op gegevens waardoor UZS een

aanvraag niet automatisch mag afhandelen.

Filterregels ZUD Claim 2A

Nummer Filterregel

40 Het betreft een directe uitkering

96 Er is geen sprake van AOW plus

191 Er is sprake van een arbeidsovereenkomst

221 Er is geen sprake van een ingetrokken ziekmelding

Als in filter ZUD Claim 2A achter alle filterregels het veld <Akkoord> is gevuld met ‘Ja’, dan voegt UZS in het scherm Beheren automatisch

proces de <Status> ‘UZS gecontroleerd, wachttijd’ toe. Als achter een filterregel het veld <Akkoord> is gevuld met ‘Nee’, dan valt de

aanvraag uit het automatisch proces en zet UZS signaal UZZ0438 Nog niet toe- of afgewezen aanvraag: uitval automatisch proces voor je

klaar. In het scherm ‘Beheren automatisch proces’ voegt UZS de regels ‘UZS, handmatig afhandelen’ en ‘Claimcontroles afgerond’ toe.

Als UZS eerder bij ‘Opvragen dagloon’ DMO een dagloon heeft berekend, bereken je bij uitval van de aanvraag niet opnieuw het dagloon. Dit

is dan al door het automatisch proces vastgesteld.

Vaste wachttijd

Na deze controles door UZS gaat de aanvraag direct door in het automatisch proces.

## Filter ZUD Claim 2B

Met dit filter controleert UZS nogmaals of alle gegevens aanwezig zijn die het automatisch proces nodig heeft om de aanvraag af te

handelen.

Filterregels ZUD Claim 2B

Nummer Filterregel

4 Er is een geldige arbeidsverhouding

5 Rekeningnummer werknemer is bekend bij directe uitkering

8 Adresgegevens komen overeen

10 Er is een voorkeur correspondentieadres of domicilieadres

bekend

11 Buitenlandse werknemer heeft een geldige verblijfstitel

16 Artikel 46 is niet van toepassing

40 Het betreft een directe uitkering

55 Er is geen andere lopende ziekmelding

56 Er is geen sprake van een verwijtbare te late ziekmelding

83 Het ziektegeval is plausibel

88 De eerste ziektedag valt op een dag waarop verzekerde werkt

105 Er is geen lopende MLA melding

170 De machtiging is verwerkt of niet van toepassing

171 Loonheffingskorting wordt toegepast

187 Arbeidsovereenkomst is voor bepaalde tijd

188 Het aantal opvolgende arbeidsovereenkomsten binnen 6

maanden is maximaal 3

189 Er is geen sprake van eerdere beëindiging

190 Totale duur van opvolgende AOK is niet

192 Er is geen sprake van faillissement

193 Gegevens komen overeen met Suwinet

221 Er is geen sprake van een ingetrokken ziekmelding

Als achter alle filterregels het veld <Akkoord> is gevuld met ‘Ja’, dan voegt UZS in het scherm Beheren automatisch proces de <Status>

‘Toekenbaarheid gecontroleerd’ toe en het automatisch proces gaat verder.

Als nog niet achter alle filterregels het veld <Akkoord> is gevuld met ‘Ja’, dan voegt UZS de <Status> ‘Toekenbaarheid, wachttijd’ toe. UZS

wacht vervolgens maximaal 7 dagen voor het automatisch proces verdergaat.

Iedere dag controleert UZS of alle filterregels akkoord zijn. Zodra alle filterregels akkoord zijn, gaat het automatisch proces verder. Dit geeft

de MVB de tijd om de plausibiliteit te verwerken. Het geeft jou ook de tijd om gegevens te verwerken waarvoor je eventueel informatie hebt

opgevraagd vanwege filter ZUD Controle 4A.

Als na deze periode nog steeds niet alle filterregels akkoord zijn, dan valt de aanvraag uit het automatisch proces. Als op het geval eerder

signaal ‘UZZ0563 Beoordelen resultaat controlefilter’ is gezet, dan zet UZS signaal UZZ0605 Nog niet toe- of afgewezen aanvraag: uitval

automatisch proces voor je klaar. Is eerder signaal ‘UZZ0563’ niet gezet, dan zet UZS signaal UZZ0438 Nog niet toe- of afgewezen

aanvraag: uitval automatisch proces voor je klaar. In het scherm ‘Beheren automatisch proces’ voegt UZS dan <Status> ‘Toekenbaarheid,

handmatig afhandelen’ en <Status> ‘Claimcontroles afgerond’ toe. Als eerder bij ‘Opvragen dagloon’ DMO een dagloon heeft berekend,

bereken je bij het verder afhandelen van de aanvraag niet opnieuw het dagloon.

## Opvragen dagloon

Nu het automatisch proces alle gegevens heeft om toe te kennen, controleert UZS of er eerder al een dagloon is vastgesteld (door DMO of

handmatig):

## •

Is het dagloon bekend, dan gaat het automatisch proces verder.

## •

Is er geen dagloon bekend, dan verstuurt UZS opnieuw een verzoek aan DMO om het dagloon te berekenen. Geeft DMO ditmaal een

dagloon terug, dan gaat het proces verder.

Als DMO het dagloon nog steeds niet kan berekenen, dan valt de aanvraag uit het automatisch proces. Als op het geval eerder signaal

‘UZZ0563 Beoordelen resultaat controlefilter’ is gezet, dan zet UZS signaal UZZ0605 Nog niet toe- of afgewezen aanvraag: uitval

automatisch proces voor je klaar. Is eerder signaal ‘UZZ0563’ niet gezet, dan zet UZS signaal UZZ0438 Nog niet toe- of afgewezen

aanvraag: uitval automatisch proces voor je klaar.

## Bepalen recht en duur

Na het vaststellen van de hoogte legt het automatisch claimproces het recht en de duur vast. UZS controleert ook of UZS rekening moet

houden met vangnetcategorie specifieke zaken. Voor de vangnetcategorie ZUD onderzoekt UZS of er een hersteldatum bekend is:

## •

Hersteldatum bekend: UZS houdt de hersteldatum aan als ‘Datum einde recht’.

## •

Hersteldatum niet bekend: UZS zet de ‘Datum einde recht’ op de Max-datum.

Als het recht en de duur zijn vastgesteld, voegt UZS in het scherm Beheren automatisch proces de <Status> ‘RHD bepaald’ toe en gaat het

automatisch proces verder. Kan UZS recht en duur alsnog niet vaststellen, dan valt de aanvraag uit het automatisch proces. Als op het geval

eerder signaal ‘UZZ0563 Beoordelen resultaat controlefilter’ is gezet, dan zet UZS signaal UZZ0605 Nog niet toe- of afgewezen aanvraag:

uitval automatisch proces voor je klaar. Is eerder signaal ‘UZZ0563’ niet gezet, dan zet UZS signaal UZZ0438 Nog niet toe- of afgewezen

aanvraag: uitval automatisch proces voor je klaar. In het scherm ‘Beheren automatisch proces’ voegt UZS dan <Status> ‘RHD niet bepaald’

en ‘Claimcontroles afgerond’ toe.

## Toekennen

Na het definitief vaststellen van recht, hoogte en duur kent UZS de aanvraag toe. Doordat de status van het geval naar ‘Toegewezen’ (T)

wijzigt, selecteert UZS de toekenningsbrief en fiatteert die. In het scherm Beheren automatisch proces voegt UZS de <Status> ‘Toekennen

geslaagd, automatisch proces afgerond’ toe en gaat het automatisch proces verder met de laatste stap.

Als UZS alsnog niet kan toekennen, dan valt de aanvraag uit het automatisch proces. Als op het geval eerder signaal ‘UZZ0563 Beoordelen

resultaat controlefilter’ is gezet, dan zet UZS signaal UZZ0605 Nog niet toe- of afgewezen aanvraag: uitval automatisch proces voor je klaar.

Is eerder signaal ‘UZZ0563’ niet gezet, dan zet UZS signaal UZZ0438 Nog niet toe- of afgewezen aanvraag: uitval automatisch proces voor

je klaar. In het scherm ‘Beheren automatisch proces’ voegt UZS dan <Status> ‘Toekennen niet geslaagd’ en ‘Claimcontroles afgerond’ toe.

Als de aanvraag op dit moment in het proces uitvalt, dan komt dat vaak omdat er na de controles van het laatste filter een gegeven in het

dossier is gewijzigd. Om de exacte reden te achterhalen waarom UZS de aanvraag niet kan toekennen, klik je op de knop “Toekennen”. UZS

geeft dan een foutmelding die vermeldt waarom UZS niet kan toekennen. Je beoordeelt of wijzigt dan alleen dat gegeven. Soms volgt er

geen foutmelding. Het probleem is dan inmiddels al opgelost (omdat bijvoorbeeld een rekeningnummer na het wijzigen is gefiatteerd).

## Toekenningsbrief

Als laatste stap in het automatisch claimproces controleert UZS of de toekenningsbrief automatisch is klaargezet en gefiatteerd. Is dit het

geval, dan is dit het einde van het automatisch claimproces. UZS rondt het automatisch claimproces af door in het scherm Beheren

automatisch proces de <Status> ‘Brief automatisch gefiatteerd’ en <Status> ‘Claimcontroles afgerond’ toe te voegen.

Als UZS de toekenningsbrief niet heeft gefiatteerd, dan zet UZS signaal UZZ0334 Afhandelen uitgaande brief voor je klaar. Je controleert en

verstuurt de brief dan handmatig. In het scherm ‘Beheren automatisch proces’ voegt UZS in deze situatie <Status> ‘Brief niet aangemaakt of

gefiatteerd’ en ‘Claimcontroles afgerond’ toe.

## Continueren

De handelingen die voor het continueren en beëindigen van de uitkering nodig zijn, behoren niet tot het automatisch claimproces.

## Tellingen

Aanvragen die automatisch verwerkt zijn, worden apart geteld in de werkverdeling en de OSI-lijsten.

Output

Intern UZS-signalen:

## •

UZZ0334 Afhandelen uitgaande brief

## •

UZZ0438 Nog niet toe- of afgewezen aanvraag: uitval

automatisch proces

## •

UZZ0563 Beoordelen resultaat controlefilter

## •

UZZ0605 Nog niet toe- of afgewezen aanvraag: uitval

automatisch proces

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

Bron: [Woo-besluit beleidsrichtlijnen samenloop van uitkeringen](https://www.uwv.nl/nl/wet-open-overheid/woo-publicaties/2025/woo-besluit-beleidsrichtlijnen-samenloop-van-uitkeringen) · [Proces automatisch toekennen Ziek uit dienst (ZUD) - Handboek omgeving - UWV (PDF, 424 kB)](https://www.uwv.nl/assets-kai/files/0fdee76b-3291-45fe-9a76-df4b07aaf9a3/proces-automatisch-toekennen-ziek-uit-dienst-(zud)---handboek-omgeving---uwv.pdf)
