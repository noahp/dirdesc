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
