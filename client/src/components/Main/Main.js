import React, { Component } from 'react'
import Link from '../Link/Link'
import Footer from '../Footer/Footer'


import './Main.css'
import Header from '../Header/Header'

class Main extends Component {



    render(){
        return(
            <div className="main-wrapper">
                <Header />
                <div className="links-box">
                    <div className="topLinks">
                        <Link emotion="happy" />
                        <Link emotion="sad" />
                        <Link emotion="peaceful" />
                    </div>
                    <div className="middleLinks">
                        <Link emotion="angry" />
                        <Link emotion="bored" />
                        <Link emotion="sleepy" />
                        <Link emotion="calm" />
                    </div>    
                    <div className="bottomLinks">
                        <Link emotion="relaxed" />
                        <Link emotion="nervous" />
                        <Link emotion="excited" />
                    </div>
                </div>
                <Footer />
            </div>
        )
    }
}

export default Main