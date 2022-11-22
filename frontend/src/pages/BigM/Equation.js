import React from "react";
import { InputText } from "primereact/inputtext";
import { Button } from 'primereact/button'

export default function Equation({
  dimension,
  equation,
  isConstraint,
  handleEquation,
  deleteConstraint
}) {
  const equationBuilder = () => {
    let _equation = [];
    for (let i = 0; i < dimension; i++) {
      _equation.push(
        <div className="col grid" key={i}>
          <div className="col-1">
            <span style={{ position: "relative", top: "10px", right: "10px" }}>X{i + 1}</span>
          </div>
          <div className="col">
            <InputText
              id={`${equation["name"]}_${i}`}
              name={`${equation["name"]}_${i}`}
              className="w-5rem"
              value={equation[i]}
              onChange={handleEquation}
            />
          </div>
        </div>
      );
    }

    if (isConstraint) {
      _equation.push(
        <>
          <div className="col">
            <InputText
              id={`${equation["name"]}_type`}
              name={`${equation["name"]}_type`}
              className="w-5rem"
              value={equation["type"]}
            />
          </div>
          <div className="col">
            <InputText
              id={`${equation["name"]}_value`}
              name={`${equation["name"]}_value`}
              className="w-5rem"
              value={equation["value"]}
            />
          </div>
          <div className="col">
            <Button
              label="Delete"
              icon="pi pi-trash"
              className="p-button-text p-button-danger"
              onClick={() => {deleteConstraint(equation["name"])}}
              type='button'
            />
          </div>
        </>
      );
    }
    return _equation;
  };
  return <div className="grid m-0">{equationBuilder()}</div>;
}
