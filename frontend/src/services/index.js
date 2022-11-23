import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/",
});

export const process = (linearProgram) => {
  return new Promise((resolve, reject) => {
    try {
        api
        .post("/BigM/process", linearProgram)
        .then((res) => {
          console.log("axios res=", res);
          resolve(res.data);
        })
        .catch((err) => {
          console.log("getAllUsers > axios err=", err);
          reject("Error in getAllUsers axios!");
        });
    } catch (error) {
      console.error("in userServices > getAllUsers, Err===", error);
      reject("Error");
    }
  });
};
