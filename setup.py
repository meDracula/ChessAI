from setuptools import find_packages, setup

setup(
        name="PokerAI",
        version="0.0.1",
        description="A Interactive game of poker as a package",
        author="meDracula, Antonse2, MahboubehAzizzadeh, marcoRanmna",
        packages=['Poker'],
        url='https://github.com/meDracula/PokerAI',
        long_description=open('README.md').read(),
        install_requires=[
            'python_version >= "3.10"',
            "treys",
        ],
)
