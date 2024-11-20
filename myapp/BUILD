docker_image(
    name="myapp-362-image",
    source="Dockerfile.gdal_362",
    tags=["final"],
)

docker_image(
    name="gdal-362-image",
    source="Dockerfile.gdal_362",
    target_stage="base",
    tags=["environment-image"],
    dependencies=[
        # this pex is not necessary for the base stage
        "!!myapp/src:main_362",
    ]
)

docker_environment(
    name="gdal-362-docker-environment",
    image="gdal-362-image",
    description="Environment with Gdal 3.6.2 and Python 3.12.",
)


docker_image(
    name="myapp-384-image",
    source="Dockerfile.gdal_384",
    tags=["final"],
)

docker_image(
    name="gdal-384-image",
    source="Dockerfile.gdal_384",
    target_stage="base",
    tags=["environment-image"],
    dependencies=[
        # this pex is not necessary for the base stage
        "!!myapp/src:main_384",
    ]
)

docker_environment(
    name="gdal-384-docker-environment",
    image="gdal-384-image",
    description="Environment with Gdal 3.8.4 and Python 3.12.",
)
