# http

def get_http_error(error_code):
    result = ""
    match error_code:
        case 200:
            result = "OK"
        case 400:
            result = "Bad request"
        case 404:
            result = "Not found"
        case _:
            result = "Unknown error"
    return result

print(get_http_error(200))