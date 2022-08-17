[![GitHub](https://img.shields.io/badge/GitHub-noahp/dirdesc-8da0cb?style=for-the-badge&logo=github)](https://github.com/noahp/dirdesc)
[![PyPI
version](https://img.shields.io/pypi/v/dirdesc.svg?style=for-the-badge&logo=PyPi&logoColor=white)](https://pypi.org/project/dirdesc/)
[![PyPI
pyversions](https://img.shields.io/pypi/pyversions/dirdesc.svg?style=for-the-badge&logo=python&logoColor=white&color=ff69b4)](https://pypi.python.org/pypi/dirdesc/)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/noahp/dirdesc/CI/main?logo=github-actions&logoColor=white&style=for-the-badge)](https://github.com/noahp/dirdesc/actions)

# dirdesc

Generate an annotated directory tree description.

```bash
❯ dirdesc tests/example --depth 4 --hidden
tests/example  # hello!
├── 📂 child0
│   ├── 📄 .hidden  # hi hidden
│   └── 📂 child1
├── 📄 file0  # some file 0
└── 📄 file1
```

This is (maybe?) useful for automatically keeping those depictions in sync if
there are changes to the directory tree.

<!-- markdown-toc-cli -->

- [dirdesc](#dirdesc)
  - [Usage](#usage)
  - [Publishing](#publishing)

<!-- markdown-toc-cli-end -->

## Usage

This tool relies on `.dirdesc.yaml` files in the directories being scanned:

```bash
❯ tree tests/example -a
tests/example
├── child0
│   ├── child1
│   │   ├── child2
│   │   └── .dirdesc.yaml
│   ├── .dirdesc.yaml
│   └── .hidden
├── .dirdesc.yaml
├── file0
└── file1

3 directories, 6 files
```

The `.dirdesc.yaml` files are either empty, or contain description strings for
the directory entries in that directory. The possible options are:

1. empty file. this just marks the directory for inclusion in the `dirdesc`
   output, but does not apply any annotation.

2. file with just a string description. this applies to the current directory,
   and overrides any parent directory `.dirdesc.yaml` description:

   ```yaml
   string describing the current directory
   ```

3. file with just a mapping. this applies the descriptions to the files named by
   the mapping keys:

   ```yaml
   somefile: description of somefile
   some-other-file: description of some-other-file
   ```

4. file with 2 yaml documents:

   1. a plain string
   2. a mapping

   the first document applies to the current directory, the second document
   applies to the named entries in the current directory:

   ```yaml
   string describing the current directory
   ---
   somefile: description of somefile
   some-other-file: description of some-other-file
   ```

## Publishing

The version is not set in `pyproject.toml`, instead it's updated when git
tagging:

```bash
# git tag, poetry version bump, build, publish
❯ git tag -a 0.1.0 -m 0.1.0 && poetry version $(git describe) && poetry build && poetry publish
# push the fresh tag
❯ git push --tags
```
