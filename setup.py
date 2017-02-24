from distutils.core import setup

setup(
    name='print_queue',
    version='0.1',
    packages=['src.accounts', 'src.accounts.migrations', 'src.profiles', 'src.profiles.migrations', 'src.print_queue',
              'src.print_queue.settings'],
    url='',
    license='Apache v2',
    author='Aliaksei Pilko',
    author_email='aliakseipilko1@gmail.com',
    description='A simple print queue'
)
