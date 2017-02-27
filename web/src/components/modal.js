import React, { PropTypes } from 'react';
import ReactModal from 'react-modal';

const Modal = (props) => {
  const inlineProps = {
    isOpen: props.show,
    contentLabel: props.title,
    onRequestClose: props.onClose,
    className: 'modal',
    closeTimeoutMS: 200
  };
  if (props.className) inlineProps.className = `${inlineProps.className} ${props.className}`;
  const footer = props.footer || <div className='modal-footer'>
      <a className='button float-right' onClick={props.onClose}>Close</a>
    </div>;
  return (
    <ReactModal {...inlineProps}>
      <span className='close-button control-button float-right' onClick={props.onClose}>&times;</span>
      <h2>{props.title}</h2>
      <hr />
      {props.children}
      <hr />
      {footer}
    </ReactModal>
  );
};

Modal.propTypes = {
  show: PropTypes.bool.isRequired,
  title: PropTypes.string.isRequired,
  onClose: PropTypes.func.isRequired,
  className: PropTypes.string,
  children: PropTypes.node,
};

export default Modal;
