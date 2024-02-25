from setuptools import setup, find_packages

setup(
    name='weather_app',
    version='1.0.0',
    description='Uma aplicação para visualizar dados meteorológicos através de uma interface gráfica',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/seuusuario/weather_app',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'weather-app=weather_app.gui:run_gui',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
