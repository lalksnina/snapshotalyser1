from setuptools import setup

setup(
    name='snapshotalyser-3000',
    version='0.1',
    author="Larisa Alksnina and Robin Norwood",
    author_email="lalksnin@gmail.com",
    description="Snapshotalyser 3000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/lalksnina/snapshotalyser1",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',
)