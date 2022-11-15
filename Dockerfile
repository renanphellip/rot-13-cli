FROM ubuntu:22.04

ENV PATH="/root/.local/bin:$PATH"

RUN apt update \
    && apt install -y curl python3 \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt remove --purge -y curl \
    && apt clean \
    && apt autoremove -y \
    && poetry config virtualenvs.in-project true
ADD . /opt/rot-cli
WORKDIR /opt/rot-cli
RUN poetry install --no-interaction --without dev

ENTRYPOINT [ "poetry", "run", "rot" ]
CMD [ "poetry", "run", "rot" ]
