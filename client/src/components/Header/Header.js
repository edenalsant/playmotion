import React, { Component } from 'react'
import './Header.css'
import Title from '../Title/Title'
import Subtitle from '../Subtitle/Subtitle'

class Header extends Component {
    
    render(){
        return(
            <div className="header-wrapper">
                <Title 
                        title="Playmotion"
                        subtitle="How are you feeling right now?"   
                />
                <Subtitle 
                    beforeImage="Select an emotion and an awesome "
                    afterImage="playlist is created for you based on your music taste"
                />
            </div>
        );
    }
}

export default Header