from setuptools import setup

setup(
    name='threaded_cv2',
    version='0.1.0',
    description='A package that contains threaded CV2 io classes implementations',
    url='https://github.com/ricglz/threaded_cv2',
    author='Ricardo Gonzalez',
    author_email='rjgcastillo2@gmail.com',
    license='MIT License',
    packages=['threaded_cv2'],
    install_requires=[
        'opencv-python',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Visualization'
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Typing :: Typed'
    ],
)
