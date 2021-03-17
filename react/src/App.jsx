import './index.css';
import React from 'react';
import {Route, Router, Switch} from "react-router";
import {Link} from "react-router-dom";
import axios from "axios";
import Game from "./components/Game";
import Main from "./routes/Main";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [],
      loading: false,
      error: null
    }
  }
  componentDidMount() {
    this.setState({loading: true});
    axios.get('http://gleb-loh/asd')
      .then(res => {
        if (res.data) {
          this.setState({
            users: res.data || [],
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
                 render={() => <Main users={this.state.users} title={"MAIN"}/>}/>
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