from setuptools import setup, find_packages

setup(
    name='sphinxcontrib_robotframework',
    version='0.1.0',
    description='Robot Framework plugin for Sphinx',
    url='http://github.com/vivekkodu/sphinxcontrib_robotframework',
    author='Vivek',
    author_email='1990vivekkumarverma@gmail.com',
    license='GPL',
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'sphinx',
        'robotframework',
        'Pygments',
    ],
    extras_require={"docs": [
        "Pillow",  # the currently maintained fork of PIL
        "robotframework-selenium2library",
    ]}
)
