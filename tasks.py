from invoke import run, task


@task
def test():
    run('py.test --pep8 --cov=flask_reggie test_flask_reggie.py', pty=True)


@task
def travisci():
    run('py.test --pep8 test_flask_reggie.py')
