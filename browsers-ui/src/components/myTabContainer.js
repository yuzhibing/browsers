import React, { Component } from 'react';
import {Tab, Nav, NavItem, Row} from 'react-bootstrap'
import MyMonitor from './monitor';
import MonitorTable from './monitorTable';
import AddressTable from './addressTable';
import PriceTrend from './priceTrend';
import AreaChart from './area';
import Transaction from './transactin';

export default class MyTabContainer extends Component {
  constructor(props) {
    super(props);
  }

  render() {

    return (
        <Tab.Container id="left-tabs-example" defaultActiveKey="first">
          <Row>
            <Nav bsStyle="pills">
              <NavItem eventKey="first">大单监控</NavItem>
              <NavItem eventKey="second">用户地址监控</NavItem>
              <NavItem eventKey="fourth">交易速度</NavItem>
              <NavItem eventKey="third">价格走势</NavItem>
            </Nav>
          <div className='white-space'></div>
          
          <Tab.Content animation>
            <Tab.Pane eventKey="first">
            <div className='pd-5'><MyMonitor /></div>
            <div className='white-space'></div>

            <div className='pd-5'><MonitorTable /></div>
            </Tab.Pane>
            <Tab.Pane eventKey="second">
              <AddressTable />
              <div className='white-space'></div>

              <AreaChart />
            </Tab.Pane>
            <Tab.Pane eventKey="third"><PriceTrend /></Tab.Pane>
            <Tab.Pane eventKey="fourth"><Transaction /></Tab.Pane>
          </Tab.Content>
        </Row>
      </Tab.Container>  
    )
  }
}
