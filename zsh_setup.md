# Zsh Shell Setup

Starting with macOS 10.15 Catalina, zsh will be the default macOS shell. Zsh is highly configurable but configuration can be tricky. Get up and running with some essential options and plugins, and an informative prompt theme.

----

### Check zsh
`% which zsh`  
the output should be `/bin/zsh`

## Config

### Change Prompt Style

```zsh
% cd && vim .zshrc
```

add following content into `.zshrc`

```zsh
PROMPT='%n:%~ %(!.#.$) '
```

Reload the current shell by `% source .zshrc` or new a terminal

### zsh-completions

#### Installation  

`$ brew install zsh-completions`

Add following content into `.zshrc`

```zsh
if type brew &>/dev/null; then
    FPATH=$(brew --prefix)/share/zsh-completions:$FPATH

    autoload -Uz compinit
    compinit
fi
```

Reload the current shell by `% source .zshrc` or new a terminal

- QA

If there shows the warning message

```shell
zsh compinit: insecure directories, run compaudit for list.
Ignore insecure directories and continue [y] or abort compinit [n]?
```

try the command : `$ compaudit | xargs chmod g-w` with a new line output `There are insecure directories:`

#### Ref

- https://github.com/zsh-users/zsh-completions/issues/680

- http://icarus4.logdown.com/posts/177661-from-bash-to-zsh-setup-tips

- http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html#Prompt-Expansion

- https://scriptingosx.com/2019/07/moving-to-zsh-06-customizing-the-zsh-prompt/

- http://www.nparikh.org/unix/prompt.php#zsh