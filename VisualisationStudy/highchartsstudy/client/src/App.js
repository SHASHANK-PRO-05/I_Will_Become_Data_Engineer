import React, {Component} from 'react';
import TopNavBar from './Layout/TopNavBar.js';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component {
    render() {
        return (<div className="App">
            <TopNavBar/>
        </div>);
    }
}

export default App;