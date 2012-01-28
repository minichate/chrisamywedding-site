class AccessControlMiddleware(object):
    '''
    Add a lazy function to the request object to get the Entry from the 
    request if the HTTP header `X-Secret` exists.
    '''
    
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        return response