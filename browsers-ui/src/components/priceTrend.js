import React, { Component } from 'react';
import Highcharts from 'highcharts';
import { connect } from 'react-redux';
import {requestPriceTrend} from 'actions/pricetrend';


class PriceTrend extends Component {
  constructor(props) {
    super(props);
    this.state = {
      period: 'day',
      format: '{value: %H:%M}',
      tickInterval: 3600 * 1000

    }
    this.renderTrend = this.renderTrend.bind(this);
    this.changePeriod = this.changePeriod.bind(this);
  }

  render() {
    let {period} = this.state;
    return (
      <div>

        <p className='change-period-tab'>
          <span className={`${period === 'day'? 'active': '' }`} onClick={() => this.changePeriod('day')}>一天</span>
          <span className={`${period === 'week'? 'active': '' }`} onClick={() => this.changePeriod('week')}>一周</span>
        </p>
        
        <div id='price-trend-container'></div>

      </div>
    )
  }

  changePeriod(period) {
    let {getPriceTrend} = this.props;
    this.setState({period})
    if(period === 'day') {
      this.setState({
        format: '{value: %H:%M}',
        tickInterval: 3600 * 1000
      })
      getPriceTrend(period)

    } else if(period === 'week') {
      this.setState({
        format: '{value: %m-%d}',
        tickInterval: 24 * 3600 * 1000
      })
      getPriceTrend(period)

    }
  }

  componentWillReceiveProps(props) {
    let data = props.data, total = [];
    data.length > 0 && data.map((item, idx) => {
      let time = item[0] + (8 * 60 * 60 * 1000);
      item[0] = time;
    })
    this.setState({data}, this.renderTrend)
  }

  componentDidMount() {
    this.renderTrend();
  }

  renderTrend() {
    let {format, tickInterval} = this.state;
    let {data} = this.state;
    // let formats='%m-%d';
    Highcharts.chart('price-trend-container', {
      chart: {
        zoomType: 'x'
      },
      title: {
        text: '',
      },
      subtitle: {
        text: ''
      },
      xAxis: {
        type: 'datetime',
        labels: {
          format: format
        },
        tickInterval: tickInterval,
        // startOnTick: true,
        // endOnTick: true,
        showLastLabel: true,
      },
      yAxis: {
        title: {
          text: ''
        },
        startOnTick: true,
        endOnTick: true,
        showLastLabel: true,
        tickPositions: [0, 1, 2, 3, 4, 5, 6]
      },
      legend: {
        enabled: false
      },
      plotOptions: {
        area: {
          fillColor: {
            linearGradient: {
              x1: 0,
              y1: 0,
              x2: 0,
              y2: 1
            },
            stops: [
              [0, Highcharts.getOptions().colors[0]],
              [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
            ]
          },
          marker: {
            radius: 2
          },
          lineWidth: 1,
          states: {
            hover: {
              lineWidth: 1
            }
          },
          threshold: null
        }
      },

      series: [{
        type: 'area',
        name: 'price',
        data: data,
      }]
    });
    
  }
}

function mapState(state) {
  return {
    data: state.priceTrend.list
  }
}

function mapDispatch(dispatch) {
	return {
		getPriceTrend: (period) => dispatch(requestPriceTrend(period)),
  }
}

export default connect(mapState, mapDispatch)(PriceTrend);