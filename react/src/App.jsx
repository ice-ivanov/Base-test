import './index.css';
import React from 'react';
import {Route, Switch} from "react-router";
import {Link} from "react-router-dom";
import axios from "axios";
// import Game from "./components/Game";
import Main from "./routes/Main";
// import Game from "./routes/Game"


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      roles: ['id'],
      users: [],
      loading: false,
      error: null
    }
  }

  componentDidMount() {
    this.setState({loading: true});
    axios.get('http://localhost:8000/auth/roles/')
      .then(res => {
        if (res.data) {
          this.setState({
            roles: res.data || [],
            loading: false
          })
        }
      })
      .catch(e => {
        this.setState({loading: false, error: e.message ? e.message : 'Some Error'})
      })
  }

  render() {
    const {loading, error} = this.state;
    return (
      <div>
        <header>
          <Link to="/"/>
          <Link to="/game"/>
        </header>
        <Switch>
          <Route exact path="/"
                 render={() => <Main roles={this.state.roles} title={"MAIN"} loading={loading}/>}/>
          <Route path="/game"
                 render={() => <Game/>}
          />
          <Route path="*" render={() => <div>Error 404</div>}/>
        </Switch>
      </div>
    )
  }
}


class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      roles: [],
      users: [],
      loading: false,
      error: null
    }
  }

  componentDidMount() {
    this.setState({loading: true});
    axios.get('http://localhost:8000/auth/roles/')
      .then(res => {
        if (res.data) {
          this.setState({
            roles: res.data || [],
            loading: false
          })
        }
      })
      .catch(e => {
        this.setState({loading: false, error: e.message ? e.message : 'Some Error'})
      })
  }

  render() {
    const {loading, error} = this.state;
    return (
      <div>
        <header>
          <Link to="/"/>
          <Link to="/game"/>
        </header>
        <Switch>
          <Route exact path="/"
                 render={() => <Game roles={this.state.roles} title={"GAME"} loading={loading}/>}/>
          <Route path="/game"
                 render={() => <Game/>}
          />
          <Route path="*" render={() => <div>Error 404</div>}/>
        </Switch>
      </div>
    )
  }
}

export default App;