# HW4 Starter Code and Instructions

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for additional context and instructions for this code.

## Model Update

We updated our model with the new attributes described in our Swagger docs:
- Absences: number of school absences (from 0 to 93)
- G1: first period grade (from 0 to 20)
- G2: second period grade (from 0 to 20)

We chose these values based on their statistical correlation to G3 (the target value) with a pandas correlation matrix. The relative values are below (higher is better, max is 1):

- Absences: 0.034247
- G1: 0.801468
- G2: 0.904868

We chose to remove Age as an attribute because of its low correlatin (-0.161579), and we did not believe that it should be used to make an acceptance decision. Additionally, we chose to exclude many of the other values in the dataset as they may lead to unnecessary biases, such as the education of the parents or the health of the student.

Because of the limited bounds of the attributes and its ability to implicitly handle collinearity in features, we decided to continue using a Random Forrest Classifier. Using a train/test split of 33%, we were able to achieve an Accuracy of 98.4733% and an F1 Score of 96.1538%, which is a significant improvement from the previous model.

## pipenv

[pipenv](https://pipenv.pypa.io/en/latest) is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.

### Installation

#### Prereqs

- The version of Python you and your team will be using (version greater than 3.8)
- pip package manager is updated to latest version
- For additional resources, check out [this link](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

#### Mac OS

To install pipenv from the command line, execute the following:

```terminal
sudo -H pip install -U pipenv
```

#### Windows OS

The same instructions for Mac OS **should** work for windows, but if it doesn't, follow the instructions [here](https://www.pythontutorial.net/python-basics/install-pipenv-windows).

### Usage

#### Downloading Packages

The repository contains `Pipfile` that declares which packages are necessary to run the `model_build.ipnyb`.
To install packages declared by the Pipfile, run `pipenv install` in the command line from the root directory.

You might want to use additional packages throughout the assignment.
To do so, run `pipenv install [PACKAGE_NAME]`, as you would install python packages using pip.
This should also update `Pipfile` and add the downloaded package under `[packages]`.
Note that `Pipfile.lock` will also be updated with the specific versions of the dependencies that were installed.
Any changes to `Pipfile.lock` should also be committed to your Git repository to ensure that all of your team is using the same dependency versions.

#### Virtual Environment

Working in teams can be a hassle since different team members might be using different versions of Python.
To avoid this issue, you can create a python virtual environment, so you and your team will be working with the same version of Python and PyPi packages.
Run `pipenv shell` in your command line to activate this project's virtual environment.
If you have more than one version of Python installed on your machine, you can use pipenv's `--python` option to specify which version of Python should be used to create the virtual environment.
If you want to learn more about virtual environments, read [this article](https://docs.python-guide.org/dev/virtualenvs/#using-installed-packages).
You can also specify which version of python you and your team should use under the `[requires]` section in `Pipfile`.

## Jupyter Notebook

You should run your notebook in the virtual environment from pipenv.
To do, you should run the following command from the root of your repository:

```terminal
pipenv run jupyter notebook
```

## API Endpoints

You should also use pipenv to run your Flask API server.
To do so, execute the following commands from the `app` directory in the pip venv shell.


Set an environment variable for FLASK_APP.
For Mac and Linux:
```terminal
export FLASK_APP=app.py
```

For Windows:
```terminal
set FLASK_APP=app
```

To run:
```terminal
pipenv run flask run
```

Or if you're in the pipenv shell, run:
```terminal
flask run
```

You can alter the port number that is used by the Flask server by changing the following line in `app/app.py`:

```python
app.run(host="0.0.0.0", debug=True, port=80)
```

## Testing

To run tests, execute the following command from the `app` directory:

```terminal
pytest
```

If you're not in the Pipenv shell, then execute the following command from the `app` directory:

```terminal
pipenv run pytest
```
