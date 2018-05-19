import React, {Component} from 'react';
import {
    Navbar,
    NavbarBrand,
    Nav, NavItem,
    NavLink, TabContent,
    TabPane, Row, Col,
    Alert
} from 'reactstrap'
import classnames from 'classnames';
import LineBasic from '../HighCharts/LineCharts/Line-Basic'


export default class TopNavBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeTab: '1'
        };
        this.toggle.bind(this);
    }

    toggle(tab) {
        if (this.state.activeTab !== tab) {
            this.setState({
                activeTab: tab
            })
        }
    }

    render() {
        return (<div>
                <Navbar color="light" expand="md">
                    <NavbarBrand>Gun Violence Report</NavbarBrand>
                </Navbar>
                <Nav tabs className="topTabs">
                    <NavItem>
                        <NavLink className={classnames({
                            active: this.state.activeTab === '1'
                        })}
                                 onClick={() => {
                                     this.toggle('1')
                                 }}>Year Wise Rise</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink className={classnames({
                            active: this.state.activeTab === '2'
                        })}
                                 onClick={() => {
                                     this.toggle('2')
                                 }}>Choropleth Map</NavLink>
                    </NavItem>
                </Nav>
                <TabContent activeTab={this.state.activeTab}>
                    <TabPane tabId="1" className="topTabs">
                        <Row>
                            <Col sm="12">
                                <LineBasic/>
                                <Alert color="Success">
                                    <h4 className="alert-heading">Inference</h4>
                                    <p>We cannot infer much from years 2013 and 2018 but from 2014-2017, the count
                                        definitely shows rise in the gun violence crime.</p>
                                </Alert>
                            </Col>
                        </Row>
                    </TabPane>
                </TabContent>
            </div>
        );
    }
}