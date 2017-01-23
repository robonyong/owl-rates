import React, { Component, PropTypes } from 'react';
import { Row } from 'react-foundation';
import Rating from 'react-rating';

const OwlReview = (props) => {
  return (
    <div>
      <Rating initialRate={props.rating} readonly={true} />
      <Row>
        {props.review}
      </Row>
      <Row>
        {props.reviewer.name}
      </Row>
    </div>
  );
}

OwlReview.propTypes = {
  rating: PropTypes.number.required,
  review: PropTypes.string.required,
  reviewer: PropTypes.object.required,
};

export default OwlReview;
