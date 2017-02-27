import React, { Component } from 'react';
import { Link } from 'react-router';
import { Button, Callout, Colors } from 'react-foundation';

import Modal from './modal';

class AuthModal extends Component {
  constructor(props) {
    super(props);

    this.state = {
      error: props.auth.error
    }
  }

  componentWillReceiveProps(nextProps) {
    this.setState({error: nextProps.auth.error});
  }

  swapView(view) {
    this.form.reset();
    this.props.swapView(view);
  }

  submit(e) {
    e.preventDefault();
    const data = {
      email: this.email.value,
      password: this.password.value,
    };
    if (this.props.viewAction === 'register') {
      const matchingPasswords = this.password.value === this.passwordConf.value;
      if (!matchingPasswords) {
        this.setState({ error: new Error('Passwords do not match')});
        return;
      }
    }
    if (this.name) {
      data.name = this.name.value;
    }
    const fn = this.props[this.props.viewAction];
    fn(data);
  }

  render() {
    const props = this.props;
    const title = props.viewAction.slice(0, 1).toUpperCase() + props.viewAction.slice(1);
    const swapViewLink = title === 'Login' ?
      <small>Don't have an account? <a tabIndex={-1} onClick={() => this.swapView('register')}>Register here</a>.</small> :
      <small>Already have an account? <a tabIndex={-1} onClick={() => this.swapView('login')}>Login here</a>.</small>
    return (
      <Modal
        show={props.show}
        onClose={props.closeModal}
        title={title}
        footer={<div></div>}>
        { this.state.error &&
          <Callout color={Colors.ALERT}>
            <h5>{this.state.error.message}</h5>
          </Callout>
        }
        <form ref={(form) => this.form = form} onSubmit={e => this.submit(e)}>
          <div className='row'>
            { props.viewAction === 'register' && 
              <div className='medium-6 columns'>
                <label>Name
                  <input name='name' type='text' ref={(input) => this.name = input} required />
                </label>
              </div>
            }
            <div className='medium-6 columns'>
              <label>Email
                <input name='email' type='email' ref={(input) => this.email = input} />
              </label>
            </div>
            <div className='medium-6 columns'>
              <label>Password
                <input name='password' type='password' ref={(input) => this.password = input} />
              </label>
            </div>
            { props.viewAction === 'register' && 
              <div className='medium-6 columns'>
                <label>Confirm Password
                  <input name='password-conf' type='password' ref={(input) => this.passwordConf = input} />
                </label>
              </div>
            }
          </div>
          <div className='row'>
            <div className='medium-12 columns text-right'>
              <Button type='submit'>{title}</Button>
              <div>{swapViewLink}</div>
            </div>
          </div>
        </form>
      </Modal>
    );
  }
};

export default AuthModal;
