import React from 'react'
import { MDBIcon} from 'mdb-react-ui-kit';
export default function StatCell(props) {
  return (

       <div className="d-flex flex-column mb-5">
        <div className="p-2">Flex item 1</div>
        <div className="p-2">
          <div class="d-flex justify-content-around">
            <div class="p-3">    <h1 >5</h1></div>
            <div class="p-3"> <MDBIcon fas icon="redo" size='4x' /></div>
          </div>
        </div>
      </div>
  )
}
