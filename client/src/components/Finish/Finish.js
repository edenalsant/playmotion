import React, { Component } from 'react'
import './Finish.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSpotify } from '@fortawesome/free-brands-svg-icons'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'


 

class Finish extends Component {
    
    render(){
        const spotify=<FontAwesomeIcon icon={faSpotify} size="lg"/>
        const arrowLeft = <FontAwesomeIcon icon={faArrowLeft} size="3x"/>
        return(
            <div className="finish-wrapper">
                <div className="finish-title">
                    <h3> Your playlist was created! </h3>
                </div>
                <div>
                    <h3>Go to your {spotify} acount to check it out!</h3>
                </div>
                <br/> <br/> <br/>  <br/>
                <div className="back">
                    <a className="finish-link" href="http://localhost:3000" title="Go back and create another one!"> {arrowLeft} </a>
                </div>
            </div>
        );
    }
}

export default Finish