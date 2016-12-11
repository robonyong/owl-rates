import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

import { fetchOwls } from '../actions/owls';

export class OwlsList extends Component {
  constructor(props) {
    super(props);
    // this.handleChange = this.handleChange.bind(this)
    // this.handleRefreshClick = this.handleRefreshClick.bind(this)
  }

  componentWillMount() {
    const { dispatch } = this.props;
    dispatch(fetchOwls());
  }

  render() {
    const { owls } = this.props;
    return (
      <div>
        owls?
      </div>
    );
  }
}

OwlsList.propTypes = {
  owls: PropTypes.object.isRequired,
  dispatch: PropTypes.func.isRequired,
};

function mapStateToProps(state) {
  const { owls } = state;
  return {
    owls,
  };
}

export default connect(mapStateToProps)(OwlsList);
