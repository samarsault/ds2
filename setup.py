from distutils.core import setup

setup(name='ds2',
      version='1.0',
      description='Encrypted file database',
      author='Samarjeet Singh',
      author_email='thelehhman@gmail.com',
      url='https://github.com/thelehhman/ds2',
      download_url = 'https://codeload.github.com/thelehhman/ds2/zip/master',
      scripts=['bin/ds2'],
      keywords= ['db', 'encrypted', 'files'],
      packages=['ds2'],
      install_requires = [ 'bson', 'cryptography', 'bcrypt', 'click', 'csvmapper' ]
     )
