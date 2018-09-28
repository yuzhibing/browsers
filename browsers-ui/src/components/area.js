import React, { Component } from 'react';
import Highcharts from 'highcharts';
import { connect } from 'react-redux';
import { isArray } from 'util';

class AreaChart extends Component {
  constructor(props) {
    super(props);
    this.state = {
        largeAccount: [],
        nonZeroAccount: [],
        activityAccount: [],
        totalAccount: [],
        categories: [],
        pointStart: ''
    }
    this.renderCharts = this.renderCharts.bind(this);
  }

  render() {
    return(
        <div className='area-container'>
            <div id='large-container'></div>
            <div className='white-space'></div>
            <div id='account-container'></div>
            <div className='white-space'></div>
            <div id='activity-container'></div>
        </div>
    )
  }

  componentWillReceiveProps(newProps) {
    if(newProps.addressList && newProps.addressList instanceof Array) {
        let addressList = newProps.addressList, largeAccount = [], totalAccount = [], activityAccount = [], nonZeroAccount = [], categories = [], pointStart = addressList[0][0];
        addressList.length > 0 && addressList.map( (item, idx) => {
        largeAccount.push(item[1]);
        nonZeroAccount.push(item[2])
        activityAccount.push(item[3]);
        totalAccount.push(item[4]);
        categories.push(item[0])
        })

        this.setState({largeAccount, nonZeroAccount, activityAccount, totalAccount, pointStart, categories}, this.renderCharts)
    }
  }

  componentDidMount() {
    this.renderCharts()
  }

  renderCharts() {      
    let {largeAccount, nonZeroAccount, activityAccount, totalAccount, categories, pointStart} = this.state;
    let chart1 = Highcharts.chart('account-container',{
        chart: {
            type: 'area'
        },
        title: {
            text: '账户数统计'
        },
        xAxis: {
            allowDecimals: false,
            categories: categories
        },
        yAxis: {
            title: {
                text: ''
            },
        },
        tooltip: {
          //   pointFormat: '{series.name} 制造 <b>{point.y:,.0f}</b>枚弹头'
        },
        
        series: [{
            name: '非零账户数',
            color: '#77a2c5',
            data: nonZeroAccount
        }, {
            name: '账户总数',
            color: '#a4c1d8',
            data: totalAccount 
        }]
    });

    let chart2 = Highcharts.chart('activity-container',{
        chart: {
            type: 'area'
        },
        title: {
            text: '活跃账户数'
        },
        xAxis: {
            allowDecimals: false,
            categories: categories
        },
        yAxis: {
            title: {
                text: ''
            },
        },
        tooltip: {
          //   pointFormat: '{series.name} 制造 <b>{point.y:,.0f}</b>枚弹头'
        },
        
        series: [{
            name: '活跃账户数',
            color: '#a4c1d8',
            data: activityAccount 
        }]
    });

    let chart3 = Highcharts.chart('large-container',{
        chart: {
            type: 'area'
        },
        title: {
            text: '大户账户'
        },
        xAxis: {
            allowDecimals: false,
            categories: categories
        },
        yAxis: {
            title: {
                text: ''
            },
        },
        tooltip: {
          //   pointFormat: '{series.name} 制造 <b>{point.y:,.0f}</b>枚弹头'
        },
        
        series: [{
            name: '大户账户数',
            color: '#a4c1d8',
            data: largeAccount 
        }]
    });
  }
}


function mapState(state) {
  return {
    addressList: state.addressList.addressList
    // orders: state.homeOrder.orders
  }
}

function mapDispatch(dispatch) {
	return {
		// getOrders: () => dispatch(requestHomeOrder())
	}
}

export default connect(mapState, mapDispatch)(AreaChart);