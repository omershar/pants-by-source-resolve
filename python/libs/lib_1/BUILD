python_sources(
    sources=['examples/*.py', 'lib_1/*.py'],
    **parametrize('app_1', interpreter_constraints=['==3.7.*'], resolve='app_1'),
    **parametrize('app_2', interpreter_constraints=['==3.8.*'], resolve='app_2'),
)
poetry_requirements(
    name='poetry',
    resolve=parametrize('app_1', 'app_2')
)