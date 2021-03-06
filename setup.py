from setuptools import setup
import os

setup(
    name='dirty-filters',
    url='https://github.com/alfred82santa/dirty-filters',
    author='alfred82santa',
    version='0.0.1',
    author_email='alfred82santa@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'],
    packages=['dirty_filters'],
    include_package_data=True,
    description="Dirty filters for python 3",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    test_suite="nose.collector",
    tests_require="nose",
    zip_safe=True,
)
