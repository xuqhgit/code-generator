



def success(data=None,message="success"):
    return {"code":1,"message":message,"data":data}

def error(data=None,message="error"):
    return {"code": 0, "message": message, "data": data}

