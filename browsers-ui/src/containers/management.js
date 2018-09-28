import React, { Component } from 'react';
import { connect } from 'react-redux';
import {Navbar, Nav, NavItem, Table} from 'react-bootstrap'


class Management extends Component {
	constructor(props) {
		super(props)
		this.state = {}
	}

  render() {
    return (
	    <div className="home-container">
		    <Navbar collapseOnSelect>
			    <Navbar.Header>
				    <Navbar.Brand>
					    <a href="#/"><img src={require('assets/icons/logo.png')} /></a>
				    </Navbar.Brand>
				    <Navbar.Toggle />
			    </Navbar.Header>
			    <Navbar.Collapse>
				    <Nav>
					    <NavItem eventKey={1} href="#">
						    用户数据管理
					    </NavItem>
					    {/* <NavItem eventKey={2} href="#">
						    Ulord
					    </NavItem>
					    <NavItem eventKey={2} href="#">
						    趋势
					    </NavItem> */}

				    </Nav>
			    </Navbar.Collapse>
		    </Navbar>

				<div className='main-container'>
					<div className='txt-title'>用户数据管理</div>
					<Table responsive bordered>
						<thead>
							<tr>
								
								<th>交易对</th>
								<th>UT</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								
								<td>卖出</td>
								<td>5000</td>
							</tr>
							<tr>
							
								<td>买入</td>
								<td>2000</td>
							</tr>
						</tbody>
					</Table>

				</div>




	    </div>

    );
  }
}

function mapState(state) {
  return {}
}

export default connect(mapState, null)(Management);
