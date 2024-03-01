import json

def handler(event, context):
    message = 'Hello, World! From Lambda in Docker'
    print(message)
    print(event)
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": message})
    }