import React from 'react'

import StatCell from './StatsCell';
export default function StatCellList(props) {
  return (
    <div class="d-flex justify-content-around">
        <div class="p-3"> <StatCell/></div>
        <div class="p-3"> <StatCell/></div>
        <div class="p-3"> <StatCell/></div>
        <div class="p-3"> <StatCell/></div>
    </div>
   

  )
}
