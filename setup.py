from setuptools import setup, find_packages

setup(
    name='LLM_Powered_V2X_Protocols',
    version='0.1.0',
    description='LLM integration with 6G V2X communication protocols',
    author='[Your Name]',
    packages=find_packages(),
    install_requires=[
        'torch',
        'transformers',
        'numpy',
        'flask',
        'MarianMT'
    ],
)