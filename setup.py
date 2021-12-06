from setuptools import setup

setup(name='run-sql-job',
      version='1.0.0',
      description='Job that run sql script',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      platforms="all",
      url="https://github.com/mantis-software-company/rabbitmq2psql-as-json",
      author='Derya Pelin Deniz',
      author_email='info@mantis.com.tr',
      packages=['run_sql_job'],
      scripts=['bin/run-sql-job'],
      install_requires=['psycopg2-binary'],
      python_requires=">3.8.*, <4",
      classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.8"]
      )
