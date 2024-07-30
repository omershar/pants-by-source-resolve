python_sources(
    sources=['lib_3/*.py'],
    **parametrize('app_2', interpreter_constraints=['==3.8.*'], resolve='app_2'),
)
poetry_requirements(
    name='poetry',
    resolve=parametrize('app_2')
)