

# Globally install the serverless framework

```
npm install -g serverless
```


# Install the virtualenv

```
pip install virtualenv
```

## Create the virtual environment
```
virtualenv venv --python=python3.8
```

## Activate the virtual environment

```
source venv/bin/activate
```

## Deactivate virtual environment

```
deactivate
```

# Install pacakages

```
npm install
```

```
pip install flask
```

```
pip install boto3
```

# Freeze requirements

```
pip freeze > requirements.txt
```

# Install dynamodb locally

```
sls dynamodb install
```

# Local development

```
sls dynamodb start >/dev/null
```

# Serve application

```
sls wsgi serve -p 8080
```

# Deploy onto AWS

```
sls deploy
```

# Remove deployment from AWS

```
serverless remove
```