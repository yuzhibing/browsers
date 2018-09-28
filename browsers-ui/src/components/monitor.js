import React, { Component } from 'react';
import Highcharts from 'highcharts';
import { connect } from 'react-redux';
import {requestHomeOrder} from 'actions/homeActions';


class MyMonitor extends Component {
  constructor(props) {
    super(props);
    this.state = {
      orders: props.orders || []
    }
    this.renderCharts = this.renderCharts.bind(this);
    this.renderOrders = this.renderOrders.bind(this);
  }

  componentWillReceiveProps(props) {
    this.setState({orders: props.orders}, this.renderOrders)
  }

  componentDidMount() {
    this.renderOrders();
  }

  render() {
    return(
      <div className='pb-10'>
        <div id='monitor'></div>
      </div>
    )
  }

  renderOrders() {
    let {orders} = this.state, data1 = [], data2 = [];
    orders.length > 0 && orders.map((item, idx) => {
      let time = item[4] + (8 * 60 * 60 * 1000);
      if(item[3]== 0) {
        // data1.push([time, Math.log(item[1])])
        data1.push({
          x: time,
          y: Math.log(item[1]),
          val: item[1]
        })
      } else if (item[3] == 1) {
        // data2.push([time, Math.log(item[1])])
        data2.push({
          x: time,
          y: Math.log(item[1]),
          val: item[1]
        })
      }
    
    })

    this.renderCharts(data1, data2)


  }

  renderCharts(data1, data2, data3, data4) {
    let formats='%H:%M';
    Highcharts.chart('monitor', {
      chart: {
        type: 'scatter',
        zoomType: 'xy'
      },
      title: {
        text: '24小时转入转出',
        style: {
          fontSize: '14px'
        }
      },
      subtitle: {
        // text: 'Source: Heinz  2003'
      },
      xAxis: {
        title: {
          enabled: true,
          text: 'time (hour)'
        },
        labels: {
          formatter: function() {
            return Highcharts.dateFormat(formats,this.value);
          }
        },
        type: 'datetime',
        startOnTick: true,
        endOnTick: true,
        showLastLabel: true,

      },
      yAxis: {
        title: {
          text: ''
        },
      },
      plotOptions: {
        scatter: {
          marker: {
            radius: 5,
            states: {
              hover: {
                enabled: true,
                lineColor: 'rgb(100,100,100)'
              }
            }
          },
          states: {
            hover: {
              marker: {
                enabled: false
              }
            }
          },
          tooltip: {
            
          }
        }
      },
      tooltip: {
        formatter: function() {
          return `${this.series.name}<br> 数量：${this.point.val}`
        }
      },
      series: [{
        name: '转出',
        color: 'rgba(252, 5, 46, 1)',
        data: data1
    
      }, {
        name: '转入',
        color: '#28a745',
        // color: '#007bff',
        data: data2
      }, 
      ]
    });
  }
}

function mapState(state) {
  return {
    orders: state.homeOrder.orders
  }
}

function mapDispatch(dispatch) {
	return {
		getOrders: () => dispatch(requestHomeOrder())
	}
}

export default connect(mapState, mapDispatch)(MyMonitor);
