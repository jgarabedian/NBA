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
        var matchup = matchTeams.replace(' vs ', '_').replace(' ', '-')
        a.href = matchup;
        appendElement(match, a)
        changeId(match.parentElement.parentElement, matchup);
        // match.parentElement.parentElement.addEventListener('click', function() {
        //     focusMatchups(matchup);
        // })
    }
}

function focusMatchups(matchup) {
    matchup = matchup.id;
    divs = document.getElementsByClassName('betting__matchup')
    for (i = 0; i < divs.length; i++) {
        if (divs[i].id !== matchup) {
            divs[i].style.display = 'none'
        }
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
function changeId(el, id) {
    el.id = id;
    return el;
}

