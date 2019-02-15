# Web application

To connect the web application with the ML module, paste the module within this directory. Then change the first 3 paths in the prediction.py to:

* from preprocess import *
* from vectorizer import build_TF
* from definitions import *

Then go to utils/definitions.py and set MODELS_DIR to "./ml/models/"

You can start the application by running:

```
$ export FLASK_APP=app.py
$ flask run --without-threads
``` 

### Libraries to install

* Flask
* flask-paginate
* MySQLdb 
