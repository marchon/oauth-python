clientkey = "Enter your consumer key here"
clientsecret = "Enter your consumer secret here"
    
# OAuth end points for Intuit
request_token_url = "https://oauth.intuit.com/oauth/v1/get_request_token"
access_token_url = "https://oauth.intuit.com/oauth/v1/get_access_token"
authorization_base_url = "https://appcenter.intuit.com/connect/begin"

# 2. Fetch a request token
# callback_uri is a callback endpoint on your web server
from requests_oauthlib import OAuth1Session
oauth = OAuth1Session(clientkey, clientsecret, callback_uri='http://localhost:8080/accesstoken.html')
oauth.fetch_request_token(request_token_url)

# 3. Redirect user to your provider implementation for authorization
# Cut and paste the authorization_url and run it in a browser
authorization_url = oauth.authorization_url(authorization_base_url)
print 'Please go here and authorize,', authorization_url

# 4. Get the authorization verifier code from the callback url
# redirect response is the complete callback_uri after you have authorized access to a company
redirect_response = 'Enter the complete callback_uri with request token, verifier, realmID and dataSource here'
oauth.parse_authorization_response(redirect_response)

# 5. Fetch the access token
# At this point, oauth session object already has the request token and request token secret
oauth.fetch_access_token(access_token_url) 

# Define the get and post endpoints for QuickBooks Online API v3
getresource = 'https://sandbox-quickbooks.api.intuit.com/v3/company/1292734305/customer/3'
postresource = 'https://sandbox-quickbooks.api.intuit.com/v3/company/1292734305/customer'

# 6. Read a customer from a company
r = oauth.get(getresource)
print r.content

# 7. Create a customer in a company
new_customer = {"DisplayName": "NewCustomer102"}
r = oauth.post(postresource, json=new_customer) 
print r.content 
