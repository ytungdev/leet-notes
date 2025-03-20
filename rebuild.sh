#!/bin/sh

cd ./scrapper
uv build --refresh
cd ..
uv tool install ./scrapper/dist/scrapper-0.3.1-py3-none-any.whl