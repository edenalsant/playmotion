import React, { Component } from 'react'
import './Footer.css'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeart } from '@fortawesome/free-solid-svg-icons'
import { faCode } from '@fortawesome/free-solid-svg-icons'
 

class Footter extends Component {
    
    render(){
        const heart=<FontAwesomeIcon icon={faHeart} size="xs"/>
        const code=<FontAwesomeIcon icon={faCode} size="xs"/>
        return(
            <div className="footter-wrapper">
                <span>Made with {heart} and {code} by Éden Ernandes</span>
            </div>
        );
    }
}

export default Footter