import React, { Component } from 'react';

import Navbar from './components/navbar';
import Main from './components/main'
import About from './components/about'

import {
    BrowserRouter as Router,
    Route,
} from 'react-router-dom'

// import style & asset
import 'semantic-ui-css/semantic.min.css';
import './App.css';


class App extends Component {
    render(){
        return (
            <Router>
                <div className={'ui container'}>
                    <Navbar/>
                    <div className={'main'}>
                        <Route exact path="/" component={Main}/>
                        <Route path="/about" component={About}/>
                    </div>
                </div>
            </Router>
        )
    }
}

export default App;
