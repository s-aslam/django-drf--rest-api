import json

def getSerializer_errors(error_dict):
    result=list()
    error_dict=dict(error_dict)
    final_data=dict()
    for error in error_dict:
    #    result.append(error+" : "+json.dumps(error_dict[error]).strip('"[]'))
       data=dict()
       data[error] = json.dumps(error_dict[error]).strip('"[]')
       result.append(data)
    print(result)
    return result

page_size = 1

response_text={
    200:"Success",
    400 :'Bad Request',
    401 :'Unauthorized',
    403 :'Forbidden',
    404 :'Not Found',
    500 :'Internal Server Error',
    601 :'Data Dupliacation',
    602 :'Could Not Save',
    603 :'No data found',
}

api_message = {
    'sms_otp':'Enter HYPE code {} to confirm your number',
    
    'error_user_have_not_access' : 'You are not permitted to do this action.',
    'email_verification_pending' : 'Your Email ID is not verified. Please verify.',
    'success_setting_updated' : 'Setting has been updated successfully.',
    'verification_pending' : "Seems like you haven't verified your Email ID. Please verify your Email ID then login.",
	'request_cancel' : 'Your request has been canceled',
				
    #general messages
    'error_in_save' : 'Error In Saving. Please try again later.',
    'something_going_wrong' : 'Something\'s going wrong. Please try again.',
    'no_data_found' : 'No such data found.',
    
    'error_mobile_not_found' : 'No such user found with this Mobile.',
    'already_verified_user' : 'You are already a verified user.',
    'error_user_not_found' : 'No such user found',
    'error_in_update' : 'Error In Updating. Please try again later.',
    'error_in_delete' : 'Error in deleting',
							
    # API
    'account_deactivate' : 'Account is inactivated, please contact administrator.',
    'successfully_logged_in'  :  'You are successfully logged in.',
    'invalid_login' : 'Invalid ID or Password.',
    'email_exist_already' : 'Email Id is Already Registered.',
    'verification_sms_sent' : 'Verification code has been succesfully sent on mobile number.',
    'phone_exist_already' : 'Phone Number is Already Registered.',
    'mobile_verified_successfully' : 'Mobile has been successfully verified.',
    'mobile_verification_mismatch' : 'Mobile verification code is invalid.',
    'forgot_password_link_sent' : 'Reset password link has been sent to your registered E-mail ID.',
    'error_forgot_password' : 'Error while reset password. Please retry.',
    'error_forgot_password_id_not_found' : 'No such user found with this ID.',
    'verification_link_sent' : 'Verification link has been succesfully sent on registered email.',
    'success_password_changed' : 'Password has been successfully changed.',
    'error_invalid_old_password' : 'Invalid old password.',
    'request_sent' : 'Your request has been sent',
    'already_cancel' : 'This ride is already cancelled',
    'promocode_not_avail': 'Promocode not available.',
    
    #notification
    'new_request' : 'You have new request',
    'cancel_by_pass' : 'Ride Id # {trip_id} has been cancelled.',
    'accept_ride' : 'You ride has been accepted.',
    'nodriver_available' : 'No more driver available.',
    'start_ride' : 'Ride started!',
    'complete_ride' : 'Ride completed!',
    'driver_arriving' : 'Your driver is arriving now.',
    'driver_arrived' : 'Your driver is arrived at your location.',


    #login messages
    'invalid_login_1' : 'Invalid Email ID or Password.',
    'invalid_login_2' : 'Invalid Mobile Number or Password.',
    'token_generate_error'  :  'Enable to generate token. Please try again.',
    'login_again' : 'Token expired , login again',

    #forgot password
    'error_forgot_password_link_expired'  :  'Your forgot password link has been expired. Please request a new one.',
    'error_view_user_not_found' : 'No such viewing user found',
    
    # users
    'success_profile_updated' : 'Profile has been updated successfully.',
    'error_unknown_statu' : 'Invalid status.',
    'email_verification_pending' : 'Your Email ID is not verified. Please verify.',
    'success_logout' : 'You are successfully logged out.',
    
    # contact us
    'contactus_message_sent' : 'Your message has been successfully sent.',
        
    # Front End
    #Verify Email ID
    'email_successfully_verified' : ' Email Id has been successfully verified.',

    "pass_match_error": "Confirm password does not match",
    "invalid_email": "Please enter valid email",
    "invalid_password": "Invalid old password",  # For wrong password format
    "email_registered": "Email already Registered",  # For sign up    
    "register_thanks": "Thank you for registering ",
    "account_deactivated": "Please activate your account first",
    "wrong_credentials": "Incorrect email or password",  # For login
    "password_change_success": "Your password changed successfully, Please login with updated details",
    "email_not_exist": "No account associated with this email",  # Forgot password
    "invalid_account": "Invalid account",
    "login_success": "Successfully Logged in",    
    "server_error": "Something went wrong, Please try again",
    "forbidden": "Forbidden Request",

}
