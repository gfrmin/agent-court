#!/usr/bin/env bash
# Install the pinned mdBook into the current directory as ./mdbook.
#
# Used by this repository's `book` workflow. The version is .mdbook-version and
# the sha256 of the x86_64 Linux release tarball is .mdbook-sha256, both at the
# repository root; bump them together. gfrmin/gfrminsite, which publishes the
# book at gfrm.in/book/, keeps its own copy of this installer and its own pin
# files, and only warns when its version differs from this one; bump it in the
# same change. Get the hash with
#   gh api repos/rust-lang/mdBook/releases/tags/v<ver> \
#     --jq '.assets[]|select(.name|test("x86_64-unknown-linux-gnu"))|.digest'
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
version="$(tr -d '[:space:]' < "$root/.mdbook-version")"
sha256="$(tr -d '[:space:]' < "$root/.mdbook-sha256")"
case "$(uname -sm)" in
  "Linux x86_64") ;;
  *) echo "install-mdbook.sh: only x86_64 Linux is pinned (this is $(uname -sm)); install mdBook ${version} another way" >&2
     exit 1 ;;
esac
tarball="mdbook-v${version}-x86_64-unknown-linux-gnu.tar.gz"
trap 'rm -f "$tarball"' EXIT

curl -fsSL -o "$tarball" \
  "https://github.com/rust-lang/mdBook/releases/download/v${version}/${tarball}"
echo "${sha256}  ${tarball}" | sha256sum -c -
tar xzf "$tarball"
./mdbook --version
