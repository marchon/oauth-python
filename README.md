# oauth-python
OAuth Sample for Python

The oauth-python code snippet demonstrates the Oauth 1.0 flow using an OAuth1Session object from the requests-oauthlib open source library.  The OAuth1Session object is a layer implemented on top of a consumer and provider.  The sample code assumes that you are running on Windows platform with Eclipse installed.  The outcome of the sample reads an existing customer and creates a new customer using Intuit’s QuickBooks Online API v3 endpoints.

Download and Install Python 2.7.9 from here:
https://www.python.org/downloads/

Learn how to install Pydev and Pydev extension for Eclipse here:
http://www.pydev.org/manual_101_install.html

Download and install  oauthlib0.7.2 here:
https://pypi.python.org/pypi/oauthlib

Download and install requests-oauthlib here:
https://github.com/requests/requests-oauthlib

Download and install requests-2.5.1 here:
https://pypi.python.org/pypi/requests/2.5.1

Unzip and move oauthlib, requests-oauthlib and requests folder to your Python Lib folder:

 

Open Eclipse and create a new PyDev Project

 

Copy OAuthTest.py to your project folder

 

Specify grammar version and interpreter location (e.g. c:\Python27\python.exe)

 

Open OAuthTest.py in Eclipse.  The following sample is based upon Requests-OAuthLib documentation using an OAuth 1.0 Session object implementation:
http://requests-oauthlib.readthedocs.org/en/latest/api.html

 

Execute code in Python command line window:
 

Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> clientkey = "qyprdcwoKwGLCUQ5omUVx7hYb0xJlr"
>>> clientsecret = "********"
>>>
... # OAuth end points for Intuit
... request_token_url = "https://oauth.intuit.com/oauth/v1/get_request_token"
>>> access_token_url = "https://oauth.intuit.com/oauth/v1/get_access_token"
>>> authorization_base_url = "https://appcenter.intuit.com/connect/begin"
>>>
>>> # 2. Fetch a request token
... # callback_uri is a callback endpoint on your web server
... from requests_oauthlib import OAuth1Session
>>> oauth = OAuth1Session(clientkey, clientsecret, callback_uri='http://localhost:8080/accesstoken.html')
>>> oauth.fetch_request_token(request_token_url)
{u'oauth_token_secret': u'********', u'oauth_token': u'qyprdNojiJ2IByEFMa0Yz7HTztbzRRWRReU36bqFvDqVEOfo', u'oauth_callback_confirmed': u'true'}
>>>
>>> # 3. Redirect user to your provider implementation for authorization
... # Cut an paste the authorization_url and run it in a browser
... authorization_url = oauth.authorization_url(authorization_base_url)
>>> print 'Please go here and authorize,', authorization_url
Please go here and authorize, https://appcenter.intuit.com/connect/begin?oauth_token=qyprdNojiJ2IByEFMa0Yz7HTztbzRRWRReU36bqFvDqVEOfo
>>>

Open authorize_url in a browser and authorize company access:

 

Copy the complete callback_uri as the redirect_response

 

>>> # 4. Get the authorization verifier code from the callback url
... # redirect response is the complete callback_uri after you have authorized access to a company
... redirect_response = 'http://localhost:8080/accesstoken.html?oauth_token=qyprdNojiJ2IByEFMa0Yz7HTztbzRRWRReU36bqFvDqVEOfo&oauth_verifier=e9x8xkg&realmId=1292734305&dataSource=QBO'
>>> oauth.parse_authorization_response(redirect_response)
{u'oauth_verifier': u'e9x8xkg', u'oauth_token': u'qyprdNojiJ2IByEFMa0Yz7HTztbzRRWRReU36bqFvDqVEOfo', u'realmId': u'1292734305', u'dataSource': u'QBO'}
>>>
>>> # 5. Fetch the access token
... # At this point, oauth session object already has the request token and request token secret
... oauth.fetch_access_token(access_token_url)
{u'oauth_token_secret': u'********', u'oauth_token': u'********'}
>>>
>>> # Define the get and post endpoints for QuickBooks Online API v3
... getresource = 'https://sandbox-quickbooks.api.intuit.com/v3/company/1292734305/customer/3'
>>> postresource = 'https://sandbox-quickbooks.api.intuit.com/v3/company/1292734305/customer'
>>>
>>> # 6. Read a customer from a company
... r = oauth.get(getresource)
>>> print r.content
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-05T17:48:58.963-08:00"><Customer domain="QBO" sparse="false"><Id>3</Id><SyncToken>0</SyncToken><MetaData><CreateTime>2014-10-11T16:51:22-07:00</CreateTime><LastUpdatedTime>2014-12-29T15:05:10-08:00</LastUpdatedTime></MetaData><GivenName>Grace</GivenName><FamilyName>Parie
nte</FamilyName><FullyQualifiedName>Cool Cars</FullyQualifiedName><CompanyName>Cool Cars</CompanyName><DisplayName>Cool Cars</DisplayName><PrintOnCheckName>Cool Cars</PrintOnCheckName><Active>true</Active><PrimaryPhone><FreeFormNumber>(415) 555-9933</FreeFormNumber></PrimaryPhone><PrimaryEmailAddr><Address>Cool_Cars@intuit.com</Address></PrimaryEmailAddr><Taxable>false</Taxable><BillAddr><Id>4</Id
><Line1>65 Ocean Dr.</Line1><City>Half Moon Bay</City><CountrySubDivisionCode>CA</CountrySubDivisionCode><PostalCode>94213</PostalCode><Lat>37.4300318</Lat><Long>-122.4336537</Long></BillAddr><Job>false</Job><BillWithParent>false</BillWithParent><Balance>30.00</Balance><BalanceWithJobs>30.00</BalanceWithJobs><PreferredDeliveryMethod>Print</PreferredDeliveryMethod></Customer></IntuitResponse>
>>>
>>> # 7. Create a customer in a company
... new_customer = {"DisplayName": "NewCustomer102"}
>>> r = oauth.post(postresource, json=new_customer)
>>> print r.content
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-05T17:48:59.177-08:00"><Customer domain="QBO" sparse="false"><Id>73</Id><SyncToken>0</SyncToken><MetaData><CreateTime>2015-02-05T17:48:59-08:00</CreateTime><LastUpdatedTime>2015-02-05T17:48:59-08:00</LastUpdatedTime></MetaData><FullyQualifiedName>NewCustomer102</FullyQua
lifiedName><DisplayName>NewCustomer102</DisplayName><PrintOnCheckName>NewCustomer102</PrintOnCheckName><Active>true</Active><DefaultTaxCodeRef>2</DefaultTaxCodeRef><Taxable>true</Taxable><Job>false</Job><BillWithParent>false</BillWithParent><Balance>0</Balance><BalanceWithJobs>0</BalanceWithJobs><PreferredDeliveryMethod>Print</PreferredDeliveryMethod></Customer></IntuitResponse>
>>>
