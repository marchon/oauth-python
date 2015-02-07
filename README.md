Welcome to the Intuit Developer's oauth-python.

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

![9](https://cloud.githubusercontent.com/assets/9324696/6089565/7d52e01a-ae19-11e4-9364-927a7fd8d642.png)

![7](https://cloud.githubusercontent.com/assets/9324696/6089426/3e69f26e-ae17-11e4-9472-81b58ad88169.png)

Copy the complete callback_uri as the redirect_response

![8](https://cloud.githubusercontent.com/assets/9324696/6089428/3f5c50cc-ae17-11e4-9932-8f0cf0f73e13.png)

![10](https://cloud.githubusercontent.com/assets/9324696/6089568/7ef84e1e-ae19-11e4-8185-84bd731c1487.png)

