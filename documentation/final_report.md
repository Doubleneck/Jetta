# Loppuraportti

Ryhmän Jetta osallistujat:
- Jaakko Paananen
- Eero Vahteri
- Taneli Härkönen
- Tatu Sorjonen
- Antti Vuorenmaa

Yleisesti voidaan todeta, että kolmen viikon (ja kolmen sprintin) aikana ryhmä oppi paljon yhteistyöstä, yhdessä koodaamisen haasteista 
ja ketterästä prosessista. Ehkä merkittävin oppi tuli siitä - vaikka kuulostaakin ehkä triviaalilta - että toisin kuin yksilötyössä
kommunikaatio nousee aivan erilaiseen asemaan. 

Suurimmaksi osaksi ryhmämme kokoontui kasvotusten sprinttien suunnitteluun ja retroihin, mutta kaikki koodasivat pääasiassa erikseen.
Päädyimme alusta lähtien käyttämään gitissä lyhyitä feature brancheja, mikä osoittautui meillä erinomaisesti toimivaksi ratkaisuksi.


## Sprint 1

Alku tuntui todella haastavalta. Meni päiviä ennen kuin saimme prosessin raiteilleen, koska toisaalta piti tavoitella toteutuvaa ohjelmaa ja toisaalta
opetella scrumia, joka ei ollut kenellekään ennalta tuttu. Suuri yllätys oli prosessin ja varsinkin alkutoimien hitaus.

Tekniset haasteet liittyivät alussa lähinnä siihen, miten saamme web-sovelluksen nettiin, Docker-osaamisen puuttuminen oli tässä kohdassa ehkä se, 
mikä hidasti ensimmäistä sprinttiä. Löysimme kuitenkin nopeasti ratkaisuja, jotka optimoivat yhtä aikaa kaksi asiaa:
Käytetään teknologioita jotka ovat kaikkien ryhmän jäsenten saatavilla, ja toisaalta toteuttavat alustavasti vaatimukset.

Eli hylättiin deployaaminen Flyhin, ja todettiin että Python Flaskin omalla demoserverillä voi demota tarvittavat asiat.
Valittiin tietokannaksi SqLite3, joka tuntui riittävältä, mutta kevyemmältä ratkaisulta kuin PostgreSql.

Testaaminen aloitettiin heti alussa. Hyväksymiskriteeriksi asetimme 70% testikattavuuden, mutta käytännössä se oli yksikkötesteillä 
noin 90% läpi projektin plus robottestit.

Toinen tekninen haaste liittyi robot-testien konfigurointiin ja niitten liittämiseen Github Actionssiin.
Saimme kuitenkin yhden User Storyn toteutettua, ja asiakastapaamisen jälkeen paineet tuntuivat hellittävän - olimme saaneet yhdessä aikaiseksi
tähän asti toimivan sovelluksen.

Viikon lopussa pidettiin glad-sad-mad retro, jossa tartuttiin isoimpiin kehityskohtiin: tuntimäärien parempi estimaatio ja sprintin aloittaminen alkuviikosta, mikä sopi ryhmän aikatauluihin paremmin. Glad -osioon tuli hyvää palautetta kommunikaatiosta, joka oikeastaan pysyi glad -osiossa, tiiviinä ja avoimena koko projektin ajan.

## Sprint 2

Toisella viikolla tilannekuva oli onnistuneen asiakastapaamisen jälkeen huomattavasti selkeämpi. Myös se, että aloimme tuntea toisiamme helpotti 
työskentelyä. Roolit jakautuivat helposti.

Teknisenä haasteena roikkui pitkän aikaa edelleen robot-testien lopullinen konfiguraatio ja toimiminen oikein CI-putkessa. Se lopulta onnistui.
Viikko kului perusrakennetta tehdessä, jatkuvasti refaktoroidessa ja pyrkimyksenä pitää CI koko ajan vihreänä. 

Otettin käyttöön Googlen lintteri, josta muokattiin meille sopiva. Monia asioita korjattiin ja muutettiin lennosta, mm. tietokantakonfiguraatiota
korjattiin.

Viikon lopussa pidettiin taas glad-sad-mad retro. Tällä kertaa tunnit pysyivät paremmin estimaateissa ja sprintin aloittaminen onnistui alkuviikosta, joten lappunen siirtyi glad -osioon.

## Sprint 3

Kolmannella viikolla toteutettiin sovelluksen ydintoiminnallisuus eli bibtexin luominen, downloadaaminen, validoinnit jne.
Tässä sprintissä tuli eniten konfliktiä sovelluksen eri osa-alueiden välillä - ja myös eniten kommunikaatiokysymyksiä, miten arkkitehtuuri pitäisi
tehdä, jne. Todettakoon vielä kerran, että näissä kohdissa myös tapahtui oppimista sekä kommunikaatiotasolla että yhteisprojektin erilaisista
vaatimuksista.


Lopputuloksena syntyi mielestämme varsin helppokäyttöinen ja selkeästi toteutettu sovellus, josta aivan kaikkia user storyja emme ehtineet toteuttaa.


