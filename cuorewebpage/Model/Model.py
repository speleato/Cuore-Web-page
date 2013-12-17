def get_initial_data():
    parameters = {'name':'John', 'surname':'Hopkins'}
    return parameters

def process_business_logic():
    #DATABASE ACCESS
    data = get_initial_data()
    return len(data)