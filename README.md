# Codeforces Vim Checker

## Overview

**Codeforces Vim Checker** lets you run and test your Codeforces solutions directly from Vim or Neovim.  
It fetches sample test cases from any Codeforces problem and checks your C++ or Python solution, showing results right inside your editor.

---

## Features

- Fetches sample test cases from any Codeforces problem link.
- Automatically compiles and runs C++ or Python solutions.
- Shows pass/fail results in Vim, including in a floating popup (with [vim-floaterm](https://github.com/voldikss/vim-floaterm)).
- Easy Vim/Neovim integration with custom commands.

---

## Installation

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/codeforces-vim-checker.git
cd codeforces-vim-checker
```

### 2. Install Python dependencies

It’s recommended to use a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage (Command Line)

You can run the checker directly from the terminal:

**For C++:**
```sh
python3 src/main.py <codeforces_problem_url> 1.cpp
```
**For Python:**
```sh
python3 src/main.py <codeforces_problem_url> python3 mysolution.py
```

---

## Vim/Neovim Integration

### 1. Install [vim-floaterm](https://github.com/voldikss/vim-floaterm) (recommended for popups)

Add to your `~/.vimrc` or `~/.config/nvim/init.vim` (using vim-plug):

```vim
call plug#begin('~/.vim/plugged')
Plug 'voldikss/vim-floaterm'
call plug#end()
```
Then run `:PlugInstall` in Vim/Neovim.

---

### 2. Add these commands to your vimrc/init.vim

```vim
" Save the Codeforces problem link for later use
command! -nargs=1 CC let g:cf_problem_link = <q-args>

" Compile the current C++ file and run the checker with the saved link in a floating popup
command! CT execute 'FloatermNew --autoclose=2 zsh -c "g++ % -o %< && python3 /full/path/to/codeforces-vim-checker/src/main.py ' . g:cf_problem_link . ' ./%<"'
```
**Replace** `/full/path/to/codeforces-vim-checker` with the actual path to your cloned repo.

---

### 3. Workflow in Vim/Neovim

1. **Open your C++ file** (e.g., `1.cpp`).
2. **Set the problem link** (once per problem):  
   ```
   :CC <codeforces_problem_url>
   ```
3. **Compile and test in a popup:**  
   ```
   :CT
   ```
   - The results will appear in a floating window.
   - The popup will close automatically if all tests pass, or stay open if there’s an error.

---
### 4. Demo

See it in action!  
[🎥 Watch the demo video](file:///home/shibe/Videos/Screencasts/Screencast%20from%202025-05-25%2017-33-12.mp4)



## Troubleshooting

- Make sure you have Python 3, `g++`, and Vim/Neovim with Python support.
- If you use a different shell, adjust `zsh -c` to `bash -c` or `sh -c` as needed.
- For Python solutions, use:  
  ```
  python3 src/main.py <codeforces_problem_url> python3 mysolution.py
  ```

---

## Contributing

Pull requests and issues are welcome!  
If you have ideas for more features or improvements, feel free to open an issue or PR.

---

## License

MIT License. See [LICENSE](LICENSE) for details.