<div align="center">
  <img src="data/icons/hicolor/scalable/apps/page.kramo.Hyperplane.svg" width="128" height="128">

  # Hyperplane

  A non-hierarchical file manager

  <img src="data/screenshots/1.png">
</div>

> [!WARNING]
> This project is currently in **BETA**. You can try it out at your own risk, but be aware that things might break, it might have annoyances, **DATA LOSS** may occur and it may kill your cat.

For now, I recommend only trying it if you have a recent backup of your files.

# The project

The problem is that current methods for tagging files are OS-, file system- or application-specific and not portable.

The app was primarily built as a proof of concept for a non-hierarchical file manager whose storage can still be conveniently browsed via conventional file managers.

It is also a playground for design ideas like file extension badges or a symbolic grid view.

## The concept

Hyperplane stores its 'tags' (called categories) on disk as regular directories.

File A tagged 'Pictures', 'Art' and 'Animals' would be stored at `/Pictures/Art/Animals/` on disk.

File B tagged 'Videos' and 'Art' would be stored at `/Videos/Art/`.

When filtering for files tagged 'Art' however, both of these would show up.

The app keeps track of the list of categories in a `.hyperplane` file at the root of the Hyperplane directory. (Which is `$HOME` by default, but can be changed with the `$HYPHOME` environment variable.)

## The name

https://en.wikipedia.org/wiki/Hyperplane

It is subject to change.


# Testing

The project is currently in beta. Most features work, but user experience still needs refinement.

If you want to test without risking data loss, please set the `$HYPHOME` environment variable to point to somewhere inside `~/.var/app/page.kramo.Hyperplane.Devel/` and remove the app's `--filesystem=host` access.

You can download the latest beta from the [Releases page](https://github.com/kra-mo/hyperplane/releases) or the latest in-development version from [here](https://nightly.link/kra-mo/hyperplane/workflows/ci/main/page.kramo.Hyperplane.Devel-x86_64.zip).

You will need the [GNOME Nightly](https://nightly.gnome.org/) runtime installed to be able to test the app.

Please report any and all issues you find!

UX suggestions and missing feature reports are also welcome, even if it seems obvious.

# Contributing

If you want to help with code or design, please reach out or file an issue before making a pull request. That being said, I appreciate any help!

## Code

### Building

```sh
git clone https://github.com/kra-mo/hyperplane.git
cd hyperplane
meson setup build
ninja -C build install
```

### Code style

All code is auto-formatted with [Black](https://github.com/psf/black) and
linted with [Pylint](https://github.com/pylint-dev/pylint). Imports are sorted
by [isort](https://github.com/pycqa/isort).

Just copy `vscode.settings.json` from the root directory of this project to the `<project root>.vscode/` subdirectory before you open vscode.

```bash
$ mkdir .vscode
$ cp vscode.settings.json .vscode/settings.json
$
```

You can install the Black, Pylint, and isort extensions via the usual Extensions sidebar in VSCode.

For other code editors, you can install them via `pip` and invoke them from the command line.

### Python Setup

There is a regular pyproject.toml file, formatted for use with [Rye](https://rye-up.com/) which also installs local versions of each of those tools as development dependencies so you can use them from the command line or in a `pre-commit` type configuration.

Just use:
```bash
$ rye sync
```

## Translations

Strings are not final yet, I will set up translations closer to an initial release.

# Code of Conduct

The project follows the [GNOME Code of Conduct](https://conduct.gnome.org/).

See [CODE_OF_CONDUCT.md](https://github.com/kra-mo/hyperplane/blob/main/CODE_OF_CONDUCT.md).
