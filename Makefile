build:
	docker build -t pyrewrite:latest .

run:
	docker build -t pyrewrite:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app pyrewrite:latest

test:
	pytest -vv lib/pyrewrite_test.py

sample:
	cp -R samples/ /tmp
	python3 lib/pyrewrite.py set /tmp/samples/

linux:
	nuitka3 lib/pyrewrite.py --nofollow-imports -o bin/pyrewrite-linux
