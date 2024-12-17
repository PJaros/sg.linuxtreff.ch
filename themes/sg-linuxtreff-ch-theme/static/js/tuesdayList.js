function formatDate(d, weekdayOverride = null) {
    // Options: https://www.w3schools.com/jsref/jsref_tolocalestring.asp
    // Combination: https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/
    const opts = {year: 'numeric', month: 'short', day: 'numeric'};
    var date = d.toLocaleString('de-CH', opts); // Result: "2. Dezember 2024"
    // From: https://stackoverflow.com/a/27347503/406423
    var weekday = d.toLocaleString('de-CH', {weekday: "long"}); // Result: "Montag"
    return (weekdayOverride || weekday) + ", " + date + ", 18:30"
}
function formatIsoDate(d) {
    // From: https://stackoverflow.com/a/29774197/406423
    return d.toISOString().split('T')[0];
}
function writeTuesdayList(blockedDates, nbClass, bClass, element) {
    const dayInMs = 24 * 60 * 60 * 1000;
    let now       = new Date();
    // let now      = new Date(new Date().getTime() - (dayInMs * 2));
    let daysUntilTuesday = 2 - now.getDay(); // "Distanz" zum Dienstag
    if (daysUntilTuesday < 0) daysUntilTuesday += 7; // Falls in der Vergangenheit -> +7 Tage

    let output = "";
    for (let i = 0; i < 3; i++) {
        let tuesday = new Date(now.getTime() + dayInMs * ((7 * i) + daysUntilTuesday));
        let weekDayOverride = (now.getDay() == 2 && i == 0) ? "Heute" : null; // 2 == Dienstag
        // let isoDate = formatIsoDate(tuesday);
        // let isBlocked = blockedDates.includes(isoDate);
        // console.log("isoDate: " + isoDate + ", isBlocked: " + isBlocked);
        let liClass = (blockedDates.includes(formatIsoDate(tuesday))) ? bClass : nbClass;
        output += "<li class='" + liClass +"' >" + formatDate(tuesday, weekDayOverride) + "</li>";
    }
    document.getElementById(element).innerHTML += output;
}
