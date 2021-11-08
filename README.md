# example-serverless-app-with-dynamodb

# install pacakages and globally install the serverless framework
```
npm install
```

```
npm install -g serverless
```

# sls install for dynamo 
```
sls login
```
```
sls dynamodb install
```

This will install dynamodb locally.


# pip commands: 
If you don't have pip you can install easily with the below command:
``` 
easy_install pip
```

```
pip install virtualenv
```

```
pip3 install flask
```

```
pip3 install boto3
```

```
virtual env:
```
```
virtualenv venv --python=python3.8
```
```
source venv/bin/activate
```

once you install new packages via pip update the requirements.txt file, this is used by the python virtual envrionment.
```
pip freeze > requirements.txt
```

```
Local development
```
```
sls dynamodb start
```

```
sls wsgi serve
```


# Removing the service. 
This will remove the finctions, Events and Resources that were created. This will also delete the AWS resources.
```
serverless remove
```