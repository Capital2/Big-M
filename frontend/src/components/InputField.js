import React from 'react';
import { MDBInput } from 'mdb-react-ui-kit';

export default function InputField() {
  return (
        <div className='d-flex justify-content-start px-5 pt-3'>
        <span className='pe-3'>Z = </span>
          <MDBInput  id='formControlSm' type='text' size='sm' wrapperClass="inputfield"/>
          <span className='pe-3 ps-1'> X </span>
          <span className='pe-3'> + </span>
          <MDBInput  id='formControlSm' type='text' size='sm' wrapperClass="inputfield"  />
          <span className='ps-1'> Y </span>
        </div>
  );
}