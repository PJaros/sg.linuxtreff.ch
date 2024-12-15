Title: Über den Linuxtreff St. Gallen
Save_as: index.html

Der Linuxtreff St. Gallen ist eine engagierte Gemeinschaft von Linux-Enthusiasten, die sich regelmäßig treffen, um Wissen zu teilen, Erfahrungen auszutauschen und anderen bei ihren Anliegen rund um Linux zu helfen. Ganz gleich, ob du ein absoluter Neuling bist, der gerade erst auf Linux umsteigt, oder ein erfahrener Anwender, der vor einer kniffligen Herausforderung steht – bei uns bist du herzlich willkommen.

## Wie wir helfen
 - **Individuelle Beratung:** Bring dein Problem mit, und wir schauen uns gemeinsam an, was los ist. Ob es um die Installation einer neuen Distribution, die Konfiguration von Software oder die Behebung von Fehlern geht - wir stehen dir zur Seite.
 - **Community-Support:** Unser Treffen bietet eine entspannte Atmosphäre, in der du Fragen stellen kannst, ohne dich unwohl zu fühlen. Es gibt keine "dummen“ Fragen – nur Gelegenheiten, dazuzulernen.
 - **Online-Support:** Neben unseren physischen Treffen sind wir über unsere [Mailingliste](https://lists.sg.linuxtreff.ch/mailman/listinfo/mailingliste) erreichbar, um schnelle Hilfe zu leisten, wenn du nicht bis zum nächsten Treffen warten kannst.

## Der Treff

![Ruum42 Eingang]({static}/pages/eingang.jpg)
![Ruum42 Eingang näher]({static}/pages/eingang2.jpg)
{: .text-center }

<!-- {: style='align:center;' } -->
<!-- {: #someid .someclass somekey='some value' } -->

Die Türen zum Linuxtreff öffnen jeden Dienstag um 18:30 im Hackerspace Ruum42 in St.&nbsp;Gallen an der Andreasstrasse 5.

Der Eingang befindet sich auf der linken Seite bei der Garage Enzler im Kellergeschoss. Für Strom und Internetzugang ist gesorgt. Getränke sind vorhanden. Wir holen uns zusammen auch immer wieder mal eine Pizza.

<div id="map" style="width: 600px; height: 400px; margin-bottom: 20px;"></div>
<script>
    const coord = [47.420653,9.355746];
    const map = L.map('map').setView(coord, 17);
    const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    var marker = L.marker(coord).addTo(map);
</script>
