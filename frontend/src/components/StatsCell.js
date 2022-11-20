import React from 'react'
import { MDBIcon} from 'mdb-react-ui-kit';
export default function StatCell(props) {
  return (

       <div className="d-flex flex-column mb-5">
        <div className="p-2">{props.title}</div>
        <div className="p-2">
          <div class="d-flex justify-content-around">
            <div class="p-3"><h1 >{props.value}</h1></div>
            <div class="p-3"> <MDBIcon fas icon={props.icon} size='4x' /></div>
          </div>
        </div>
      </div>
  )
}
