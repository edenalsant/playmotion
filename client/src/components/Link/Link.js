import React, { Component } from 'react'
import './Link.css'

class Link extends Component {

    
    render(){
        const baseUrl = 'http://localhost:8080/v1/'

        return(
            <div>
                <a className="link" href={baseUrl+this.props.emotion} > 
                    <span className="gradient">{this.props.emotion}</span>
                </a>
                
            </div>
        );
    }

}

export default Link


