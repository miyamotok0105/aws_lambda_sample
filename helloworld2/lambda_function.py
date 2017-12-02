import json

def myfunc01_handler(event, context):
    x = int(event["x"])
    y = int(event["y"])
    print(" x = "+str(x))
    print(" y = "+str(y))
    retval = ("result:"+str(x/y))
    return json.dumps(retval)
    
def lambda_handler(event, context):
    # TODO implement
    return 'Hello from Lambda'
