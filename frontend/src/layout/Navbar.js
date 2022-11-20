import React from 'react'
import {
  MDBContainer,
  MDBNavbar,
  MDBNavbarBrand
} from 'mdb-react-ui-kit';
export default function Navbar() {
  return (
    <div> 
        <MDBNavbar light bgColor='primary'>
      <MDBContainer fluid>
        <MDBNavbarBrand href='#'>
          <div className='navBarText'>BigM algorithm</div>
          </MDBNavbarBrand>
      </MDBContainer>
    </MDBNavbar>
  </div>
  )
}
