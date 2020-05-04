import React, { Component } from "react";
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Main from './components/Main/Main';
import Finish from './components/Finish/Finish'


class App extends Component {
  
  render() {
    return(
      <div>
        <BrowserRouter>
          <div>
            <Switch>
              <Route exact path='/' component={Main}/>
              <Route exact path='/finish' component={Finish} />
            </Switch>
          </div>
        </BrowserRouter>
      </div>
    );
  }
}
export default App;
