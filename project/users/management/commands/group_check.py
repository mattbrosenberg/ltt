import json
import urllib

def checkBody( body ):
    '''request.body.decode() and json.loads() do not like empty arguments
    so we always at least pass it an empty JSON object '''

    if( body == '' ):
        return '{}'
    return body

def parseDataByMethod( request ):
    ''' Decode HTTP request data based on METHOD '''

    if( request.method == 'GET' ):
        return urllib.parse.unquote( request.META['QUERY_STRING'] )
    else:
        return checkBody( request.body.decode('utf-8') )

class JSON( object ):
    ''' When a content type of "json" comes in, decode the data and pass
    add it to the request object as a dict '''
    
    def process_request( self, request ):

        if( 'json' in request.META.get('CONTENT_TYPE') ):
            request.json = json.loads( parseDataByMethod( request ) )