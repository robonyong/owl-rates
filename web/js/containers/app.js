import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

export class App extends Component {
	constructor(props) {
    super(props)
    // this.handleChange = this.handleChange.bind(this)
    // this.handleRefreshClick = this.handleRefreshClick.bind(this)
  }

  render() {
    const { owls, isFetching } = this.props
    return (
      <div>
      </div>
    )
  }
}

App.propTypes = {
  owls: PropTypes.object.isRequired,
  visibilityFilter: PropTypes.string.isRequired,
  auth: PropTypes.object.isRequired,
  dispatch: PropTypes.func.isRequired
}

function mapStateToProps(state) {
  const { owls, isFetching } = state

  return {
    owls,
    isFetching
  }
}

export default connect(mapStateToProps)(App)