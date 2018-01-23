from paver.tasks import task, BuildFailure, needs
from paver.easy import sh


@needs('unit_tests', 'lettuce_tests', 'behave_tests', 'run_pylint')
@task
def default():
    pass

@task
def unit_tests():
    sh('nosetests --with-coverage test/unit')

@task
def lettuce_tests():
    sh('lettuce test/bdd')

@task
def behave_tests():
    sh('behave test/bdd')

@task
def run_pylint():
    try:
        sh('pylint > pylint.txt')
    except BuildFailure:
        pass
