// Initialize
var mpgChart = echarts.init(document.getElementById('mpg-left'));

// testData
var testData = {
    'Jrue Holiday': {
        'min': '34:08'
    },
    'Mike Conley': {
        'min': '30:33'
    }
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
    time = min + sec;
    return time;
}

function getMPGDiff(time) {
    let maxTime = 48;
    let mpgDiff = maxTime - time;
    return mpgDiff;
}

function paintMPG() {
    mpgChart.setOption(mpgOption);
}

var mpgOption = {
    color: ['lime', 'transparent'],
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        x: 'left',
        data: ['Playing', 'Bench']
    },
    series: [
        {
            name: 'Time',
            type: 'pie',
            radius: ['70%', '90%'],
            avoidLabelOverlap: false,
            label: {
                normal: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '30',
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
                    value: getMPG(testData, 0),
                    name: 'Playing'
                },
                {
                    value: getMPGDiff(getMPG(testData, 0)),
                    name: 'Bench'
                }
            ]
        }
    ]
};