from setuptools import setup

package_name = 'pydyna_simple'

setup(
    name=pydyna_simple,
    version='0.0.0',
    packages=[pydyna_simple],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + pydyna_simple]),
        ('share/' + pydyna_simple, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bruno',
    maintainer_email='bruno.c.scaglione@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simul = pydyna_simple.pydyna_simple:main',
        ],
    },
)
