import React, { Component } from 'react';
import Highcharts from 'highcharts';
import { connect } from 'react-redux';
import {requestTransList} from 'actions/transAction';

class Transaction extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      period: 'hour',
      categories: []
    }
    this.renderTrend = this.renderTrend.bind(this);
    this.changePeriod = this.changePeriod.bind(this);

  }

  changePeriod(period) {
    let {getTransData} = this.props;
    this.setState({
      period
    })
    getTransData(period)
  }

  render() {
    let {period} = this.state;

    return (
      <div>
        <p className='change-period-tab'>
          <span className={`${period === 'hour'? 'active': '' }`} onClick={() => this.changePeriod('hour')}>每时</span>
          <span className={`${period === 'day'? 'active': '' }`} onClick={() => this.changePeriod('day')}>每天</span>
          <span className={`${period === 'week'? 'active': '' }`} onClick={() => this.changePeriod('week')}>每周</span>
          <span className={`${period === 'month'? 'active': '' }`} onClick={() => this.changePeriod('month')}>每月</span>
        </p>
        <div id='trans-container'></div>
        <p className='trans-label'>交易速度</p>
      </div>
    )
  }

 
  componentWillReceiveProps(newProps) {
    let {period} = this.state;
    let transData = newProps.transData, categories = [], data = [];
    transData.length > 0 && transData.map( (item, idx) => {
      if(period === 'month') {
        let month = item[1].split('-')[0]+ '-' + item[1].split('-')[1];
        categories.push(month)
      } else if (period === 'day') {
        let day = item[1].split('-')[0] + '-' + item[1].split('-')[1] + '-' + item[1].split('-')[2].split(' ')[0];
        categories.push(day);
      } else if(period === 'week') {
        let temp = ''
        switch(item[0]) {
          case 'Monday':
            temp = '星期一';
            break;
          case 'Tuesday':
            temp = '星期二';
            break;
          case 'Wednesday':
            temp = '星期三';
            break;
          case 'Thursday':
            temp = '星期四';
            break;
          case 'Friday':
            temp = '星期五';
            break;
          case 'Saturday':
            temp = '星期六';
            break;
          case 'Sunday':
            temp = '星期天';
            break;
          
        }
        categories.push(temp)
      } else if(period === 'hour') {
        let hour =item[1].split('-')[2].split(' ')[1] + ':00';
        categories.push(hour)
      }
      data.push( { y: Number(item[6]), trans_num: item[2], total_block: item[3], total_block_size: item[5], speed: item[6]});
    })
    this.setState({categories, data}, this.renderTrend)
  }

  componentDidMount() {
    this.renderTrend();
  }

  renderTrend() {
    let { categories, data, format, tickInterval} = this.state;  
    Highcharts.chart('trans-container', {
    
      title: {
        text: '',
      },
      xAxis: {
        categories: categories,
      },
      yAxis: {
        title: {
          text: ''
        },
        startOnTick: true,
        endOnTick: true,
        showLastLabel: true,
      },
      legend: {
        enabled: false
      },
      tooltip: {
        pointFormat: 'Total Transaction: {point.trans_num}<br/>Total block: {point.total_block}<br/>avg blockSize: {point.total_block_size}<br>Transaction Speed: {point.speed}'
      },
      series: [{
        name: '交易速度',
        data: data,
      }]
    });
    
  }
}

function mapState(state) {
  return {
    transData: state.transListReducer.transList
  }
}

function mapDispatch(dispatch) {
	return {
		getTransData: (period) => dispatch(requestTransList(period)),
  }
}

export default connect(mapState, mapDispatch)(Transaction);