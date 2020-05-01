import React from 'react'
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

//components
import { Navbar } from './components/Navbar'
import { About } from './components/About'
import { Tasks } from './components/Tasks'

export const App = () => {
  return (
    <Router>
      <Navbar/>
      <div className="container p-4">
        <Switch>
          <Route path="/about" component={About}/>
          <Route path="/" component={Tasks}/>
        </Switch>
      </div>
    </Router>
  )
}
