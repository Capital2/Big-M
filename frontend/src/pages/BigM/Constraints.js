import React from "react";
import Equation from "./Equation";

export default function Constraints({ dimension, constraints, handleEquation, deleteConstraint }) {
  const constraintsBuilder = () => {
    let constraintsJSX = [];
    for (let i = 0; i < constraints.length; i++) {
      constraintsJSX.push(
        <Equation key={i} dimension={dimension} equation={{...constraints[i]}} isConstraint={true} handleEquation={handleEquation} deleteConstraint={deleteConstraint} />
      );
    }

    return constraintsJSX;
  };
  return constraintsBuilder()
}
