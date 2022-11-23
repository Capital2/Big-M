import React from "react";

export default function Iteration({ iteration }) {
  const renderIteration = () => {
    let rows = [];
    for (let i = 0; i < iteration["iteration"].length; i++) {
      let cols = [];
      for (let j = 0; j < iteration["iteration"][i].length; j++) {
        cols.push(
          <div className="col bg-cyan-500 text-white font-bold border-round m-2 flex align-items-center justify-content-center">
            {iteration["iteration"][i][j]}
          </div>
        );
      }
      rows.push(<div className="grid">{cols}</div>);
    }

    return rows;
  };

  return (
    <>
      {renderIteration()}
      <br />
    </>
  );
}
