from setuptools import setup, find_packages

setup(
    name='gdrive_notifier',
    version='0.0.1',
    description='Notify backup status to Uptime Kuma via Push URL',
    author='Your Company',
    author_email='you@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
