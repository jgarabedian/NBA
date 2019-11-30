// Initialize
var mpgChart = echarts.init(document.getElementById('mpg-left'));
var mpgChart1 = echarts.init(document.getElementById('mpg-right'));

// testData
var testData = {
    'Jrue Holiday': {
        'min': '34:08'
    },
    'Mike Conley': {
        'min': '30:33'
    }
}

function getMPGData(data) {
    var player1Name = getPlayerNames(data)[0],
        player2Name = getPlayerNames(data)[1],
        player1 = {},
        player2 = {};
    var player1Stats = data[player1Name],
        player2Stats = data[player2Name];
    var mpgData = {};

    player1['min'] = player1Stats['min'];
    player2['min'] = player2Stats['min'];
    mpgData[player1Name] = player1;
    mpgData[player2Name] = player2;
    return mpgData;
}

function getMPG(data, playerIdx) {
    var min = Object.values(data[getPlayerNames(data)[playerIdx]]);
    var minData = [],
        i = 0;
    for (i; i < min.length; i++) {
        minData.push(convertTime(min[i]));
    }
    return minData;
}

function convertTime(time) {
    let sec = time.substr(3, 2);
    let min = parseInt(time.substr(0, 2), 10);
    sec = parseInt(sec, 10) / 60;
    time = (min + sec).toFixed(2);
    return time;
}

function getMPGDiff(time) {
    let maxTime = 48;
    let mpgDiff = maxTime - time;
    return mpgDiff;
}

function paintMPG(mpgData) {
    mpgChart.setOption(setChartOption(mpgData, 0));
    mpgChart1.setOption(setChartOption(mpgData, 1));
}

function setChartOption(data, idx) {
    var mpgOption = {
        color: ['lime', 'transparent'],
        title: {
            show: true,
            text: getPlayerNames(data)[idx] + '  MPG',
            textStyle: {
                color: 'white',
                fontStyle: 'italic'
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: "{c} mpg"
        },
        series: [
            {
                name: getPlayerNames(data)[idx],
                type: 'pie',
                radius: ['70%', '80%'],
                avoidLabelOverlap: false,
                label: {
                    show: false,
                    normal: {
                        show: true,
                        position: 'center',
                        formatter: '{c} MPG'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '20',
                            fontWeight: 'bolder'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data: [
                    {
                        value: getMPG(data, idx),
                        name: 'Playing',
                        selected: true
                    },
                    {
                        value: getMPGDiff(getMPG(data, idx)),
                        name: 'Bench'
                    }
                ]
            }
        ]
    };
    return mpgOption;
}

// var mpgOption0 = {
//     color: ['lime', 'transparent'],
//     title: {
//         show: true,
//         text: getPlayerNames(mpgData)[0] + '  MPG',
//         textStyle: {
//             color: 'white',
//             fontStyle: 'italic'
//         }
//     },
//     tooltip: {
//         trigger: 'item',
//         formatter: "{c} mpg"
//     },
//     series: [
//         {
//             name: getPlayerNames(mpgData)[0],
//             type: 'pie',
//             radius: ['70%', '80%'],
//             avoidLabelOverlap: false,
//             label: {
//                 show: false,
//                 normal: {
//                     show: true,
//                     position: 'center',
//                     formatter: '{c} MPG'
//                 },
//                 emphasis: {
//                     show: true,
//                     textStyle: {
//                         fontSize: '20',
//                         fontWeight: 'bolder'
//                     }
//                 }
//             },
//             labelLine: {
//                 normal: {
//                     show: false
//                 }
//             },
//             data: [
//                 {
//                     value: getMPG(mpgData, 0),
//                     name: 'Playing',
//                     selected: true
//                 },
//                 {
//                     value: getMPGDiff(getMPG(mpgData, 0)),
//                     name: 'Bench'
//                 }
//             ]
//         }
//     ]
// };

// var mpgOption1 = {
//     color: ['lime', 'transparent'],
//     title: {
//         show: true,
//         text: getPlayerNames(mpgData)[1] + '  MPG',
//         textStyle: {
//             color: 'white',
//             fontStyle: 'italic'
//         }
//     },
//     tooltip: {
//         trigger: 'item',
//         formatter: "{c} mpg"
//     },
//     series: [
//         {
//             name: getPlayerNames(mpgData)[1],
//             type: 'pie',
//             radius: ['70%', '80%'],
//             avoidLabelOverlap: false,
//             label: {
//                 show: false,
//                 normal: {
//                     show: true,
//                     position: 'center',
//                     formatter: '{c} MPG'
//                 },
//                 emphasis: {
//                     show: true,
//                     textStyle: {
//                         fontSize: '20',
//                         fontWeight: 'bolder'
//                     }
//                 }
//             },
//             labelLine: {
//                 normal: {
//                     show: false
//                 }
//             },
//             data: [
//                 {
//                     value: getMPG(mpgData, 1),
//                     name: 'Playing',
//                     selected: true
//                 },
//                 {
//                     value: getMPGDiff(getMPG(mpgData, 1)),
//                     name: 'Bench'
//                 }
//             ]
//         }
//     ]
// };