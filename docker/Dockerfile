FROM debian
MAINTAINER adam@zely.cz

ENV CONTAINER_VERSION=1.0

# Set variables
ARG APP_VERSION=1.0
ARG USERNAME=ddns-updater
ARG UID=1000
ARG APP_DIR=/ddns-updater

# Install dependencies
RUN \
	apt-get update; \
	apt-get install -y \
		chromedriver \
		python3-pip \
		curl \
		wget \
		; \
    python3 -m pip install selenium \
	rm -rf /var/lib/apt/lists/*; \
	\
	echo


# Create project folder and user and set permissions
COPY .. ${APP_DIR}
RUN \
	mkdir -p ${APP_DIR}/; \
	useradd -d $APP_DIR $USERNAME; \
	chmod a+x ${APP_DIR}/ddns-updater.sh;

VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}
USER ${USERNAME}

#CMD ["bash"]

