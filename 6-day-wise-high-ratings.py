from calendar import month, week
import justpy as jp
import pandas
from datetime import datetime

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Daynumber'] = data['Timestamp'].dt.strftime('%w')


weekday_average = data.groupby(['Weekday','Daynumber']).mean()
weekday_average = weekday_average.sort_values('Daynumber')

print(weekday_average)

char_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pt-md")
    p1 = jp.QDiv(a=wp, text = "These graph represents course review analysis", classes = "text-h5 text-center q-pt-md")
    hc = jp.HighCharts(a=wp, options = char_def)
    hc.options.title.text = "Average Ratings by Course by MOnth"

    #hc.options.xAxis.categories = list(weekday_average.index)

    # hc_data = [{"name":v1, "data": [v2 for v2 in month_average[v1]]} for v1 in month_average.columns]
    # print(hc_data)
    x = weekday_average.index.get_level_values(0)
    y = weekday_average['Rating']
    hc.options.xAxis.categories = list(x)
    hc.options.series[0].data = list(y)
    print(hc.options.title.text)
    print(type(hc.options))

    return wp

jp.justpy(app)