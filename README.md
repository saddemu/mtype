# mtype

A [monkeytype](https://monkeytype.com/)-inspired typing test for the terminal.
Single Python file, standard library only — no dependencies to install.

- Live WPM and accuracy
- Time mode (15 / 30 / 60 / 120 s) and words mode (10 / 25 / 50 / 100)
- English and Italian word lists (Italian words are all accent-free, so no special keyboard layout is needed)
- Three-line scrolling view that follows the cursor, monkeytype-style
- Correct characters in white, mistakes in red and underlined, untyped text dimmed

## Requirements

- Linux (or any Unix with a `curses`-capable terminal)
- Python 3.8+

That's it. `curses` ships with the Python standard library.

## Installation

Clone the repo and run the install script:

```sh
git clone https://github.com/saddemu/mtype.git
cd mtype
./install.sh           # user-local install -> ~/.local/bin/mtype
# or
sudo ./install.sh      # system-wide install -> /usr/local/bin/mtype
```

The script is plain POSIX `sh` and works on any Linux distribution (Debian, Ubuntu, Fedora, Arch, Alpine, …). It auto-detects whether it's running as root: as a regular user it installs into `~/.local/bin`, with `sudo` it installs into `/usr/local/bin`.

For a user-local install, make sure `~/.local/bin` is on your `PATH`. The install script will warn you if it isn't; in that case add this to your shell rc file (`~/.bashrc`, `~/.zshrc`, `~/.config/fish/config.fish`, …):

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Verify the install:

```sh
mtype --help
```

### Manual install

If you'd rather not run the script:

```sh
chmod +x mtype.py
mkdir -p ~/.local/bin
cp mtype.py ~/.local/bin/mtype
```

### Run without installing

```sh
python3 /path/to/mtype.py
```

## Usage

```sh
mtype                       # 30-second test in English (default)
mtype -l it                 # Italian word list
mtype -m time -t 60         # time mode, 60 seconds
mtype -m words -w 50        # words mode, 50 words
mtype -l it -m words -w 25  # Italian, 25 words
```

### Flags

| Flag | Values | Default | Meaning |
| --- | --- | --- | --- |
| `-l`, `--lang` | `en`, `it` | `en` | Word list language |
| `-m`, `--mode` | `time`, `words` | `time` | Test mode |
| `-t`, `--time` | `15`, `30`, `60`, `120` | `30` | Seconds (time mode) |
| `-w`, `--words` | `10`, `25`, `50`, `100` | `25` | Word count (words mode) |

### Key bindings

| Key | Action |
| --- | --- |
| Letters / space | Type |
| `Backspace` | Delete the last character |
| `Tab` | Restart with the same settings |
| `Esc` | Quit |

## Customizing the word lists

The English and Italian word lists are plain Python lists at the top of `mtype.py` (`ENGLISH_WORDS`, `ITALIAN_WORDS`). Add, remove, or replace entries directly in the file — no rebuild needed.

If you want to add a new language, copy one of the existing lists, give it a new name, and add the language code to the `-l/--lang` choices in `parse_args` and to the lookup in `make_test`.

## Uninstall

Run the uninstall script with the same scope you used to install:

```sh
./uninstall.sh         # removes ~/.local/bin/mtype
# or
sudo ./uninstall.sh    # removes /usr/local/bin/mtype
```

Then delete the cloned directory if you no longer need it:

```sh
rm -rf /path/to/mtype
```
