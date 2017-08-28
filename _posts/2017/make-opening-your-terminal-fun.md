---
date: 2017-05-15 14:41:30.072518
title: Make opening your terminal fun
featured-image: make-terminal-fun-again.png
---

My favorite and least useful thing I have set up on my laptop is to run fortune | ponysay when I open a new bash session.
In my .bashrc file I have the following snipped:

<pre><code>
if [ -x /usr/local/bin/ponysay -a -x /usr/local/bin/fortune ]; then
    fortune | ponysay
fi
</code></pre>

If you want one script to install everything for you:

<pre><code>
#!/bin/bash

echo 'Installing homebrew'
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo 'Installing fortune and ponysay
brew install fortune ponysay

echo "if [ -x /usr/local/bin/ponysay -a -x /usr/local/bin/fortune ]; then\n
    fortune | ponysay\n
fi\n" >> ~/.bashrc
</code></pre>
