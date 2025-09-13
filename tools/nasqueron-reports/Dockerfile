#   -------------------------------------------------------------
#   Nasqueron Reports :: Docker image
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------

#   -------------------------------------------------------------
#   Build Python package
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FROM debian:trixie AS build

COPY . /app
WORKDIR /app
RUN apt-get update && apt install -y python3-pip python3-build git && \
    git clone https://devcentral.nasqueron.org/source/reports.git /usr/src/reports && \
    python3 -m build

#   -------------------------------------------------------------
#   Final image
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

FROM debian:trixie AS runner

COPY --from=build /app/dist/nasqueron_reports-0.1.0-py3-none-any.whl /app/
COPY --from=build /usr/src/reports/sql /usr/share/nasqueron-reports/sql
COPY conf/reports.yaml /etc/reports.yaml

RUN apt-get update && \
    apt install -y python3-pip locales --no-install-recommends && \
    rm -r /var/lib/apt/lists/* && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8 && \
    pip install /app/nasqueron_reports-0.1.0-py3-none-any.whl --break-system-packages

WORKDIR /app
ENV LANG=en_US.UTF-8
CMD ["run-report"]
