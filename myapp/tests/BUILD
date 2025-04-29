__defaults__(
    {
        python_test: dict(
            extra_env_vars=default_env_vars()
        )
    },
)

python_test(
    name="env_test",
    source="env_test.py",
)

python_test(
    name="env_inside_environment_test.py",
    source="env_inside_environment_test.py",
    environment="test-environment",
)
