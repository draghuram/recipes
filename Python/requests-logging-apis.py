
import http
import json
import traceback

"""

The recipe in this file lets you print request and response of every 
API call made with "requests" package. To use it, call the function
"print_request_and_response" from requests's "response" hook, 
as described at: 

https://requests.readthedocs.io/en/master/user/advanced/#event-hooks

Here is an example:

def response_callback(resp, *args, **kwargs):
    print_request_and_response(resp)
    # ...

conn = requests.Session()
conn.hooks.update({"response": response_callback})

"""

def print_request_and_response(resp):
    """Print request and response of the API call.

    resp - requests.Response

    """

    # Get the request object for this API call.
    req = resp.request

    print("\n######## {} ########".format(time.asctime()))
    print("\n{} {}".format(req.method, req.url))
    print()
    for k, v in req.headers.items():
        print("{}: {}".format(k, v))
    print()

    try:
        d = json.loads(req.body.decode("utf-8"))
        print(json.dumps(d, sort_keys=True, indent=4))
    except AttributeError:
        # "body" is not present in request object.
        pass
    except:
        print(traceback.format_exc())

    try:
        status_str = http.HTTPStatus(resp.status_code).name
    except:
        status_str = "UNKNOWN"

    print("\n{} {}\n".format(resp.status_code, status_str))
    for k, v in resp.headers.items():
        print("{}: {}".format(k, v))
    print()

    if resp.content:
        try:
            d = resp.json()
            print(json.dumps(d, sort_keys=True, indent=4))
        except:
            print(resp.content)

    print("################")
