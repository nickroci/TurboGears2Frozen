#!/usr/bin/env python
import setuptools
from distutils.core import setup

from sys import version
from setuptools import find_packages

if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
    
setup(name='TurboGears2Frozen',
      install_requires=(
        """
        Babel==0.9.6
        Beaker==1.5.4
        FormEncode==1.2.4
        Genshi==0.6
        Mako==0.7.0
        MarkupSafe==0.15
        Paste==1.7.5.1
        PasteDeploy==1.3.4
        PasteScript==1.7.5
        Pygments==1.4
        Pylons==1.0
        Routes==1.12.3
        SQLAlchemy
        Tempita==0.5.1
        ToscaWidgets==0.9.12
        repoze.tm2==1.0
        TurboGears2==2.1.5
        WebError==0.10.3
        WebFlash==0.1a9
        WebHelpers==1.3
        WebOb==1.0.8
        WebTest==1.2.4
        decorator==3.3.2
        nose==1.0.0
        simplejson==2.3.0
        tg.devtools==2.1.5
        wsgiref==0.1.2
        zope.interface==4.0.1
        zope.sqlalchemy==0.7.1
        transaction==1.3.0
        """
        ),
        classifiers=[
          "Environment :: Web Environment",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Framework :: TurboGears"
          ],
        keywords='turbogears2',
        version='2.1.5',
        description='Reference this rather than Turbogears2 as a dependency to get a consistent install with your package',
        author='Nick Holden',
        author_email='nickpholden@gmail.com',
        url='https://github.com/nickpholden/TurboGears2Frozen',
        license='LGPL',
        packages=find_packages(exclude=['ez_setup'])
        )
