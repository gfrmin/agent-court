#!/usr/bin/env bash
# Install the pinned mdBook into the current directory as ./mdbook.
#
# The one installer for both builds of this book: this repository's `book`
# workflow and gfrmin/gfrminsite's publish workflow, which runs it from its
# checkout of this repository. The version is .mdbook-version and the sha256 of
# the x86_64 Linux release tarball is .mdbook-sha256, both at the repository
# root; bump them together. Get the hash with
#   gh api repos/rust-lang/mdBook/releases/tags/v<ver> \
#     --jq '.assets[]|select(.name|test("x86_64-unknown-linux-gnu"))|.digest'
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
version="$(tr -d '[:space:]' < "$root/.mdbook-version")"
sha256="$(tr -d '[:space:]' < "$root/.mdbook-sha256")"
tarball="mdbook-v${version}-x86_64-unknown-linux-gnu.tar.gz"

curl -fsSL -o "$tarball" \
  "https://github.com/rust-lang/mdBook/releases/download/v${version}/${tarball}"
echo "${sha256}  ${tarball}" | sha256sum -c -
tar xzf "$tarball"
rm "$tarball"
./mdbook --version
