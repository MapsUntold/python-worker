FROM runpod/base:0.6.2-cuda11.1.1

# --- Optional: System dependencies ---
# COPY builder/setup.sh /setup.sh
# RUN /bin/bash /setup.sh && \
#     rm /setup.sh

# Work directory 
RUN mkdir /data
WORKDIR /data

# Python dependencies
COPY builder/requirements.txt /data/requirements.txt
RUN python3.11 -m pip install --upgrade pip && \
    python3.11 -m pip install --upgrade -r requirements.txt --no-cache-dir && \
    rm requirements.txt

# Add src files (Worker Template)
ADD src .

CMD python3.11 -u runner.py
