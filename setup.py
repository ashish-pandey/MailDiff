
from setuptools import setup

setup(name="mail_diff",
	version="1.0",
	description="Automatically mails your group members the local changes you make in your project",
	url="https://github.com/ashish-pandey/MailDiff.git",
	author="Ashish Pandey",
	author_email="apndey.15@gmail.com",
	license='MIT',
	packages=["mail_diff"],
	scripts=["bin/mail_diff"],
	zip_safe=False)
