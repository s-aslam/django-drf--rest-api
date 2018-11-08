def getProductList(self_args,objects):
 
    result_data = []
    for obj in objects:
        data_info = {}
        data_info['name'] = obj.name
        data_info['discription'] = obj.discription
        data_info['unit'] = obj.unit
        data_info['price'] = obj.price
        data_info['is_active'] = obj.is_active
        result_data.append(data_info)
    
    return result_data
    
def getProductData(self_args,obj):
    data_info = {}
    data_info['name'] = obj.name
    data_info['discription'] = obj.discription
    data_info['unit'] = obj.unit
    data_info['price'] = obj.price
    data_info['is_active'] = obj.is_active
    return data_info