/**
 * Created by admin on 2017/3/3.
 */
import React, {Component} from 'react'
import {connect} from 'react-redux';
import { Navbar, Nav, NavItem } from 'react-bootstrap';
import MyTabContainer from 'components/myTabContainer';

import {requestHomeOrder} from 'actions/homeActions';
import {requestAddressList} from 'actions/addressAction';
import {requestPriceTrend} from 'actions/pricetrend';
import {requestTransList} from 'actions/transAction';


class Home extends Component {
	constructor(props) {
		super(props);
		this.state = {
		};
	}

	componentDidMount() {
		let {getOrders, getAddressList, getPriceTrend, getTransData} = this.props;
		getOrders();
		getAddressList();
		getPriceTrend();
		getTransData();
	}

	render() {
		return (
	    <div className="home-container">
				<Navbar>
			    <Navbar.Header>
				    <Navbar.Brand>
					    <a href="#"><img src={require('assets/icons/logo.png')} /></a>
				    </Navbar.Brand>
				    <Navbar.Toggle />
			    </Navbar.Header>
			    <Navbar.Collapse>
				    <Nav>
					    <NavItem eventKey={1} href="http://explorer.ulord.one/">
						    Blocks
					    </NavItem>
					    <NavItem eventKey={2} href="http://ulord.one/">
						    Ulord
					    </NavItem>
					    <NavItem eventKey={3} href="#">
						    Monitor
					    </NavItem>

				    </Nav>
			    </Navbar.Collapse>
		    </Navbar>
		    
				
				<div className='main-container'>
					<MyTabContainer />
				</div>

	    </div>

    );
	}

	shouldComponentUpdate(nextProps, nextState) {
		return this.props.router.location.action === 'PUSH';   //防止页面二次渲染
	}
}


function mapStateToProps(state) {
	return {orders: state.homeOrder.orders}
}

function mapDispatchToProps(dispatch) {
	return {
		getOrders: () => dispatch(requestHomeOrder()),
		getAddressList: () => dispatch(requestAddressList()),
		getPriceTrend: () => dispatch(requestPriceTrend('day')),
		getTransData: () => dispatch(requestTransList()),

	}
}

export default connect(mapStateToProps, mapDispatchToProps)(Home)