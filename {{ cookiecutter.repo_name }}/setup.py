from setuptools import setup

setup(name='{{ cookiecutter.repo_name }}',
      version='POC',
      url='https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}.git',
      author='{{ cookiecutter.author_name }}',
      packages=['src'],
      zip_safe=False)
