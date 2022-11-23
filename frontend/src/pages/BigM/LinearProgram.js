import React, { useState } from "react";
import { Chip } from "primereact/chip";
import { Button } from "primereact/button";
import { Dropdown } from "primereact/dropdown";
import Equation from "./Equation";
import Constraints from "./Constraints";
import { process } from "../../services";

export default function LinearProgram() {
  const [userInput, setUserInput] = useState({
    dimension: { name: "R2", code: 2 },
    equationType: { name: "Maximisation", code: "max" },
    equation: { 0: 5, 1: 10, name: "equation" },
    constraints: [
      { 0: 5, 1: 10, name: "c1", type: "<=", value: 50 },
      { 0: 5, 1: 10, name: "c2", type: "=", value: 100 },
      { 0: 5, 1: 10, name: "c3", type: ">=", value: 200 },
    ],
  });

  const supportedDimensions = [
    { name: "R2", code: 2 },
    { name: "R3", code: 3 },
  ];

  const equationTypes = [
    { name: "Maximisation", code: "max" },
    { name: "Minimisation", code: "min" },
  ];

  const handleChange = (e) => {
    setUserInput({ ...userInput, [e.target.name]: e.target.value });
  };

  const handleEquation = (e) => {
    const equationInfo = e.target.name.split("_");
    let _constraints = [];
    for (let i = 0; i < userInput.constraints.length; i++) {
      _constraints.push({ ...userInput.constraints[i] });
    }

    if (equationInfo[0] !== "equation") {
      for (let i = 0; i < _constraints.length; i++) {
        if (_constraints[i]["name"] === equationInfo[0]) {
          _constraints[i][equationInfo[1]] = e.target.value;
          break;
        }
      }

      setUserInput({ ...userInput, constraints: [..._constraints] });
    } else {
      setUserInput({
        ...userInput,
        equation: { ...userInput.equation, [equationInfo[1]]: e.target.value },
      });
    }
  };

  const deleteConstraint = (constraintName) => {
    let filtredConstraints = userInput.constraints.filter(
      (constraint) => constraint.name !== constraintName
    );

    for (let i = 0; i < filtredConstraints.length; i++) {
      filtredConstraints[i] = {
        ...filtredConstraints[i],
        name: `c${i + 1}`,
      };
    }

    setUserInput({ ...userInput, constraints: [...filtredConstraints] });
  };

  const addConstraint = () => {
    setUserInput({
      ...userInput,
      constraints: [
        ...userInput.constraints,
        {
          0: 0,
          1: 0,
          name: `c${userInput.constraints.length + 1}`,
          type: "=",
          value: 0,
        },
      ],
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let res = await process(userInput);
      console.log(res);
    } catch (error) {
      console.log("errors");
    }
  };

  return (
    <div className="surface-0 p-4">
      <div className="font-medium text-3xl text-900 mb-3">
        Linear Program User Input
      </div>
      <div className="text-500 mb-5">
        This interface will allow you to set your linear program
      </div>
      <form onSubmit={handleSubmit}>
        <ul className="list-none p-0 m-0">
          <li className="flex align-items-center py-3 px-2 border-top-1 border-300 flex-wrap">
            <div className="text-500 w-6 md:w-2  font-medium">Dimension</div>
            <div className="text-900 w-full md:w-8 md:flex-order-0 flex-order-1">
              <Dropdown
                optionLabel="name"
                value={userInput["dimension"]}
                options={supportedDimensions}
                onChange={handleChange}
                placeholder="Select a dimension"
                name="dimension"
                id="dimension"
                className="w-12rem"
              />
            </div>
            {/* <div className="w-6 md:w-2 flex justify-content-end">
              <Button
                label="Reset"
                icon="pi pi-pencil"
                className="p-button-text"
              />
            </div> */}
          </li>
          <li className="flex align-items-center py-3 px-2 border-top-1 border-300 flex-wrap">
            <div className="text-500 w-6 md:w-2 font-medium">Equation</div>
            <div className="text-900 w-full md:w-4 md:flex-order-0 flex-order-1">
              <Dropdown
                optionLabel="name"
                value={userInput.equationType}
                options={equationTypes}
                onChange={handleChange}
                placeholder="Select an equation type"
                className="w-12rem"
                name="equationType"
                id="equationType"
              />
            </div>
            <div className="text-900 w-full md:w-4 md:flex-order-0 flex-order-1">
              <Equation
                dimension={userInput.dimension.code}
                equation={userInput.equation}
                isConstraint={false}
                handleEquation={handleEquation}
              />
            </div>
          </li>
          <li className="flex align-items-center py-3 px-2 border-top-1 border-300 flex-wrap">
            <div className="text-500 w-6 md:w-2 font-medium">Constraints</div>
            <div className="text-900 w-full md:w-10 md:flex-order-0 flex-order-1">
              <Constraints
                dimension={userInput.dimension.code}
                constraints={userInput.constraints}
                handleEquation={handleEquation}
                deleteConstraint={deleteConstraint}
              />
            </div>
            <Button
              label="Add Constraint"
              icon="pi pi-pencil"
              className="relative left-50 mt-4"
              type="button"
              onClick={addConstraint}
            />
          </li>
          <li className="flex align-items-center py-3 px-2 border-top-1 border-300 flex-wrap">
            <div className="text-500 w-6 md:w-2 font-medium">
              <Button
                label="Process"
                icon="pi pi-check"
                className="p-button-success"
                type="submit"
              />
            </div>
          </li>
        </ul>
      </form>
    </div>
  );
}
