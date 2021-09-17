import os
from glob import glob
from setuptools import setup

package_name = 'pydyna_simple'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', [os.path.join('resource', package_name)]),
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'logs', 'mylogs'), []),
        (os.path.join('share', package_name, 'logs', 'pydynalogs'), []),
        (os.path.join('share', package_name, 'logs', 'rosbags'), []),
        (os.path.join('share', package_name, 'logs', 'roslogs'), []),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bruno',
    maintainer_email='bruno.c.scaglione@gmail.com',
    description='High Fidelity Ship Maneuvering Simulator',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simul = pydyna_simple.pydyna_simple:main',
        ],
    },
)
