# Build with: docker build -t nuesschen .
# Run with:   docker run nuesschen


# Python image to use.
FROM python:3.8

# Set the exposed port of the streamlit app
EXPOSE 8080

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .



# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'



# Run app.py when the container launches
CMD ["sh", "-c", "streamlit run --server.port 8080 streamlit_app.py"]