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

![1](https://cloud.githubusercontent.com/assets/9324696/6089413/1b679848-ae17-11e4-9b97-a22c27897ebd.png)

Open Eclipse and create a new PyDev Project

![2](https://cloud.githubusercontent.com/assets/9324696/6089418/33d7e3c4-ae17-11e4-8ce2-46dfc9c54607.png)

Copy OAuthTest.py to your project folder

![3](https://cloud.githubusercontent.com/assets/9324696/6089421/39e24e80-ae17-11e4-92fe-a8342ed54560.png)

Specify grammar version and interpreter location (e.g. c:\Python27\python.exe)

![4](https://cloud.githubusercontent.com/assets/9324696/6089422/3b6df542-ae17-11e4-92d9-657485cfbab6.png)

Open OAuthTest.py in Eclipse.  The following sample is based upon Requests-OAuthLib documentation using an OAuth 1.0 Session object implementation:
http://requests-oauthlib.readthedocs.org/en/latest/api.html

![5](https://cloud.githubusercontent.com/assets/9324696/6089423/3c75988c-ae17-11e4-9fcd-75bf4fcc98ff.png)

Execute code in Python command line window:

![6](https://cloud.githubusercontent.com/assets/9324696/6089424/3d956f3a-ae17-11e4-8197-3aa571c7d999.png)

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

![7](https://cloud.githubusercontent.com/assets/9324696/6089426/3e69f26e-ae17-11e4-9472-81b58ad88169.png)

Copy the complete callback_uri as the redirect_response

![8](https://cloud.githubusercontent.com/assets/9324696/6089428/3f5c50cc-ae17-11e4-9932-8f0cf0f73e13.png)


