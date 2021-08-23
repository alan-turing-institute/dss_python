FROM python:3.8

RUN apt-get update && apt-get install patchelf

# Copy only the files that we need to build the wheel into the image
COPY dss/ dss_python/dss/
COPY cffi/ dss_python/cffi/
COPY ["README.md", "setup.py", "dss_build.py", "dss_setup_common.py", "dss_python/"]

ENV LD_LIBRARY_PATH=/dss_python/dss:$LD_LIBRARY_PATH
ENV DSS_PYTHON_MANYLINUX=1

# Download and extract compiled dss_capi package
# Build scripts assume we have two directories at the same level, dss_python and dss_capi
RUN wget https://github.com/dss-extensions/dss_capi/releases/download/0.10.7-1/dss_capi_0.10.7-1_linux_x64.tar.gz && tar -xvf dss_capi_0.10.7-1_linux_x64.tar.gz

# Build the Linux wheel; to copy to local folder "wheels", use e.g.:
# docker build -t dss_python_image .
# docker run -d --name dss_python_wheel -t dss_python_image
# docker cp dss_python_wheel:/dss_python/dist dist
# docker stop dss_python_wheel
RUN cd dss_python && \
    pip install --upgrade pip && \
    pip install wheel auditwheel && \
    python setup.py bdist_wheel && \
    auditwheel repair dist/*linux*.whl -w outputs/
