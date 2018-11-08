from users.models import User

def get_login_user_dict(request,user_object,token):
    user_info = {
        'id': user_object.id,
        'first_name' : user_object.first_name,
        'last_name': user_object.last_name,
        'full_name': user_object.getFullName(),
        'email': user_object.email,
        'phone_number': user_object.phone_number,
    }
    token_info = {
        'token': token.key,
        'type':'Token'
    }
    result = dict()
    result['User'] = user_info
    result['Token'] = token_info
    return result 
