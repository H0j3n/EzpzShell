from setuptools import setup

setup(name='ezpzShell',
      version='0.5.1',
      description='Eazy Peazy Reverse Shell',
      author='H0j3n',
      author_email='',
      maintainer='H0j3n',
      maintainer_email='',
      url='https://github.com/H0j3n/EzpzShell',
      packages=['ezpzShell',
                'ezpzShell.utils'],
      license='MIT',
      install_requires=[
          'netifaces==0.11.0',
          'pyaml==21.10.1',
          'PyYAML==6.0'
      ],
      classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
      ],
      entry_points= {
        'console_scripts': ['listen=ezpzShell:main']
      }
    )
