# Base image: official Python on a minimal Debian.
# Use Python 3.13-slim to match the local development version.
FROM python:3.13-slim

# Working directory inside the image. All subsequent commands run from here.
WORKDIR /app

# Copy the dependency file first — this enables Docker layer caching for the
# slow pip install step, so it only re-runs when requirements actually change.
COPY test-tagging/requirements.txt .

# Install Python dependencies. --no-cache-dir keeps the image smaller by not
# leaving pip's download cache behind in the layer.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test code into the image. This is done AFTER pip install so code
# changes don't invalidate the dependency cache layer.
COPY test-tagging/tests/ ./tests/
COPY test-tagging/pytest.ini .

# Default command when a container starts from this image.
# Format: JSON array, ["program", "arg1", "arg2"]
CMD ["pytest", "--alluredir=allure-results"]