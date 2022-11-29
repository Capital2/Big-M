from fastapi import status, HTTPException, Response
from ..core.BigM import BigM
from ..core.aliases import Iterations
import pandas as pd
import numpy as np

class BigMController():
    def format_data(self, req_body):       
        formatted_req_body = []
        for i in range(0, req_body["dimension"]["code"]):
            dimension_coefs = []
            for c in range(0, len(req_body["constraints"])):
                dimension_coefs.append(req_body["constraints"][c][f'{i}'])

            dimension_coefs.append(req_body["equation"][f'{i}'])

            formatted_req_body.append(dimension_coefs)


        conditions = []
        conditions_types = []
        for c in range(0, len(req_body["constraints"])):
            # dimension_coefs.append(req_body["constraitns"]["value"])
            conditions.append(req_body["constraints"][c]["value"])
            if req_body["constraints"][c]["type"] == '<=':
                conditions_types.append(-2)
            if req_body["constraints"][c]["type"] == '<':
                conditions_types.append(-1)
            elif req_body["constraints"][c]["type"] == '=':
                conditions_types.append(0)
            elif req_body["constraints"][c]["type"] == '>':
                conditions_types.append(1)
            elif req_body["constraints"][c]["type"] == '>=':
                conditions_types.append(2)

        conditions.append(0)
        conditions_types.append(0)
        formatted_req_body.append(conditions)
        formatted_req_body.append(conditions_types)

        for i in range(0, len(formatted_req_body)):
            for j in range (0, len(formatted_req_body[i])):
                formatted_req_body[i][j] = int(formatted_req_body[i][j])

        return formatted_req_body


    def perform_BigM(self, formatted_req_body):
        big_m = BigM()        
        iterations = big_m.runBigM(np.array(formatted_req_body))
        return iterations

    def format_result(self, iterations: Iterations):
        data = []
        for iteration in iterations:
            tmp = iteration[0].astype(str)
            tmp_bv = []
            tmp_nbv = []
            for i in range(0, len(iteration[1])):
                tmp_bv.append({
                    "value": float(iteration[1][i][1]),
                    "name": iteration[1][i][0],
                    "equation":  float(iteration[1][i][2])
                })

            for i in range(0, len(iteration[2])):
                tmp_nbv.append({
                    "value": float(iteration[2][i][1]),
                    "name": iteration[2][i][0],
                    "equation":  float(iteration[2][i][2])
                })
            data.append({
                "iteration": tmp.values.tolist(),
                "bv": tmp_bv,
                "nbv": tmp_nbv
            })

        print(data)
        return {
            "data": data,
            "columns": list(iterations[0][0].columns)
        }
        

if __name__ == '__main__':
    BigM_controller = BigMController()
