from setuptools import setup, find_packages

setup(
    name='sphinxcontrib_robotframework',
    version='0.1.1.dev0',
    description='Robot Framework plugin for Sphinx',
    url='http://github.com/vivekkodu/sphinxcontrib_robotframework',
    author='Vivek',
    author_email='1990vivekkumarverma@gmail.com',
    license='GPL',
    py_modules=[
        'sphinxcontrib_robotframework'
    ],
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Sphinx',
        'robotframework',
        'Pygments',
    ],
    extras_require={"docs": [
        "robotframework-selenium2library",
        "robotframework-selenium2screenshots[Pillow]",
    ]}
)
