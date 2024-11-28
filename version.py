import sys
from prefect import flow
from prefect.docker import DockerImage


@flow
def python_version():
    print(sys.version)


if __name__ == "__main__":
    python_version.deploy(
        name="python-version-deployment",
        work_pool_name="my-worker-pool",
    )
