from distutils.core import setup
setup(
  name = 'Scrapper',         # name of the Package
  packages = ['Scrapper'],   # Name of the package
  version = '0.1',      # Current version of the package
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'RSS Feed News Scrapper',   # Give a short description about your library
  author = 'iNeuron',                   # Type in your name
  author_email = 'megh.patel0607@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['News Scrapper', 'Web Scrapper', 'RSS Feed News Scrapper', 'Scrapper'],   # Keywords that define our package best
  install_requires=[ 'os','bs4','time','typing', 'socket', 'urllib.request', 'urllib.error', 'pandas','datetime', 'logging'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)