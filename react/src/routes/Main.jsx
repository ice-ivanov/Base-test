import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      color: 'grey'
    }
  }

  changeColor = () => {
    this.setState({color: this.state.color === 'red' ? 'grey' : 'red'})
  };

  render() {
    const {users, title} = this.props;
    return(
      <div className="main-wrapper">
        <h1 className={`header-h ${title ? 'fulled' : ''}`}>
          {title ? title : 'No'}
        </h1>
        <span onClick={() => this.changeColor()}>Change Color</span>
        <ul style={{color: this.state.color}}>
          {users.map(user => <li key={user.id}>{user.name}</li>)}
        </ul>
      </div>
    )
  }
}

export default Main;