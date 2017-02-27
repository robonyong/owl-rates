import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { browserHistory } from 'react-router';
import { MediaObject, MediaObjectSection, Thumbnail } from 'react-foundation';
import Rating from 'react-rating';

import OwlReview from '../components/owlReview';
import Modal from '../components/modal';

import { fetchOwlBySlug } from '../actions/owls';

export class OwlView extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showDescription: false,
      showZoom: false,
    };
  }

  componentWillMount() {
    const { slug, dispatch } = this.props;
    if (!slug) {
      browserHistory.replace('/owls');
    }
    dispatch(fetchOwlBySlug(slug));
  }

  launchZoom() {
    this.setState({showZoom: true});
  }

  launchAudubonDescription() {
    this.setState({showDescription: true});
  }

  closeModals() {
    this.setState({showDescription: false, showZoom: false});
  }

  render() {
    const { owl } = this.props;
    const reviews = owl.ratings.map((rating, idx) => {
      return <OwlReview
        key={`${owl.name}-${idx}`}
        rating={rating.rating}
        review={rating.review}
        reviewer={rating.reviewer} />;
    });
    return (
      <div>
        <p className='m-b-20'><small><a href="/owls">&larr; Back to owls</a></small></p>
        <MediaObject>
          <MediaObjectSection className='text-center'>
            <Thumbnail className='m-b-0' src={owl.imageThumbnail} />
            <br />
            <a tabIndex={-1} onClick={() => this.launchZoom()}>Click to zoom</a>
          </MediaObjectSection>
          <MediaObjectSection isMain>
            <h3>{owl.name}</h3>
            <Rating initialRate={owl.avgRating} readonly={true} fractions={10} />
            { !owl.ratings.length &&
              <div><small>{owl.name} does not have any ratings yet.</small></div>
            }
            <a tabIndex={-1} onClick={() => this.launchAudubonDescription()}>John Audubon's Words</a>
            {reviews}
          </MediaObjectSection>
        </MediaObject>
        <Modal
          show={this.state.showZoom}
          title={`${owl.name}`}
          onClose={() => this.closeModals()}
          className='text-center'
        >
          <img src={owl.image} />
        </Modal>
        <Modal
          show={this.state.showDescription}
          title={`John Audubon's ${owl.name}`}
          onClose={() => this.closeModals()}
        >
          <p><small><a href={`http://www.audubon.org${owl.nasLink}`}>Read on Audubon.org</a></small></p>
          { owl.descriptions.map(d => <p key={`${owl.slug}-description-${d.idx}`}>{d.description}</p>) }
        </Modal>
      </div>
    );
  }
}

OwlView.propTypes = {
  owl: PropTypes.object,
  dispatch: PropTypes.func.isRequired,
};

function mapStateToProps(state, ownProps) {
  const { owls } = state;
  return {
    owl: owls.selectedOwl,
    slug: ownProps.params.slug,
  };
}

export default connect(mapStateToProps)(OwlView);
