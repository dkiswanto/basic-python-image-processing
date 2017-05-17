import React, { Component } from 'react';
import {Grid, Message} from "semantic-ui-react";
import Request from 'superagent'

// import component
import Display from '../components/display';
import Toolbox from '../components/toolbox';

const API_URL = 'http://localhost:8000';
// const API_URL = window.location.origin;

export default class Main extends Component {
    constructor(props){
        super(props);
        this.state = {
            image: null, fileImage: null, isLoading: false,
            defaultImage: null, greyscale: false
        };
        // TODO: default placeholder
    }

    handleUpload = (e) => {
        e.preventDefault();

        // get image File object
        const image = e.target.files[0];

        if(image.type.match(/.(jpg|jpeg|png|gif)$/i)){
            const reader  = new FileReader();
            reader.addEventListener("load", () => {

                // reader.result == base64 string
                this.setState({image: reader.result, fileImage: image, defaultImage: image});
            }, false);
            reader.readAsDataURL(image);
        } else {
            alert("not image files, please upload an image files")
        }

    };

    handleToolbox = (id) => {

        if(this.state.image === null){
            alert('please load the image first');
            return false;
        }

        // show loading state in display image
        this.setState({isLoading: true});

        // set opration
        const operation = id;
        if(operation === 'greyscale'){
            this.setState({greyscale: true})
        }

        // make a request image
        Request.post(API_URL + '/api/transform/')
            .field('image', this.state.fileImage)
            .field('operation', operation)
            .field('greyscale', this.state.greyscale)
            .responseType('blob')
            .end((err,res)=>{
                if (err || !res.ok) {
                    this.setState({isLoading: false});
                    alert("can't connected to server, please check your internet connection");
                } else {
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        this.setState({image : e.target.result,
                            fileImage : res.body, isLoading: false});
                    };
                    reader.readAsDataURL(res.body);
                }
            })
    };

    handleReset = () => {
        const reader  = new FileReader();
        reader.addEventListener("load", () => {
            this.setState({image: reader.result, fileImage: this.state.defaultImage, greyscale: false});
        }, false);
        reader.readAsDataURL(this.state.defaultImage);
    };

    render() {
        return (
        <div>
            <Message warning>
                Please use a small resolution / size image due to server limitation, (1KB - 200KB image)
                or resize the image by using zoom out toolbox
            </Message>
            <Grid>
                <Grid.Row columns={2} className={'ui container'}>
                    <Grid.Column>
                        <Display image={this.state.image} isLoading={this.state.isLoading}/>
                    </Grid.Column>
                    <Grid.Column>
                        <Toolbox handleUpload={this.handleUpload}
                                 onToolboxClick={this.handleToolbox} handleReset={this.handleReset}/>
                    </Grid.Column>
                </Grid.Row>
            </Grid>
        </div>

        );
    }

}