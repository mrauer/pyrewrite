build:
	docker build -t pyrewrite:latest .

run:
	docker build -t pyrewrite:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app pyrewrite:latest
