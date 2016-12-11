import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

export class OwlView extends Component {
  constructor(props) {
    super(props);
    // this.handleChange = this.handleChange.bind(this)
    // this.handleRefreshClick = this.handleRefreshClick.bind(this)
  }

  render() {
    const { owls } = this.props;
    return (
      <div>
        just one owl
      </div>
    );
  }
}

OwlView.propTypes = {
  owls: PropTypes.object.isRequired,
};

function mapStateToProps(state) {
  const { owls } = state;
  return {
    owls,
  };
}

export default connect(mapStateToProps)(OwlView);
