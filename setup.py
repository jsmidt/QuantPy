from distutils.core import setup

setup(
    name='QuantPy',
    version='0.1',
    author='Joseph Smidt',
    author_email='josephsmidt@gmail.com',
    packages=['quantpy'],
    url='https://github.com/jsmidt/QuantPy',
    license='LICENSE',
    description='A framework for quantitative finance In python',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy >= 1.23.5",
        "pandas >= 0.10.0",
        "matplotlib >= 1.1.0",
        "statsmodels >= 0.14.0",
        "arch >= 6.0.1",
        "sklearn >= 1.1.0",
    ],
)
