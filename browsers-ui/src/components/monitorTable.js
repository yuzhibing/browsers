import React, { Component } from 'react';
import {Table} from 'react-bootstrap';
import { connect } from 'react-redux';


class MonitorTable extends Component {
  constructor(props) {
    super(props);
    this.renderTable = this.renderTable.bind(this);
    this._onClick = this._onClick.bind(this);
  }

  render() {
    return(
      <div className='monitor-table-container bg-white'>
        <Table responsive>
         {/* <thead> */}
            
          {/* </thead> */}
          <tbody className='monitor-table-body'>
          <tr className='table-header'>     
              <th>交易对</th>
              <th>UT</th>
            </tr>
          { this.renderTable()}
          </tbody>
        </Table>
        </div>
      
    )
  }

  renderTable(){
    let {data} = this.props;
    return data.length > 0 && data.map( (item, idx) => {
      return (
        <tr key={idx}>
            <td className='table-left-td'>
              <p>{item[3]==1? <span className='moni-label'>入</span> : <span className='red moni-label'>出</span>} <span>{item[2]}</span></p>
              <p style={{cursor:'pointer'}} onClick={() => this._onClick(item[0])}>{item[0]}</p>
            </td>
            <td className='num'>{item[1]}</td>
        </tr>
      )
    })
  }

  _onClick(hash) {
    location.href = `http://explorer.ulord.one/address/${hash}`;
  }
}



function mapState(state) {
  return {
    data: state.homeOrder.orders
  }
}


export default connect(mapState, null)(MonitorTable);
