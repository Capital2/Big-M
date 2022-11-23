import React from "react";
import Iteration from "./Iteration";

export default function Iterations({ iterations, columns }) {
  console.log("yo");
  console.log(iterations);
  console.log(columns);
  if (iterations == null || columns == null) {
    return null;
  }
  const renderColumns = () => {
    let ds = [];
    for (let i = 0; i < columns.length; i++) {
      ds.push(
        <div
          class="col bg-cyan-500 text-white font-bold border-round m-2 flex align-items-center justify-content-center"
          style={{
            minWidth: "20px",
            minHeight: "20px",
          }}
        >
          {columns[i]}
        </div>
      );
    }

    return ds;
  };

  const renderIterations = () => {
    let _iterations = [];
    for (let i = 0; i < iterations.length; i++) {
      _iterations.push(<Iteration iteration={iterations[i]} />);
      _iterations.push(<hr />);
    }

    return _iterations;
  };
  return (
    <>
      <div className="grid">{renderColumns()}</div>
      <br />
      {renderIterations()}
    </>
  );
}
