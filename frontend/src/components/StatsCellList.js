import React from 'react'

import StatCell from './StatsCell';
export default function StatCellList(props) {
  return (
    /*icons to choose from: https://mdbootstrap.com/docs/react/content-styles/icons/ */
    <div class="d-flex justify-content-around">
        
        <div class="p-3"> <StatCell title="Iteration" value={5} icon="redo"/></div>
        <div class="p-3"> <StatCell title="Time" value={0.5} icon ="clock"/></div>
        <div class="p-3"> <StatCell title="Gain" value={1800} icon="chart-line"/></div>
        <div class="p-3"> <StatCell title="coordinates"value="x=5  y=6" icon ="map-pin"/></div>
    </div>
   

  )
}
