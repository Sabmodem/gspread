def authorize(
    credentials,
    http_client = None,
    session = None,
):
    
    class one:
        def get_all_records(self):
            return [{
                'Email': '123',
                'email': '123',
                'Timestamp': '0001-01-01 01:01:01',
                'Status': '123'
            }]            
        def append_row(self, data):
            pass

    class two:
        def __init__(self):
            self.sheet1 = one()


    class three:
        def open(self, four):
            return two()

    return three()