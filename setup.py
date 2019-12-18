import setuptools

setuptools.setup(
    name="jupyter-codeserver-proxy",
    version='1_Domino',
    url="https://github.com/ChuckRIHead/jupyter_codeserver_proxy-",
    author="Based on a project by Dirk Grunwald based on Project Jupyter Contributors",
    description="support@dominodatalab.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'codeserver = jupyter_codeserver_proxy:setup_codeserver',
        ]
    },
    package_data={
        'jupyter_codeserver_proxy': ['icons/*'],
    },
)
