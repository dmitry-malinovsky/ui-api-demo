# Use the pre-built image with Python and ChromeDriver
FROM joyzoursky/python-chromedriver:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Set the environment variable for headless mode
ENV HEADLESS=true

# Command to run the Behave tests with HTML output
CMD ["behave", "--tags=@UI", "-f", "html", "-o", "behave-report.html"]