class OpenAPI_manager:
    def __init__(self, API_key):
        self.API_key = API_key
    
    def echoKey(self):
        print self.API_key
