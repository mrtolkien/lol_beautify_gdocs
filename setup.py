from setuptools import setup

setup(
    name='lol_beautify_gdocs',
    packages=['lol_beautify_gdocs'],
    version='0.1',
    license='MIT',
    description='Beautifying Google documents related to League of Legends',
    author='Gary Mialaret',
    author_email='gary.mialaret@gmail.com',
    url='https://github.com/mrtolkien',
    download_url='https://github.com/mrtolkien/lol_beautify_gdocs/archive/v0.1-alpha.tar.gz',
    keywords=['lol', 'gdocs'],
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'static-data',
        'joblib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.8',
    ],
)
