import React, { Component } from 'react'

export default class About extends Component {
    render(){
        return (
            <div>
                <h1>About Page</h1>
                <h2>Identity</h2>
                <p>Name : Dede Kiswanto</p>
                <p>NIM  : 1301140171</p>

                <h2>Back-end tech (Server-side)</h2>
                <ul class="ui list">
                    <li>Python 3 - <a href="https://www.python.org">https://www.python.org</a></li>
                    <li>Numpy (Matrix Data Structure & Processing) - <a href="http://www.numpy.org/">http://www.numpy.org/</a></li>
                    <li>Pillow - <a href="https://python-pillow.org/">https://python-pillow.org/</a></li>
                    <li>Django - <a href="https://www.djangoproject.com">https://www.djangoproject.com</a></li>
                </ul>

                <h2>Front-end tech (Client-side)</h2>
                <ul class="ui list">
                    <li>ReactJS - <a href="https://facebook.github.io/react/">https://facebook.github.io/react/</a></li>
                    <li>ReactRouter <a href="https://github.com/ReactTraining/react-router">https://github.com/ReactTraining/react-router</a></li>
                    <li>SemanticUI (React Version) - <a href="https://react.semantic-ui.com">https://react.semantic-ui.com</a></li>
                    <li>Superagent (HTTP REST Client) - <a href="https://github.com/visionmedia/superagent">https://github.com/visionmedia/superagent</a></li>
                </ul>

            </div>
        );
    }
}