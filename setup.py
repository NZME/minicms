from setuptools import setup, find_packages

setup(name='minicms',
      version='0.1',
      description='a mini cms module',
      url='https://github.com/robertzp/minicms.git',
      author='robertzp',
      author_email='robertzp@gmail.com',
      license='MIT',
      packages=['minicms'],
      include_package_data=True,
      zip_safe=False,
      classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: Alpha",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent"
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Framework :: Django",
      ]
)