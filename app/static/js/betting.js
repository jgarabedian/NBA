console.log('Betting page, welcome!')

/*
* @desc Add a span tag to isolate the teams in the matchup
*
*/

function isolateMatchups() {
    matchups = document.getElementsByClassName('betting__matchup__game__header');
    for (i = 0; i < matchups.length; i++) {
        match = matchups[i];
        matchItems = match.innerText.split(': ', [3])
        match.innerText = matchItems[0].trim() + ' '
        matchTeams = matchItems[1].trim()
        a = createElement('a')
        a.innerText = matchTeams
        addClass(a, 'matchup__teams')
        a.href = matchTeams.replace(' vs ', '_').replace(' ', '-');
        appendElement(match, a)
        
    }
}

function getUrl(string) {
    string.replace(' vs ', '-').replace(' ', '-')
    return string
}

function createElement(el) {
    return document.createElement(el)
}
function appendElement(parent, el) {
    return parent.appendChild(el);
}
function addClass(el, className) {
    el.className = className;
    return el;
}

window.onload = function () {
    this.isolateMatchups();
}