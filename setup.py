try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

dir_n = os.path.dirname(__file__)
readme_filename = os.path.join(dir_n, 'README.md')
requirements_filename = os.path.join(dir_n, 'requirements.txt')

PACKAGE_NAME = 'facebook_business'
PACKAGE_VERSION = '18.0.3'
PACKAGE_AUTHOR = 'Facebook'
PACKAGE_AUTHOR_EMAIL = 'smshad0001@gmail.com'
PACKAGE_URL = 'https://github.com/iamsamkhan/facebook.marketing.git'
PACKAGE_DOWNLOAD_URL = \
    'https://github.com/iamsamkhan/facebook_marketing.git/' + PACKAGE_VERSION
PACKAGES = [
    'facebook_business',
    'facebook_business.test',
    'facebook_business.utils',
    'facebook_business.adobjects',
    'facebook_business.adobjects.helpers',
    'facebook_business.adobjects.serverside',
]
PACKAGE_DATA = {
    'facebook_business': ['*.crt'],
    'facebook_business.test': ['*.jpg']
}
PACKAGE_LICENSE = 'LICENSE.txt'
PACKAGE_DESCRIPTION = 'Facebook Business SDK'

with open(readme_filename) as f:
    PACKAGE_LONG_DESCRIPTION = f.read()

with open(requirements_filename) as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]



setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    author=PACKAGE_AUTHOR,
    author_email=PACKAGE_AUTHOR_EMAIL,
    url=PACKAGE_URL,
    download_url=PACKAGE_DOWNLOAD_URL,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    license=PACKAGE_LICENSE,
    description=PACKAGE_DESCRIPTION,
    long_description=PACKAGE_LONG_DESCRIPTION,
    install_requires=PACKAGE_INSTALL_REQUIRES,
    long_description_content_type="text/markdown",
)
