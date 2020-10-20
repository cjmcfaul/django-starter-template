<h1>django-starter-template</h1>

<h3>Installation:</h3>

1. Create a new directory for your project and move into it. You should replace "my-project", with the name of your project.
```bash
mkdir my-project && cd $_
```

2. Next, create a new virutal environment and activate it.
```bash
python3 -m venv venv && source venv/bin/activate
```

3. Then install django
```bash
pip3 install django
```

4. Finally, start the django project from a template using 
the git repository. Replace "my-project" with the name of your project.
```bash
django-admin startproject --template=https://github.com/colinmipapi/django-starter-template/archive/main.zip --name=Dockerfile --extension=py,yml,json,env my_project .
```

5. Setup the example.env file as your .env file
```bash
mv example.env .env
```


6. Now you are able to setup Docker
```bash
docker-compose up --build
```

<p></p>