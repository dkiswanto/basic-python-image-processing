import React, { Component } from 'react'
import { Menu } from 'semantic-ui-react'
import { Link } from 'react-router-dom'


export default class Navbar extends Component {
    state = { activeItem: '' };

    handleItemClick = (e, { name }) => this.setState({ activeItem: name });

    render() {
        const { activeItem } = this.state;

        return (
            <Menu className={'ui large top fixed menu'}>
                <div className={'ui container'}>
                    <Menu.Item header>Final Task PCD 2017</Menu.Item>

                    <Link to="/">
                        <Menu.Item name='main' active={activeItem === 'main'} onClick={this.handleItemClick} />
                    </Link>

                    <Link to="/about">
                        <Menu.Item name='about' active={activeItem === 'about'} onClick={this.handleItemClick} />
                    </Link>

                </div>
            </Menu>
        )
    }
}
