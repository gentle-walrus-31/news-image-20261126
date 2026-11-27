#!/usr/bin/env python3
"""Drones Over Kuwait -- World News, 26 November 2026.

This is the entrypoint for the make.fun bounty
"Sum up 26 November's world news in one image"
(news-image-20261126). The finished front page ships next to this
file as ``front-page.png``; this program checks that the bundled
file is exactly the image the entry was built from, then installs
it as ``<output-dir>/entry.png``.

Known facts about the bundled image (a damaged or swapped file
fails the checks below instead of being submitted silently):
  image:  front-page.png
  bytes:  117199
  sha256: 973f2374be0841bb86947dd6340ad73a46c9c6be8274290dace85a0bb6db14d4
  size:   1024 x 1024 pixels

The program uses only the Python standard library, reads nothing
from the network, and writes the same bytes on every run.

Usage:
  python3 main.py [--check] [output-dir]

  --check     inspect the bundled image and stop, writing nothing.
  output-dir  folder that receives entry.png (default /output).
"""

import hashlib
import struct
import sys
from pathlib import Path

IMAGE_FILE = "front-page.png"
IMAGE_BYTES = 117199
IMAGE_SHA256 = "973f2374be0841bb86947dd6340ad73a46c9c6be8274290dace85a0bb6db14d4"
IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024
BYTE_LIMIT = 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def die(reason):
    """Report a problem on stderr and exit non-zero."""
    print("entry: %s" % reason, file=sys.stderr)
    raise SystemExit(1)


def bundled_image():
    """Return the bytes of the image shipped beside this file."""
    path = Path(__file__).resolve().parent / IMAGE_FILE
    if not path.is_file():
        die("bundled image missing: %s" % path)
    return path.read_bytes()


def inspect_png(blob):
    """Check the PNG bytes against the known facts; return its digest.

    Every mismatch stops the program with a plain-language reason,
    so a wrong file can never be installed as the entry.
    """
    if len(blob) > BYTE_LIMIT:
        die("image is %d bytes, above the 1 MiB limit" % len(blob))
    if len(blob) != IMAGE_BYTES:
        die("image is %d bytes, expected %d" % (len(blob), IMAGE_BYTES))
    if blob[:8] != PNG_SIGNATURE:
        die("first eight bytes are not the PNG signature")
    if len(blob) < 33 or blob[12:16] != b"IHDR":
        die("no IHDR chunk where a PNG header belongs")
    if blob[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        die("no valid IEND chunk at the end: the image is truncated")
    width, height = struct.unpack(">II", blob[16:24])
    if width != IMAGE_WIDTH or height != IMAGE_HEIGHT:
        die("image is %dx%d, expected %dx%d"
            % (width, height, IMAGE_WIDTH, IMAGE_HEIGHT))
    digest = hashlib.sha256(blob).hexdigest()
    if digest != IMAGE_SHA256:
        die("sha256 mismatch: %s" % digest)
    return digest


def install(blob, digest, outdir):
    """Write the image byte-for-byte and confirm the written copy."""
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.png"
    target.write_bytes(blob)
    if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
        die("written copy failed its sha256 check")
    return target


def parse_args(argv):
    """Split the command line into (check_only, output_dir)."""
    check_only = False
    positional = []
    for arg in argv[1:]:
        if arg == "--check":
            check_only = True
        elif arg.startswith("-"):
            print(__doc__, file=sys.stderr)
            print("entry: usage: python3 main.py [--check] [output-dir]",
                  file=sys.stderr)
            raise SystemExit(2)
        else:
            positional.append(arg)
    if len(positional) > 1:
        print(__doc__, file=sys.stderr)
        print("entry: usage: python3 main.py [--check] [output-dir]",
              file=sys.stderr)
        raise SystemExit(2)
    return check_only, positional[0] if positional else "/output"


def main(argv):
    check_only, outdir = parse_args(argv)
    blob = bundled_image()
    digest = inspect_png(blob)
    if check_only:
        print("check ok: %s, %dx%d, %d bytes, sha256 %s"
              % (IMAGE_FILE, IMAGE_WIDTH, IMAGE_HEIGHT, len(blob), digest))
        return 0
    target = install(blob, digest, outdir)
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (target, IMAGE_WIDTH, IMAGE_HEIGHT, len(blob), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
