from setuptools import find_packages, setup


__version__ = "0.0.1"

setup_args = dict(
    name="kafkaspam",
    version=__version__,
    author="Armadik",
    platforms="Linux",
    description="Generate kafka spam",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "kafka-python==2.0.2",
    ],
    entry_points={
        'console_scripts': [
            'app = kafkaspam.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8"
)


def main():
    setup(**setup_args)


if __name__ == '__main__':
    main()
