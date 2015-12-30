from setuptools import find_packages, setup

from pip.req import parse_requirements


def get_requirements(filename):
    try:
        from pip.download import PipSession

        session = PipSession()
    except ImportError:
        session = None

    reqs = parse_requirements(filename, session=session)

    return [str(r.req) for r in reqs]


def get_install_requires():
    return get_requirements('requirements.txt')


setup_args = dict(
    name='flask-website',
    version='0.1.0',
    packages=find_packages(),
    namespace_packages=['website'],
    include_package_data=True,
    install_requires=get_install_requires(),
    entry_points={
        'console_scripts': [
            'webserver=website.main:run_server',
        ]
    },
    package_data={
        'static': 'website/static/*',
        'templates': 'website/templates/*',
    },
)


if __name__ == '__main__':
    setup(**setup_args)
