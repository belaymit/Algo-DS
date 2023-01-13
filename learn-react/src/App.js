import React, { PureComponent } from 'react'

export class App extends PureComponent {
  constructor(props) {
    console.log("Constructor");
    super(props);

  this.state = {
    counter:0,
  }

  this.increment = () => this.setState({counter: this.state.counter + 1});
  this.decrement = () => this.setState({counter: this.state.counter - 1});
}

componentDidMount() {
  console.log("ComponentDidMount");
}

componentDidUpdate () {
  console.log("ComponentDidUpdate");
}

  render() {
    console.log("Render");
    return (
      <div className="app-container">
        <div className="app-item">
          <button onClick={this.increment}>+</button>
          <button onClick={this.decrement}>-</button>
        </div>
        <div className="counter">
          Counter: {this.state.counter}
        </div>
      </div>
    )
  }
}

export default App