from setuptools import setup, find_packages


version = '0.1.4.2'

setup(
    name='django-file-form',
    version=version,
    packages=find_packages(),
    license='Apache License, Version 2.0',
    include_package_data=True,
    zip_safe=False,
    author='Marco Braak',
    author_email='mbraak@ridethepony.nl',
    install_requires=['ajaxuploader==0.3.0.2', 'six==1.4.1'],
    dependency_links=[
        'https://github.com/mbraak/django-ajax-uploader/archive/0.3.0.2.tar.gz#egg=ajaxuploader-0.3.0.2',
    ]
)
