import React, { Component } from 'react';
import { Nav, NavItem, } from 'react-bootstrap';


export default class NavInstance extends Component {
  constructor(props){
    super(props);
    this.state = {
      activeKey: 1
    }
  }

  render() {

    let {activeKey} = this.state;

    return(
      <Nav bsStyle="pills" activeKey={activeKey} onSelect={this.handleSelect}>
        <NavItem eventKey={1}>
          大单趋势
        </NavItem>
        <NavItem eventKey={2} title="Item">
          NavItem 2 content
        </NavItem>
        <NavItem eventKey={3} >
          NavItem 3 content
        </NavItem>
      </Nav>
    )
  }

  handleSelect = (activeKey) => {
    this.setState({activeKey})
    console.log('activeKey:', activeKey)
  }
}