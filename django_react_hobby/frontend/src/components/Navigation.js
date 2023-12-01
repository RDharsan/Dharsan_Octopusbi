import React from 'react';
import {Navbar,Nav} from 'react-bootstrap';
import logo from '../static/logo.png'
import "../App.css";
import {NavLink} from 'react-router-dom';
import {
  CDBSidebar,
  CDBSidebarContent,
  CDBSidebarFooter,
  CDBSidebarHeader,
  CDBSidebarMenu,
  CDBSidebarMenuItem,
} from 'cdbreact';


const Navigation = () => {
  return (
    <div className='sidebar'>
<CDBSidebar textColor="#333" backgroundColor="#f0f0f0">
    <CDBSidebarHeader prefix={<i className="fa fa-bars" />}>
      Navigation
    </CDBSidebarHeader>
    <CDBSidebarContent>
      <CDBSidebarMenu>
        <NavLink exact to="/" activeClassName="activeClicked">
          <CDBSidebarMenuItem icon="home">Home</CDBSidebarMenuItem>
        </NavLink>
        <NavLink exact to="/users" activeClassName="activeClicked">
          <CDBSidebarMenuItem icon="list">User List</CDBSidebarMenuItem>
        </NavLink>
        <NavLink exact to="/hobby" activeClassName="activeClicked">
          <CDBSidebarMenuItem icon="list">Hobby List</CDBSidebarMenuItem>
        </NavLink>
        <NavLink exact to="/manage" activeClassName="activeClicked">
          <CDBSidebarMenuItem icon="user">Manage Hobby</CDBSidebarMenuItem>
        </NavLink>
      </CDBSidebarMenu>
    </CDBSidebarContent>
  </CDBSidebar>
</div>
  );
};

export default Navigation;