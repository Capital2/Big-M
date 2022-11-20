import React from 'react';
import { MDBRadio } from 'mdb-react-ui-kit';

export default function DimensionSelection() {
  return (
    <div  className="ps-5">
      <MDBRadio name='inlineRadio' id='inlineRadio1' value='option1' label="R2" inline  labelClass="radioLabel"/>
      <MDBRadio name='inlineRadio' id='inlineRadio2' value='option2' label='R3' inline  labelClass="radioLabel"/>
    </div>
  );
}