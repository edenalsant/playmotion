import React, { Component } from 'react'
import './Title.css'

class Title extends Component {

    render(){
        return(
            <div>
                <div className="logo">
                    <span className="title">{this.props.title}</span>
                    <span className="sub-title">{this.props.subtitle}</span>
                </div>
                <span>{this.props.subsubtitle1}</span>
            </div>
        );
    }
}

export default Title