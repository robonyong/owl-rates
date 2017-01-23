import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router';
import { Row, Column, Thumbnail } from 'react-foundation';

import { fetchOwls } from '../actions/owls';

export class OwlsList extends Component {
  constructor(props) {
    super(props);
  }

  componentWillMount() {
    const { dispatch } = this.props;
    dispatch(fetchOwls());
  }

  render() {
    const { owls } = this.props;
    const columns = owls.owlList.map((owl) => {
      return (
        <Column key={`owl-${owl.id}`}>
          <Link className='owl-thumbnail' to={`/owls/${owl.slug}`}>
            <Thumbnail src={owl.imageWeb} />
            <div className='owl-thumbnail-name m-b-20'>{owl.name}</div>
          </Link>
        </Column>
      );
    });

    const owlsView = (owls.isFetching) ? <div className='loading' /> :
      <Row upOnSmall={1} upOnMedium={2} upOnLarge={4}>
        {columns}
      </Row>;

    return owlsView;
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
