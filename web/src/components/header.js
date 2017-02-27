import React, { Component, PropTypes } from 'react';
import { TopBar, TopBarTitle, TopBarRight, Menu, MenuItem, Icon } from 'react-foundation';
import { Link } from 'react-router';

import AuthModal from './authModal';
import '../../scss/nav.scss';

import { authenticate, register } from '../actions/auth';

export default class Header extends Component {
  constructor(props) {
    super(props);
    this.state = {
      openMobile: false,
      showAuth: false,
      authView: 'login',
    };
  }

  toggleMobileMenu() {
    this.setState({ openMobile: !this.state.openMobile });
  }

  toggleLogin() {
    this.setState({ showAuth: !this.state.showAuth });
  }

  swapAuthView(view) {
    this.setState({ authView: view });
  }

  attemptLogin(data) {
    const { dispatch } = this.props;
    dispatch(authenticate(data));
  }

  register(data) {
    const { dispatch } = this.props;
    dispatch(register(data));
  }

  render() {
    const { auth } = this.props;
    const accountLink = (auth.user) ?
      (<Link to='/account'>
        <Icon name='fi-torso-female' /> <span>{auth.user.name}</span>
      </Link>) :
      <a tabIndex='0' onClick={() => this.toggleLogin()}>Login</a>;
    const mobileClass = (this.state.openMobile) ? 'open' : '';

    return (
      <TopBar>
        <area tabIndex={-1} onClick={() => this.toggleMobileMenu()} className={`overlay ${mobileClass}`} />
        <TopBarTitle>
          <Menu>
            <MenuItem onClick={() => this.toggleMobileMenu()} className='show-for-small-only'>
              <span className='menu-icon black' />
            </MenuItem>
            <MenuItem className='menu-title'><Link to='/'>GoodHoots</Link></MenuItem>
          </Menu>
        </TopBarTitle>
        <TopBarRight className={`navbar-collapse ${mobileClass}`}>
          <Menu>
            <MenuItem><Link to='/owls'>Owls</Link></MenuItem>
            <MenuItem><Link to='/reviewers'>Reviewers</Link></MenuItem>
            <MenuItem><Link to='/about'>About</Link></MenuItem>
            <MenuItem>{accountLink}</MenuItem>
          </Menu>
        </TopBarRight>
        { !auth.user &&
          <AuthModal
            auth={auth}
            show={this.state.showAuth}
            viewAction={this.state.authView}
            closeModal={() => this.toggleLogin()}
            login={(data) => this.attemptLogin(data)}
            register={(data) => this.register(data)}
            swapView={(view) => this.swapAuthView(view)} />
        }
      </TopBar>
    );
  }
}

Header.propTypes = {
  auth: PropTypes.object.isRequired,
  dispatch: PropTypes.func.isRequired,
};
