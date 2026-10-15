# Camera Diagnostics Lab

A **learning project**, not a production LPR diagnostic system. Analyzes an image for average grayscale brightness and Laplacian sharpness (a rough blur indicator). Can optionally test TCP connectivity to a camera host/port. Does **not** access live camera streams or recognize license plates.

## Run
```bash
python -m pip install -r requirements.txt
python diagnose.py --image /path/to/sample.jpg
python diagnose.py --image /path/to/sample.jpg --host 192.0.2.10 --port 554
```

Use images you own or have permission to inspect. Thresholds are illustrative, not calibrated camera acceptance criteria.
