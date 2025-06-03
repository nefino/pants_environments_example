# Pants environments example

Repo to showcase our needs for the Pants environments feature.

## Goals

The main goal is to use the pants environments feature to build our pexes and
run tests inside custom environments.

### Features and bugfixes we need
- Set which envs should be passed from the host inside environments. Issue:
  https://github.com/pantsbuild/pants/issues/18577.
- Use Dockerfiles as environments and the abiltiy to specify a stage. Issue:
  https://github.com/pantsbuild/pants/issues/17714
- Cleanup containers after using them as environments. Issue:
  https://github.com/pantsbuild/pants/issues/18307
- Make sure the docker image isn't built or pulled if the test is cached. Issue:
  https://github.com/pantsbuild/pants/issues/17958.
- Allow the use of
  [macros](https://www.pantsbuild.org/stable/docs/writing-plugins/macros) inside
  `__defaults__` in `BUILD` files with Pants environments set. Issue: https://github.com/pantsbuild/pants/issues/22376. Example: Moving
  the `__default__` block from `myapp/tests/BUILD` to `myapp/BUILD` results in
  this error:
  ```
  InvalidFieldTypeException: The 'extra_env_vars' field in target
  myapp#__defaults__ must be an iterable of strings (e.g. a list of strings),
  but was `default_env_vars()` with type `<unrecognized symbol>`.
  ```

## Setup

- You can use the devcontainer configured in `.devcontainer/devcontainer.json`
  or take care of the required dependencies like pants and exporting the env in
  `.env` manually.
- The images used as environments have to be built beforehand, since it's not
  possible to set Dockerfiles as environments yet. Run the script:
  `scripts/build_environment_images.sh`

## Tests

- `env_test.py`: Checks if the env inside `.env` exists in your local
  environment. This one should always pass.
- `env_inside_environment_test.py`: Checks if the env exists inside the
  pants environment. This should pass once the feature is implemented.
- Build and check the final images with: `scripts/check_final_images.sh`.

## Additional Information

- Most targets are categorized by the Gdal lib version used inside the image or
  environment. This is for testing if the pex was built inside the correct
  environment.
