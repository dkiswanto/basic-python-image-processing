import React, { Component } from 'react'
import {Image, Segment} from 'semantic-ui-react'

export default class Display extends Component {
    render(){
        return (
            <Segment basic={false} loading={this.props.isLoading}>
                <Image src={this.props.image} bordered={true} centered={true}/>
            </Segment>

        );
    }
}
