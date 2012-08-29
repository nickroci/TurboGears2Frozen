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
        Beaker==1.6.3
        FormEncode==1.2.4
        Genshi==0.6
        Mako==0.7.0
        MarkupSafe==0.15
        Paste==1.7.5.1
        PasteDeploy==1.5.0
        PasteScript==1.7.5
        Pygments==1.5
        Pylons==1.0
        Routes==1.13
        SQLAlchemy
        Tempita==0.5.1
        TurboGears2==2.2.0
        WebError==0.10.3
        WebFlash==0.1a9
        WebHelpers==1.3
        WebOb==1.1.1
        WebTest==1.3.4
        crank==0.6.4
        decorator==3.3.3
        nose
        repoze.lru==0.5
        repoze.tm2==1.0
        repoze.who==2.0
        repoze.who-friendlyform==1.0.8
        repoze.who.plugins.sa==1.0.1
        simplejson==2.6.0
        speaklater==1.2
        sprox==0.8
        sqlalchemy-migrate==0.7.2
        tg.devtools==2.2.0
        tgext.admin==0.5.3
        tgext.crud==0.5.3
        transaction==1.1.1
        ToscaWidgets==0.9.12
        tw2.core==2.1.0b1
        tw2.forms==2.0.3
        wsgiref==0.1.2
        zope.interface==3.6.3
        zope.sqlalchemy==0.7
        """
        ),
        classifiers=[
          "Environment :: Web Environment",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Framework :: TurboGears"
          ],
        keywords='turbogears2',
        version='2.2.0',
        description='Reference this rather than Turbogears2 as a dependency to get a consistent install with your package',
        author='Nick Holden',
        author_email='nickpholden@gmail.com',
        url='https://github.com/nickpholden/TurboGears2Frozen',
        license='LGPL',
        packages=find_packages(exclude=['ez_setup'])
        )
