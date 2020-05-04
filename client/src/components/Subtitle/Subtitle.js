import React, { Component } from 'react'
import './Subtitle.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSpotify } from '@fortawesome/free-brands-svg-icons'
 

class Subtitle extends Component {
    
    render(){
        const spotify=<FontAwesomeIcon icon={faSpotify} size="lg"/>
        return(
            <div>
                <h3>{this.props.beforeImage} {spotify} {this.props.afterImage}</h3>
                
            </div>
        );
    }
}

export default Subtitle