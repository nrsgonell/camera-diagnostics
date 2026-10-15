"""Educational image diagnostics for camera troubleshooting."""
import argparse
import json
import socket


def check_tcp(host, port, timeout=2.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def image_metrics(path):
    import cv2
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Unable to read image: {path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return {
        "brightness_mean": round(float(gray.mean()), 2),
        "laplacian_variance": round(float(cv2.Laplacian(gray, cv2.CV_64F).var()), 2),
        "width": int(gray.shape[1]),
        "height": int(gray.shape[0]),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", required=True)
    parser.add_argument("--host")
    parser.add_argument("--port", type=int, default=554)
    args = parser.parse_args()
    result = image_metrics(args.image)
    if args.host:
        result["tcp_reachable"] = check_tcp(args.host, args.port)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
