import setuptools


with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    author='Marco Rossi',
    author_email='developer@marco-rossi.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Generate your personal RSS feed for open source software you follow.',
    install_requires=[
        'requests',
    ],
    keywords=[
        'rss',
        'github',
    ],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='oss_release_feed',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0', 'setuptools_scm'],
    url='https://github.com/m-rossi/oss-release-feed',
    use_scm_version=True,
)

