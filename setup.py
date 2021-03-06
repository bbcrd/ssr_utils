from distutils.core import setup
setup(name='ssr_utils', 
	  version='0.1', 
	  description='Python modules for playing the BWF sound scenes with the SoundScape Renderer.',
	  author='David Marston, Chris Pike',
	  author_email='david.marston@bbc.co.uk, chris.pike@bbc.co.uk',
	  url='http://data.bbcarp.org.uk/saqas/',
	  license = "GNU GPLv3",
	  py_modules=['adm2asdf', 'ssr_control', 'asdf_write', 'ssr_player'],)



