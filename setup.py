from setuptools import setup

setup(
    name='your_script',
    version='0.1',
    packages=['your_script'],
    entry_points={
        'console_scripts': [
            'your_script = your_script.script:main',
        ],
    },
    install_requires=[
        # any dependencies your script may have
    ],
)
