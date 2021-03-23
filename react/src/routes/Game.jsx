import React from 'react';
import './main.css';

class Main2 extends React.Component {
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
        const {roles, title, loading} = this.props;
        return(
            <div className="main-wrapper">
                <h1 className={`header-h ${title ? 'fulled' : ''}`}>
                    {title ? title : 'No'}
                </h1>
                <span style={{color: this.state.color}} onClick={() => this.changeColor()}>Change Color</span>
                <span> {loading ? 'loading' : ''}
        </span>
                <ul style={{color: this.state.color}}>
                    {roles.map(role => <li key={role.id}>{role.name}</li>)}
                </ul>
            </div>
        )
    }
}

export default Main2;
