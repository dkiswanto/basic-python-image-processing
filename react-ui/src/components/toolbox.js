import React, { Component } from 'react'
import {Button, Grid} from "semantic-ui-react";

export default class Toolbox extends Component {

    handleUploadButton = (e) => {
        this.uploadImage.click();
    };

    render(){
        return (
            <Grid>
                {/* Open and Select Files*/}
                <Grid.Row columns={3}>
                    <Grid.Column>
                        {/*<form onSubmit={this.props.handleUpload} ref={e => this.formUpload = e}>*/}
                            <input ref={e => this.uploadImage = e} id="upload-image"
                                   type="file" name="image" accept="image/*" onChange={this.props.handleUpload}/>
                            <Button type="button" inverted color="blue" onClick={this.handleUploadButton}>Open an Image</Button>
                            {/*<Button inverted color="blue">Upload an Image</Button>*/}
                        {/*</form>*/}
                    </Grid.Column>

                    <Grid.Column>
                        <Button inverted color="red" onClick={this.props.handleReset}>Reset Image</Button>
                    </Grid.Column>

                    <Grid.Column>
                        <Button onClick={() => this.props.onToolboxClick('greyscale')}>To Greyscale</Button>
                    </Grid.Column>
                </Grid.Row>

                {/* Rotate */}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('rotate-90')}>
                                Rotate 90
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('rotate-180')}>
                                Rotate 180
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('rotate-270')}>
                                Rotate 270
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/* Move */}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('move-up')}>
                                Move Up
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('move-down')}>
                                Move Down
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('move-left')}>
                                Move Left
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('move-right')}>
                                Move Right
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/* Flip & Zoom*/}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('flip-h')}>
                                Flip Horizontal
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('flip-v')}>
                                Flip Vertical
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('zoom-in')}>
                                Zoom in 2X
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('zoom-out')}>
                                Zoom out 2X
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/* Brightness */}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('bright+10')}>
                                Brightness +10
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('bright-10')}>
                                Brightness -10
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('brightX2')}>
                                Brightness X 2
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('bright/2')}>
                                Brightness / 2
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/* Sharpening, Edge Detection, Warping, Histogram */}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('sharpening')}>
                                Sharpening
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('edge-detect')}>
                                Edge Detection
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('warping')}>
                                Warping
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('histogram')}>
                                Histogram
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/* Conv Kernel One, Conv GaussianBlur */}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('conv-blur')}>
                                Conv-Blur
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('conv-gaussian')}>
                                Conv-Gaussian Blur
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('conv-one')}>
                                Conv-KernelOne
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/* Smoothing */}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('smooth-modus')}>
                                Smooth Modus
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('smooth-mean')}>
                                Smooth Mean
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('smooth-median')}>
                                Smooth Median
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/* Segmentation Treshold and Region Growth*/}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('segmentation')}>
                                Segment-Treshold
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('segmentation-binary')}>
                                Segment-BinaryTreshold
                            </Button>
                            <Button disabled size='small' onClick={() => this.props.onToolboxClick('')}>
                                Segment-RegionGrowth
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

                {/*Erotion, Dilation*/}
                <Grid.Row>
                    <Grid.Column>
                        <div>
                            <Button size='small' onClick={() => this.props.onToolboxClick('erosion')}>
                                Erosion
                            </Button>
                            <Button size='small' onClick={() => this.props.onToolboxClick('dilation')}>
                                Dilation
                            </Button>
                        </div>
                    </Grid.Column>
                </Grid.Row>

            </Grid>


        );
    }
}
