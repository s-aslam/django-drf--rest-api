import json

def getSerializer_errors(error_dict):
    result=list()
    error_dict=dict(error_dict)
    final_data=dict()
    for error in error_dict:
    #    result.append(error+" : "+json.dumps(error_dict[error]).strip('"[]'))
       data=dict()
       data[error] = json.dumps(error_dict[error]).strip('"[]')
       result.append(data)
    print(result)
    return result
   

def successResponse(success = True,data = list(),message = None,code=200):
    success = 1
    result = dict()
   
    result['data'] = list()
    if data != list():
        result['data'] = data;
    
    if message:
        result['data']['message'] = message;

    if data == list() and message == '':
        result['data'] = dict()

    result['error'] = [];
    result['success'] = success;
    result['code'] = code
    return result;

def errorResponse(success=False,error=list(),code=400):
    success = 0
    result = dict()

    result['data'] = dict()
    result['error'] = error    
    result['success'] = success;
    result['code'] = code
    return result



