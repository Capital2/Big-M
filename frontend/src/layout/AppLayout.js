import React from 'react'
import DimensionSelection from '../components/DimensionSelection'
import InputField from '../components/InputField'
import StatCellList from '../components/StatsCellList'

export default function AppLayout() {
  return (
    <div>
      
      <StatCellList/>
      <DimensionSelection/>
      <InputField/>
      </div>
  )
}
