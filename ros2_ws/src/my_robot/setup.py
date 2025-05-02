from setuptools import setup
import os
from glob import glob

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (f'share/{package_name}/launch', glob('launch/*.py')),
        (f'share/{package_name}/config', glob('config/*.yaml')),  # <-- TO DODAJ
        (f'share/{package_name}', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kamil',
    maintainer_email='your@email.com',
    description='Opis pakietu',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # np. 'your_node = my_robot.your_node:main',
        ],
    },
)
