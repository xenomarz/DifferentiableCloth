import os
from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

# Python interface
setup(
    name='arcsim',
    install_requires=['torch'],
    ext_modules=[
        CppExtension(
            name='arcsim',
            include_dirs=[
                '/home/roy/GitHub/forks/DifferentiableCloth/arcsim/src',
                '/home/roy/GitHub/forks/DifferentiableCloth/arcsim/dependencies/include',
                '/home/roy/GitHub/forks/DifferentiableCloth/arcsim/dependencies/include/alglib'],
            sources=[
                'pybind/bind.cpp',
            ],
            libraries=['make_pytorch','json','taucs','alglib',
            'png','z','lapack','blas','boost_system','boost_filesystem','boost_thread','gomp','glut','GLU','GL','GLdispatch'],
            library_dirs=['objs','./arcsim/dependencies/lib','/usr/lib/x86_64-linux-gnu'],
        )
    ],
    cmdclass={'build_ext': BuildExtension},
    zip_safe=False,
)
