import React, { Component, PropTypes } from 'react';
import { TopBar, TopBarTitle, TopBarRight, Menu, MenuItem, Icon } from 'react-foundation';
import { Link } from 'react-router';

import '../../scss/nav.scss';

export default class Header extends Component {
  constructor(props) {
    super(props);
    // this.handleChange = this.handleChange.bind(this)
    // this.handleRefreshClick = this.handleRefreshClick.bind(this)
    this.state = {
      openMobile: false,
    };
  }

  toggleMobileMenu() {
    this.setState({ openMobile: !this.state.openMobile });
  }

  render() {
    const { auth } = this.props;
    const accountLink = (auth.user) ?
      (<Link to='/account'>
        <Icon name='fi-torso-female' /> <span>{auth.user.name}</span>
      </Link>) :
      <a tabIndex='0' onClick={() => { console.log('hey'); }}>Login</a>;
    const mobileClass = (this.state.openMobile) ? 'open' : '';

    return (
      <TopBar>
        <area tabIndex='-1' onClick={() => this.toggleMobileMenu()} className={`overlay ${mobileClass}`} />
        <TopBarTitle>
          <Menu>
            <MenuItem onClick={() => this.toggleMobileMenu()} className='show-for-small-only'>
              <span className='menu-icon black' />
            </MenuItem>
            <MenuItem text className='menu-title'><Link to='/'>GoodHoots</Link></MenuItem>
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
      </TopBar>
    );
  }
}

Header.propTypes = {
  auth: PropTypes.object.isRequired,
};
