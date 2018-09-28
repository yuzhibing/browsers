import React, { Component } from 'react';
import {Table} from 'react-bootstrap';
import { connect } from 'react-redux';


class AddressTable extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    let {addressList} = this.props, lastAddressData = addressList && addressList[addressList.length -1] || [];
    return(
      <div className='monitor-table-container pd-5'>
        <Table responsive>
         {/* <thead> */}
           {/* <tr>
           <th colSpan="2">地址监控</th>
           </tr> */}
            
          {/* </thead> */}
          <tbody className='monitor-table-body'>
            <tr>     
                <th>项目</th>
                <th>数量</th>
              </tr>
            <tr>
              <td>
                <p>大账户地址</p>
                <p className='small-size'>大于10000UT的账户数量</p>
              </td>
              <td>{lastAddressData[1]}</td>
            </tr>

            <tr>
              <td>
                <p>账户数量统计</p>
                <p className='small-size'>有余额账户数量</p>
              </td>
              <td>{lastAddressData[2]}</td>
            </tr>

            <tr>
              <td>
                <p>活跃地址</p>
                <p className='small-size'>近7天有交易的账户数量</p>
              </td>
              <td>{lastAddressData[3]}</td>
            </tr>
          
          </tbody>
        </Table>
        </div>
      
    )
  }


}

function mapState(state) {
  return {
    addressList: state.addressList.addressList
  }
}


export default connect(mapState, null)(AddressTable);
