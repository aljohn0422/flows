import sys
from prefect import flow
from prefect.docker import DockerImage


@flow(log_prints=True)
def python_version():
    print(sys.version)


if __name__ == "__main__":
    python_version()
