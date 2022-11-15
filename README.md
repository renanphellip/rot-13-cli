# 📦 **ROT CLI**
The command line interface tool to encrypt and decrypt using 'Rotate by N Places' algorithm.

## **Requirements**
- [Python 3.10 or higher](https://www.python.org/downloads/)
- [Poetry 1.2.2 or higher](https://python-poetry.org/docs/#installation)
- [GNU Make 3.0 or higher](https://www.gnu.org/software/make/)

## **Using the CLI**
1. Download **package** from [latest Continuous Delivery run](https://github.com/renanphellip/rot-cli/actions/workflows/cd.yml).

1. Extract **rot-cli.tgz** package:
    ```shell
    $ tar -xf rot-cli.tgz
    ```

1. Access the **rot-cli** folder:

1. Run the following command:
    ```shell
    $ make config
    ```

1. Run the tool:
    ```shell
    $ rot --help
    ```

## **Using the CLI via Docker**
```shell
$ docker run renanphellip/rot --help
```

## **Install and Test Project**
1. `make install`
1. `make format`
1. `make lint`
1. `make sec`
1. `make test`

## **Credits**
Project based on the [cesar-live-192](https://github.com/dunossauro/cesar-live-192) project created by [Eduardo Mendes](https://github.com/dunossauro).  
[Como organizar um projeto Python? - Live de Python #192](https://www.youtube.com/watch?v=O3bs4JtHrow)
