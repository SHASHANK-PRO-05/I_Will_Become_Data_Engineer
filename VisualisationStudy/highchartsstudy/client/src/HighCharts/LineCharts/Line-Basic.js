import React, {Component} from 'react'
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class LineBasic extends Component {
    state = {
        data: [],
        year: [],
        options: {
            title: {
                text: ''
            },
            series: [{
                data: []
            }]
        }
    };

    componentWillMount() {
        this.callAPI().then(res => {
            let sortedData = res.sort((a, b) => a._id > b._id)
            let years = [];
            let data = [];
            for (let iter = 0; iter < sortedData.length; iter++) {
                years.push(sortedData[iter]._id);
                data.push(sortedData[iter].count);
            }
            console.log(data);
            this.setState({
                data: data,
                years: years,
                options: {
                    title: {
                        text: 'Gun Violence Count 2013-2018'
                    },
                    subtitle: {
                        text: 'Kaggle Data set'
                    },
                    yAxis: {
                        title: {text: 'Count-->'}
                    },
                    xAxis: {
                        title: {
                            text: 'Year-->'
                        },
                        categories: years
                    },
                    legend: {
                        verticalAlign: 'bottom'
                    },
                    series: [{
                        name: 'Year wise count',
                        data: data
                    }]
                }
            })
        }).catch(err => console
            .log(err))
    };

    callAPI = async () => {
        const response = await fetch('/api/getYearWiseCount');
        const body = await response.json();
        if (response.status !== 200) throw Error(body.message)
        return body;
    };

    render() {
        return (<div><HighchartsReact
            highcharts={Highcharts}
            options={this.state.options}/></div>)
    }
}

export default LineBasic